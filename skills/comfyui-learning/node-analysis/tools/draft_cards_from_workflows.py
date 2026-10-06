# -*- coding: utf-8 -*-
"""
从学习记录对应的工作流 JSON 里自动起草节点知识卡。

对每个「用了但没卡」的节点类型，扫描全部 workflow JSON，收集：
    - 输入/输出槽（workflow JSON 里的 inputs/outputs 数组，
      name/type 是节点定义的真实字段，不是猜的）
    - widgets_values 的取值分布（按位置记录，参数名未知）
    - 有多少个 workflow 在用它

产出：
    - comfyui_library/knowledge/nodes/<slug>.md（可信度 Generated）
    - node_index.json 追加条目（version 升位）

卡片的「作用」一段只有节点名可推断时写推断，否则明确写
「作用未知」—— 禁止编造参数与行为（AGENTS.md 第 6 节）。

用法（仓库根目录）：
    python -X utf8 skills/comfyui-learning/node-analysis/tools/draft_cards_from_workflows.py
"""

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from engine.workflow_learning.ignore_nodes import is_ignored  # noqa: E402

WORKFLOW_DIR = ROOT / "comfyui_library" / "workflows"
NODES_DIR = ROOT / "comfyui_library" / "knowledge" / "nodes"
INDEX_PATH = ROOT / "comfyui_library" / "knowledge" / "node_index.json"

# 作用推断表：节点名里的关键词 → 分类与一句话作用（推断，卡内标注）
ROLE_HINTS = [
    ("Loader", "Model Loading", "加载类节点：把磁盘上的资源装入图中"),
    ("Load", "Input", "输入类节点：读入外部数据"),
    ("Save", "Output", "输出类节点：把结果写到磁盘"),
    ("Upscaler", "Upscale", "放大类节点：提升图像/视频分辨率"),
    ("Upscale", "Upscale", "放大类节点：提升图像/视频分辨率"),
    ("Encoder", "Encoding", "编码类节点：把数据编码为另一表示"),
    ("Encode", "Encoding", "编码类节点：把数据编码为另一表示"),
    ("Decoder", "Decoding", "解码类节点：把编码数据还原"),
    ("Decode", "Decoding", "解码类节点：把编码数据还原"),
    ("Sampler", "Sampling", "采样类节点：执行扩散去噪"),
    ("Scheduler", "Sampling", "调度器：控制去噪步长序列"),
    ("Switch", "Control Flow", "分支类节点：按条件选择输入"),
    ("Math", "Utility", "计算类节点：数值/表达式运算"),
    ("String", "Utility", "文本工具节点"),
    ("Text", "Utility", "文本工具节点"),
    ("Prompt", "Prompt", "提示词处理节点"),
    ("Mask", "Mask", "遮罩类节点：生成或处理遮罩"),
    ("ControlNet", "Conditioning", "ControlNet 控制类节点"),
    ("Video", "Video", "视频处理节点"),
    ("Audio", "Audio", "音频处理节点"),
    ("Image", "Image Processing", "图像处理节点"),
    ("Latent", "Latent", "latent 空间处理节点"),
    ("VAE", "Latent", "VAE 相关节点"),
    ("CLIP", "Conditioning", "CLIP/条件相关节点"),
    ("Conditioning", "Conditioning", "条件处理节点"),
    ("Cache", "Optimization", "缓存/优化类节点"),
    ("Attention", "Optimization", "注意力/加速优化节点"),
]


def guess_role(name):
    """按节点名关键词推断分类与作用（推断值，卡内标注待验证）"""
    for kw, cat, role in ROLE_HINTS:
        if kw.lower() in name.lower():
            return cat, role
    return "Other", "作用未知，需人工补充"


def slugify(name):
    s = re.sub(r"[^0-9A-Za-z]+", "_", name).strip("_").lower()
    return s or "node"


def collect_usage(targets):
    """扫全部 workflow JSON，按节点类型归并 inputs/outputs/widget 分布"""
    usage = {
        t: {
            "workflows": 0,
            "inputs": Counter(),
            "outputs": Counter(),
            "widgets": Counter(),
        }
        for t in targets
    }

    for path in WORKFLOW_DIR.rglob("*.json"):
        if "learning" in path.parts or path.name.startswith("_"):
            continue
        try:
            data = json.loads(path.read_text(encoding="utf-8-sig"))
        except Exception:
            continue
        nodes = data.get("nodes", []) if isinstance(data, dict) else []
        seen = set()
        for n in nodes:
            t = n.get("type")
            if t not in usage:
                continue
            if t not in seen:
                usage[t]["workflows"] += 1
                seen.add(t)
            for i in n.get("inputs", []) or []:
                usage[t]["inputs"][f"{i.get('name')}:{i.get('type')}"] += 1
            for o in n.get("outputs", []) or []:
                usage[t]["outputs"][f"{o.get('name')}:{o.get('type')}"] += 1
            wv = n.get("widgets_values")
            if isinstance(wv, list):
                usage[t]["widgets"][json.dumps(wv, ensure_ascii=False)] += 1
            elif isinstance(wv, dict):
                usage[t]["widgets"][
                    json.dumps(wv, ensure_ascii=False, sort_keys=True)
                ] += 1
    return usage


def render_card(name, stat):
    cat, role = guess_role(name)
    wf_n = stat["workflows"]
    lines = [
        f"# {name}",
        "",
        "## 节点类型",
        "",
        f"`{name}`",
        "",
        "## 分类",
        "",
        cat,
        "",
        "## 作用",
        "",
        f"{role}（按节点名关键词推断，TODO(待验证)）",
        "",
        "## 实测使用",
        "",
        f"出现在本库 {wf_n} 个 workflow 中。",
        "",
    ]

    if stat["inputs"]:
        lines += ["## 输入", ""]
        for io, c in stat["inputs"].most_common(10):
            lines.append(f"- `{io}`（{c} 次）")
        lines.append("")
    if stat["outputs"]:
        lines += ["## 输出", ""]
        for io, c in stat["outputs"].most_common(10):
            lines.append(f"- `{io}`（{c} 次）")
        lines.append("")
    if stat["widgets"]:
        lines += [
            "## 参数（widgets_values 按位置，参数名未知）",
            "",
            "常见取值：",
            "",
        ]
        for v, c in stat["widgets"].most_common(5):
            lines.append(f"- `{v[:120]}`（{c} 次）")
        lines.append("")

    lines += [
        "## 可信度",
        "",
        "Generated（自动起草：输入/输出/取值分布为 workflow 实测；"
        "作用为名称推断）TODO(待验证)",
        "",
    ]
    return "\n".join(lines)


def main():
    index = json.loads(INDEX_PATH.read_text(encoding="utf-8-sig"))
    known = set(index["nodes"])

    # 目标 = 学习记录里用过、没卡、非布线的节点类型
    from engine.workflow_learning import LearningStore
    freq = LearningStore().node_frequency()
    targets = sorted(
        n for n, c in freq.items()
        if n not in known and not is_ignored(n) and c >= 2
    )
    print(f"目标节点类型：{len(targets)}（出现 ≥2 次，已有卡 {len(known)} 张）")

    usage = collect_usage(targets)

    created = 0
    for name in targets:
        stat = usage[name]
        card_path = NODES_DIR / f"{slugify(name)}.md"
        if card_path.exists():
            # 同名 slug 已存在（不同节点类型）——加类型后缀防覆盖
            card_path = NODES_DIR / f"{slugify(name)}_{abs(hash(name)) % 10000}.md"
        card_path.write_text(render_card(name, stat), encoding="utf-8")

        cat, role = guess_role(name)
        index["nodes"][name] = {
            "knowledge_file": card_path.name,
            "category": cat,
            "role": role,
            "difficulty": "unknown",
            "learning_topics": [],
            "auto_drafted": True,
        }
        created += 1

    index["version"] = "1.2"
    INDEX_PATH.write_text(
        json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"新建卡片 {created} 张，node_index 共 {len(index['nodes'])} 条")


if __name__ == "__main__":
    main()
