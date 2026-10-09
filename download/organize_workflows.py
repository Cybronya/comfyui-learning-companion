#!/usr/bin/env python3
"""整理 download/ 和 download/workflows-json/ 中散落的工作流文件。

根据文件名关键词 + JSON 内容节点判断分类，移动到 workflows-by-tag/<大类>/<子分类>/。

分类体系（对应 RunningHub 标签）：
    图片生成/文生图      图片生成/图生图      图片生成/反推提示词
    视频生成/文生视频    视频生成/图生视频    视频生成/视频生视频
    视频生成/数字人      视频生成/动作迁移    视频生成/其它视频处理
    图片生成/其它图片处理
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

BASE = Path(r"F:\Program Files\ComfyUI\download")
DEST_BASE = BASE / "workflows-by-tag"

# 分类关键词（按优先级从高到低，越具体越优先）
CATEGORY_KEYWORDS: list[tuple[str, str, list[str]]] = [
    # (大类, 子分类, 关键词列表)
    ("视频生成", "动作迁移", ["动作迁移", "FL2VA", "FL2AV", "Ref2VA", "Ref2AV"]),
    ("视频生成", "数字人", ["数字人", "音频驱动", "对口型", "口播"]),
    ("视频生成", "其它视频处理", ["视频编辑", "视频换背景", "视频复刻", "角色替换",
                                 "视频换人", "视频翻拍", "视频换脸", "去水印", "视频换产品"]),
    ("视频生成", "视频生视频", ["视频生视频", "视频参考生视频", "参考视频驱动", "视频延长",
                                 "视频参考编辑", "视频参考生视频加速"]),
    ("视频生成", "图生视频", ["图生视频", "首尾帧", "多图参考", "首帧生视频", "人物替换",
                                "角色一致性", "人物图生视频"]),
    ("视频生成", "文生视频", ["文生视频", "文戏"]),
    ("图片生成", "反推提示词", ["反推提示词", "提示词反推", "免手写提示词", "提示词增强"]),
    ("图片生成", "文生图", ["文生图", "Qwen Image", "Qwen-image", "Qwen_image", "G-IMAGE", "G Image"]),
    ("图片生成", "图生图", ["图生图"]),
    ("图片生成", "其它图片处理", ["换装", "换脸", "换背景", "换包装", "商品替换", "精修",
                                    "局部重绘", "扩图", "抠图", "擦除"]),
]

# 需要跳过的文件（非工作流）
SKIP_FILES = {"minimax-h3-ids-state.json", "_name_backfill.json", "manifest.csv", "README.md"}

# 节点名 -> 分类推断（用于内容判断）
NODE_CATEGORY_MAP = {
    # 视频输入
    "LoadVideo": "视频生成/视频生视频",
    "VHS_LoadVideo": "视频生成/视频生视频",
    "HAIGC_VideoLoader": "视频生成/视频生视频",
    # 图片输入（视频生成类）
    "LoadImage": "视频生成/图生视频",
    "VHS_LoadImage": "视频生成/图生视频",
    # 数字人相关
    "MiniMaxH3AudioToVideo": "视频生成/数字人",
    "MiniMaxH3ImageToVideo": "视频生成/数字人",
    # 动作迁移
    "MiniMaxH3FL2VA": "视频生成/动作迁移",
    "MiniMaxH3FL2AV": "视频生成/动作迁移",
}


def classify_by_filename(fname: str) -> str | None:
    """根据文件名关键词分类，返回 '大类/子分类' 或 None。"""
    lower = fname.lower()
    for category, subcat, keywords in CATEGORY_KEYWORDS:
        for kw in keywords:
            if kw.lower() in lower:
                return f"{category}/{subcat}"
    return None


def classify_by_content(json_path: Path) -> str | None:
    """读取 JSON，根据节点类型推断分类。"""
    try:
        data = json.loads(json_path.read_text(encoding="utf-8-sig"))
    except Exception:
        return None
    nodes = data.get("nodes", []) if isinstance(data, dict) else []
    node_types = set()
    for n in nodes:
        if isinstance(n, dict):
            t = n.get("type", "")
            if t:
                node_types.add(t)
    # 按优先级匹配
    for node_type, cat in NODE_CATEGORY_MAP.items():
        if node_type in node_types:
            return cat
    # 有视频相关节点但没匹配到精确分类
    video_nodes = {"MiniMaxH3", "MiniMaxH3Node", "MiniMaxVideoNode"}
    if node_types & video_nodes:
        return "视频生成/其它视频处理"
    return None


def main() -> int:
    # 收集所有散落的 JSON 文件
    files: list[Path] = []
    # download/ 根目录
    for f in (BASE).glob("*.json"):
        if f.name not in SKIP_FILES:
            files.append(f)
    # download/workflows-json/
    for f in (BASE / "workflows-json").glob("*.json"):
        files.append(f)

    print(f"共找到 {len(files)} 个散落的工作流文件\n")

    # 分类 + 移动
    stats: dict[str, int] = {}
    unclassified: list[tuple[str, str]] = []

    for f in files:
        # 先按文件名分类
        cat = classify_by_filename(f.name)
        if cat is None:
            # 文件名不明确，按内容分类
            cat = classify_by_content(f)

        if cat is None:
            unclassified.append((f.name, str(f.parent.name)))
            continue

        # 目标目录
        dest_dir = DEST_BASE / cat
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / f.name

        # 如果目标已存在同名文件，加序号
        if dest.exists() and dest != f:
            stem = f.stem
            suffix = f.suffix
            for i in range(2, 100):
                candidate = dest_dir / f"{stem}_{i}{suffix}"
                if not candidate.exists():
                    dest = candidate
                    break

        f.rename(dest)
        stats[cat] = stats.get(cat, 0) + 1

    # 打印结果
    print("=== 分类统计 ===")
    for cat in sorted(stats.keys()):
        print(f"  {cat}: {stats[cat]} 个")
    print(f"  合计: {sum(stats.values())} 个")

    if unclassified:
        print(f"\n=== 未分类（{len(unclassified)} 个）===")
        for name, src in unclassified:
            print(f"  {src}/{name}")

    return 0 if not unclassified else 1


if __name__ == "__main__":
    raise SystemExit(main())
