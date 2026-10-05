r"""
comfyui_library/database（Workflow 学习数据库）测试

从仓库根目录运行：
    cd "F:\Program Files\ComfyUI"
    python -X utf8 -m engine.test_database

-X utf8 必须加，否则中文输出乱码。
全部读写都走 TemporaryDirectory，不碰真实 storage/。
"""

import json
import sys
from dataclasses import asdict
from pathlib import Path
from tempfile import TemporaryDirectory

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from comfyui_library.database import (
    WorkflowDatabase,
    WorkflowRepository,
    NodeRepository,
    PatternRepository,
    ExperienceRepository,
    IndexManager,
    WorkflowRecord,
    NodeRecord,
    PatternRecord,
    ExperienceRecord,
)
from comfyui_library.database.database import SCHEMA_VERSION


# ============================================================
# 测试数据
# ============================================================

def make_wf(wid="sdxl/portrait_001", nodes=None, **kwargs):
    """构造一个 WorkflowRecord，字段可覆盖"""
    fields = dict(
        id=wid,
        name=Path(wid).name,
        file_path=f"comfyui_library/workflows/{wid}.json",
        status="learned",
        workflow_type="Image To Image",
        nodes=["KSampler", "ControlNetApply", "LoraLoader"],
        report="## 报告\n流程链 Model→Condition→Latent→Sampling→Decode",
    )
    fields.update(kwargs)
    if nodes is not None:
        fields["nodes"] = nodes
    return WorkflowRecord(**fields)


# ============================================================
# A. 数据库核心
# ============================================================

def test_models_vocabulary():
    """测试四个模型的默认值与形状（asdict 往返锁形状）"""
    print("=" * 60)
    print("测试 A1：数据模型词汇表")
    print("=" * 60)

    r = WorkflowRecord(id="a", name="a", file_path="x")
    assert r.status == "unlearned"
    assert r.nodes == [] and r.patterns == [] and r.report == ""
    assert r.content_hash == ""

    n = NodeRecord(name="KSampler")
    assert n.category == "" and n.used_in == []

    p = PatternRecord(name="p")
    assert p.workflows == [] and p.description == ""

    e = ExperienceRecord(workflow_id="a", content="x")
    assert e.tags == [] and e.data == {}

    for d in (asdict(r), asdict(n), asdict(p), asdict(e)):
        assert isinstance(d, dict)
    print("  四个模型默认值与 asdict 往返 OK")


def test_empty_database():
    """测试空库默认结构：四个 section 齐，未 save 不落盘"""
    print("=" * 60)
    print("测试 A2：空库默认结构")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "db.json"
        db = WorkflowDatabase(path)

        assert not path.exists(), "未 save 不该写文件"
        for section in ("workflows", "nodes", "patterns", "experiences"):
            assert section in db.data, f"缺 section {section}"
            assert db.data[section] == {}
        assert db.data["version"] == SCHEMA_VERSION
    print("  空库结构 OK")


def test_save_load_roundtrip():
    """测试整库写盘后重开一致（中文 / tags 不丢）"""
    print("=" * 60)
    print("测试 A3：save → load 往返")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "db.json"
        db = WorkflowDatabase(path)
        wid = "sd1.5/basic"
        db.workflows.add(make_wf(wid, workflow_type="Text To Image"))
        db.patterns.add("sd15-t2i", [wid], "SD1.5 文生图基线")
        db.experiences.add(wid, "cfg 降到 8 出图更稳", tags=["cfg", "sd1.5"])

        fresh = WorkflowDatabase(path)
        assert fresh.workflows.get(wid)["type"] == "Text To Image"
        assert fresh.patterns.get("sd15-t2i")["description"] == "SD1.5 文生图基线"
        exp = fresh.experiences.get(wid)
        assert exp["content"] == "cfg 降到 8 出图更稳"
        assert exp["tags"] == ["cfg", "sd1.5"]

        s = fresh.summary()
        assert "1 workflow" in s and "1 pattern" in s, s
        print(f"  往返一致，summary: {s}")


def test_utf8_sig_bom():
    """测试带 BOM 的库文件也能读（硬约定 3.3）"""
    print("=" * 60)
    print("测试 A4：utf-8-sig 读 BOM 文件")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "db.json"
        payload = {
            "version": SCHEMA_VERSION,
            "workflows": {"a": {"name": "甲", "nodes": ["KSampler"]}},
            "nodes": {},
            "patterns": {},
            "experiences": {},
        }
        with open(path, "w", encoding="utf-8-sig") as f:
            json.dump(payload, f, ensure_ascii=False)

        db = WorkflowDatabase(path)
        assert db.workflows.get("a")["name"] == "甲"
    print("  BOM 文件读取 OK")


def test_missing_sections_backfilled():
    """测试旧文件缺 section 回填为空 dict，不 KeyError"""
    print("=" * 60)
    print("测试 A5：缺键回填")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "db.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"version": SCHEMA_VERSION,
                       "workflows": {"a": {"name": "A"}}}, f)

        db = WorkflowDatabase(path)
        assert db.data["nodes"] == {}
        assert db.data["patterns"] == {}
        assert db.data["experiences"] == {}
        assert db.workflows.get("a")["name"] == "A"
    print("  缺键回填 OK")


def test_corrupt_json_raises():
    """测试非法 JSON 报 ValueError 且带文件名"""
    print("=" * 60)
    print("测试 A6：非法 JSON 明确报错")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "db.json"
        path.write_text("{oops", encoding="utf-8")

        try:
            WorkflowDatabase(path)
        except ValueError as e:
            assert "不是合法 JSON" in str(e), str(e)
            assert str(path) in str(e), "报错必须带文件名"
        else:
            raise AssertionError("非法 JSON 必须报 ValueError")
    print("  非法 JSON 报错 OK")


def test_version_guard():
    """测试版本不符明确拒绝（GraphStore 踩过的坑）"""
    print("=" * 60)
    print("测试 A7：version 守卫")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "db.json"
        with open(path, "w", encoding="utf-8") as f:
            json.dump({"version": 999, "workflows": {}}, f)

        try:
            WorkflowDatabase(path)
        except ValueError as e:
            assert "版本" in str(e), str(e)
        else:
            raise AssertionError("版本不符必须报 ValueError")
    print("  version 守卫 OK")


def test_default_path():
    """测试默认路径指向本包 storage/（只读路径属性，不写真实库）"""
    print("=" * 60)
    print("测试 A8：默认路径")
    print("=" * 60)

    db = WorkflowDatabase()
    assert db.path.name == "workflow_database.json"
    assert db.path.parent.name == "storage"
    assert db.path.parent.parent.name == "database"
    print(f"  默认路径: {db.path}")


# ============================================================
# B. Workflow 仓库
# ============================================================

def test_add_and_get():
    """测试 add / get / all 与字段映射（workflow_type → type）"""
    print("=" * 60)
    print("测试 B1：add / get 字段映射")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")
        wid = "sdxl/portrait_001"
        stored = db.workflows.add(make_wf(wid, content_hash="deadbeef"))

        assert stored["type"] == "Image To Image"
        assert stored["status"] == "learned"
        assert stored["nodes"] == ["KSampler", "ControlNetApply", "LoraLoader"]
        assert stored["patterns"] == []
        assert stored["content_hash"] == "deadbeef"
        assert "流程链" in stored["report"]

        got = db.workflows.get(wid)
        assert got["name"] == "portrait_001"
        assert got["file_path"] == "comfyui_library/workflows/sdxl/portrait_001.json"
        assert len(db.workflows.all()) == 1
        assert db.workflows.get("不存在") is None

        # 返回的是副本，改它不影响库
        got["nodes"] = []
        assert db.workflows.get(wid)["nodes"] != []
    print("  字段映射与副本语义 OK")


def test_add_upsert():
    """测试同 id 再 add 是覆盖，不新增"""
    print("=" * 60)
    print("测试 B2：upsert 覆盖")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")
        wid = "sd1.5/basic"
        db.workflows.add(make_wf(wid, status="learned"))
        db.workflows.add(make_wf(wid, status="failed", name="改名"))

        assert len(db.workflows.all()) == 1
        assert db.workflows.get(wid)["status"] == "failed"
        assert db.workflows.get(wid)["name"] == "改名"
    print("  upsert OK")


def test_add_registers_used_in():
    """测试 add 自动登记节点反向索引，与 NodeRepository 视角一致"""
    print("=" * 60)
    print("测试 B3：add 自动登记 used_in")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")
        wid = "sdxl/portrait_001"
        db.workflows.add(make_wf(wid))

        assert db.data["nodes"]["KSampler"]["used_in"] == [wid]
        assert db.nodes.workflows_using("ControlNetApply") == [wid]
        # 节点重复出现在 nodes 里也只登记一次
        db.workflows.add(make_wf(wid, nodes=["KSampler", "KSampler"]))
        assert db.data["nodes"]["KSampler"]["used_in"] == [wid]
        assert db.data["nodes"]["KSampler"]["used_in"].count(wid) == 1
    print("  反向索引自动登记 OK")


def test_add_reconciles_shrink():
    """测试更新时节点缩减，used_in 同步摘除（防两处状态漂移）"""
    print("=" * 60)
    print("测试 B4：节点缩减对账")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")
        wid = "sd1.5/basic"
        db.workflows.add(
            make_wf(wid, nodes=["KSampler", "LoraLoader", "VAEDecode"])
        )
        db.workflows.add(make_wf(wid, nodes=["KSampler", "VAEDecode"]))

        assert db.data["nodes"]["LoraLoader"]["used_in"] == [], \
            "缩减的节点必须从 used_in 摘除"
        assert db.data["nodes"]["KSampler"]["used_in"] == [wid]

        idx = db.indexes.build_workflow_index()
        assert "LoraLoader" not in idx, "派生索引不得再有悬空映射"
        assert idx == {"KSampler": [wid], "VAEDecode": [wid]}
    print("  缩减对账 OK")


def test_add_patterns_union():
    """测试 patterns 并集合并：回填的归属不被更新抹掉"""
    print("=" * 60)
    print("测试 B5：patterns 并集合并")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")
        wid = "sd1.5/lora"
        db.workflows.add(make_wf(wid))
        db.patterns.add("sd15-t2i", [wid])

        # 重新 add（比如内容变更重学），不带 patterns
        db.workflows.add(make_wf(wid, status="learned"))
        assert db.workflows.get(wid)["patterns"] == ["sd15-t2i"], \
            "PatternRepository 回填的归属不能被 upsert 抹掉"
    print("  并集合并 OK")


def test_delete_cleans_up():
    """测试 delete：记录删、used_in 清、patterns/experiences 悬空可见"""
    print("=" * 60)
    print("测试 B6：delete 清理")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")
        wid = "sd1.5/broken"
        db.workflows.add(make_wf(wid))
        db.patterns.add("sd15-t2i", [wid])
        db.experiences.add(wid, "这条经验先留着")

        assert db.workflows.delete(wid) is True
        assert db.workflows.get(wid) is None
        assert db.data["nodes"]["KSampler"]["used_in"] == []
        assert db.nodes.workflows_using("LoraLoader") == []

        # 悬空引用保持可见，不静默连带删
        assert db.patterns.get("sd15-t2i")["workflows"] == [wid]
        assert db.experiences.get(wid) is not None

        assert db.workflows.delete(wid) is False, "再删应返回 False"
    print("  delete 清理 OK")


# ============================================================
# C. Node 仓库
# ============================================================

def test_register_dedup_and_category():
    """测试 register 去重；category 只填空、不覆盖已有值"""
    print("=" * 60)
    print("测试 C1：register 去重与 category")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")
        db.nodes.register("KSampler", "a", category="sampling")
        db.nodes.register("KSampler", "a")           # 重复登记
        db.nodes.register("KSampler", "b", category="other")

        entry = db.nodes.get("KSampler")
        assert entry["used_in"] == ["a", "b"], "重复登记不得产生重复项"
        assert entry["category"] == "sampling", "category 只填空，不覆盖"

        # 空分类后到也不清掉已有值
        db.nodes.register("KSampler", "c")
        assert db.nodes.get("KSampler")["category"] == "sampling"
        assert db.nodes.workflows_using("KSampler") == ["a", "b", "c"]

        assert db.nodes.get("没登记过") is None
        assert db.nodes.workflows_using("没登记过") == []
        assert len(db.nodes.all()) == 1
    print("  register 去重与 category OK")


# ============================================================
# D. Pattern 仓库
# ============================================================

def test_pattern_add_backfill():
    """测试 add 回填 workflow.patterns；幽灵 workflow 不创建"""
    print("=" * 60)
    print("测试 D1：模式回填")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")
        wid = "sdxl/portrait"
        db.workflows.add(make_wf(wid))
        db.patterns.add("sdxl-portrait", [wid, "ghost/none"], "SDXL 人像流程")

        got = db.patterns.get("sdxl-portrait")
        assert got["workflows"] == [wid, "ghost/none"]
        assert got["description"] == "SDXL 人像流程"

        assert db.workflows.get(wid)["patterns"] == ["sdxl-portrait"]
        # 悬空成员只记录、不猜着建 workflow
        assert db.workflows.get("ghost/none") is None
        assert len(db.workflows.all()) == 1
        assert len(db.patterns.all()) == 1
    print("  模式回填与悬空可见 OK")


def test_pattern_upsert_dedup():
    """测试同名覆盖与成员去重"""
    print("=" * 60)
    print("测试 D2：模式 upsert 与去重")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")
        db.patterns.add("p", ["a", "a", "b"])
        assert db.patterns.get("p")["workflows"] == ["a", "b"]

        db.patterns.add("p", ["b", "c"], "更新说明")
        assert db.patterns.get("p")["workflows"] == ["b", "c"]
        assert db.patterns.get("p")["description"] == "更新说明"
    print("  upsert 与去重 OK")


# ============================================================
# E. Experience 仓库
# ============================================================

def test_experience_lifecycle():
    """测试 add / get / 覆盖语义 / delete / all"""
    print("=" * 60)
    print("测试 E1：经验生命周期")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")
        db.experiences.add("a", "第一版理解", tags=["旧"])
        db.experiences.add("a", "第二版理解")       # 同 id 覆盖，tags 缺省 []

        assert db.experiences.get("a") == {
            "content": "第二版理解", "tags": [], "data": {}
        }

        # 结构化载荷：归纳引擎按字段取用，content 只是给人看的摘要
        db.experiences.add(
            "b", "带载荷", tags=["t"],
            data={"status": "completed", "nodes": ["KSampler"]},
        )
        assert db.experiences.get("b")["data"]["nodes"] == ["KSampler"]

        assert len(db.experiences.all()) == 2

        assert db.experiences.delete("a") is True
        assert db.experiences.get("a") is None
        assert db.experiences.delete("a") is False
    print("  经验生命周期 OK")


# ============================================================
# F. 索引
# ============================================================

def test_build_workflow_index():
    """测试 node → 排序后的 workflow id 列表"""
    print("=" * 60)
    print("测试 F1：workflow 索引")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")
        db.workflows.add(make_wf(
            "b/second", nodes=["KSampler", "VAEDecode"]))
        db.workflows.add(make_wf(
            "a/first", nodes=["KSampler", "LoraLoader"]))
        db.workflows.add(make_wf(
            "c/third", nodes=["KSampler", "KSampler"]))  # 库内也去重

        idx = db.indexes.build_workflow_index()
        assert idx == {
            "KSampler": ["a/first", "b/second", "c/third"],
            "VAEDecode": ["b/second"],
            "LoraLoader": ["a/first"],
        }
    print("  workflow 索引构建 OK")


def test_build_node_and_pattern_index():
    """测试 node_index 的 usage_count 与 pattern_index 的 workflow_count"""
    print("=" * 60)
    print("测试 F2：node / pattern 索引")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")
        db.workflows.add(make_wf("a/one", nodes=["KSampler", "VAEDecode"]))
        db.workflows.add(make_wf("b/two", nodes=["KSampler"]))
        db.nodes.register("VAEDecode", "a/one", category="decode")
        db.patterns.add("p1", ["b/two", "a/one"], "说明")

        nidx = db.indexes.build_node_index()
        assert nidx["KSampler"] == {
            "category": "", "used_in": ["a/one", "b/two"],
            "usage_count": 2,
        }
        assert nidx["VAEDecode"]["category"] == "decode"
        assert nidx["VAEDecode"]["usage_count"] == 1

        pidx = db.indexes.build_pattern_index()
        assert pidx["p1"]["workflows"] == ["a/one", "b/two"]
        assert pidx["p1"]["workflow_count"] == 2
        assert pidx["p1"]["description"] == "说明"
    print("  node / pattern 索引构建 OK")


def test_save_load_index():
    """测试单索引落盘读回；缺文件返回 {}；save_all 落三个文件"""
    print("=" * 60)
    print("测试 F3：索引落盘与读回")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")
        db.workflows.add(make_wf("a/one", nodes=["KSampler"]))

        idx = {"KSampler": ["a/one"]}
        db.indexes.save_index("workflow_index", idx)
        assert db.indexes.load_index("workflow_index") == idx
        assert db.indexes.load_index("没有这个索引") == {}

        paths = db.indexes.save_all()
        assert set(paths) == {"workflow_index", "node_index", "pattern_index"}
        for name, path in paths.items():
            assert Path(path).exists(), f"{name} 未落盘"
            with open(path, "r", encoding="utf-8-sig") as f:
                assert isinstance(json.load(f), dict)
    print("  索引落盘与读回 OK")


def test_index_follows_reconciliation():
    """测试缩减 + 删除后重建索引，无悬空映射"""
    print("=" * 60)
    print("测试 F4：索引跟随对账")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        db = WorkflowDatabase(Path(tmp) / "db.json")
        db.workflows.add(make_wf("a/keep", nodes=["KSampler", "LoraLoader"]))
        db.workflows.add(make_wf("b/gone", nodes=["LoraLoader", "ControlNet"]))

        db.workflows.add(make_wf("a/keep", nodes=["KSampler"]))
        db.workflows.delete("b/gone")

        idx = db.indexes.build_workflow_index()
        assert idx == {"KSampler": ["a/keep"]}, idx

        nidx = db.indexes.build_node_index()
        # 空的节点条目保留可见（usage_count 0），不静默删
        assert nidx["LoraLoader"]["used_in"] == []
        assert nidx["LoraLoader"]["usage_count"] == 0
        assert "ControlNet" not in nidx or \
            nidx["ControlNet"]["used_in"] == []
    print("  索引跟随对账 OK")


# ============================================================
# G. 端到端
# ============================================================

def test_end_to_end():
    """测试存查闭环：三个 workflow → 模式 → 经验 → 索引 → 重开查询"""
    print("=" * 60)
    print("测试 G1：端到端")
    print("=" * 60)

    with TemporaryDirectory() as tmp:
        path = Path(tmp) / "db.json"
        db = WorkflowDatabase(path)

        basic = "sd1.5/basic"
        lora = "sd1.5/lora"
        portrait = "sdxl/portrait"
        db.workflows.add(make_wf(
            basic, workflow_type="Text To Image",
            nodes=["CheckpointLoaderSimple", "CLIPTextEncode",
                   "EmptyLatentImage", "KSampler", "VAEDecode", "SaveImage"]))
        db.workflows.add(make_wf(
            lora, workflow_type="Text To Image",
            nodes=["CheckpointLoaderSimple", "LoraLoader", "CLIPTextEncode",
                   "KSampler", "VAEDecode", "SaveImage"]))
        db.workflows.add(make_wf(
            portrait, workflow_type="Image To Image",
            nodes=["CheckpointLoaderSimple", "ControlNetApply",
                   "CLIPTextEncode", "KSampler", "VAEDecode", "SaveImage"]))

        db.nodes.register("LoraLoader", lora, category="loaders")
        db.nodes.register("ControlNetApply", portrait, category="conditioning")

        db.patterns.add("sd15-t2i", [basic, lora], "SD1.5 文生图基线")
        db.patterns.add("sdxl-portrait", [portrait], "SDXL 人像")
        db.experiences.add(lora, "cfg 12 会烧图，8 稳", tags=["cfg", "sd1.5"])

        db.indexes.save_all()

        # 重开一个全新实例查询
        fresh = WorkflowDatabase(path)
        assert fresh.nodes.workflows_using("KSampler") == \
            sorted([basic, lora, portrait])
        assert fresh.nodes.workflows_using("ControlNetApply") == [portrait]
        assert fresh.workflows.get(lora)["patterns"] == ["sd15-t2i"]
        assert fresh.experiences.get(lora)["tags"] == ["cfg", "sd1.5"]

        nidx = fresh.indexes.load_index("node_index")
        assert nidx["LoraLoader"]["category"] == "loaders"
        assert nidx["LoraLoader"]["usage_count"] == 1
        pidx = fresh.indexes.load_index("pattern_index")
        assert pidx["sd15-t2i"]["workflow_count"] == 2

        s = fresh.summary()
        assert "3 workflow" in s and "2 pattern" in s, s
        print(f"  端到端 OK，summary: {s}")


# ============================================================
# main
# ============================================================

def main():
    """运行全部测试"""
    print("\n" + "=" * 60)
    print("comfyui_library/database 模块测试")
    print("=" * 60 + "\n")

    # A 数据库核心
    test_models_vocabulary()
    test_empty_database()
    test_save_load_roundtrip()
    test_utf8_sig_bom()
    test_missing_sections_backfilled()
    test_corrupt_json_raises()
    test_version_guard()
    test_default_path()

    # B Workflow 仓库
    test_add_and_get()
    test_add_upsert()
    test_add_registers_used_in()
    test_add_reconciles_shrink()
    test_add_patterns_union()
    test_delete_cleans_up()

    # C Node 仓库
    test_register_dedup_and_category()

    # D Pattern 仓库
    test_pattern_add_backfill()
    test_pattern_upsert_dedup()

    # E Experience 仓库
    test_experience_lifecycle()

    # F 索引
    test_build_workflow_index()
    test_build_node_and_pattern_index()
    test_save_load_index()
    test_index_follows_reconciliation()

    # G 端到端
    test_end_to_end()

    print("=" * 60)
    print("全部测试通过")
    print("=" * 60 + "\n")


if __name__ == "__main__":
    main()
