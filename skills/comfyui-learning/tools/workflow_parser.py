#!/usr/bin/env python3
"""workflow_parser.py — 解析 ComfyUI workflow JSON（自动识别 UI / API 格式）。

用法:
    python workflow_parser.py <workflow.json>            # 人类可读摘要
    python workflow_parser.py <workflow.json> --json     # 机器可读归一化 JSON
    python workflow_parser.py <workflow.json> --mermaid  # 输出 mermaid flowchart
    python workflow_parser.py <workflow.json> --comfyui-root ../../comfyui
                                                        # 扫描 custom_nodes 识别插件归属

只依赖 Python 标准库。归一化输出结构:
    {"format": "ui|api", "nodes": [{"id","class_type","title","plugin","inputs",
      "widgets","output_types"}], "links": [...], "order": [...], "output_nodes": [...]}
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from collections import Counter, deque

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


# ---------------------------------------------------------------- 格式判别

def detect_format(data: dict) -> str:
    """返回 'ui' / 'api' / 抛 ValueError。"""
    if "nodes" in data and isinstance(data.get("nodes"), list):
        return "ui"
    if data and all(isinstance(k, str) and k.isdigit() for k in data.keys()) \
            and all("class_type" in v for v in data.values()):
        return "api"
    raise ValueError("无法识别的 workflow 格式：既非 UI 格式（含 nodes 数组），"
                     "也非 API 格式（数字键 + class_type）")


# ---------------------------------------------------------------- custom_nodes 插件归属扫描

def scan_custom_nodes(comfyui_root: str | Path) -> dict[str, str]:
    """扫描 comfyui/custom_nodes/*/，从 NODE_CLASS_MAPPINGS 提取 class_type → 插件名。"""
    mapping: dict[str, str] = {}
    base = Path(comfyui_root) / "custom_nodes"
    if not base.is_dir():
        return mapping
    pat_block = re.compile(r"NODE_CLASS_MAPPINGS\s*=\s*\{", re.S)
    pat_key = re.compile(r"^\s*[\"']?([A-Za-z0-9_.\-]+)[\"']?\s*:", re.M)
    for repo in sorted(p for p in base.iterdir() if p.is_dir() and not p.name.startswith(".")):
        plugin = repo.name
        for py in list(repo.rglob("*.py"))[:40]:  # 每个插件最多扫 40 个文件，控制耗时
            try:
                text = py.read_text(encoding="utf-8", errors="ignore")
            except OSError:
                continue
            for m in pat_block.finditer(text):
                # 取从 "NODE_CLASS_MAPPINGS = {" 起到配对大括号的块
                start = m.end() - 1
                depth, end = 0, start
                for i in range(start, len(text)):
                    if text[i] == "{":
                        depth += 1
                    elif text[i] == "}":
                        depth -= 1
                        if depth == 0:
                            end = i
                            break
                block = text[start:end]
                for km in pat_key.findall(block):
                    mapping.setdefault(km, plugin)
    return mapping


# ---------------------------------------------------------------- 归一化

def parse_ui(data: dict) -> dict:
    """解析 UI 格式（画布保存版）。"""
    links: dict[int, dict] = {}
    for ln in data.get("links", []):
        # [link_id, from_node, from_slot, to_node, to_slot, type]
        lid, src, _s_slot, dst, _d_slot, ltype = ln[:6]
        links[lid] = {"src": src, "type": ltype}

    nodes: dict[str, dict] = {}
    for n in data.get("nodes", []):
        inputs: dict[str, object] = {}
        for inp in n.get("inputs", []):
            lid = inp.get("link")
            if lid is not None and lid in links:
                # inputs 里直接记录来源节点 id（ref）与 link 类型，不再回查 link 表
                inputs[inp.get("name", "?")] = {
                    "ref": str(links[lid]["src"]),
                    "type": links[lid]["type"],
                }
        widgets = n.get("widgets_values")
        if isinstance(widgets, dict):
            widgets = {k: v for k, v in widgets.items()}
        nodes[str(n["id"])] = {
            "id": str(n["id"]),
            "class_type": n.get("type", "?"),
            "title": n.get("title") or n.get("type", "?"),
            "mode": n.get("mode", 0),
            "inputs": inputs,
            "widgets": widgets,
            "output_types": [o.get("type") for o in n.get("outputs", []) if o.get("type")],
        }

    link_rows = [
        {"from": val["ref"], "to": nid, "type": val.get("type"), "input": k}
        for nid, node in nodes.items()
        for k, val in node["inputs"].items()
        if isinstance(val, dict) and val.get("ref") in nodes
    ]
    return {"format": "ui", "nodes": nodes, "link_rows": link_rows}


def parse_api(data: dict) -> dict:
    """解析 API 格式（Save API 导出版）。"""
    nodes: dict[str, dict] = {}
    link_rows: list[dict] = []
    for nid, body in data.items():
        inputs: dict[str, object] = {}
        for name, val in (body.get("inputs") or {}).items():
            if isinstance(val, list) and len(val) == 2 and isinstance(val[0], str) \
                    and val[0].isdigit():
                inputs[name] = {"ref": val[0], "slot": val[1], "type": None}
            else:
                inputs[name] = val
        nodes[nid] = {
            "id": nid,
            "class_type": body.get("class_type", "?"),
            "title": body.get("_meta", {}).get("title", body.get("class_type", "?")),
            "mode": 0,
            "inputs": inputs,
            "widgets": {k: v for k, v in inputs.items() if not isinstance(v, dict)},
            "output_types": [],
        }
    for nid, node in nodes.items():
        for k, val in node["inputs"].items():
            if isinstance(val, dict) and val.get("ref") in nodes:
                link_rows.append({"from": val["ref"], "to": nid, "type": val.get("type"), "input": k})
    return {"format": "api", "nodes": nodes, "link_rows": link_rows}


OUTPUT_HINTS = ("SaveImage", "VHS_VideoCombine", "SaveAnimated", "SaveWEBM", "PreviewImage",
                "PreviewVideo", "SaveImageSequence", "SaveAudio", "SaveVideo")


def topological_order(nodes: dict) -> list[str]:
    """按输入依赖拓扑排序（被依赖者在前；有环或孤立节点附加在后）。"""
    deps = {nid: {v["ref"] for v in n["inputs"].values()
                  if isinstance(v, dict) and v.get("ref") in nodes}
            for nid, n in nodes.items()}
    indeg = {nid: len(d) for nid, d in deps.items()}
    rev: dict[str, list[str]] = {}
    for nid, d in deps.items():
        for p in d:
            rev.setdefault(p, []).append(nid)
    queue = deque(sorted([n for n, d in indeg.items() if d == 0], key=lambda x: int(x)))
    order: list[str] = []
    while queue:
        cur = queue.popleft()
        order.append(cur)
        for nxt in rev.get(cur, []):
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                queue.append(nxt)
    order += [n for n in nodes if n not in order]  # 环/孤立兜底
    return order


def normalize(data: dict, plugin_map: dict[str, str] | None = None) -> dict:
    fmt = detect_format(data)
    parsed = parse_ui(data) if fmt == "ui" else parse_api(data)
    nodes = parsed["nodes"]
    for n in nodes.values():
        if plugin_map:
            n["plugin"] = plugin_map.get(n["class_type"], "内置/未知")
        else:
            n["plugin"] = None
    order = topological_order(nodes)
    out_nodes = [nid for nid in order
                 if any(h in nodes[nid]["class_type"] for h in OUTPUT_HINTS)]
    stats = Counter(n["class_type"] for n in nodes.values())
    return {
        "format": fmt,
        "nodes": [nodes[nid] for nid in order],
        "links": parsed["link_rows"],
        "order": order,
        "output_nodes": out_nodes,
        "stats": dict(stats.most_common()),
    }


# ---------------------------------------------------------------- 展示

def human_report(wf: dict) -> str:
    lines: list[str] = []
    lines.append(f"格式: {wf['format']} | 节点数: {len(wf['order'])} | "
                 f"输出节点: {', '.join(wf['output_nodes']) or '未识别'}")
    lines.append("\n== 节点清单（按执行顺序估计）==")
    lines.append(f"{'id':>5}  {'class_type':<38} {'插件':<22} title")
    for n in wf["nodes"]:
        lines.append(f"{n['id']:>5}  {n['class_type']:<38} {(n['plugin'] or '-'):<22} {n['title']}")
    lines.append("\n== 连接（from → to.input [type]）==")
    for l in wf["links"]:
        src_t = wf["nodes"][[n["id"] for n in wf["nodes"]].index(l["from"])]["class_type"] \
            if any(n["id"] == l["from"] for n in wf["nodes"]) else "?"
        lines.append(f"  [{l['type'] or '?'}] {l['from']}({src_t}) → {l['to']}.{l['input']}")
    lines.append("\n== 节点出现频率 ==")
    for ct, c in wf["stats"].items():
        lines.append(f"  {c:>2} × {ct}")
    return "\n".join(lines)


def mermaid(wf: dict) -> str:
    ct = {n["id"]: n["class_type"] for n in wf["nodes"]}
    out = ["flowchart LR"]
    for nid in wf["order"]:
        label = ct.get(nid, "?").replace('"', "'")
        out.append(f'    n{nid}["{label}\\n#{nid}"]')
    for l in wf["links"]:
        t = l["type"] or ""
        out.append(f'    n{l["from"]} -->|{t}| n{l["to"]}')
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="解析 ComfyUI workflow JSON")
    ap.add_argument("workflow", help="workflow JSON 路径")
    ap.add_argument("--json", action="store_true", help="输出归一化 JSON")
    ap.add_argument("--mermaid", action="store_true", help="输出 mermaid flowchart")
    ap.add_argument("--comfyui-root", default=None,
                    help="ComfyUI 根目录（用于扫描 custom_nodes 识别插件归属）")
    args = ap.parse_args()

    raw = Path(args.workflow).read_text(encoding="utf-8", errors="replace")
    data = json.loads(raw)
    plugin_map = scan_custom_nodes(args.comfyui_root) if args.comfyui_root else None
    wf = normalize(data, plugin_map)

    if args.json:
        print(json.dumps(wf, ensure_ascii=False, indent=2))
    elif args.mermaid:
        print(mermaid(wf))
    else:
        print(human_report(wf))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
