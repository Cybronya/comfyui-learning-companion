r"""
WorkflowDatabase —— 统一持久化核心

所有仓库共享同一份 self.data（dict），save() 整库写盘。
量级是「个人知识库」（几十到几百条），不做增量与压缩。

设计稿的问题，落地时补上：

1. 读 JSON 用的是 utf-8。项目硬约定读 JSON 一律 utf-8-sig
   （Windows 下别的工具写出的 JSON 可能带 BOM）。
2. 文件不记版本。GraphStore 踩过的坑：将来改结构时旧文件会被
   当成新结构读，报错还很难懂 —— 加 version 守卫，不符就拒绝。
3. load() 不回填缺键。旧文件少一个 section 就 KeyError。
4. 非法 JSON 抛裸 JSONDecodeError，不带文件名 —— 包一层。
"""

import json
from pathlib import Path

from .workflow_repository import WorkflowRepository
from .node_repository import NodeRepository
from .pattern_repository import PatternRepository
from .experience_repository import ExperienceRepository
from .index_manager import IndexManager

#: 存储格式版本。结构不兼容变更时 +1，
#: load() 会拒绝读旧版本而不是给出莫名其妙的错。
SCHEMA_VERSION = 1

#: 数据库的四个 section，load 时缺了就回填成空 dict
SECTIONS = ("workflows", "nodes", "patterns", "experiences")

#: 默认落盘位置（本包 storage/ 下，与调用方 cwd 无关）
DEFAULT_PATH = (
    Path(__file__).resolve().parent / "storage" / "workflow_database.json"
)


class WorkflowDatabase:
    """workflow / node / pattern / experience 四类数据的统一存储"""

    def __init__(self, path=None):
        """
        Args:
            path: 数据库文件路径；None 时用本包 storage/workflow_database.json
        """
        self.path = Path(path) if path is not None else DEFAULT_PATH
        self.data = {"version": SCHEMA_VERSION}
        for section in SECTIONS:
            self.data[section] = {}
        self.load()

        # 便捷入口：db.workflows.add(...) 即可，不必再手工 new 仓库
        self.workflows = WorkflowRepository(self)
        self.nodes = NodeRepository(self)
        self.patterns = PatternRepository(self)
        self.experiences = ExperienceRepository(self)
        self.indexes = IndexManager(self)

    # ---------- 读 ----------

    def load(self):
        """从磁盘读入；文件不存在时保持空库"""
        if not self.path.exists():
            return

        try:
            # utf-8-sig：项目约定读 JSON 一律用它（BOM 兼容）
            with open(self.path, "r", encoding="utf-8-sig") as f:
                data = json.load(f)
        except json.JSONDecodeError as e:
            raise ValueError(
                f"数据库文件不是合法 JSON: {self.path}（{e}）"
            ) from e

        if not isinstance(data, dict):
            raise ValueError(f"数据库文件顶层应为对象: {self.path}")

        version = data.get("version", SCHEMA_VERSION)
        if version != SCHEMA_VERSION:
            # 结构变了就明确拒绝，比读出一堆 None 强
            raise ValueError(
                f"数据库版本不支持：文件 version={version}，"
                f"当前支持 {SCHEMA_VERSION}，请重建或迁移: {self.path}"
            )

        # 缺键回填：旧文件少一个 section 不至于 KeyError
        for section in SECTIONS:
            data.setdefault(section, {})

        self.data = data

    # ---------- 写 ----------

    def save(self):
        """整库写盘（全量覆盖；数据量小，不做增量）"""
        self.data["version"] = SCHEMA_VERSION
        self.path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)
            f.write("\n")

    # ---------- 汇总 ----------

    def summary(self) -> str:
        """一行摘要，存完直接可读"""
        c = {s: len(self.data[s]) for s in SECTIONS}
        return (
            f"{self.path}：{c['workflows']} workflow / "
            f"{c['nodes']} node / {c['patterns']} pattern / "
            f"{c['experiences']} experience"
        )
