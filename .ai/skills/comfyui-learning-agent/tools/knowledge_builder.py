#!/usr/bin/env python3
"""knowledge_builder.py — 扫描工作流目录，统计节点使用情况，辅助沉淀知识卡。

用法:
    # 统计目录下所有 workflow 的节点频率，并列出 knowledge/ 尚未覆盖的节点
    python knowledge_builder.py <workflows_dir> [--knowledge <knowledge_dir>] [--json]

    # 为指定节点生成知识卡草稿（写入 --out 目录，默认 knowledge/nodes/）
    python knowledge_builder.py <workflows_dir> --card KSampler --out ../knowledge/nodes/

    # 把统计结果写入 memory/workflow_index.json 的 node_stats
    python knowledge_builder.py <workflows_dir> --init-index ../memory/workflow_index.json

只依赖 Python 标准库。
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path
from collections import Counter

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from workflow_parser import normalize, detect_format  # 同目录复用

CARD_TEMPLATE = """---
name: {name}
title: {name}（待补全）
category: nodes
tags: []
updated: {today}
---

# {name}

> 草稿由 knowledge_builder.py 生成，出现在 {hits} 个工作流中：{workflows}

## 作用
TODO(待验证)：这个节点做什么？

## 所属插件
TODO(待验证)：ComfyUI 内置，还是 custom_nodes？
（custom_nodes 请对照 comfyui/custom_nodes/NODES_SOURCES.md 写上游仓库）

## 关键参数
| 参数 | 说明 |
|---|---|
| TODO | |

## 使用要点
- TODO

## 常见坑
- TODO

## 关联卡片
- TODO
"""


def find_workflows(root: Path) -> list[Path]:
    """递归收集看起来像 workflow 的 JSON。"""
    found: list[Path] = []
    for p in sorted(root.rglob("*.json")):
        if p.name.startswith("workflow_index"):
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8", errors="replace"))
            detect_format(data)
            found.append(p)
        except (ValueError, json.JSONDecodeError, OSError):
            continue
    return found


def known_card_names(knowledge_dir: Path) -> set[str]:
    """从 knowledge/*/​*.md 的 frontmatter name + 文件名收集已覆盖的节点。"""
    names: set[str] = set()
    if not knowledge_dir.is_dir():
        return names
    for md in knowledge_dir.rglob("*.md"):
        names.add(md.stem.lower())
        try:
            head = md.read_text(encoding="utf-8", errors="replace")[:400]
        except OSError:
            continue
        m = re.search(r"^name:\s*(\S+)", head, re.M)
        if m:
            names.add(m.group(1).lower())
    return names


def norm(s: str) -> str:
    return re.sub(r"[^a-z0-9]", "", s.lower())


def scan(workflows: list[Path]) -> tuple[Counter, dict[str, list[str]]]:
    """返回 (节点频率, class_type → 出现过的文件)。"""
    freq: Counter = Counter()
    where: dict[str, list[str]] = {}
    for p in workflows:
        try:
            wf = normalize(json.loads(p.read_text(encoding="utf-8", errors="replace")))
        except (ValueError, json.JSONDecodeError, OSError):
            continue
        for ct, c in wf["stats"].items():
            freq[ct] += c
            where.setdefault(ct, []).append(p.name)
    return freq, where


def main() -> int:
    ap = argparse.ArgumentParser(description="扫描工作流统计节点，辅助知识沉淀")
    ap.add_argument("workflows_dir", help="存放 workflow JSON 的目录")
    ap.add_argument("--knowledge", default=None,
                    help="knowledge 目录（默认取脚本位置 ../knowledge）")
    ap.add_argument("--card", default=None, help="为指定 class_type 生成知识卡草稿")
    ap.add_argument("--out", default=None, help="知识卡输出目录")
    ap.add_argument("--init-index", default=None,
                    help="把统计写入指定 workflow_index.json")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    root = Path(args.workflows_dir)
    workflows = find_workflows(root)
    if not workflows:
        print(f"在 {root} 下没有找到可解析的 workflow JSON。")
        return 1
    freq, where = scan(workflows)
    knowledge_dir = Path(args.knowledge) if args.knowledge else Path(__file__).parent.parent / "knowledge"

    result = {
        "scanned_dir": str(root),
        "workflow_count": len(workflows),
        "workflows": [p.name for p in workflows],
        "node_stats": {k: v for k, v in freq.most_common()},
        "uncovered": [],  # knowledge/ 未覆盖的节点
    }
    known = known_card_names(knowledge_dir)
    for ct in freq:
        if norm(ct) not in known and not any(norm(ct) in k or k in norm(ct) for k in known if len(k) >= 3):
            result["uncovered"].append(ct)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"扫描 {len(workflows)} 个 workflow：{', '.join(result['workflows'])}\n")
        print("== 节点使用频率 ==")
        for ct, c in freq.most_common():
            print(f"  {c:>3} × {ct}   （出现于 {len(where[ct])} 个文件）")
        print("\n== knowledge/ 尚未覆盖的节点 ==")
        print("  " + ("\n  ".join(result["uncovered"]) if result["uncovered"] else "（全覆盖，做得好！）"))

    if args.card:
        out_dir = Path(args.out) if args.out else knowledge_dir / "nodes"
        out_dir.mkdir(parents=True, exist_ok=True)
        today = datetime.date.today().isoformat()
        hits = len(where.get(args.card, []))
        wfs = ", ".join(dict.fromkeys(where.get(args.card, []))) or "-"
        card = CARD_TEMPLATE.format(name=args.card, today=today, hits=hits, workflows=wfs)
        dest = out_dir / f"{norm(args.card)}.md"
        dest.write_text(card, encoding="utf-8")
        print(f"\n知识卡草稿已生成: {dest}")

    if args.init_index:
        idx_path = Path(args.init_index)
        idx: dict = {}
        if idx_path.exists():
            idx = json.loads(idx_path.read_text(encoding="utf-8", errors="replace"))
        idx["node_stats"] = result["node_stats"]
        idx["updated"] = datetime.datetime.now().isoformat(timespec="seconds")
        idx_path.write_text(json.dumps(idx, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"已更新索引: {idx_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
