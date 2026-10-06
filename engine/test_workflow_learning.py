r"""
Workflow Learning 模块测试

从仓库根目录运行：
    cd "F:\Program Files\ComfyUI"
    python -X utf8 -m engine.test_workflow_learning

-X utf8 必须加，否则中文输出乱码。

测试全部在 TemporaryDirectory 里跑，不写脏仓库。
"""

import sys
import json
import shutil
from pathlib import Path
from tempfile import TemporaryDirectory

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from engine.workflow_learning import (
    LearningRecord,
    LearningStore,
    WorkflowScanner,
    WorkflowLearner,
    BatchWorkflowLearner,
    create_batch_learner,
    load_png_workflow,
    to_markdown,
    from_markdown,
    parse_frontmatter,
    build_frontmatter,
    split_frontmatter,
    WORKFLOWS_DIR,
    STATE_DIR,
    INDEX_PATH,
    record_path_for,
    index_link_for,
    relative_to_project,
    ensure_state_dir,
)

# 保留临时目录引用，避免被 GC 提前回收
_TEMPS = []


def temp_path() -> str:
    d = TemporaryDirectory()
    _TEMPS.append(d)
    return d.name


def write_json(path: Path, data: dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    # 刻意用 utf-8 + BOM 模拟 ComfyUI 的真实导出
    with open(path, "w", encoding="utf-8-sig") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


SAMPLE_WORKFLOW = {
    "last_node_id": 6,
    "last_link_id": 3,
    "nodes": [
        {"id": 1, "type": "CheckpointLoaderSimple",
         "widgets_values": ["model.safetensors"], "outputs": []},
        {"id": 2, "type": "CLIPTextEncode", "widgets_values": ["a cat"]},
        {"id": 3, "type": "EmptyLatentImage", "widgets_values": [512, 512, 1]},
        {"id": 4, "type": "KSampler",
         "widgets_values": [1, "random", 20, 7.0, "euler", "normal", 1.0]},
        {"id": 5, "type": "VAEDecode"},
        {"id": 6, "type": "SaveImage"},
    ],
    "links": [],
}


def build_learner(**extra):
    """装配真实模块的 WorkflowLearner"""
    from engine.workflow_parser import WorkflowParser, NodeKnowledgeLoader
    from engine.workflow_analyzer import WorkflowAnalyzer
    from engine.diagnostics import DiagnosticEngine
    from engine.retrieval import KnowledgeRetriever
    from engine.autonomous_learning import (
        WorkflowExplorer,
        KnowledgeGapDetector,
    )

    project = Path(__file__).parent.parent
    knowledge_dir = project / "comfyui_library" / "knowledge"

    retriever = KnowledgeRetriever()
    retriever.build_index(
        index_path=str(Path(temp_path()) / "index.json"),
        knowledge_dir=str(knowledge_dir),
        experience_store=str(
            project / "engine" / "learning_loop" / "experience_store.json"
        ),
        evolution_store=str(
            project / "engine" / "knowledge_evolution" / "evolution_store.json"
        ),
    )

    loader = NodeKnowledgeLoader(str(knowledge_dir))

    return WorkflowLearner(
        analyzer=WorkflowAnalyzer(),
        retriever=retriever,
        parser=WorkflowParser(loader),
        diagnostics=DiagnosticEngine(),
        explorer=WorkflowExplorer(
            analyzer=WorkflowAnalyzer(), knowledge_loader=loader
        ),
        gap_detector=KnowledgeGapDetector(),
        **extra,
    )


def sample_record(**overrides) -> LearningRecord:
    data = dict(
        workflow_name="basic",
        file_path="comfyui_library/workflows/sd1.5/basic.json",
        key="sd1.5/basic.json",
        workflow_type="Text To Image",
        nodes=["CheckpointLoaderSimple", "CLIPTextEncode", "KSampler"],
        important_nodes=["KSampler"],
        covered_nodes=["CheckpointLoaderSimple", "CLIPTextEncode", "KSampler"],
        missing_nodes=[],
        pipeline=["Model", "Condition", "Sampling"],
        parameters={"cfg": 7.0, "steps": 20},
        patterns=["text_to_image"],
        content_hash="abc123def456",
        learned_at="2026-10-06T01:12:39",
        knowledge_refs=["KSampler"],
        discoveries=["核心节点齐备"],
    )
    data.update(overrides)
    return LearningRecord(**data)


# ============================================================
# A. frontmatter 读写
# ============================================================

def test_frontmatter_roundtrip():
    """测试 frontmatter 解析与序列化"""
    print("=" * 60)
    print("测试 A1：frontmatter 往返")
    print("=" * 60)

    front = build_frontmatter({
        "key": "sd1.5/basic.json",
        "name": "basic",
        "coverage": 0.778,
        "learned_at": "2026-10-06T01:12:39",
        "nodes": ["KSampler", "VAEDecode"],
        "missing": [],
        "error": None,
    })
    print(front)

    parsed = parse_frontmatter(front)
    print(f"  解析结果: {parsed}")

    assert parsed["key"] == "sd1.5/basic.json"
    assert parsed["name"] == "basic"
    assert parsed["nodes"] == ["KSampler", "VAEDecode"]
    assert parsed["missing"] == []
    # 解析器不猜类型，一律返回 str；数值转换由 from_markdown 负责
    assert parsed["coverage"] == "0.778"
    # None 值不写入
    assert "error" not in parsed

    # split 必须正确剥离分隔符
    body, rest = split_frontmatter(front + "\n# 标题\n\n正文\n")
    print(f"  正文: {rest.strip()[:40]!r}")
    assert rest.strip().startswith("# 标题")
    assert "key:" in body

    # 无 frontmatter 的文本应原样返回
    no_front = "# 只是标题\n\n正文"
    body2, rest2 = split_frontmatter(no_front)
    assert body2 == ""
    assert rest2 == no_front, "无 frontmatter 时不应吞掉内容"

    # 含半角逗号的元素必须能被引号保护，否则读回时被切错
    tricky = sample_record(
        diagnostic_issues=[
            "[medium] CFG 偏高, 建议降到 7-10, 或更低",
            '[low] 含引号的 "奇怪" 描述',
        ]
    )
    back = from_markdown(to_markdown(tricky))
    print(f"  含逗号条目往返: {back.diagnostic_issues}")
    assert back.diagnostic_issues == tricky.diagnostic_issues, \
        f"含逗号的条目被切错了: {back.diagnostic_issues}"

    print("frontmatter 往返正确 [OK]\n")


def test_record_markdown_roundtrip():
    """测试学习记录 ↔ Markdown 往返"""
    print("=" * 60)
    print("测试 A2：记录 Markdown 往返")
    print("=" * 60)

    record = sample_record()
    md = to_markdown(record)
    print()
    print(md)
    print()

    # 不能出现 Python 字面量
    assert "['" not in md, "不应出现 Python 列表字面量"

    restored = from_markdown(md)
    print(f"  还原: key={restored.key} type={restored.workflow_type} "
          f"覆盖={restored.coverage:.0%}")

    assert restored.key == record.key
    assert restored.workflow_name == record.workflow_name
    assert restored.workflow_type == record.workflow_type
    assert restored.nodes == record.nodes
    assert restored.content_hash == record.content_hash
    assert abs(restored.coverage - record.coverage) < 0.01
    assert restored.important_nodes == [], "important_nodes 不在 frontmatter 内"

    # 缺卡节点应保留
    with_missing = sample_record(missing_nodes=["LoraLoader"])
    assert from_markdown(
        to_markdown(with_missing)
    ).missing_nodes == ["LoraLoader"]

    print("记录往返正确 [OK]\n")


def test_coverage_reconstruction():
    """测试覆盖率能反推 covered_nodes"""
    print("=" * 60)
    print("测试 A3：覆盖率反推")
    print("=" * 60)

    # 4 节点，3 个有卡 → coverage 0.75
    record = sample_record(
        nodes=["A", "B", "C", "D"],
        covered_nodes=["A", "B", "C"],
    )
    md = to_markdown(record)
    restored = from_markdown(md)

    print(f"  原始覆盖: {record.coverage:.0%}")
    print(f"  还原覆盖: {restored.coverage:.0%}")
    assert abs(restored.coverage - 0.75) < 0.01, \
        f"覆盖率应还原为 0.75，实际 {restored.coverage}"
    print("覆盖率反推正确 [OK]\n")


# ============================================================
# B. LearningStore
# ============================================================

def test_store_markdown_backend():
    """测试存储走 Markdown 而非 JSON"""
    print("=" * 60)
    print("测试 B1：Markdown 存储")
    print("=" * 60)

    root = temp_path()
    store = LearningStore(root)

    # 什么都没学
    assert store.exists("sd1.5/basic.json") is False
    assert store.all_records() == []

    record = sample_record()
    path = store.write(record)
    print(f"  写入: {path}")

    assert Path(path).exists(), "应生成文件"
    assert path.endswith(".md"), "应是 Markdown 文件"
    assert "registry.json" not in str(store.root), \
        "不该再有 JSON 存储"

    # 目录结构应镜像源文件
    assert Path(path).parent.name == "sd1.5"
    assert Path(path).stem == "basic"

    # 文件存在即已学
    assert store.exists("sd1.5/basic.json")
    assert store.exists("sd1.5/basic.json", "abc123def456")
    # 指纹变了 → 需重学
    assert not store.exists("sd1.5/basic.json", "different")
    assert store.needs_learn("sd1.5/basic.json", "different")

    # 读回来
    loaded = store.read("sd1.5/basic.json")
    assert loaded is not None
    assert loaded.nodes == record.nodes

    print(f"  全部记录: {[r.key for r in store.all_records()]}")
    assert len(store.all_records()) == 1

    # 删除
    assert store.remove("sd1.5/basic.json")
    assert not store.exists("sd1.5/basic.json")
    assert not Path(path).exists()
    print("Markdown 存储正确 [OK]\n")


def test_store_failed_record_retried():
    """测试失败的记录会被重试"""
    print("=" * 60)
    print("测试 B2：失败记录重试")
    print("=" * 60)

    store = LearningStore(temp_path())

    failed = sample_record(
        key="broken.json",
        status="failed",
        error="解析失败",
        content_hash="h1",
    )
    store.write(failed)

    print(f"  失败记录已写入，exists = {store.exists('broken.json', 'h1')}")
    assert not store.exists("broken.json", "h1"), \
        "失败的记录不该算已学，否则永远不会被重试"
    assert store.needs_learn("broken.json", "h1")

    print("失败记录重试正确 [OK]\n")


def test_store_aggregates():
    """测试聚合统计（供挖模式用）"""
    print("=" * 60)
    print("测试 B3：聚合统计")
    print("=" * 60)

    store = LearningStore(temp_path())

    datasets = [
        (["KSampler", "VAEDecode", "CheckpointLoaderSimple"], ["VAEDecode"]),
        (["KSampler", "VAEDecode"], ["VAEDecode"]),
        (["KSampler", "LoraLoader"], ["LoraLoader"]),
    ]

    for i, (nodes, missing) in enumerate(datasets):
        store.write(sample_record(
            key=f"w{i}.json",
            workflow_name=f"w{i}",
            nodes=nodes,
            covered_nodes=[n for n in nodes if n not in missing],
            missing_nodes=missing,
            # node_frequency 按内容指纹去重（聚合层默认口径），
            # 夹具必须给每条独立指纹，否则三条会被当成同一文件
            content_hash=f"hash-{i}",
        ))

    freq = store.node_frequency()
    print(f"  节点频次: {freq}")
    assert freq["KSampler"] == 3
    assert freq["VAEDecode"] == 2

    common = store.common_nodes(min_count=2)
    print(f"  至少出现 2 次: {common}")
    assert "KSampler" in common and "VAEDecode" in common
    assert "LoraLoader" not in common

    summary = store.coverage_summary()
    print(f"  覆盖概览: {summary}")
    assert summary["total"] == 3
    # VAEDecode 在两个 workflow 里都缺卡 → 属共性缺口，值得建卡
    assert "VAEDecode" in summary["nodes_with_no_card"]
    # LoraLoader 只缺一次 → 只是个例，不算共性缺口
    assert "LoraLoader" not in summary["nodes_with_no_card"]

    stats = store.summary()
    print(f"  概览: {stats}")
    assert stats["total"] == 3 and stats["completed"] == 3

    print("聚合统计正确 [OK]\n")


def test_store_index_generated():
    """测试汇总索引自动生成"""
    print("=" * 60)
    print("测试 B4：汇总索引")
    print("=" * 60)

    root = Path(temp_path())
    store = LearningStore(str(root))

    store.write(sample_record(key="sd1.5/basic.json"))
    store.write(sample_record(
        key="sdxl/portrait.json",
        workflow_name="portrait",
        workflow_type="SDXL Portrait",
        missing_nodes=["IPAdapterApply"],
        content_hash="zzz999",
    ))
    store.write(sample_record(
        key="flux/bad.json",
        status="failed",
        error="缺 nodes 字段",
    ))

    index_path = root / "index.md"
    assert index_path.exists(), "应生成 index.md"

    text = index_path.read_text(encoding="utf-8")
    print()
    print(text)
    print()

    assert "sd1.5/basic.json" in text
    assert "sdxl/portrait.json" in text
    # 链接应指向记录文件
    assert "(sd1.5/basic.md)" in text, "应给出可点击的相对链接"
    assert "Text To Image" in text
    assert "100%" in text
    # 失败项应单独列出
    assert "未完成" in text
    assert "缺 nodes 字段" in text

    # index.md 本身不该被当成一条记录
    records = store.all_records()
    print(f"  记录数: {len(records)}（应为 3，index.md 不计入）")
    assert len(records) == 3

    print("汇总索引正确 [OK]\n")


def test_prune_missing():
    """测试清理已删除文件的记录"""
    print("=" * 60)
    print("测试 B5：清理失效记录")
    print("=" * 60)

    store = LearningStore(temp_path())

    for key in ("sd1.5/basic.json", "sdxl/portrait.json"):
        store.write(sample_record(key=key))

    assert len(store.all_records()) == 2

    # sdxl/portrait.json 对应的文件被删了
    pruned = store.prune_missing(["sd1.5/basic.json"])
    print(f"  清理: {pruned}")

    assert pruned == ["sdxl/portrait.json"]
    assert [r.key for r in store.all_records()] == ["sd1.5/basic.json"]
    # 空目录应被清掉
    assert not (Path(store.root) / "sdxl").exists()

    print("清理正确 [OK]\n")


# ============================================================
# C. 扫描与路径
# ============================================================

def test_scanner_filters_sidecars_and_state():
    """测试扫描器跳过伴生文件与状态目录"""
    print("=" * 60)
    print("测试 C1：扫描过滤")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        root = Path(tmp) / "workflows"
        write_json(root / "sd1.5" / "basic.json", SAMPLE_WORKFLOW)
        write_json(root / "sd1.5" / "_workflow.json", SAMPLE_WORKFLOW)
        write_json(root / "sd1.5" / "_prompt.json", {"3": {"class_type": "KS"}})
        (root / "sd1.5" / "out.png").write_bytes(b"\x89PNG\r\n\x1a\n")
        write_json(root / "sdxl" / "basic.json", SAMPLE_WORKFLOW)

        # 模拟状态目录
        write_json(root / "learning" / "old_registry.json", {"x": 1})
        (root / "learning" / "sd1.5").mkdir(parents=True, exist_ok=True)
        (root / "learning" / "sd1.5" / "basic.md").write_text(
            to_markdown(sample_record()), encoding="utf-8"
        )

        found = WorkflowScanner().scan(str(root))
        keys = [f["key"] for f in found]
        print(f"  扫到: {keys}")

        assert "sd1.5/basic.json" in keys
        assert "sdxl/basic.json" in keys, "同名文件应各自独立"
        assert "sd1.5/out.png" in keys
        # 伴生文件必须跳过（_prompt.json 是 API 格式）
        assert "sd1.5/_prompt.json" not in keys
        assert "sd1.5/_workflow.json" not in keys
        # 状态目录必须跳过（否则把自己的记录当成 workflow，无限循环）
        assert not any("learning" in k for k in keys), \
            f"状态目录被当成了 workflow: {keys}"

        # 真实目录也要干净
        real = WorkflowScanner().scan(str(WORKFLOWS_DIR))
        real_keys = [f["key"] for f in real]
        print(f"  真实目录: {real_keys}")
        assert not any("learning" in k for k in real_keys)

        # 不存在的目录返回空列表
        assert WorkflowScanner().scan(str(Path(tmp) / "无")) == []

    print("扫描过滤正确 [OK]\n")


def test_png_extraction():
    """测试 PNG 元数据提取"""
    print("=" * 60)
    print("测试 C2：PNG 元数据")
    print("=" * 60)

    png = WORKFLOWS_DIR / "sd1.5" / "lora.png"
    if not png.exists():
        print("  找不到 lora.png，跳过")
        return

    data = load_png_workflow(str(png))
    if data is None:
        print("  lora.png 未内嵌 workflow 元数据，跳过")
        return

    nodes = [n.get("type") for n in data.get("nodes", []) if n.get("type")]
    print(f"  提取到 {len(nodes)} 个节点: {nodes[:6]}")
    assert nodes
    assert data.get("_extracted_from") == "png"
    assert load_png_workflow(str(png) + ".nope") is None

    print("PNG 提取正确 [OK]\n")


def test_unified_paths():
    """测试路径统一"""
    print("=" * 60)
    print("测试 C3：统一路径")
    print("=" * 60)

    print(f"  workflow 目录: {WORKFLOWS_DIR}")
    print(f"  状态目录:      {STATE_DIR}")
    print(f"  索引文件:      {INDEX_PATH}")

    assert STATE_DIR.parent == WORKFLOWS_DIR, \
        "状态应在 workflows/ 下"
    assert STATE_DIR.name == "learning"
    assert INDEX_PATH.parent == STATE_DIR

    # 记录路径应镜像源文件结构
    assert record_path_for("sd1.5/basic.json").name == "basic.md"
    assert record_path_for("flux/a.png").name == "a.md"
    assert record_path_for("wan\\x.json").name == "x.md", \
        "Windows 分隔符也要处理"
    assert index_link_for("sd1.5/basic.json") == "sd1.5/basic.md"

    # 相对路径
    rel = relative_to_project(WORKFLOWS_DIR / "sd1.5" / "basic.json")
    print(f"  相对路径: {rel}")
    assert rel == "comfyui_library/workflows/sd1.5/basic.json"
    assert "F:" not in rel, "换机器会失效"

    ensure_state_dir()
    assert STATE_DIR.exists()

    # 默认参数应是 None（表示用统一位置），不是硬编码字符串
    assert LearningStore.__init__.__defaults__[0] is None
    assert BatchWorkflowLearner.learn_folder.__defaults__[0] is None

    print("统一路径正确 [OK]\n")


# ============================================================
# D. 端到端
# ============================================================

def test_learn_single_file():
    """端到端：学一个真实 workflow"""
    print("=" * 60)
    print("测试 D1：单文件学习")
    print("=" * 60)

    wf = WORKFLOWS_DIR / "sd1.5" / "basic.json"
    if not wf.exists():
        print("  找不到 basic.json，跳过")
        return

    learner = build_learner()
    record = learner.learn(str(wf), key="sd1.5/basic.json")

    print(f"  状态: {record.status}")
    print(f"  类型: {record.workflow_type}")
    print(f"  节点: {record.nodes}")
    print(f"  流程链: {' → '.join(record.pipeline)}")
    print(f"  参数: cfg={record.parameters.get('cfg')}")
    print(f"  覆盖: {record.coverage:.0%}")
    print(f"  发现: {record.discoveries[:2]}")

    assert record.status == "completed", record.error
    assert record.nodes and record.pipeline
    assert record.parameters.get("cfg") is not None
    assert record.content_hash
    # 路径应相对化
    assert record.file_path.startswith("comfyui_library/")
    assert "/" not in record.workflow_name
    assert "\\" not in record.workflow_name

    print("单文件学习正确 [OK]\n")


def test_learn_bom_and_bad_input():
    """测试 BOM 与异常输入"""
    print("=" * 60)
    print("测试 D2：BOM 与异常输入")
    print("=" * 60)

    root = Path(temp_path())
    learner = build_learner()

    wf = root / "bom.json"
    write_json(wf, SAMPLE_WORKFLOW)
    assert wf.read_bytes()[:3] == b"\xef\xbb\xbf", "应为带 BOM 的文件"

    record = learner.learn(str(wf))
    print(f"  带 BOM: {record.status}")
    assert record.status == "completed", \
        f"带 BOM 应能解析（utf-8 读会失败）: {record.error}"
    assert record.nodes

    bad = root / "bad.json"
    bad.write_text("{ 不是 json", encoding="utf-8")
    r1 = learner.learn(str(bad))
    print(f"  非法 JSON: {r1.status} - {r1.error}")
    assert r1.status == "failed" and r1.error

    r2 = learner.learn(str(root / "nope.json"))
    assert r2.status == "failed" and "不存在" in r2.error

    arr = root / "arr.json"
    arr.write_text("[1,2,3]", encoding="utf-8")
    assert learner.learn(str(arr)).status == "failed"

    empty = root / "empty.json"
    write_json(empty, {"nodes": []})
    r3 = learner.learn(str(empty))
    print(f"  空 nodes: {r3.status}")
    assert r3.status == "completed", "空工作流不算失败"

    print("BOM 与异常处理正确 [OK]\n")


def test_learn_folder_idempotent():
    """端到端：批量学习 + 幂等 + 内容变更重学"""
    print("=" * 60)
    print("测试 D3：批量学习与幂等")
    print("=" * 60)

    root = Path(temp_path())
    wf_dir = root / "workflows"

    write_json(wf_dir / "sd1.5" / "basic.json", SAMPLE_WORKFLOW)
    write_json(wf_dir / "sdxl" / "basic.json", SAMPLE_WORKFLOW)
    write_json(wf_dir / "flux" / "_prompt.json", {"x": {}})

    learner = build_learner()
    store = LearningStore(str(root / "state"))
    batch = BatchWorkflowLearner(
        learner=learner, store=store, verbose=False
    )

    first = batch.learn_folder(str(wf_dir))
    print(f"  第一次: 找到 {first['total_found']}，学习 {first['learned']}，"
          f"跳过 {first['skipped']}，失败 {first['failed']}")
    assert first["total_found"] == 2, "_prompt.json 应跳过"
    assert first["learned"] == 2
    assert first["failed"] == 0

    # 记录文件应落盘，且是 Markdown
    records = sorted(Path(store.root).rglob("*.md"))
    print(f"  记录文件: {[p.relative_to(store.root).as_posix() for p in records]}")
    assert len(records) == 3, "2 条记录 + index.md"
    assert any(p.name == "index.md" for p in records)

    # index.md 应能打开且含链接
    index_text = (Path(store.root) / "index.md").read_text(encoding="utf-8")
    assert "(sd1.5/basic.md)" in index_text

    # 第二次全部跳过
    second = batch.learn_folder(str(wf_dir))
    print(f"  第二次: 学习 {second['learned']}，跳过 {second['skipped']}")
    assert second["learned"] == 0, "重复运行不应重复学习"
    assert second["skipped"] == 2

    # 改内容 → 触发重学
    modified = json.loads(json.dumps(SAMPLE_WORKFLOW))
    for node in modified["nodes"]:
        if node["type"] == "KSampler":
            node["widgets_values"] = [1, "random", 20, 28.0,
                                      "euler", "normal", 1.0]
    write_json(wf_dir / "sd1.5" / "basic.json", modified)

    pending = batch.pending(str(wf_dir))
    print(f"  改动后待学: {[p['key'] for p in pending]}")
    assert "sd1.5/basic.json" in [p["key"] for p in pending], \
        "内容变更必须触发重学"

    third = batch.learn_folder(str(wf_dir))
    print(f"  第三次: 学习 {third['learned']}，跳过 {third['skipped']}")
    assert third["learned"] == 1

    # 重学后应记下新参数与体检结果
    record = learner.learn(str(wf_dir / "sd1.5" / "basic.json"),
                           key="sd1.5/basic.json")
    print(f"  重学后 cfg={record.parameters.get('cfg')}，"
          f"体检 {len(record.diagnostic_issues)} 项")
    assert record.parameters.get("cfg") == 28.0
    assert record.diagnostic_issues, "cfg=28 应被体检出问题"

    # 删除文件 → 清理记录
    (wf_dir / "sdxl" / "basic.json").unlink()
    fourth = batch.learn_folder(str(wf_dir))
    print(f"  删除后清理: {fourth['pruned']}")
    assert "sdxl/basic.json" in fourth["pruned"]

    # force 强制重学
    forced = batch.learn_folder(str(wf_dir), force=True)
    print(f"  force: 学习 {forced['learned']}")
    assert forced["learned"] == 1

    print("批量与幂等正确 [OK]\n")


def test_grep_friendliness():
    """测试可被 grep 交叉检索（选 Markdown 而非 JSON 的核心理由）"""
    print("=" * 60)
    print("测试 D4：文本可检索")
    print("=" * 60)

    store = LearningStore(temp_path())

    store.write(sample_record(key="a.json", nodes=["KSampler", "LoraLoader"]))
    store.write(sample_record(key="b.json", nodes=["KSampler", "ControlNetApply"]))
    store.write(sample_record(key="c.json", nodes=["WanVideoSampler"]))

    # 模拟 grep -rl "LoraLoader"：哪些记录提到这个节点
    hits = []
    for path in Path(store.root).rglob("*.md"):
        if path.name == "index.md":
            continue
        if "LoraLoader" in path.read_text(encoding="utf-8"):
            hits.append(path.name)

    print(f"  含 LoraLoader 的记录: {hits}")
    assert hits == ["a.md"], "文本检索应精确命中"

    # 汇总表也应可 grep
    index_text = (Path(store.root) / "index.md").read_text(encoding="utf-8")
    assert "a.json" in index_text
    assert "c.json" in index_text

    print("文本可检索 [OK]\n")


def test_default_location_end_to_end():
    """端到端：不传路径，走统一位置（跑完还原）"""
    print("=" * 60)
    print("测试 D5：默认位置端到端")
    print("=" * 60)

    ensure_state_dir()

    # 备份现有状态，并清空 —— 测试必须自足，
    # 不能依赖统一位置恰好是空的（手动跑过就会留记录）
    backup = {}
    for path in list(STATE_DIR.rglob("*")):
        if path.is_file():
            backup[path] = path.read_text(encoding="utf-8")
            path.unlink()
    for path in sorted(STATE_DIR.rglob("*"), reverse=True):
        if path.is_dir():
            try:
                path.rmdir()
            except OSError:
                pass

    try:
        learner = build_learner()
        batch = BatchWorkflowLearner(learner=learner, verbose=False)

        print(f"  记录根目录: {batch.store.root}")
        assert batch.store.root == STATE_DIR

        summary = batch.learn_folder()
        print(f"  批次: 找到 {summary['total_found']}，"
              f"学习 {summary['learned']}，跳过 {summary['skipped']}")
        # 不硬编码样本数（目录会持续扩充）；
        # 关键不变量：扫描到的 = 学到的，状态目录/伴生文件不算 workflow
        expected = len(WorkflowScanner().scan(str(WORKFLOWS_DIR)))
        assert summary["total_found"] == expected, \
            "状态目录里的文件不应被算成 workflow"
        assert summary["learned"] == expected

        # 记录落在统一位置，目录结构镜像
        record = batch.store.read("sd1.5/basic.json")
        print(f"  读回记录: {record.key} 覆盖 {record.coverage:.0%}")
        assert record is not None
        assert record.coverage > 0.8

        # index.md 应在统一位置
        assert INDEX_PATH.exists()
        print(f"  索引: {INDEX_PATH.name}")

        # 重跑全部跳过
        again = batch.learn_folder()
        print(f"  第二次: 学习 {again['learned']}，跳过 {again['skipped']}")
        assert again["learned"] == 0, "重跑应全部跳过"

        # 路径全相对
        for path in STATE_DIR.rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            assert "F:\\" not in text, f"{path.name} 含绝对路径"
            assert "F:/" not in text, f"{path.name} 含绝对路径"

    finally:
        # 还原仓库
        for path in list(STATE_DIR.rglob("*")):
            if path.is_file():
                path.unlink()
        for path in sorted(
            STATE_DIR.rglob("*"), reverse=True
        ):
            if path.is_dir():
                try:
                    path.rmdir()
                except OSError:
                    pass

        for path, content in backup.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(content, encoding="utf-8")

    print("默认位置端到端正确 [OK]\n")


def test_minimal_dependencies():
    """测试只注入 analyzer 也能工作"""
    print("=" * 60)
    print("测试 D6：最小依赖")
    print("=" * 60)

    from engine.workflow_analyzer import WorkflowAnalyzer

    wf = Path(temp_path()) / "min.json"
    write_json(wf, SAMPLE_WORKFLOW)

    learner = WorkflowLearner(analyzer=WorkflowAnalyzer())
    record = learner.learn(str(wf))
    print(f"  仅 analyzer: {record.status}，节点 {len(record.nodes)}")
    assert record.status == "completed" and record.nodes

    bare = WorkflowLearner(auto_modules=False)
    bare_record = bare.learn(str(wf))
    print(f"  无模块: {bare_record.status}，节点 {len(bare_record.nodes)}")
    assert bare_record.status == "completed"
    assert bare_record.nodes, "没有 analyzer 时应从原始 JSON 取节点"

    print("最小依赖正确 [OK]\n")


def main():
    """运行全部测试"""
    print("\n" + "=" * 60)
    print("Workflow Learning 模块测试")
    print("=" * 60 + "\n")

    test_frontmatter_roundtrip()
    test_record_markdown_roundtrip()
    test_coverage_reconstruction()

    test_store_markdown_backend()
    test_store_failed_record_retried()
    test_store_aggregates()
    test_store_index_generated()
    test_prune_missing()

    test_scanner_filters_sidecars_and_state()
    test_png_extraction()
    test_unified_paths()

    test_learn_single_file()
    test_learn_bom_and_bad_input()
    test_learn_folder_idempotent()
    test_grep_friendliness()
    test_default_location_end_to_end()
    test_minimal_dependencies()

    print("=" * 60)
    print("全部测试通过")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
