"""
库侧只读事实适配层（v0.6 第 1 步）

解决 AGENTS.md 9.3 待办 14 / 17 / 20 的共同前置：结构层的派生索引
（workflow_index / node_index / pattern_index）只由 IndexManager 写、
检索层与图谱层完全读不到，导致「哪些工作流出过这类问题」这类跨条目
事实无从查询。

设计约束（重要）：
    1. **全程只读**。只消费 database/storage/ 下的派生索引，绝不写 sqlite
       主库——管线（learn_pipeline）运行时也能安全调用，避免 AGENTS.md
       2026-10-19「两进程同写 sqlite」的禁令冲突。
    2. **不新建索引**。派生索引里存的是「节点/模式 → 文件路径」，
       没有「workflow id → 属性」。真正需要 workflow_id 维度的查询
       （如 workflows_with_problem）目前没有索引支撑，本模块不臆造，
       返回空并说明原因，而不是给出一个看似有结果实则残缺的答案。
    3. **路径 → ID 转换在内部完成**。索引里存的是长路径文本，调用方
       不该被迫做字符串解析。

索引语义（2026-10-26 实测）：
    node_index.json     键=节点名   值={category, used_in:[路径…], usage_count}
    workflow_index.json 键=节点名   值=[路径…]（与 node_index.used_in 重复）
    pattern_index.json  键=模式名   值={workflows:[路径…], workflow_count, description}
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Dict, Iterable, List, Optional

# 项目根：engine/retrieval/db_facts.py → 上溯三层
ROOT = Path(__file__).resolve().parents[2]
STORAGE = ROOT / "comfyui_library" / "database" / "storage"

NODE_INDEX = STORAGE / "node_index.json"
WORKFLOW_INDEX = STORAGE / "workflow_index.json"
PATTERN_INDEX = STORAGE / "pattern_index.json"

# 文件名里的工作流 ID。两种命名都要认：
#   「某某工作流_2087218383308812289.json」——带标题前缀（多数）
#   「2029394586908499969.json」——裸 ID（少数，10-09 那批历史落盘）
# 后者不带下划线前缀，只按 _ID 匹配会漏掉，导致计数与 usage_count 对不上。
_WORKFLOW_ID_RE = re.compile(r"_(\d{15,})\.json$")
_BARE_ID_RE = re.compile(r"^(\d{15,})\.json$")


def _extract_workflow_id(path: str) -> Optional[str]:
    """从文件名尾部提取 workflow id；非标准文件名返回 None。"""
    name = path.replace("\\", "/").rsplit("/", 1)[-1]
    m = _WORKFLOW_ID_RE.search(name)
    if m:
        return m.group(1)
    m = _BARE_ID_RE.match(name)
    return m.group(1) if m else None


def _extract_workflow_ids(paths: Iterable[str]) -> List[str]:
    """批量提取，保持原顺序，去重。"""
    seen = set()
    out: List[str] = []
    for p in paths:
        wid = _extract_workflow_id(p)
        if wid and wid not in seen:
            seen.add(wid)
            out.append(wid)
    return out


# 官方模板的路径前缀。node_index 里另有 190 个 UUID 形态的键属于这一类，
# 其路径是英文模板名（如 template_rob_realistic_2k_images_quick_variations.json），
# 不含工作流 ID，因此无法反查到真实工作流——统计时要与真实路径分开。
TEMPLATE_PREFIX = "comfyui-workflow-templates-json/"


class _JsonCache:
    """派生索引的懒加载 + 进程内缓存。

    索引体积不小（node_index 187MB / workflow_index 180MB），不能每次查询
    都重新读盘；但也不能常驻内存，所以只缓存「已经读过的那个文件」。
    """

    def __init__(self) -> None:
        self._cache: Dict[Path, object] = {}

    def get(self, path: Path) -> Optional[object]:
        if path in self._cache:
            return self._cache[path]
        if not path.exists():
            return None
        try:
            with open(path, encoding="utf-8-sig") as fh:
                data = json.load(fh)
        except (OSError, json.JSONDecodeError):
            return None
        self._cache = {path: data}  # 只保留最近一个，避免多索引同时占内存
        return data

    def clear(self) -> None:
        self._cache.clear()


_CACHE = _JsonCache()


def clear_cache() -> None:
    """清空索引缓存（索引被管线刷新后调用）。"""
    _CACHE.clear()


class DatabaseFacts:
    """派生索引只读查询门面。

    用法：
        facts = DatabaseFacts()
        ids = facts.workflows_using_node("KSampler")
        ids = facts.patterns_for_workflow("2087218383308812289")
    """

    # ---- 节点维度 ----

    def workflows_using_node(self, node_name: str) -> List[str]:
        """用了某个节点的所有 workflow id。

        数据源：node_index.json 的 used_in（workflow_index 的值与它重复，
        此处只读一份，避免重复占用内存）。
        """
        idx = _CACHE.get(NODE_INDEX)
        if not isinstance(idx, dict):
            return []
        entry = idx.get(node_name)
        if not isinstance(entry, dict):
            return []
        return _extract_workflow_ids(entry.get("used_in") or [])

    def node_usage_count(self, node_name: str) -> int:
        """某节点被多少个工作流使用（0 表示索引里没有该节点）。

        注意：官方模板的引用也计入 usage_count。要看真实工作流数量，
        用 `real_workflow_count()`。
        """
        idx = _CACHE.get(NODE_INDEX)
        if not isinstance(idx, dict):
            return 0
        entry = idx.get(node_name)
        if not isinstance(entry, dict):
            return 0
        return int(entry.get("usage_count") or 0)

    def real_workflow_count(self, node_name: str) -> int:
        """某节点被多少个**真实工作流**使用（剔除官方模板引用）。

        usage_count 含官方模板，对「这个节点在全库有多常见」的判断会被
        稀释；这个口径只数能解析出工作流 ID 的真实路径。
        """
        idx = _CACHE.get(NODE_INDEX)
        if not isinstance(idx, dict):
            return 0
        entry = idx.get(node_name)
        if not isinstance(entry, dict):
            return 0
        return len(self.workflows_using_node(node_name))

    def is_template_only(self, node_name: str) -> bool:
        """该节点的引用是否全部来自官方模板（无真实工作流引用）。"""
        idx = _CACHE.get(NODE_INDEX)
        if not isinstance(idx, dict):
            return False
        entry = idx.get(node_name)
        if not isinstance(entry, dict):
            return False
        used_in = entry.get("used_in") or []
        return bool(used_in) and all(
            p.startswith(TEMPLATE_PREFIX) for p in used_in
        )

    def node_category(self, node_name: str) -> str:
        """节点分类（未知返回空串）。"""
        idx = _CACHE.get(NODE_INDEX)
        if not isinstance(idx, dict):
            return ""
        entry = idx.get(node_name)
        if not isinstance(entry, dict):
            return ""
        return str(entry.get("category") or "")

    def all_node_names(self) -> List[str]:
        """索引里全部节点名。"""
        idx = _CACHE.get(NODE_INDEX)
        return sorted(idx.keys()) if isinstance(idx, dict) else []

    # ---- 模式维度 ----

    def workflows_with_pattern(self, pattern_name: str) -> List[str]:
        """命中某个模式的所有 workflow id。"""
        idx = _CACHE.get(PATTERN_INDEX)
        if not isinstance(idx, dict):
            return []
        entry = idx.get(pattern_name)
        if not isinstance(entry, dict):
            return []
        return _extract_workflow_ids(entry.get("workflows") or [])

    def patterns_for_workflow(self, workflow_id: str) -> List[str]:
        """某个 workflow 命中的所有模式名。

        反向查询：pattern_index 的键是模式名，值里含 workflow 列表，
        需要扫描全部模式条目。9,604 条尚可接受；若模式数继续增长，
        应另建 workflow_id → patterns 的正排索引（见 v0.6-plan.md 第 3 步）。
        """
        idx = _CACHE.get(PATTERN_INDEX)
        if not isinstance(idx, dict):
            return []
        target = str(workflow_id)
        out: List[str] = []
        for pat, entry in idx.items():
            if not isinstance(entry, dict):
                continue
            for p in entry.get("workflows") or []:
                if _extract_workflow_id(p) == target:
                    out.append(pat)
                    break
        return out

    def pattern_description(self, pattern_name: str) -> str:
        """模式说明文本（未知返回空串）。"""
        idx = _CACHE.get(PATTERN_INDEX)
        if not isinstance(idx, dict):
            return ""
        entry = idx.get(pattern_name)
        if not isinstance(entry, dict):
            return ""
        return str(entry.get("description") or "")

    def all_pattern_names(self) -> List[str]:
        """索引里全部模式名。"""
        idx = _CACHE.get(PATTERN_INDEX)
        return sorted(idx.keys()) if isinstance(idx, dict) else []

    # ---- 尚无索引支撑的查询（诚实返回空，不臆造） ----

    def workflows_with_problem(self, problem_key: str) -> List[str]:
        """出过某类问题的工作流。

        **当前无索引支撑**：三个派生索引均为「节点/模式 → 路径」，
        不含 problem 维度。`problem_in` 边虽在图谱模型中已定义
        （engine/knowledge_graph/__init__.py），但建图侧尚未消费。

        待办 17 需要先在图谱侧落一份 problem 维度的正排索引，
        本方法才能真正返回结果。在那之前返回空列表是正确行为——
        返回残缺结果会让上层误以为「没有工作流出过这个问题」。
        """
        return []


__all__ = [
    "DatabaseFacts",
    "clear_cache",
    "NODE_INDEX",
    "WORKFLOW_INDEX",
    "PATTERN_INDEX",
]
