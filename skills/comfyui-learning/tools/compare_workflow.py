#!/usr/bin/env python3
"""compare_workflow.py — 将新 workflow 与已知 workflow 集合对比，输出三层差异。

用法:
    python compare_workflow.py new.json --index workflow_index.json
    python compare_workflow.py new.json known1.json known2.json --json

比较层级:
  1) Node level     — 新增节点 / 删除节点（相对已知集合）
  2) Parameter level— 共有同名节点的参数变化（如 steps: 20 → 30）
  3) Pattern level  — 判断 same pattern 还是 new pattern

依赖同目录 workflow_parser / workflow_compare，只使用标准库。
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict, List

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

sys.path.insert(0, str(Path(__file__).parent))

from workflow_parser import normalize
from workflow_compare import compare as diff_two
from workflow_compare import load


def compare(new_workflow: dict,
            known_workflows: List[dict]) -> Dict[str, Any]:
    """核心入口：new_workflow 与已知 workflow 列表对比。

    new_workflow / known_workflows 均为 normalize 后的 workflow dict。
    """
    node_level = _compare_nodes(new_workflow, known_workflows)
    param_level = _compare_params(new_workflow, known_workflows)
    pattern_level = _judge_pattern(node_level)

    return {
        "node_level": node_level,
        "param_level": param_level,
        "pattern_level": pattern_level,
    }


def _compare_nodes(new_wf: dict, known_wfs: List[dict]) -> Dict[str, Any]:
    known_counter: Dict[str, int] = {}
    for wf in known_wfs:
        for ct, n in wf["stats"].items():
            known_counter[ct] = max(known_counter.get(ct, 0), n)

    added: Dict[str, int] = {}
    removed: Dict[str, int] = {}
    for ct, n in new_wf["stats"].items():
        base = known_counter.get(ct, 0)
        if n > base:
            added[ct] = n - base
    for ct, base in known_counter.items():
        n = new_wf["stats"].get(ct, 0)
        if base > n:
            removed[ct] = base - n

    return {"added_nodes": added, "removed_nodes": removed,
            "new_workflow_nodes": len(new_wf["order"])}


def _compare_params(new_wf: dict,
                    known_wfs: List[dict]) -> List[Dict[str, Any]]:
    """同 class_type 节点逐对匹配（与每个已知 workflow 对比，取非空差异）。"""
    param_diffs: List[Dict[str, Any]] = []
    for known in known_wfs:
        res = diff_two(known, new_wf)
        for d in res["param_diffs"]:
            param_diffs.append({
                "against": known.get("source", "known"),
                "class_type": d["class_type"],
                "diffs": [{"param": k, "old": va, "new": vb}
                          for k, va, vb in d["diffs"]],
            })
    return param_diffs


def _judge_pattern(node_level: Dict[str, Any]) -> Dict[str, Any]:
    added = node_level["added_nodes"]
    removed = node_level["removed_nodes"]
    if not added and not removed:
        verdict = "same pattern"
    else:
        verdict = "new pattern"
    return {
        "verdict": verdict,
        "extensions": sorted(added),   # 例如 ControlNetLoader / LoraLoader
        "removed": sorted(removed),
    }


def human(res: dict) -> str:
    nl, pl, pat = res["node_level"], res["param_level"], res["pattern_level"]
    out = ["== Node level ==",
           f"  新增节点: {nl['added_nodes'] or 'None'}",
           f"  删除节点: {nl['removed_nodes'] or 'None'}",
           "",
           "== Parameter level =="]
    if not pl:
        out.append("  （共有节点参数一致）")
    for d in pl:
        out.append(f"  [{d['class_type']}] vs {d['against']}")
        for p in d["diffs"]:
            out.append(f"      {p['param']}: {p['old']!r} → {p['new']!r}")
    out += ["", "== Pattern level ==",
            f"  判定: {pat['verdict']}"]
    if pat["extensions"]:
        out.append(f"  扩展节点: {', '.join(pat['extensions'])}")
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser(description="新 workflow vs 已知 workflow 集合")
    ap.add_argument("new", help="新 workflow JSON")
    ap.add_argument("known", nargs="*", help="已知 workflow JSON（可多个）")
    ap.add_argument("--index", help="workflow_index.json，自动展开已知 workflow 的节点集合")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    new_wf = load(args.new)
    known_wfs = [load(p) for p in args.known]

    if args.index and not known_wfs:
        idx_path = Path(args.index)
        idx = json.loads(idx_path.read_text(encoding="utf-8"))
        # 索引条目的 path 指向真实 workflow 文件（PNG/JSON），逐条加载
        for w in idx.get("workflows", []):
            raw = w.get("path")
            if not raw:
                continue
            p = Path(raw)
            if not p.exists():
                p = idx_path.parent / raw  # 兼容相对索引目录的写法
            if not p.exists():
                print(f"警告: 索引条目文件不存在，跳过: {raw}", file=sys.stderr)
                continue
            try:
                wf = load(str(p))
                wf["source"] = w.get("name") or p.name  # 参数差异输出里显示来源名
                known_wfs.append(wf)
            except (ValueError, json.JSONDecodeError, OSError) as e:
                print(f"警告: 无法加载 {raw}: {e}", file=sys.stderr)
        if not known_wfs:
            # 兜底：退化为全局 node_stats 基线（跨工作流累计值，可能偏高）
            stats = idx.get("node_stats") or {}
            if stats:
                known_wfs.append({"stats": dict(stats), "nodes": [], "order": [],
                                  "source": "index/node_stats"})

    if not known_wfs:
        print("错误: 请提供 known workflow 文件或 --index", file=sys.stderr)
        return 2

    res = compare(new_wf, known_wfs)
    if args.json:
        print(json.dumps(res, ensure_ascii=False, indent=2, default=str))
    else:
        print(human(res))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
