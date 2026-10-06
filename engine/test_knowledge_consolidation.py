r"""
Knowledge Consolidation 模块测试

从仓库根目录运行：
    cd "F:\Program Files\ComfyUI"
    python -X utf8 -m engine.test_knowledge_consolidation

-X utf8 必须加，否则中文输出乱码。
"""

import sys
from pathlib import Path
from tempfile import TemporaryDirectory

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from engine.knowledge_consolidation import (
    ConsolidationEngine,
    ExperienceLoader,
    ExperienceRow,
    PatternMiner,
    ParameterStatistics,
    KnowledgeBuilder,
    KnowledgeStore,
    jaccard,
    LEVEL_STRONG,
    LEVEL_WEAK,
)


# ============================================================
# A. 聚类（核心修正点）
# ============================================================

def test_jaccard():
    """测试相似度计算"""
    print("=" * 60)
    print("测试 A1：Jaccard 相似度")
    print("=" * 60)

    a = {"KSampler", "ControlNetApply", "VAEDecode"}
    b = {"KSampler", "ControlNetApply", "VAEDecode", "LoraLoader"}
    c = {"UNETLoader", "WanVideoSampler"}

    print(f"  a vs b（多一个节点）: {jaccard(a, b):.2f}")
    print(f"  a vs c（完全不同）:   {jaccard(a, c):.2f}")
    print(f"  a vs a:              {jaccard(a, a):.2f}")
    print(f"  空 vs 空:            {jaccard(set(), set()):.2f}")

    assert jaccard(a, a) == 1.0
    assert jaccard(a, c) == 0.0
    assert 0.6 < jaccard(a, b) < 1.0, "多一个节点应仍算相似"
    print("相似度计算正确 [OK]\n")


def test_cluster_ignores_extra_nodes():
    """测试「多一个特色节点」不会被拆成不同模式

    这是设计稿里精确匹配做不出来的：
        key = "_".join(sorted(nodes)) 要求节点集合完全相等。
    """
    print("=" * 60)
    print("测试 A2：聚类容忍额外节点")
    print("=" * 60)

    base = ["CheckpointLoaderSimple", "CLIPTextEncode", "KSampler",
            "VAEDecode", "SaveImage"]

    rows = [
        # 完全相同
        ExperienceRow(key="a", workflow_type="SDXL", nodes=base),
        # 多了 LoRA
        ExperienceRow(key="b", workflow_type="SDXL",
                      nodes=base + ["LoraLoader"]),
        # 多了 Upscale
        ExperienceRow(key="c", workflow_type="SDXL",
                      nodes=base + ["UpscaleModelLoader"]),
    ]

    patterns = PatternMiner(similarity=0.6).mine(rows)

    print(f"  3 个 workflow → {len(patterns)} 个模式")
    for p in patterns:
        print(f"    {p.name}: {p.frequency} 个成员 {p.members}")

    assert len(patterns) == 1, \
        f"节点高度重合应聚成 1 个模式，实际 {len(patterns)}"
    assert patterns[0].frequency == 3
    # 共有节点 = 三者都有的
    assert set(patterns[0].common_nodes) == set(base), \
        f"共有节点应为基础集合: {patterns[0].common_nodes}"
    # 可变部分应含两个特色节点
    variable = patterns[0].variable_nodes
    assert variable.get("LoraLoader") == 1, \
        f"LoraLoader 应只在 1 个里出现: {variable}"
    assert variable.get("UpscaleModelLoader") == 1
    print("容忍额外节点正确 [OK]\n")


def test_cluster_ignores_note_nodes():
    """测试注释节点不干扰聚类"""
    print("=" * 60)
    print("测试 A3：忽略注释节点")
    print("=" * 60)

    base = ["CheckpointLoaderSimple", "KSampler", "VAEDecode"]

    rows = [
        ExperienceRow(key="a", workflow_type="SDXL", nodes=base),
        # 只多了一个便签节点，结构其实一样
        ExperienceRow(key="b", workflow_type="SDXL",
                      nodes=base + ["MarkdownNote"]),
    ]

    patterns = PatternMiner(similarity=0.6).mine(rows)
    print(f"  模式数: {len(patterns)}")

    assert len(patterns) == 1, \
        "便签节点不应把结构相同的两个 workflow 拆开"
    assert "MarkdownNote" not in patterns[0].common_nodes
    assert "MarkdownNote" not in patterns[0].all_nodes
    print("注释节点被忽略 [OK]\n")


def test_cluster_separates_types():
    """测试不同 workflow_type 分开，不混合统计"""
    print("=" * 60)
    print("测试 A4：按类型分组")
    print("=" * 60)

    sd_nodes = ["CheckpointLoaderSimple", "KSampler", "VAEDecode"]
    wan_nodes = ["UNETLoader", "WanVideoSampler", "WanVideoDecode"]

    rows = [
        ExperienceRow(key="sd1", workflow_type="SD1.5 Text2Image",
                      nodes=sd_nodes, parameters={"cfg": 7, "steps": 25}),
        ExperienceRow(key="sd2", workflow_type="SD1.5 Text2Image",
                      nodes=sd_nodes, parameters={"cfg": 8, "steps": 30}),
        ExperienceRow(key="wan1", workflow_type="Wan Text2Video",
                      nodes=wan_nodes, parameters={"cfg": 5, "steps": 50}),
        ExperienceRow(key="wan2", workflow_type="Wan Text2Video",
                      nodes=wan_nodes, parameters={"cfg": 6, "steps": 60}),
    ]

    patterns = PatternMiner().mine(rows)
    print(f"  模式数: {len(patterns)}")
    for p in patterns:
        print(f"    {p.name} ({p.workflow_type}): {p.frequency} 个")

    assert len(patterns) == 2, "两种类型应聚成两个模式"
    types = {p.workflow_type for p in patterns}
    assert types == {"SD1.5 Text2Image", "Wan Text2Video"}

    # 模式名应能区分（命名带 type slug 或特征词）
    names = {p.name for p in patterns}
    assert any("video" in n or "sampler" in n for n in names), names
    print("按类型分组正确 [OK]\n")


def test_min_frequency():
    """测试样本数不足不成模式"""
    print("=" * 60)
    print("测试 A5：最小成员数")
    print("=" * 60)

    nodes = ["CheckpointLoaderSimple", "KSampler", "VAEDecode"]

    # 三个互不相同的 workflow
    rows = [
        ExperienceRow(key="a", workflow_type="X", nodes=nodes),
        ExperienceRow(key="b", workflow_type="X",
                      nodes=nodes + ["LoraLoader"]),
        ExperienceRow(key="c", workflow_type="X",
                      nodes=nodes + ["ControlNetApply"]),
    ]

    # 阈值高时三者互不相似，各自成簇但成员数不足 2 → 不成模式
    strict = PatternMiner(similarity=0.9, min_frequency=2).mine(rows)
    print(f"  similarity=0.9 → {len(strict)} 个模式（应 0）")
    assert len(strict) == 0, \
        f"高阈值下应各自分散，都不足最小成员数: {strict}"

    # 阈值放宽后链式合并成 1 个模式
    # （贪心聚类的并集会扩张，后续成员与并集比较 —— 这是有意的链式归并）
    loose = PatternMiner(similarity=0.6, min_frequency=2).mine(rows)
    print(f"  similarity=0.6 → {len(loose)} 个模式")
    assert len(loose) == 1
    assert loose[0].frequency == 3

    # 成员数够但只出现一次 → 也不该成模式
    single = PatternMiner(
        similarity=0.9, min_frequency=1
    ).mine([rows[0]])
    assert len(single) == 1
    assert single[0].frequency == 1

    print("最小成员数正确 [OK]\n")


def test_pattern_naming():
    """测试模式命名可读"""
    print("=" * 60)
    print("测试 A6：模式命名")
    print("=" * 60)

    cases = [
        (["KSampler", "ControlNetApply", "VAEDecode"], "SDXL",
         "controlnet"),
        (["CheckpointLoaderSimple", "LoraLoader", "KSampler"], "SD1.5",
         "lora"),
        (["IPAdapterApply", "KSampler", "VAEDecode"], "SDXL", "ipadapter"),
        (["UNETLoader", "WanVideoSampler", "WanVideoDecode"], "Wan",
         "video"),
    ]

    for nodes, wf_type, expected in cases:
        rows = [
            ExperienceRow(key=f"{expected}-{i}", workflow_type=wf_type,
                          nodes=nodes + (["LoraLoader"] if i else []))
            for i in range(2)
        ]
        patterns = PatternMiner().mine(rows)
        name = patterns[0].name if patterns else "(无)"
        print(f"  {wf_type} + {nodes[1]:20} → {name}")
        assert expected in name, \
            f"模式名应含 {expected}，实际 {name}"

    print("模式命名正确 [OK]\n")


# ============================================================
# B. 参数统计
# ============================================================

def test_parameter_stats_per_group():
    """测试参数统计按组，不混算"""
    print("=" * 60)
    print("测试 B1：分组参数统计")
    print("=" * 60)

    sd = [
        ExperienceRow(key=f"sd{i}", parameters={"cfg": c, "steps": s})
        for i, (c, s) in enumerate([(7, 20), (8, 25), (7, 30), (9, 25)])
    ]
    wan = [
        ExperienceRow(key=f"wan{i}", parameters={"cfg": c, "steps": s})
        for i, (c, s) in enumerate([(5, 50), (6, 60)])
    ]

    stat = ParameterStatistics()

    sd_stats = stat.analyze(sd)
    wan_stats = stat.analyze(wan)

    print(f"  SD 组: cfg median={sd_stats['cfg'].median} "
          f"steps median={sd_stats['steps'].median}")
    print(f"  Wan 组: cfg median={wan_stats['cfg'].median} "
          f"steps median={wan_stats['steps'].median}")

    # 关键：两组结果必须不同
    assert sd_stats["steps"].median == 25, \
        f"SD 组 steps 中位数应为 25，实际 {sd_stats['steps'].median}"
    assert wan_stats["steps"].median == 55, \
        f"Wan 组 steps 中位数应为 55，实际 {wan_stats['steps'].median}"

    # 若全局混算：steps 会是 (20+25+30+25+50+60)/6 = 35，毫无代表性
    mixed = stat.analyze(sd + wan)
    print(f"  混算: steps median={mixed['steps'].median} "
          f"mean={mixed['steps'].mean:.1f}  ← 35 对两组都不代表")
    assert mixed["steps"].median == 27.5

    print("分组统计正确 [OK]\n")


def test_parameter_stats_quality():
    """测试中位数抗异常值、集中度、样本门槛"""
    print("=" * 60)
    print("测试 B2：统计质量")
    print("=" * 60)

    # 一个异常值把均值拉偏
    rows = [
        ExperienceRow(key=f"r{i}", parameters={"steps": s})
        for i, s in enumerate([20, 22, 24, 26, 1])
    ]
    stat = ParameterStatistics().analyze(rows)["steps"]

    print(f"  mean={stat.mean:.1f}  median={stat.median:g}  "
          f"consistency={stat.consistency:.2f}")

    assert stat.mean < stat.median, "均值应被 steps=1 拉低"
    # sorted [1,20,22,24,26] 的中位数是 22 —— 恰好忽略了异常值 1
    assert stat.median == 22, f"中位数应为 22，实际 {stat.median}"

    # 集中度：取值一致时应高
    consistent = ParameterStatistics().analyze([
        ExperienceRow(key=f"c{i}", parameters={"cfg": 7})
        for i in range(4)
    ])["cfg"]
    scattered = ParameterStatistics().analyze([
        ExperienceRow(key=f"s{i}", parameters={"cfg": v})
        for i, v in enumerate([1, 5, 8, 15])
    ])["cfg"]

    print(f"  一致 consistency={consistent.consistency:.2f}  "
          f"分散 consistency={scattered.consistency:.2f}")
    assert consistent.consistency > scattered.consistency

    # 样本不足时不给区间
    two = ParameterStatistics().analyze([
        ExperienceRow(key="a", parameters={"steps": 20}),
        ExperienceRow(key="b", parameters={"steps": 30}),
    ])["steps"]
    print(f"  2 个样本的 typical_range: {two.typical_range}")
    assert two.typical_range is None, "样本 <3 不该给区间（那是噪声）"

    ok = ParameterStatistics().analyze([
        ExperienceRow(key=f"k{i}", parameters={"steps": 20 + i})
        for i in range(4)
    ])["steps"]
    assert ok.typical_range == "20 - 23", ok.typical_range

    print("统计质量正确 [OK]\n")


def test_parameter_stats_textual():
    """测试非数值参数与噪声参数"""
    print("=" * 60)
    print("测试 B3：非数值与噪声参数")
    print("=" * 60)

    rows = [
        ExperienceRow(key="a", parameters={
            "sampler_name": "dpmpp_2m", "seed": 1}),
        ExperienceRow(key="b", parameters={
            "sampler_name": "dpmpp_2m", "seed": 2}),
        ExperienceRow(key="c", parameters={
            "sampler_name": "euler", "seed": 3}),
    ]

    stats = ParameterStatistics().analyze(rows)
    print(f"  统计到的参数: {list(stats)}")

    assert "sampler_name" in stats, \
        "采样算法是最典型的归纳知识，不能丢"
    assert stats["sampler_name"].most_common == "dpmpp_2m"
    # seed 是随机值，统计了反而误导
    assert "seed" not in stats, "seed 无规律，不该进统计"

    print("非数值与噪声参数正确 [OK]\n")


def test_cross_pattern_comparison():
    """测试跨模式参数对比"""
    print("=" * 60)
    print("测试 B4：跨模式对比")
    print("=" * 60)

    grouped = {
        "portrait": [
            ExperienceRow(key=f"p{i}",
                          parameters={"cfg": 7, "steps": 30})
            for i in range(3)
        ],
        "video": [
            ExperienceRow(key=f"v{i}",
                          parameters={"cfg": 4, "steps": 50})
            for i in range(3)
        ],
    }

    notes = ParameterStatistics().compare_across(grouped)
    print(f"  对比结论 {len(notes)} 条:")
    for n in notes:
        print(f"    {n}")

    cfg_notes = [n for n in notes if n.startswith("cfg")]
    assert cfg_notes, "cfg 在两组差异明显（7 vs 4），应产出对比结论"
    assert "portrait" in cfg_notes[0] and "video" in cfg_notes[0]

    # 差异太小不该报
    same = {
        "a": [ExperienceRow(key=f"a{i}", parameters={"cfg": 7})
              for i in range(3)],
        "b": [ExperienceRow(key=f"b{i}", parameters={"cfg": 7.5})
              for i in range(3)],
    }
    assert not ParameterStatistics().compare_across(same), \
        "差异 <20% 应视为噪声，不报"

    print("跨模式对比正确 [OK]\n")


# ============================================================
# C. 知识构建
# ============================================================

def test_common_problems_aggregation():
    """测试常见问题聚合（设计稿完全没做这一步）"""
    print("=" * 60)
    print("测试 C1：常见问题聚合")
    print("=" * 60)

    rows = [
        ExperienceRow(key="a", problems=[
            "[medium] CFG值较高（当前 30.0），可能导致Prompt约束过强 → 建议尝试CFG 7-10"]),
        ExperienceRow(key="b", problems=[
            "[medium] CFG值较高（当前 25.0），可能导致Prompt约束过强 → 建议尝试CFG 7-10"]),
        ExperienceRow(key="c", problems=[
            "[high] 未检测到 VAEDecode 节点 → 添加 VAEDecode 把 latent 转成图像"]),
        ExperienceRow(key="d", problems=[
            "[low] 分辨率较低 → 建议提升到 768"]),
    ]

    problems = KnowledgeBuilder().aggregate_problems(rows)

    print(f"  {len(rows)} 条问题 → {len(problems)} 类:")
    for p in problems:
        print(f"    [{p['count']}次] {p['problem']}")

    # 两条 CFG 问题数值不同但属同类，应合并
    cfg = [p for p in problems if "CFG" in p["problem"]]
    assert len(cfg) == 1, f"同类 CFG 问题应合并，实际 {len(cfg)} 个"
    assert cfg[0]["count"] == 2
    assert cfg[0]["severity"] == "medium"
    # 归并后数值应被抹掉
    assert "30.0" not in cfg[0]["problem"], \
        f"归并后不应保留具体数值: {cfg[0]['problem']}"

    # 按次数降序
    assert problems[0]["count"] == 2

    print("常见问题聚合正确 [OK]\n")


def test_recommendations_risk():
    """测试建议含风险提示，且复用既有阈值"""
    print("=" * 60)
    print("测试 C2：建议与风险")
    print("=" * 60)

    from engine.knowledge_consolidation.models import (
        WorkflowPattern, ParameterStat,
    )

    pattern = WorkflowPattern(
        name="test", workflow_type="SDXL", frequency=5,
        common_nodes=["KSampler"],
    )
    pattern.parameter_stats = {
        "cfg": ParameterStat(
            count=5, min=6, max=30, mean=12, median=7,
            consistency=0.5, values=[6, 7, 7, 8, 30],
        ),
    }

    recs = KnowledgeBuilder().recommend(pattern)
    print("  建议:")
    for r in recs:
        print(f"    - {r}")

    joined = " ".join(recs)
    assert "中位数 7" in joined, "应给出中位数"
    assert "风险" in joined, "cfg 观测到 30 超上限应触发风险"
    # 阈值应复用 knowledge_evolution 的 RISK_RULES（cfg 上限 12）
    from engine.knowledge_evolution.knowledge_generator import RISK_RULES
    assert str(int(RISK_RULES["cfg"]["max"])) in joined, \
        "应复用 RISK_RULES 的阈值而不是自己定义"

    print("建议与风险正确 [OK]\n")


def test_sample_size_honesty():
    """测试样本不足时明说，而不是硬给结论"""
    print("=" * 60)
    print("测试 C3：样本量诚实性")
    print("=" * 60)

    from engine.knowledge_consolidation.models import (
        WorkflowPattern, ParameterStat,
    )

    # 只有 2 个样本，却有很"漂亮"的参数区间
    pattern = WorkflowPattern(name="thin", frequency=2)
    pattern.parameter_stats = {
        "steps": ParameterStat(count=2, min=20, max=30, mean=25,
                               median=25, consistency=1.0, values=[20, 30]),
    }

    recs = KnowledgeBuilder().recommend(pattern)
    joined = " ".join(recs)
    print("  建议:")
    for r in recs:
        print(f"    - {r}")

    assert "仅 2 个样本" in joined, "样本不足必须明说"
    assert "仅供参考" in joined

    # 3 个样本以上不给这个警告
    pattern.frequency = 5
    pattern.parameter_stats["steps"].count = 5
    recs2 = KnowledgeBuilder().recommend(pattern)
    assert not any("仅" in r and "样本" in r for r in recs2)

    # 等级判定
    builder = KnowledgeBuilder()
    pattern.frequency = 2
    assert builder._level(pattern) == LEVEL_WEAK
    pattern.frequency = 5
    pattern.parameter_stats = {
        "cfg": ParameterStat(count=5, median=7, mean=7,
                             consistency=0.95, values=[7] * 5)
    }
    assert builder._level(pattern) == LEVEL_STRONG

    print("样本量诚实性正确 [OK]\n")


# ============================================================
# D. 端到端
# ============================================================

def build_sample_rows():
    """构造一批有差异的样本，覆盖聚类与统计各条路径"""
    rows = []

    # SDXL 人像：4 个，含 LoRA 与 ControlNet
    # 问题文本要与实际参数自洽：cfg=9 触发 CFG 过高，其余正常
    for i, (cfg, steps, cn) in enumerate([
        (7, 30, 0.7), (8, 25, 0.6), (7, 28, 0.75), (9, 35, 0.65),
    ]):
        nodes = ["CheckpointLoaderSimple", "CLIPTextEncode",
                 "EmptyLatentImage", "KSampler", "VAEDecode", "SaveImage",
                 "LoraLoader"]
        if cn:
            nodes.append("ControlNetApply")
        rows.append(ExperienceRow(
            key=f"sdxl_portrait_{i}.json",
            workflow_type="SDXL Portrait",
            nodes=nodes + (["UpscaleModelLoader"] if i == 3 else []),
            parameters={
                "cfg": cfg, "steps": steps,
                "controlnet_strength": cn,
                "sampler_name": "dpmpp_2m",
                "seed": 100 + i,
            },
            problems=(
                ["[medium] CFG值较高（当前 9.0），可能导致Prompt约束过强 "
                 "→ 建议尝试CFG 7-10"]
                if cfg >= 9 else
                ["[low] 分辨率未达 SDXL 常用值（当前 512）→ 建议提升到 768 或以上"]
            ),
            missing_nodes=["ControlNetApply"] if i == 0 else [],
            coverage=0.85,
        ))

    # SD1.5 基础文生图：3 个
    for i, (cfg, steps) in enumerate([(7, 20), (8, 25), (7, 22)]):
        rows.append(ExperienceRow(
            key=f"sd15_basic_{i}.json",
            workflow_type="SD1.5 Text2Image",
            nodes=["CheckpointLoaderSimple", "CLIPTextEncode",
                   "EmptyLatentImage", "KSampler", "VAEDecode", "SaveImage"],
            parameters={"cfg": cfg, "steps": steps,
                        "sampler_name": "euler", "seed": 200 + i},
            coverage=1.0,
        ))

    # Wan 视频：3 个，步数完全不同
    for i, (cfg, steps) in enumerate([(5, 50), (6, 60), (5, 55)]):
        rows.append(ExperienceRow(
            key=f"wan_t2v_{i}.json",
            workflow_type="Wan Text2Video",
            nodes=["UNETLoader", "CLIPTextEncode", "WanVideoSampler",
                   "WanVideoDecode", "VHS_VideoCombine"],
            parameters={"cfg": cfg, "steps": steps, "seed": 300 + i},
            problems=(
                ["[low] 未检测到 VAEDecode 节点，图像将无法解码 → 添加 VAEDecode"]
                if i == 0 else []
            ),
            missing_nodes=["WanVideoSampler", "WanVideoDecode"],
            coverage=0.4,
        ))

    return rows


def test_end_to_end():
    """端到端：聚类 → 统计 → 构建 → 落盘"""
    print("=" * 60)
    print("测试 D1：端到端归纳")
    print("=" * 60)

    rows = build_sample_rows()

    with TemporaryDirectory() as tmp:
        engine = ConsolidationEngine(
            store=KnowledgeStore(str(Path(tmp) / "out"))
        )
        knowledge = engine.consolidate(experiences=rows)

        print(f"  输入 {knowledge.source_count} 个 workflow，"
              f"形成 {len(knowledge.patterns)} 个模式")
        for p in knowledge.patterns:
            print(f"    {p.name}: {p.workflow_type} · {p.frequency} 个 "
                  f"· 覆盖 {p.coverage:.0%} · {p.level}")

        assert len(knowledge.patterns) == 3, \
            f"应聚成 3 个模式，实际 {len(knowledge.patterns)}"
        assert knowledge.ungrouped == 0, "所有样本都应归入某个模式"

        # 找到人像模式
        portrait = next(
            p for p in knowledge.patterns if "portrait" in p.name
        )
        print(f"\n  【{portrait.name}】")
        print(f"    共有节点: {portrait.common_nodes}")
        print(f"    可变部分: {portrait.variable_nodes}")
        print(f"    参数统计:")
        for name, stat in portrait.parameter_stats.items():
            print(f"      {name}: median={stat.median} "
                  f"count={stat.count} "
                  f"typical={stat.typical_range}")
        print(f"    常见问题:")
        for p in portrait.common_problems:
            print(f"      [{p['count']}次] {p['problem']}")
        print(f"    建议:")
        for r in portrait.recommendations:
            print(f"      - {r}")

        # 断言：分组统计生效
        assert portrait.parameter_stats["cfg"].median == 7.5, \
            f"人像组 cfg 中位数应为 7.5，实际 {portrait.parameter_stats['cfg'].median}"
        assert portrait.parameter_stats["sampler_name"].most_common \
            == "dpmpp_2m"

        # 断言：不同类型的同一参数统计不同
        wan = next(
            p for p in knowledge.patterns if "video" in p.name
        )
        sd15 = next(
            p for p in knowledge.patterns if "text2image" in p.name
        )
        print(f"\n  跨模式 steps 中位数:")
        print(f"    {sd15.name}: {sd15.parameter_stats['steps'].median}")
        print(f"    {portrait.name}: {portrait.parameter_stats['steps'].median}")
        print(f"    {wan.name}: {wan.parameter_stats['steps'].median}")

        assert wan.parameter_stats["steps"].median == 55, \
            f"Wan 组应独立统计，实际 {wan.parameter_stats['steps'].median}"
        assert sd15.parameter_stats["steps"].median == 22
        assert portrait.parameter_stats["steps"].median == 29

        # 断言：缺卡节点被记录（值得建卡的线索）
        assert "WanVideoSampler" in wan.missing_nodes
        assert any("还没有知识卡" in r for r in wan.recommendations)

        # 断言：跨模式对比
        assert knowledge.global_observations, "应有全局观察"
        steps_notes = [
            o for o in knowledge.global_observations if "steps" in o
        ]
        print(f"\n  跨模式 steps 对比: {steps_notes}")
        assert steps_notes, "不同流程 steps 差异大，应产出对比结论"

    print("端到端归纳正确 [OK]\n")


def test_store_markdown_output():
    """测试落盘为 Markdown 且可读回"""
    print("=" * 60)
    print("测试 D2：Markdown 落盘")
    print("=" * 60)

    rows = build_sample_rows()

    with TemporaryDirectory() as tmp:
        out = Path(tmp) / "patterns"
        engine = ConsolidationEngine(
            store=KnowledgeStore(str(out))
        )
        engine.consolidate(experiences=rows)

        files = sorted(p.name for p in out.glob("*.md"))
        print(f"  产出文件: {files}")

        assert "index.md" in files
        assert len(files) == 4, "3 个模式 + index.md"

        # 索引应可读
        index_text = (out / "index.md").read_text(encoding="utf-8")
        print()
        print("\n".join(index_text.split("\n")[:12]))
        print()
        assert "| 模式 | 类型 | 样本 |" in index_text
        assert "全局观察" in index_text

        # 单个模式文件
        portrait_file = next(
            p for p in out.glob("*.md")
            if p.name != "index.md" and "portrait" in p.name
        )
        text = portrait_file.read_text(encoding="utf-8")
        print(f"  --- {portrait_file.name} ---")
        print("\n".join(text.split("\n")[:16]))
        print()

        assert text.startswith("---"), "应有 frontmatter"
        assert "frequency:" in text
        assert "common_nodes:" in text
        assert "## 典型参数" in text
        assert "## 常见问题" in text
        # 不能出现 Python 字面量
        assert "{'count'" not in text

        # 读回
        store = KnowledgeStore(str(out))
        loaded = store.load_all()
        print(f"  读回 {len(loaded)} 个模式: "
              f"{[p.name for p in loaded]}")
        assert len(loaded) == 3
        assert all(p.frequency > 0 for p in loaded)

    print("Markdown 落盘正确 [OK]\n")


def test_grep_friendliness():
    """测试产出可被 grep 交叉检索"""
    print("=" * 60)
    print("测试 D3：文本可检索")
    print("=" * 60)

    rows = build_sample_rows()

    with TemporaryDirectory() as tmp:
        out = Path(tmp) / "patterns"
        ConsolidationEngine(
            store=KnowledgeStore(str(out))
        ).consolidate(experiences=rows)

        # 检索「哪些模式提到 LoRA」
        hits = [
            p.name for p in out.glob("*.md")
            if p.name != "index.md"
            and "LoraLoader" in p.read_text(encoding="utf-8")
        ]
        print(f"  含 LoraLoader 的模式: {hits}")
        assert len(hits) >= 1

        # 检索「哪些模式提到了 CFG 风险」
        risk_hits = [
            p.name for p in out.glob("*.md")
            if p.name != "index.md"
            and "风险" in p.read_text(encoding="utf-8")
        ]
        print(f"  含风险提示的模式: {risk_hits}")

        print("文本可检索 [OK]\n")


def test_engine_from_real_records():
    """端到端：用真实学习记录归纳"""
    print("=" * 60)
    print("测试 D4：从真实学习记录归纳")
    print("=" * 60)

    from engine.workflow_learning import LearningStore, STATE_DIR

    records = LearningStore().completed_records()
    if not records:
        print("  没有学习记录 —— 先运行 workflow_learning.learn_folder()")
        return

    print(f"  找到 {len(records)} 条真实学习记录")

    with TemporaryDirectory() as tmp:
        engine = ConsolidationEngine(
            store=KnowledgeStore(str(Path(tmp) / "out"))
        )
        # 不传 experiences，直接从学习记录读
        knowledge = engine.consolidate()

        print(f"\n{engine.render_report(knowledge)}")

        # 归纳输入经过内容去重 + 空节点记录过滤，
        # source_count ≤ 记录数（2026-10-06 起去重是聚合层默认口径）
        assert 0 < knowledge.source_count <= len(records)
        if knowledge.source_count >= 2:
            assert knowledge.patterns, "应至少形成一个模式"

    print("真实记录归纳正常 [OK]\n")


def test_empty_input():
    """测试无输入时的行为"""
    print("=" * 60)
    print("测试 D5：空输入")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        engine = ConsolidationEngine(
            store=KnowledgeStore(str(Path(tmp) / "out"))
        )

        # 空列表
        knowledge = engine.consolidate(experiences=[])
        print(f"  空列表: {knowledge.source_count} 源，"
              f"{len(knowledge.patterns)} 模式")
        assert knowledge.patterns == []

        # 全部节点为空
        knowledge2 = engine.consolidate(
            experiences=[ExperienceRow(key="a", nodes=[])]
        )
        assert knowledge2.patterns == []

        report = engine.render_report(knowledge)
        print(f"  报告: {report}")
        assert report

    print("空输入处理正确 [OK]\n")


def test_loader_compat():
    """测试加载器兼容 dict 与旧路径参数"""
    print("=" * 60)
    print("测试 D6：加载器兼容")
    print("=" * 60)

    loader = ExperienceLoader()

    rows = loader.load_rows([
        {
            "key": "a.json",
            "type": "SDXL",
            "nodes": ["KSampler", "VAEDecode", "KSampler"],
            "parameters": {"cfg": 7},
            "problems": ["[low] x"],
            "coverage": 1.0,
        },
    ])

    print(f"  {rows}")
    assert len(rows) == 1
    # 重复节点应去重（CLIPTextEncode 常出现两次）
    assert rows[0].nodes == ["KSampler", "VAEDecode"]
    assert rows[0].parameters == {"cfg": 7}
    assert rows[0].problems == ["[low] x"]

    # 旧参数名 workflow_type 也认
    rows2 = loader.load_rows([
        {"key": "b", "workflow_type": "SD1.5", "nodes": ["KSampler"]}
    ])
    assert rows2[0].workflow_type == "SD1.5"

    # 传字符串路径（设计稿用法）应给提示而非崩溃
    rows3 = loader.load("workflow_experience.json")
    print(f"  传旧路径后读到 {len(rows3)} 条（来自实际记录）")

    print("加载器兼容正确 [OK]\n")


def main():
    """运行全部测试"""
    print("\n" + "=" * 60)
    print("Knowledge Consolidation 模块测试")
    print("=" * 60 + "\n")

    test_jaccard()
    test_cluster_ignores_extra_nodes()
    test_cluster_ignores_note_nodes()
    test_cluster_separates_types()
    test_min_frequency()
    test_pattern_naming()

    test_parameter_stats_per_group()
    test_parameter_stats_quality()
    test_parameter_stats_textual()
    test_cross_pattern_comparison()

    test_common_problems_aggregation()
    test_recommendations_risk()
    test_sample_size_honesty()

    test_end_to_end()
    test_store_markdown_output()
    test_grep_friendliness()
    test_engine_from_real_records()
    test_empty_input()
    test_loader_compat()

    print("=" * 60)
    print("全部测试通过")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
