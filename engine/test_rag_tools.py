r"""
RAG 工具链测试（v0.6 第 4 步：键名统一 + 内容拼装）

从仓库根目录运行：
    cd "F:\Program Files\ComfyUI"
    python -X utf8 -m engine.test_rag_tools

覆盖：
    A. prepare_documents：content 不再是 repr，按类型拼装规范正文
    B. build_index：产出 content（兼容 text 别名）
    C. search_database：读 content / text 都能命中；多词查询更宽容
    D. 端到端：prepare → build → search 全链路能检索到目标

说明：skills/ 目录带连字符且不是 Python 包（无 __init__.py），
所以用 importlib 按文件路径加载，不走常规 import。
"""

import importlib.util
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

RAG_TOOLS = project_root / "skills" / "comfyui-learning" / "rag" / "tools"

PASS, FAIL = "PASS", "FAIL"
_results = []


def check(name, cond, detail=""):
    _results.append((PASS if cond else FAIL, name, detail))
    print(f"  [{PASS if cond else FAIL}] {name}" + (f" — {detail}" if detail else ""))


def load_tool(name):
    """按文件路径加载 skills 下的工具模块。"""
    spec = importlib.util.spec_from_file_location(name, RAG_TOOLS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


prepare_documents = load_tool("prepare_documents")
build_index_mod = load_tool("build_index")
search_database = load_tool("search_database")


def test_prepare_documents():
    print("\n[A] prepare_documents 内容拼装")
    wf = {
        "name": "Wan Character Video",
        "category": "video_generation",
        "nodes": ["WanVideoLoader", "KSampler"],
        "models": ["Wan2.1"],
        "description": "角色一致性视频生成",
        "parameters": {"steps": 20, "cfg": 7.0},
    }
    docs = prepare_documents.create_documents("workflow", [wf])
    check("产出一条文档", len(docs) == 1)
    content = docs[0]["content"]
    check("content 不是 repr", not content.startswith("{"), content[:60])
    check("content 含名称", "Wan Character Video" in content)
    check("content 含分类", "video_generation" in content)
    check("content 含节点", "KSampler" in content)
    check("content 含模型", "Wan2.1" in content)
    check("content 含描述", "角色一致性" in content)
    check("content 含参数", "steps" in content and "20" in content)
    check("metadata 保留原对象", docs[0]["metadata"] is wf)

    # 节点类型
    node = {"name": "KSampler", "purpose": "采样生成", "input": "latent",
            "output": "latent", "category": "sampler"}
    ndoc = prepare_documents.create_documents("node", [node])[0]
    check("节点 content 含名称", "KSampler" in ndoc["content"])
    check("节点 content 含用途", "采样生成" in ndoc["content"])
    check("节点 content 含分类", "sampler" in ndoc["content"])

    # 模型类型
    model = {"name": "Wan2.1", "type": "t2v", "architecture": "DiT",
             "compatibility": ["ComfyUI"], "requirement": "16GB VRAM"}
    mdoc = prepare_documents.create_documents("model", [model])[0]
    check("模型 content 含架构", "DiT" in mdoc["content"])
    check("模型 content 含显存要求", "16GB" in mdoc["content"])

    # 别名兼容
    alias = {"workflow_name": "别名流程", "task_type": "image_generation"}
    adoc = prepare_documents.create_documents("workflow", [alias])[0]
    check("识别别名 workflow_name", "别名流程" in adoc["content"])
    check("识别别名 task_type", "image_generation" in adoc["content"])

    # dict-of-lists 输入
    multi = prepare_documents.create_documents("node", {
        "a": [{"name": "n1"}], "b": [{"name": "n2"}]})
    check("dict-of-lists 输入被合并", len(multi) == 2, f"{len(multi)} 条")


def test_build_index():
    print("\n[B] build_index 键名统一")
    docs = [{"type": "node", "content": "KSampler 采样", "metadata": {"n": 1}}]
    idx = build_index_mod.build_index(docs)
    check("产出一条", len(idx) == 1)
    check("含 content 键", "content" in idx[0])
    check("含兼容 text 别名", idx[0].get("text") == idx[0]["content"])
    check("含 type 键", idx[0].get("type") == "node")
    check("含 metadata 键", idx[0].get("metadata") == {"n": 1})


def test_search():
    print("\n[C] search_database 键名与匹配")
    docs = [
        {"content": "KSampler 负责去噪采样", "metadata": {"id": 1}},
        {"content": "VAEDecode 把 latent 解码成图像", "metadata": {"id": 2}},
        {"text": "ControlNet 条件控制", "metadata": {"id": 3}},   # 历史键名
    ]
    r1 = search_database.search("KSampler", docs)
    check("content 键能命中", len(r1) == 1 and r1[0]["metadata"]["id"] == 1)

    r2 = search_database.search("ControlNet", docs)
    check("text 键（历史索引）能命中", len(r2) == 1 and r2[0]["metadata"]["id"] == 3)

    r3 = search_database.search("latent 解码", docs)
    check("多词查询命中", len(r3) == 1 and r3[0]["metadata"]["id"] == 2,
          f"{len(r3)} 条")

    r4 = search_database.search("不存在的词", docs)
    check("无匹配返回空", r4 == [])

    r5 = search_database.search("", docs)
    check("空查询返回空", r5 == [])

    r6 = search_database.search("KSampler", docs, limit=1)
    check("limit 生效", len(r6) <= 1)


def test_end_to_end():
    print("\n[D] 端到端 prepare → build → search")
    raw = [
        {"name": "ControlNet 深度控制", "category": "image_generation",
         "nodes": ["ControlNetLoader", "KSampler"], "description": "用深度图约束生成"},
        {"name": "Latent 放大", "category": "image_generation",
         "nodes": ["LatentUpscale"], "description": "潜空间放大细节"},
    ]
    docs = prepare_documents.create_documents("workflow", raw)
    idx = build_index_mod.build_index(docs)
    hits = search_database.search("ControlNet", idx)
    check("端到端能检索到目标", len(hits) == 1)
    check("命中的是正确条目",
          hits and hits[0]["metadata"].get("name") == "ControlNet 深度控制")
    check("索引项保留 content 键", hits and "content" in hits[0])


def main():
    print("=" * 62)
    print("RAG 工具链测试")
    print("=" * 62)
    test_prepare_documents()
    test_build_index()
    test_search()
    test_end_to_end()

    passed = sum(1 for s, _, _ in _results if s == PASS)
    failed = [r for r in _results if r[0] == FAIL]
    print("\n" + "=" * 62)
    print(f"通过 {passed} / 失败 {len(failed)}")
    if failed:
        for _, name, detail in failed:
            print(f"  失败: {name} {detail}")
        return 1
    print("全部通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
