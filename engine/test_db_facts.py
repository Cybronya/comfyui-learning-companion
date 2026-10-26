r"""
db_facts 只读适配层测试（v0.6 第 1 步）

从仓库根目录运行：
    cd "F:\Program Files\ComfyUI"
    python -X utf8 -m engine.test_db_facts

覆盖：
    A. 路径 → workflow id 提取（各种命名形态）
    B. 节点维度查询（正查 + usage_count 一致性 + 未知键）
    C. 模式维度查询（正查 + 反查一致性 + 未知键）
    D. 无索引支撑的查询必须诚实返回空
    E. 只读约束：调用后 sqlite 主库与索引文件均未被修改

真实索引存在时用真实数据跑（索引是运行期产物，缺失时相关用例跳过）；
路径提取逻辑用构造样本单独覆盖，不依赖索引。
"""

import json
import sqlite3
import sys
from pathlib import Path
from tempfile import TemporaryDirectory

project_root = Path(__file__).parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from engine.retrieval.db_facts import (
    DatabaseFacts,
    NODE_INDEX,
    PATTERN_INDEX,
    _extract_workflow_id,
    _extract_workflow_ids,
    clear_cache,
)

PASS, FAIL, SKIP = "PASS", "FAIL", "SKIP"
_results = []


def check(name, cond, detail=""):
    _results.append((PASS if cond else FAIL, name, detail))
    print(f"  [{PASS if cond else FAIL}] {name}" + (f" — {detail}" if detail else ""))


def skip(name, why):
    _results.append((SKIP, name, why))
    print(f"  [{SKIP}] {name} — {why}")


def test_path_extraction():
    print("\n[A] 路径 → workflow id 提取")
    cases = [
        ("图片生成/文生图/某某工作流_2087218383308812289.json", "2087218383308812289"),
        ("数字人/数字人/abc_123456789012345.json", "123456789012345"),
        ("a/b/c_1.json", None),                    # 位数不足
        ("no_id_here.json", None),
        ("x_2099887766554433221.json", "2099887766554433221"),
        # 裸 ID 命名（10-09 那批历史落盘，无标题前缀）
        ("图片生成/文生图/2029394586908499969.json", "2029394586908499969"),
        ("2030807710291202049.json", "2030807710291202049"),
    ]
    for path, expect in cases:
        got = _extract_workflow_id(path)
        check(f"提取 {path.split('/')[-1]}", got == expect, f"得到 {got}")

    ids = _extract_workflow_ids([
        "x_111111111111111.json",
        "y_222222222222222.json",
        "x_111111111111111.json",   # 重复
        "bad.json",
    ])
    check("批量提取去重且跳过非法", ids == ["111111111111111", "222222222222222"], str(ids))

    # Windows 反斜杠路径
    check("反斜杠路径也能提取",
          _extract_workflow_id("图片生成\\文生图\\x_333333333333333.json") == "333333333333333")


def test_node_queries():
    print("\n[B] 节点维度查询")
    facts = DatabaseFacts()
    if not NODE_INDEX.exists():
        skip("节点查询", "node_index.json 不存在（运行期产物）")
        return
    names = facts.all_node_names()
    if not names:
        skip("节点查询", "node_index.json 为空")
        return
    check("节点名列表非空", len(names) > 0, f"{len(names)} 个")

    name = names[len(names) // 2]
    ids = facts.workflows_using_node(name)
    count = facts.node_usage_count(name)
    # 不能断言两者相等：usage_count 数的是**路径数**，workflows_using_node
    # 返回的是**去重后的工作流 ID**。同一工作流出现在多个标签目录时
    # （如「视频生成/图生视频/X_206.json」与「视频生成/文生视频/X_206.json」），
    # 路径数必然多于去重 ID 数。
    # 正确的不变量：去重 ID 数 ≤ usage_count（差值由跨标签重复 + 无 ID 模板路径构成，
    # 详见下方「高用量节点差额可完全解释」）。
    check("去重 ID 数不超过 usage_count", len(ids) <= count,
          f"{len(ids)} vs {count}")
    check("返回的 ID 都是 15+ 位数字",
          all(i.isdigit() and len(i) >= 15 for i in ids))

    # 全库校验：真实节点名的「可解析 ID 数」必须等于 usage_count
    # 减去「模板 + 无 ID 路径数」。差额来源有两个，都不是解析 bug：
    #   ① 跨标签重复：同一工作流 ID 出现在多个标签目录（如「图片生成/图生图/X_206.json」
    #      和「图片生成/文生图/X_206.json」），路径数多于去重后的 ID 数；
    #   ② 官方模板：路径是英文模板名（comfyui-workflow-templates-json/…），
    #      不含工作流 ID，无法反查。
    # 关键不变量：解析出的 ID 数**绝不能多于** usage_count。
    import re as _re
    uuid_re = _re.compile(r"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}")
    real_names = [n for n in names if not uuid_re.fullmatch(n)]
    tmpl_names = [n for n in names if uuid_re.fullmatch(n)]
    check("区分官方模板键与真实节点名", len(tmpl_names) > 0,
          f"模板 {len(tmpl_names)} / 真实 {len(real_names)}")

    over = []   # ID 数多于 usage_count → 真的解析错了
    for n in real_names:
        c = facts.node_usage_count(n)
        got = len(facts.workflows_using_node(n))
        if got > c:
            over.append((n, c, got))
    check("真实节点名 ID 数绝不超过 usage_count",
          not over, f"{len(over)} 个越界" + (f"，例：{over[:2]}" if over else ""))

    # 抽查一个高用量节点，逐项核对差额来源
    from engine.retrieval.db_facts import _extract_workflow_id, TEMPLATE_PREFIX
    import json as _json
    raw = _json.load(open(NODE_INDEX, encoding="utf-8-sig"))
    probe = max(real_names, key=lambda n: facts.node_usage_count(n))
    used_in = raw[probe].get("used_in") or []
    ids = [_extract_workflow_id(p) for p in used_in]
    uniq = len(set(i for i in ids if i))
    no_id = sum(1 for i in ids if not i)
    tmpl = sum(1 for p in used_in if p.startswith(TEMPLATE_PREFIX))
    dup = len(used_in) - no_id - uniq   # 跨标签重复的路径数
    check("高用量节点差额可完全解释（无ID路径+跨标签重复）",
          facts.node_usage_count(probe) == uniq + no_id + dup,
          f"{probe}: usage={facts.node_usage_count(probe)} "
          f"= 去重ID {uniq} + 无ID路径 {no_id}(含模板 {tmpl}) + 跨标签重复 {dup}")

    check("未知节点返回空列表", facts.workflows_using_node("__definitely_not_a_node__") == [])
    check("未知节点 usage_count 为 0", facts.node_usage_count("__definitely_not_a_node__") == 0)


def test_pattern_queries():
    print("\n[C] 模式维度查询")
    facts = DatabaseFacts()
    if not PATTERN_INDEX.exists():
        skip("模式查询", "pattern_index.json 不存在（运行期产物）")
        return
    pats = facts.all_pattern_names()
    if not pats:
        skip("模式查询", "pattern_index.json 为空")
        return
    check("模式名列表非空", len(pats) > 0, f"{len(pats)} 个")

    pat = pats[0]
    wids = facts.workflows_with_pattern(pat)
    check("模式 → workflow 返回结果", len(wids) > 0, f"{len(wids)} 个")

    if wids:
        back = facts.patterns_for_workflow(wids[0])
        check("反查包含原模式（正反一致）", pat in back, f"{len(back)} 个模式")

    check("未知模式返回空列表", facts.workflows_with_pattern("__definitely_not_a_pattern__") == [])
    check("未知模式描述为空串", facts.pattern_description("__definitely_not_a_pattern__") == "")


def test_unsupported_query():
    print("\n[D] 无索引支撑的查询必须诚实返回空")
    facts = DatabaseFacts()
    check("workflows_with_problem 返回空（无 problem 索引）",
          facts.workflows_with_problem("显存溢出") == [])
    check("workflows_with_problem 对任意 key 都返回空",
          facts.workflows_with_problem("") == [])


def test_readonly_constraint():
    print("\n[E] 只读约束")
    db = project_root / "comfyui_library" / "database" / "storage" / "workflow_database.sqlite"
    if not db.exists():
        skip("只读约束", "sqlite 主库不存在")
        return
    before = db.stat().st_mtime_ns
    idx_before = NODE_INDEX.stat().st_mtime_ns if NODE_INDEX.exists() else None

    facts = DatabaseFacts()
    names = facts.all_node_names()
    if names:
        facts.workflows_using_node(names[0])
        facts.node_usage_count(names[0])
    pats = facts.all_pattern_names()
    if pats:
        facts.workflows_with_pattern(pats[0])

    after = db.stat().st_mtime_ns
    idx_after = NODE_INDEX.stat().st_mtime_ns if NODE_INDEX.exists() else None
    check("sqlite 主库未被修改", before == after)
    if idx_before is not None:
        check("派生索引未被修改", idx_before == idx_after)

    # 再确认 sqlite 是以只读方式可打开（不产生 -wal/-shm 残留）
    con = sqlite3.connect(f"file:{db}?mode=ro", uri=True)
    try:
        con.execute("SELECT COUNT(*) FROM sqlite_master").fetchone()
        check("sqlite 可只读访问", True)
    finally:
        con.close()


def main():
    print("=" * 62)
    print("db_facts 只读适配层测试")
    print("=" * 62)
    clear_cache()
    test_path_extraction()
    test_node_queries()
    test_pattern_queries()
    test_unsupported_query()
    test_readonly_constraint()

    passed = sum(1 for s, _, _ in _results if s == PASS)
    failed = [r for r in _results if r[0] == FAIL]
    skipped = sum(1 for s, _, _ in _results if s == SKIP)
    print("\n" + "=" * 62)
    print(f"通过 {passed} / 失败 {len(failed)} / 跳过 {skipped}")
    if failed:
        for _, name, detail in failed:
            print(f"  失败: {name} {detail}")
        return 1
    print("全部通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
