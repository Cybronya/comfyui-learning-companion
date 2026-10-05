"""
知识图谱的数据模型

三个概念：**顶点（GraphNode）**、**边（GraphEdge）**、**命名空间**。

## 为什么顶点 id 必须带类型前缀

设计稿里 id 是裸名（`{"id": "sdxl_portrait", "type": "workflow"}`），
有两个真实的撞车场景：

    1. workflow 的 key 是相对路径 —— `sd1.5/basic.json` 与 `sdxl/basic.json`
       同名不同族。这是 LearningStore 早就踩过的坑（当年用文件名当键，
       同名 workflow 互相覆盖），改成相对路径才修好。
    2. 不同类型的对象可能重名 —— 一个 pattern 叫 `basic`，
       一个 workflow 也叫 `basic`，放进同一个 dict 会互相覆盖。

所以 id 一律是 `类型:名字`（`workflow:sd1.5/basic.json`、`node:KSampler`）。
名字单独放在 `name` 字段里，查询用 `nid()` / `split_id()` 转换。
"""

from dataclasses import dataclass, field
from typing import Dict, List, Any, Optional, Tuple


# ---------- 顶点类型 ----------

TYPE_WORKFLOW = "workflow"      # 学过的一个 workflow
TYPE_NODE = "node"              # ComfyUI 节点类型（KSampler…）
TYPE_PATTERN = "pattern"        # 归纳出的模式
TYPE_CARD = "card"              # 知识卡文件
TYPE_PROBLEM = "problem"        # 诊断出的问题
TYPE_SOLUTION = "solution"      # 对应的建议
TYPE_FAMILY = "family"          # workflow 族（sd1.5 / sdxl / flux / wan）
TYPE_CONCEPT = "concept"        # 主题词（diffusion / steps / cfg）

ALL_TYPES = (
    TYPE_WORKFLOW, TYPE_NODE, TYPE_PATTERN, TYPE_CARD,
    TYPE_PROBLEM, TYPE_SOLUTION, TYPE_FAMILY, TYPE_CONCEPT,
)


# ---------- 关系 ----------

REL_CONTAINS = "contains"        # workflow 包含 node
REL_MEMBER_OF = "member_of"      # workflow 属于 family
REL_MATCHES = "matches"          # workflow 命中 pattern
REL_REQUIRES = "requires"        # workflow 依赖核心节点（生成流程必需）
REL_USES = "uses"                # workflow 使用某节点类型（非结构包含）
REL_HAS_CARD = "has_card"        # node 有知识卡
REL_HAS_PROBLEM = "has_problem"  # workflow 存在某问题
REL_PROBLEM_IN = "problem_in"    # 问题出在某个节点/参数上
REL_SUGGESTS = "suggests"        # 问题 → 建议
REL_CO_USED = "co_used"          # 节点共现（弱关系，仅供参考）
REL_HAS_TOPIC = "has_topic"      # node/pattern → 主题
REL_FIXED_BY = "fixed_by"        # workflow 采用某模式修好了问题

REL_COVERS = "covers"            # 知识卡覆盖某节点（与 has_card 成对）

#: 反向遍历时用。显式列出而非推断，避免「把 in 边的方向搞反」
#: 这类错误 —— 图里 has_card 与 covers 是成对存在的两条独立边，
#: 不是同一条边的两个方向。
#: 注意必须定义在它引用的所有常量之后：模块级 dict 字面量
#: 在导入时就会求值，前向引用直接 NameError。
REVERSE_RELATIONS = {
    REL_CONTAINS: REL_CONTAINS,
    REL_MEMBER_OF: REL_CONTAINS,
    REL_MATCHES: REL_CONTAINS,
    REL_REQUIRES: REL_CONTAINS,
    REL_USES: REL_CONTAINS,
    REL_HAS_CARD: REL_COVERS,
    REL_HAS_PROBLEM: REL_PROBLEM_IN,
}


def nid(node_type: str, name: str) -> str:
    """
    生成带类型前缀的顶点 id

    Args:
        node_type: 顶点类型（TYPE_* 之一）
        name: 对象名 / 相对路径

    Returns:
        `类型:名字`

    Examples:
        >>> nid(TYPE_NODE, "KSampler")
        'node:KSampler'
        >>> nid(TYPE_WORKFLOW, "sd1.5/basic.json")
        'workflow:sd1.5/basic.json'
    """
    return f"{node_type}:{name}"


def split_id(full_id: str) -> Tuple[str, str]:
    """
    拆回 (类型, 名字)

    没带前缀的 id 按 vertex 猜 —— 兼容手写数据。
    """
    if ":" in full_id:
        type_part, _, name = full_id.partition(":")
        return type_part, name

    return TYPE_NODE, full_id


@dataclass
class GraphNode:
    """
    图中的一个顶点

    properties 是开放字典，各类型约定如下：
        workflow  key / workflow_type / status / coverage / node_count
                   / missing_nodes / parameters / learned_at / source_file
        node      has_card / category / role / difficulty / used_in
        pattern   workflow_type / frequency / level / coverage / members
        card      file / category / role / difficulty / topics
        problem   severity / message / suggestion / issue_type
        family    workflow_count
    """

    id: str
    type: str = TYPE_NODE
    name: str = ""
    properties: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        if not self.name:
            _, self.name = split_id(self.id)

    # ---------- 便捷读写 ----------

    def get(self, key: str, default: Any = None) -> Any:
        return self.properties.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.properties[key] = value

    def merge(self, props: Dict[str, Any]) -> None:
        """合并属性（同 id 的顶点由多个来源贡献信息）"""
        self.properties.update(
            {k: v for k, v in (props or {}).items() if v is not None}
        )

    def to_dict(self) -> Dict:
        return {
            "id": self.id,
            "type": self.type,
            "name": self.name,
            "properties": dict(self.properties),
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "GraphNode":
        return cls(
            id=data.get("id", ""),
            type=data.get("type", TYPE_NODE),
            name=data.get("name", ""),
            properties=data.get("properties", {}) or {},
        )

    def describe(self) -> str:
        """一行人话描述（给 Agent 直接读）"""
        if self.type == TYPE_WORKFLOW:
            return (
                f"workflow {self.name}"
                f"（{self.get('workflow_type', '未分类')}，"
                f"{self.get('node_count', 0)} 节点，"
                f"覆盖率 {self.get('coverage', 0)}）"
            )
        if self.type == TYPE_NODE:
            card = "有卡" if self.get("has_card") else "无卡"
            return f"节点 {self.name}（{card}）"
        if self.type == TYPE_PATTERN:
            return (
                f"模式 {self.name}"
                f"（{self.get('workflow_type', '?')}，"
                f"{self.get('frequency', 0)} 个成员，"
                f"{self.get('level', 'weak')}）"
            )
        if self.type == TYPE_CARD:
            return f"知识卡 {self.name}（{self.get('category', '?')}）"
        if self.type == TYPE_PROBLEM:
            return f"问题 {self.get('message', self.name)}"
        if self.type == TYPE_SOLUTION:
            return f"建议 {self.name}"
        if self.type == TYPE_FAMILY:
            return f"族 {self.name}"

        return f"{self.type} {self.name}"


@dataclass
class GraphEdge:
    """
    图中的一条边

    properties 承载关系的附加信息，例如：
        contains   count（该节点在 workflow 里出现几次）、role（core/aux）
        co_used    strength（共现次数）
    """

    source: str
    relation: str
    target: str
    properties: Dict[str, Any] = field(default_factory=dict)

    @property
    def triple(self) -> Tuple[str, str, str]:
        """用于去重的三元组"""
        return (self.source, self.relation, self.target)

    def get(self, key: str, default: Any = None) -> Any:
        """读属性（与 GraphNode.get 同签名，查询层写起来一致）"""
        return self.properties.get(key, default)

    def set(self, key: str, value: Any) -> None:
        self.properties[key] = value

    def merge(self, props: Dict[str, Any]) -> None:
        """合并属性（重复边只更新信息，不新增一条）"""
        self.properties.update(
            {k: v for k, v in (props or {}).items() if v is not None}
        )

    def other(self, node_id: str) -> str:
        """给定一端，返回另一端"""
        if node_id == self.source:
            return self.target
        if node_id == self.target:
            return self.source
        return ""

    def to_dict(self) -> Dict:
        return {
            "source": self.source,
            "relation": self.relation,
            "target": self.target,
            "properties": dict(self.properties),
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "GraphEdge":
        return cls(
            source=data.get("source", ""),
            relation=data.get("relation", ""),
            target=data.get("target", ""),
            properties=data.get("properties", {}) or {},
        )

    def __repr__(self) -> str:
        return (
            f"<{self.source} -[{self.relation}]-> {self.target}>"
        )