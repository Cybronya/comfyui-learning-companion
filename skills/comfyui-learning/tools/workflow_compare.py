#!/usr/bin/env python3
"""workflow_compare.py — 对比两个 ComfyUI workflow 的节点与参数差异。

用法:
    python workflow_compare.py old.json new.json
    python workflow_compare.py old.json new.json --json

对比维度:
  1) class_type 层面：仅 A 有 / 仅 B 有 / 共有数量变化
  2) 节点参数层面：同 class_type 的节点逐对匹配，列出 widgets/inputs 中标量参数的差异
依赖 workflow_parser 的解析逻辑，只使用标准库。
a/b 可为 workflow JSON，也可为 ComfyUI 导出的 PNG（自动提取内嵌 prompt/workflow chunk）。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from collections import Counter

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from workflow_parser import normalize  # 同目录复用
from extract_png_workflow import extract_text_chunks  # 同目录复用


def load(path: str) -> dict:
    """加载 workflow：JSON 直接解析；PNG 提取内嵌元数据（优先 API 格式 prompt chunk）。"""
    p = Path(path)
    if p.suffix.lower() == ".png":
        chunks = extract_text_chunks(str(p))
        raw = chunks.get("prompt") or chunks.get("workflow")
        if raw is None:
            raise ValueError(f"{path}: PNG 未内嵌 workflow 元数据（prompt/workflow chunk）")
        data = json.loads(raw)
    else:
        data = json.loads(p.read_text(encoding="utf-8", errors="replace"))
    return normalize(data)


def scalar_params(node: dict) -> tuple[dict, list]:
    """提取参数，返回 (命名参数, 位置参数)。

    API 格式：inputs 里的标量（命名）；UI 格式：widgets_values 数组（位置）。
    """
    w = node.get("widgets")
    if isinstance(w, dict):
        return {k: v for k, v in w.items() if not isinstance(v, (dict, list))}, []
    if isinstance(w, list):
        return [], [v for v in w if isinstance(v, (int, float, str, bool))]
    inputs = node.get("inputs") or {}
    named = {k: v for k, v in inputs.items()
             if isinstance(v, (int, float, str, bool)) and not (isinstance(v, str) and v.isdigit())}
    return named, []


MISSING = "<无>"


def diff_params(a: dict, b: dict) -> tuple[list, bool]:
    """返回 (差异列表 [(参数名, A值, B值)], 跨格式对齐标志)。"""
    na, pa = scalar_params(a)
    nb, pb = scalar_params(b)
    diffs: list[tuple] = []
    cross = False
    if na and nb:  # 同为命名（API vs API）
        for k in sorted(set(na) | set(nb)):
            if na.get(k, MISSING) != nb.get(k, MISSING):
                diffs.append((k, na.get(k, MISSING), nb.get(k, MISSING)))
    elif pa and pb:  # 同为位置（UI vs UI）
        if len(pa) != len(pb):
            diffs.append(("参数个数", len(pa), len(pb)))
        for i, (va, vb) in enumerate(zip(pa, pb)):
            if va != vb:
                diffs.append((f"widget[{i}]", va, vb))
    elif na and pb:  # A 命名(API) vs B 位置(UI)：按顺序对齐
        cross = True
        if len(na) != len(pb):
            diffs.append(("参数个数(命名/位置)", len(na), len(pb)))
        for (k, va), vb in zip(na.items(), pb):
            if va != vb:
                diffs.append((k, va, vb))
    elif pa and nb:  # A 位置(UI) vs B 命名(API)：按顺序对齐
        cross = True
        if len(pa) != len(nb):
            diffs.append(("参数个数(位置/命名)", len(pa), len(nb)))
        for va, (k, vb) in zip(pa, nb.items()):
            if va != vb:
                diffs.append((k, va, vb))
    return diffs, cross


def compare(a: dict, b: dict) -> dict:
    ca, cb = Counter(a["stats"]), Counter(b["stats"])
    only_a = {k: v for k, v in ca.items() if cb.get(k, 0) < v}
    only_b = {k: v for k, v in cb.items() if ca.get(k, 0) < v}
    common = {k: (ca[k], cb[k]) for k in ca if k in cb}

    # 同 class_type 逐对匹配（按出现顺序贪心配对）
    param_diffs: list[dict] = []
    used_b: set[str] = set()
    buckets: dict[str, list[dict]] = {}
    for n in b["nodes"]:
        buckets.setdefault(n["class_type"], []).append(n)
    for n in a["nodes"]:
        cands = [m for m in buckets.get(n["class_type"], []) if m["id"] not in used_b]
        if not cands:
            continue
        m = cands[0]
        used_b.add(m["id"])
        diffs, cross = diff_params(n, m)
        if diffs:
            param_diffs.append({"class_type": n["class_type"],
                                "a": f"{n['id']}:{n['title']}",
                                "b": f"{m['id']}:{m['title']}",
                                "cross_format": cross,
                                "diffs": diffs})
    return {"only_in_a": only_a, "only_in_b": only_b, "common": common,
            "param_diffs": param_diffs,
            "summary": {"nodes_a": len(a["order"]), "nodes_b": len(b["order"])}}


def human(res: dict, path_a: str, path_b: str) -> str:
    out = [f"A: {path_a}  ({res['summary']['nodes_a']} 节点)",
           f"B: {path_b}  ({res['summary']['nodes_b']} 节点)", ""]
    out.append("== 仅 A 有 ==")
    out += [f"  {v} × {k}" for k, v in res["only_in_a"].items()] or ["  （无）"]
    out.append("== 仅 B 有（A→B 新增）==")
    out += [f"  {v} × {k}" for k, v in res["only_in_b"].items()] or ["  （无）"]
    out.append("== 两边都有（A 数, B 数）==")
    out += [f"  {k}: {va} → {vb}" for k, (va, vb) in sorted(res["common"].items())]
    out.append("\n== 共有节点参数差异 ==")
    if not res["param_diffs"]:
        out.append("  （同名节点参数一致）")
    for d in res["param_diffs"]:
        tag = "  [跨格式对齐，仅供参考]" if d.get("cross_format") else ""
        out.append(f"  [{d['class_type']}]  {d['a']}  vs  {d['b']}{tag}")
        for k, va, vb in d["diffs"]:
            out.append(f"      {k}: {va!r} → {vb!r}")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="对比两个 ComfyUI workflow")
    ap.add_argument("a", help="旧 workflow JSON")
    ap.add_argument("b", help="新 workflow JSON")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    res = compare(load(args.a), load(args.b))
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2, default=str))
    else:
        print(human(res, args.a, args.b))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
