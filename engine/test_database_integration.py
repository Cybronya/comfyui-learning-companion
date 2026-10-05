r"""
database 集成测试 —— 三个引擎模块接入 WorkflowDatabase

从仓库根目录运行：
    cd "F:\Program Files\ComfyUI"
    python -X utf8 -m engine.test_database_integration

覆盖的接缝：
    A. database_bridge   LearningRecord ↔ 库 的翻译与「已学」判定
    B. workflow_learning 批量学习写库镜像 + 存量迁移
    C. learning_scheduler 查库判已学（含指纹变更 / 回退 Markdown）
    D. knowledge_consolidation 从库读结构化经验
    E. 端到端            文件 → 学习 → 库 → 调度跳过 → 归纳读取

全部走 TemporaryDirectory，不碰真实 storage/ 与 learning/。
"""

import json
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from engine.workflow_learning import (
    LearningRecord,
    LearningStore,
    BatchWorkflowLearner,
    WorkflowScanner,
    WorkflowLearner,
    STATUS_COMPLETED,
    STATUS_SKIPPED,
    STATUS_LEARNED,
    sync_record,
    sync_all,
    is_learned,
    workflow_record_of,
)
from engine.learning_scheduler import (
    LearningScheduler,
    TaskQueue,
    ScheduleStore,
)
from engine.knowledge_consolidation import (
    ExperienceLoader,
    create_consolidation_engine,
)
from comfyui_library.database import WorkflowDatabase


# ============================================================
# 测试数据
# ============================================================

BASE_NODES = [
    "CheckpointLoaderSimple", "CLIPTextEncode", "EmptyLatentImage",
    "KSampler", "VAEDecode", "SaveImage",
]


def make_record(key="sd1.5/basic", status=STATUS_COMPLETED, **kwargs):
    """构造一条 LearningRecord，字段可覆盖"""
    fields = dict(
        workflow_name=Path(key).stem,
        file_path=f"comfyui_library/workflows/{key}.json",
        key=key,
        status=status,
        content_hash=f"h-{key}",
        workflow_type="Text To Image",
        nodes=list(BASE_NODES),
        covered_nodes=["KSampler", "VAEDecode"],
        missing_nodes=["MarkdownNote"],
        parameters={"KSampler": {"cfg": 8.0, "steps": 24}},
        diagnostic_issues=["[warning] CFG值较高（当前 12.0）"],
        discoveries=["cfg 8 比 12 稳"],
        learned_at="2026-10-06 12:00:00",
    )
    fields.update(kwargs)
    return LearningRecord(**fields)


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )


SAMPLE_WORKFLOW = {
    "nodes": [
        {"id": i, "type": t, "widgets_values": []}
        for i, t in enumerate(BASE_NODES)
    ],
    "links": [],
}


class FakeLearner:
    """假 WorkflowLearner：不真学，按 key 产出记录"""

    def __init__(self, fail_keys=()):
        self.calls = []
        self.fail_keys = set(fail_keys)

    def learn(self, path, key=""):
        self.calls.append(key)
        if key in self.fail_keys:
            return LearningRecord(
                workflow_name=Path(path).stem,
                file_path=str(path), key=key,
                status="failed", error="模拟失败",
            )
        return make_record(key=key or Path(path).stem)


class FakeStore:
    """假 LearningStore：exists 可控，用于验证库优先 / 回退路径"""

    def __init__(self, exists_keys=()):
        self.exists_keys = set(exists_keys)
        self.written = []
        self.records = []

    def exists(self, key, content_hash=None):
        return key in self.exists_keys

    def completed_records(self):
        return self.records

    def write(self, record):
        self.written.append(record)
        self.records.append(record)
        return f"state/{record.key}.md"


def make_scheduler(tmp, store, database=None, learner=None):
    return LearningScheduler(
        scanner=WorkflowScanner(),
        store=store,
        learner=learner,
        queue=TaskQueue(max_retries=3),
        schedule_store=ScheduleStore(str(Path(tmp) / "queue.md")),
        database=database,
    )


# ============================================================
# A. database_bridge
# ============================================================

def test_workflow_record_of():
    """测试记录翻译：status 映射、字段搬运"""
    print("=" * 60)
    print("测试 A1：LearningRecord → WorkflowRecord")
    print("=" * 60)

    from engine.workflow_learning import workflow_record_of

    rec = make_record()
    wf = workflow_record_of(rec)
    assert wf.id == "sd1.5/basic"
    assert wf.status == STATUS_LEARNED, "completed 必须映射为 learned"
    assert wf.content_hash == rec.content_hash
    assert wf.nodes == rec.nodes
    assert wf.workflow_type == rec.workflow_type

    failed = workflow_record_of(make_record(status="failed"))
    assert failed.status == "failed", "failed 原样透传，是重学信号"
    print("  状态映射与字段搬运 OK")


def test_experience_args_of():
    """测试经验载荷：content 给人读、data 给机器读"""
    print("=" * 60)
    print("测试 A2：LearningRecord → 经验载荷")
    print("=" * 60)

    from engine.workflow_learning import experience_args_of

    args = experience_args_of(make_record())
    assert "cfg 8 比 12 稳" in args["content"]
    assert "CFG值较高" in args["content"]
    assert args["tags"] == ["Text To Image", "json"]
    assert args["data"]["key"] == "sd1.5/basic"
    assert args["data"]["status"] == STATUS_COMPLETED
    assert args["data"]["parameters"]["KSampler"]["cfg"] == 8.0

    failed = experience_args_of(
        make_record(status="failed", error="文件损坏")
    )
    assert "文件损坏" in failed["content"]
    print("  经验载荷组装 OK")


def test_sync_record():
    """测试单条镜像：workflow + experience 都进库；skipped 不镜像"""
    print("=" * 60)
    print("测试 A3：sync_record")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")

        assert sync_record(make_record(), db) is True
        wf = db.workflows.get("sd1.5/basic")
        assert wf["status"] == STATUS_LEARNED
        assert wf["content_hash"].startswith("h-")
        assert db.nodes.workflows_using("KSampler") == ["sd1.5/basic"]
        exp = db.experiences.get("sd1.5/basic")
        assert exp["data"]["parameters"]["KSampler"]["steps"] == 24

        # 节点清单入索引，归纳与图谱都能吃到
        assert "KSampler" in db.indexes.build_workflow_index()

        assert sync_record(
            make_record(key="sd1.5/x", status=STATUS_SKIPPED), db
        ) is False, "skipped 不是学习结果，不得写库"
        assert db.workflows.get("sd1.5/x") is None
    print("  单条镜像与 skipped 跳过 OK")


def test_sync_all_and_is_learned():
    """测试全量迁移与「已学」四分支判定"""
    print("=" * 60)
    print("测试 A4：sync_all + is_learned")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        store = LearningStore(str(Path(tmp) / "state"))
        store.write(make_record("a/one"))
        store.write(make_record("b/two", status="failed"))
        store.write(make_record("c/skip", status=STATUS_SKIPPED))

        db = WorkflowDatabase(Path(tmp) / "db.json")
        result = sync_all(store, db)
        assert result == {"synced": 2, "skipped": 1, "failed": 0}, result
        assert len(db.workflows.all()) == 2

        # 已学且内容未变
        assert is_learned(db, "a/one", "h-a/one") is True
        # 库里有但失败过 → 必须可重试
        assert is_learned(db, "b/two", "h-b/two") is False
        # 库里没有 → None（调用方回退，不猜）
        assert is_learned(db, "c/skip", "") is None
        assert is_learned(db, "没有的", "") is None
        # 未接数据库
        assert is_learned(None, "a/one", "") is None

        # 指纹变了 → False（改参数必须重学的老坑）
        assert is_learned(db, "a/one", "h-新的") is False
        # 传空指纹时不比对（老记录没有指纹也算已学）
        assert is_learned(db, "a/one", "") is True
    print("  全量迁移与已学判定 OK")


# ============================================================
# B. 批量学习接库
# ============================================================

def test_batch_learner_mirrors_to_db():
    """测试 learn_folder 学完即镜像进库"""
    print("=" * 60)
    print("测试 B1：批量学习写库")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        wf_dir = root / "workflows"
        write_json(wf_dir / "sd1.5" / "basic.json", SAMPLE_WORKFLOW)
        write_json(wf_dir / "sdxl" / "portrait.json", SAMPLE_WORKFLOW)

        db = WorkflowDatabase(root / "db.json")
        batch = BatchWorkflowLearner(
            learner=FakeLearner(),
            store=LearningStore(str(root / "state")),
            scanner=WorkflowScanner(),
            verbose=False,
            database=db,
        )
        summary = batch.learn_folder(str(wf_dir))
        assert summary["learned"] == 2

        for key in ("sd1.5/basic.json", "sdxl/portrait.json"):
            wf = db.workflows.get(key)
            assert wf is not None and wf["status"] == STATUS_LEARNED
            assert db.experiences.get(key)["data"]["key"] == key
        assert db.nodes.workflows_using("KSampler") == \
            ["sd1.5/basic.json", "sdxl/portrait.json"]

        # 失败的记录也镜像（状态 failed，可被重试）
        batch2 = BatchWorkflowLearner(
            learner=FakeLearner(fail_keys={"sd1.5/broken.json"}),
            store=LearningStore(str(root / "state2")),
            scanner=WorkflowScanner(),
            verbose=False,
            database=db,
        )
        write_json(wf_dir / "broken" / "x.json", {"nodes": []})
        # broken 目录下文件名不同，直接换个目录学
        root2 = Path(tmp) / "wfs2"
        write_json(root2 / "sd1.5" / "broken.json", SAMPLE_WORKFLOW)
        s2 = batch2.learn_folder(str(root2))
        assert s2["failed"] == 1
        assert db.workflows.get("sd1.5/broken.json")["status"] == "failed"
    print("  批量学习写库（成功与失败）OK")


def test_batch_sync_database_migration():
    """测试存量迁移 sync_database；未指定库时报错"""
    print("=" * 60)
    print("测试 B2：存量记录迁移")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        store = LearningStore(str(root / "state"))
        store.write(make_record("sd1.5/basic"))
        store.write(make_record("sd1.5/lora"))

        batch = BatchWorkflowLearner(
            learner=FakeLearner(), store=store, verbose=False
        )
        try:
            batch.sync_database()
        except RuntimeError as e:
            assert "数据库" in str(e)
        else:
            raise AssertionError("未指定数据库必须报 RuntimeError")

        db = WorkflowDatabase(root / "db.json")
        result = batch.sync_database(db)
        assert result["synced"] == 2, result
        assert db.workflows.get("sd1.5/lora") is not None

        # 幂等：再跑一遍还是 2 条
        assert batch.sync_database(db)["synced"] == 2
        assert len(db.workflows.all()) == 2
    print("  存量迁移 OK")


# ============================================================
# C. 调度器接库
# ============================================================

def _write_scan_file(root, rel, data=SAMPLE_WORKFLOW):
    path = Path(root) / rel
    write_json(path, data)
    return str(path)


def test_scheduler_skips_via_db():
    """测试库里 status=learned 且指纹为空 → 判已学，不查 Markdown"""
    print("=" * 60)
    print("测试 C1：查库判已学")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        wfs = root / "wfs"           # 扫描目录，库文件不放里面
        _write_scan_file(wfs, "sd1.5/basic.json")

        db = WorkflowDatabase(root / "db.json")
        # 无指纹：库里已学 → 无论文件内容如何都判已学
        db.workflows.add(
            workflow_record_of(make_record("sd1.5/basic.json", content_hash=""))
        )

        # store 声称什么都没学过 —— 跳过只能来自数据库
        scheduler = make_scheduler(
            root, FakeStore(exists_keys=()), database=db
        )
        tasks = scheduler.build_schedule(str(wfs))
        assert tasks == [], "库里已学的必须被跳过"
    print("  查库判已学 OK")


def test_scheduler_relearn_on_hash_mismatch():
    """测试库里指纹与文件对不上 → 判需重学并加内容变更分"""
    print("=" * 60)
    print("测试 C2：指纹变更触发重学")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        wfs = root / "wfs"
        _write_scan_file(wfs, "sd1.5/basic.json")

        db = WorkflowDatabase(root / "db.json")
        db.workflows.add(workflow_record_of(
            make_record("sd1.5/basic.json", content_hash="旧的指纹")
        ))

        scheduler = make_scheduler(
            root, FakeStore(exists_keys={"sd1.5/basic"}), database=db
        )
        tasks = scheduler.build_schedule(str(wfs))
        assert len(tasks) == 1, "指纹对不上必须重学"
        reasons = " ".join(tasks[0].priority_reasons)
        assert "内容已变更" in reasons, reasons
    print("  指纹变更触发重学 OK")


def test_scheduler_fallback_to_store():
    """测试库里没有的 key 回退查 Markdown（不猜）"""
    print("=" * 60)
    print("测试 C3：回退 LearningStore")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        wfs = root / "wfs"
        _write_scan_file(wfs, "sd1.5/basic.json")
        _write_scan_file(wfs, "sd1.5/lora.json")

        db = WorkflowDatabase(root / "db.json")
        # 只有 basic 镜像进库（learned、无指纹）
        db.workflows.add(workflow_record_of(
            make_record("sd1.5/basic.json", content_hash="")
        ))

        # lora 不在库里 → 回退查 store；store 说学过 → 跳过
        store = FakeStore(exists_keys={"sd1.5/lora.json"})
        scheduler = make_scheduler(root, store, database=db)
        tasks = scheduler.build_schedule(str(wfs))
        assert tasks == [], "库判定 + 回退判定都应跳过"

        # store 说什么都没学过、库里也只有 basic → lora 应出现
        scheduler2 = make_scheduler(
            root, FakeStore(exists_keys=()), database=db
        )
        tasks2 = scheduler2.build_schedule(str(wfs))
        assert [t.key for t in tasks2] == ["sd1.5/lora.json"]

        # 未接库 → 全按 store（旧行为）
        scheduler3 = make_scheduler(
            root, FakeStore(exists_keys=()), database=None
        )
        tasks3 = scheduler3.build_schedule(str(wfs))
        assert len(tasks3) == 2
    print("  回退与旧行为 OK")


def test_scheduler_run_mirrors_to_db():
    """测试 run() 学完写 Markdown 后镜像进库"""
    print("=" * 60)
    print("测试 C4：run 写库镜像")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        wfs = root / "wfs"
        _write_scan_file(wfs, "sd1.5/basic.json")

        db = WorkflowDatabase(root / "db.json")
        store = FakeStore(exists_keys=())
        scheduler = make_scheduler(
            root, store, database=db, learner=FakeLearner()
        )
        state = scheduler.run(str(wfs), save=False)
        assert state.completed == 1, state.summary() if hasattr(
            state, "summary"
        ) else vars(state)

        wf = db.workflows.get("sd1.5/basic.json")
        assert wf is not None and wf["status"] == STATUS_LEARNED
        assert db.experiences.get("sd1.5/basic.json") is not None
    print("  run 写库镜像 OK")


# ============================================================
# D. 归纳接库
# ============================================================

def test_loader_from_database():
    """测试从库读结构化经验，结果与读 Markdown 一致"""
    print("=" * 60)
    print("测试 D1：ExperienceLoader 走库")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        db = WorkflowDatabase(root / "db.json")
        # 学习时的镜像走内存中的完整记录 —— parameters 等都在
        sync_record(make_record("a/one"), db)
        sync_record(
            make_record("b/two", workflow_type="Image To Image"), db
        )

        rows = ExperienceLoader(database=db).load()
        assert [r.key for r in rows] == ["a/one", "b/two"]

        row = rows[0]
        assert row.parameters["KSampler"]["cfg"] == 8.0
        assert row.problems == ["[warning] CFG值较高（当前 12.0）"]
        assert row.missing_nodes == ["MarkdownNote"]
        assert row.workflow_type == "Text To Image"

        # 对照：Markdown 源。frontmatter 不带 parameters ——
        # 经 Markdown 往返的存量记录迁移后本来就没有参数，
        # 但 nodes / problems / missing 等 frontmatter 字段仍在
        store = LearningStore(str(root / "state"))
        store.write(make_record("a/one"))
        md_rows = ExperienceLoader(store=store).load()
        assert md_rows[0].nodes == row.nodes
        assert md_rows[0].problems == row.problems
        assert md_rows[0].missing_nodes == row.missing_nodes
        assert md_rows[0].parameters == row.parameters, \
            "frontmatter 带参数后，Markdown 往返应无损"
    print("  库来源与 Markdown 来源一致（含参数）OK")


def test_loader_fallback_and_filter():
    """测试库空回退 Markdown；失败载荷被过滤"""
    print("=" * 60)
    print("测试 D2：回退与过滤")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        store = LearningStore(str(root / "state"))
        store.write(make_record("a/one"))

        # 库空 → 打印提示并回退
        empty_db = WorkflowDatabase(root / "empty.json")
        rows = ExperienceLoader(
            store=store, database=empty_db
        ).load()
        assert [r.key for r in rows] == ["a/one"]

        # 库里有失败载荷 → 不进归纳
        db = WorkflowDatabase(root / "db.json")
        sync_record(make_record("b/two", status="failed"), db)
        rows2 = ExperienceLoader(
            store=LearningStore(str(root / "none")), database=db
        ).load()
        assert rows2 == [], "failed 的经验不得参与归纳"
    print("  回退与失败过滤 OK")


def test_consolidation_via_database():
    """测试 create_consolidation_engine(database=...) 端到端归纳"""
    print("=" * 60)
    print("测试 D3：归纳引擎走库")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        db = WorkflowDatabase(root / "db.json")
        sync_record(make_record("a/one"), db)
        sync_record(make_record("b/two"), db)   # 同节点 → 必聚成一类
        sync_record(make_record("c/none", nodes=[]), db)  # 空节点不计

        engine = create_consolidation_engine(
            store_path=str(root / "out"),
            database=db,
        )
        knowledge = engine.consolidate(save=True)

        assert knowledge.source_count == 2, "空节点记录不参与归纳"
        assert len(knowledge.patterns) >= 1
        pattern = knowledge.patterns[0]
        assert sorted(pattern.members) == ["a/one", "b/two"]
        assert any("CFG" in rec for rec in pattern.recommendations), \
            pattern.recommendations
    print("  归纳引擎走库 OK")


# ============================================================
# E. 端到端
# ============================================================

def test_full_chain():
    """测试完整链路：文件 → 学习 → 库 → 调度跳过 → 归纳读取"""
    print("=" * 60)
    print("测试 E1：文件→学习→库→调度→归纳")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        root = Path(tmp)
        wf_dir = root / "workflows"
        write_json(wf_dir / "sd1.5" / "basic.json", SAMPLE_WORKFLOW)
        write_json(wf_dir / "sd1.5" / "lora.json", SAMPLE_WORKFLOW)

        db = WorkflowDatabase(root / "db.json")

        # ① 学习（镜像进库）
        batch = BatchWorkflowLearner(
            learner=FakeLearner(),
            store=LearningStore(str(root / "state")),
            scanner=WorkflowScanner(),
            verbose=False,
            database=db,
        )
        assert batch.learn_folder(str(wf_dir))["learned"] == 2

        # ② 调度：库说学过了（按真实文件指纹）→ 不再排
        scheduler = make_scheduler(
            wf_dir, FakeStore(exists_keys=()), database=db
        )
        # FakeLearner 填的是 h- 前缀假指纹，这里用真指纹重灌两条记录
        # （「指纹变了要重学」的分支在 C2 已覆盖）
        for key in ("sd1.5/basic.json", "sd1.5/lora.json"):
            real_hash = WorkflowLearner._hash_file(wf_dir / key)
            db.workflows.add(
                workflow_record_of(
                    make_record(key, content_hash=real_hash)
                )
            )
        assert scheduler.build_schedule(str(wf_dir)) == []

        # ③ 归纳：直接吃库
        rows = ExperienceLoader(database=db).load()
        assert len(rows) == 2
    print("  端到端链路 OK")


# ============================================================
# main
# ============================================================

def main():
    """运行全部测试"""
    print("\n" + "=" * 60)
    print("database 集成测试")
    print("=" * 60 + "\n")

    # A 桥
    test_workflow_record_of()
    test_experience_args_of()
    test_sync_record()
    test_sync_all_and_is_learned()

    # B 批量学习
    test_batch_learner_mirrors_to_db()
    test_batch_sync_database_migration()

    # C 调度器
    test_scheduler_skips_via_db()
    test_scheduler_relearn_on_hash_mismatch()
    test_scheduler_fallback_to_store()
    test_scheduler_run_mirrors_to_db()

    # D 归纳
    test_loader_from_database()
    test_loader_fallback_and_filter()
    test_consolidation_via_database()

    # E 端到端
    test_full_chain()

    print("=" * 60)
    print("全部测试通过")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
