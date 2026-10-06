"""
学习记录存储（Markdown 后端）

一个 workflow 一个 Markdown 文件，frontmatter 存元数据、正文存学到的内容。

替代原先的 registry.json + experience.json + reports/*.md 三份文件 ——
那三份描述的是同一件事，却分散在不同格式里，
「已学过了吗」和「学到了什么」可能不一致。
合成一份后，「文件存在」即「已学过」，没有第二种可能。

查询方式（都是 Agent 能直接做的）：
    exists(key)                 这个 workflow 学过吗
    read(key)                    学到了什么
    all_records()                全部学了什么
    node_frequency()             哪些节点最常用（供挖模式）
    node_frequency(min_count=n)  至少在 n 个 workflow 里出现过的节点
    grep -r "LoraLoader" learning/   哪些 workflow 用了某节点
"""

from pathlib import Path
from typing import Dict, List, Optional

from .learning_record import (
    LearningRecord,
    STATUS_COMPLETED,
)
from .ignore_nodes import is_ignored
from .markdown_format import (
    to_markdown,
    from_markdown,
    render_body,
    build_frontmatter,
)
from .paths import (
    STATE_DIR,
    INDEX_PATH,
    record_path_for,
    index_link_for,
    ensure_state_dir,
)


class LearningStore:
    """
    学习记录存储
    """

    def __init__(
        self,
        root: str = None,
        use_hash: bool = True,
        write_index: bool = True
    ) -> None:
        """
        初始化存储

        Args:
            root: 记录根目录；None 时用统一位置
                  `comfyui_library/workflows/learning/`
            use_hash: 是否用内容指纹判断是否需要重学。
                      关闭后只按「文件是否存在」判断
            write_index: 写入时是否同步更新 index.md 汇总表
        """
        if root is None:
            root = STATE_DIR

        self.root = Path(root)
        self.use_hash = use_hash
        self.write_index = write_index

        # 记录缓存（key -> record），惰性构建。库过千条后，
        # write() 每次为渲染 index.md 全量重读所有 Markdown
        # （单次写 7s+），这是批量学习变慢的主因之一。
        # 进程内一旦读过就信任缓存；write/prune 会同步维护。
        self._cache = None

    # ---------- 读写单条 ----------

    def record_file(self, key: str) -> Path:
        """
        某 workflow 的记录文件路径
        """
        if self.root == STATE_DIR:
            return record_path_for(key)

        # 自定义根（测试用）：沿用同样的目录镜像规则
        relative = str(key).replace("\\", "/")
        for suffix in (".json", ".png"):
            if relative.lower().endswith(suffix):
                relative = relative[:-len(suffix)]
                break
        return self.root / f"{relative}.md"

    def exists(
        self,
        key: str,
        content_hash: str = None
    ) -> bool:
        """
        是否已学习过

        Args:
            key: workflow 相对路径
            content_hash: 当前文件指纹。传入且开启指纹判定时，
                          内容变了就算没学过

        Returns:
            是否已学习过
        """
        path = self.record_file(key)

        if not path.exists():
            return False

        if not content_hash or not self.use_hash:
            return True

        record = self.read(key)
        if record is None:
            return False

        # 上次没学成功的不算学过，否则失败的文件永远不会被重试
        if record.status != STATUS_COMPLETED:
            return False

        previous = record.content_hash
        if previous and previous != content_hash:
            return False

        return True

    def needs_learn(
        self,
        key: str,
        content_hash: str = ""
    ) -> bool:
        """
        是否需要学习（exists 的语义化别名）
        """
        return not self.exists(key, content_hash)

    def read(self, key: str) -> Optional[LearningRecord]:
        """
        读某 workflow 的学习记录

        Args:
            key: workflow 相对路径

        Returns:
            LearningRecord；未学过返回 None
        """
        path = self.record_file(key)

        if not path.exists():
            return None

        try:
            return from_markdown(
                path.read_text(encoding="utf-8-sig")
            )
        except Exception as e:
            print(f"读取学习记录失败 {path}: {e}")
            return None

    def write(self, record: LearningRecord) -> str:
        """
        写入学习记录

        Args:
            record: 学习记录

        Returns:
            记录文件路径；失败返回空串
        """
        try:
            path = self.record_file(record.key)
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                to_markdown(record), encoding="utf-8"
            )

            if self._cache is not None:
                self._cache[record.key] = record

            if self.write_index:
                self._update_index()

            return str(path)
        except Exception as e:
            print(f"保存学习记录失败: {e}")
            return ""

    def remove(self, key: str) -> bool:
        """
        删除一条记录（便于强制重学）

        Args:
            key: workflow 相对路径

        Returns:
            是否确实删除了
        """
        path = self.record_file(key)

        if path.exists():
            path.unlink()

            if self._cache is not None:
                self._cache.pop(key, None)

            # 顺带清掉空目录，保持 learning/ 干净
            parent = path.parent
            while parent != self.root and parent.is_dir():
                if any(parent.iterdir()):
                    break
                parent.rmdir()
                parent = parent.parent

            if self.write_index:
                self._update_index()

            return True

        return False

    # ---------- 全量查询 ----------

    def keys(self) -> List[str]:
        """
        全部已学习的 workflow key
        """
        return [r.key for r in self.all_records() if r.key]

    def all_records(self) -> List[LearningRecord]:
        """
        全部学习记录
        """
        if not self.root.exists():
            return []

        if self._cache is not None:
            return list(self._cache.values())

        cache = {}

        for path in sorted(self.root.rglob("*.md")):
            # index.md 是汇总表，不是记录
            if path.name == INDEX_PATH.name:
                continue

            try:
                record = from_markdown(
                    path.read_text(encoding="utf-8-sig")
                )
            except Exception:
                continue

            if record.key:
                cache[record.key] = record

        self._cache = cache
        return list(cache.values())

    def completed_records(self) -> List[LearningRecord]:
        """
        学习成功的记录
        """
        return [
            r for r in self.all_records()
            if r.status == STATUS_COMPLETED
        ]

    def prune_missing(self, existing_keys: List[str]) -> List[str]:
        """
        清理已不存在的文件对应的记录

        Args:
            existing_keys: 当前扫描到的 key 列表

        Returns:
            被清理的 key
        """
        existing = set(existing_keys)
        removed = []

        for record in self.all_records():
            if record.key not in existing:
                self.remove(record.key)
                removed.append(record.key)

        return removed

    # ---------- 聚合统计 ----------

    def unique_records(self) -> List[LearningRecord]:
        """
        completed_records() 的内容去重视图

        同一 workflow 以不同文件名重复上传时（content_hash 相同）
        只保留首次出现 —— 聚合统计应该用它，否则频次被夸大
        （2026-10-06 实测 504 条里有 96 条是重复拷贝）。
        """
        from .dedupe import dedupe_by_content_hash
        unique, _ = dedupe_by_content_hash(self.completed_records())
        return unique

    def node_frequency(
        self, exclude_ignored: bool = False
    ) -> Dict[str, int]:
        """
        节点出现频次

        高频节点 = 通用必备；只出现一次的节点 = 该 workflow 特有。
        这正是 knowledge_evolution 挖模式需要的输入。

        exclude_ignored=True 时排除布线/注释/预览类节点
        （ignore_nodes.IGNORED_NODES），用于排建卡优先级——
        否则 Note/Reroute/GetNode 这类纯布线节点永久霸榜。

        按内容指纹去重后统计：重复上传的拷贝只算一次，
        否则「被 N 个 workflow 使用」说的是夸大的数字。
        """
        counter: Dict[str, int] = {}

        for record in self.unique_records():
            for node in record.nodes:
                if exclude_ignored and is_ignored(node):
                    continue
                counter[node] = counter.get(node, 0) + 1

        return counter

    def common_nodes(self, min_count: int = 2) -> List[str]:
        """
        至少出现在 min_count 个 workflow 里的节点
        """
        return [
            node for node, count in self.node_frequency().items()
            if count >= min_count
        ]

    def filter_by_type(self, workflow_type: str) -> List[LearningRecord]:
        """
        按工作流类型过滤
        """
        return [
            r for r in self.completed_records()
            if r.workflow_type == workflow_type
        ]

    def coverage_summary(self) -> Dict:
        """
        覆盖率概览
        """
        records = self.completed_records()

        if not records:
            return {
                "total": 0,
                "avg_coverage": 0.0,
                "nodes_with_no_card": [],
            }

        coverages = [r.coverage for r in records]

        missing_counter: Dict[str, int] = {}
        for record in records:
            for node in record.missing_nodes:
                missing_counter[node] = missing_counter.get(node, 0) + 1

        return {
            "total": len(records),
            "avg_coverage": round(
                sum(coverages) / len(coverages), 3
            ),
            "nodes_with_no_card": [
                node for node, count in missing_counter.items()
                if count >= 2
            ],
        }

    def summary(self) -> Dict:
        """
        概览
        """
        records = self.all_records()
        completed = self.completed_records()

        coverages = [r.coverage for r in completed]

        return {
            "total": len(records),
            "completed": len(completed),
            "failed": len(records) - len(completed),
            "avg_coverage": (
                round(sum(coverages) / len(coverages), 3)
                if coverages else 0.0
            ),
        }

    # ---------- 汇总索引 ----------

    def render_index(self) -> str:
        """
        渲染 index.md 汇总表

        表格里直接给出相对链接，点开就是记录正文 ——
        Agent 读一个文件就知道全貌，不必逐个打开。
        """
        records = sorted(
            self.completed_records(),
            key=lambda r: r.key,
        )

        lines = [
            "# Workflow 学习索引",
            "",
            "> 本文件由 `engine/workflow_learning/` 自动生成，勿手改。",
            "> 每个 workflow 的完整记录在同目录下的 `<路径>.md`，"
            "frontmatter 存元数据、正文存学习内容。",
            "",
            "| workflow | 类型 | 节点 | 覆盖 | 指纹 | 学于 |",
            "|---|---|---|---|---|---|",
        ]

        for record in records:
            link = index_link_for(record.key) \
                if self.root == STATE_DIR \
                else self.record_file(record.key).relative_to(
                    self.root
                ).as_posix()

            lines.append(
                f"| [`{record.key}`]({link}) "
                f"| {record.workflow_type or '未识别'} "
                f"| {len(record.nodes)} "
                f"| {record.coverage:.0%} "
                f"| `{record.content_hash[:8]}` "
                f"| {record.learned_at} |"
            )

        failed = [
            r for r in self.all_records()
            if r.status != STATUS_COMPLETED
        ]

        if failed:
            lines.extend([
                "",
                "## 未完成",
                "",
                "| workflow | 状态 | 原因 |",
                "|---|---|---|",
            ])
            for record in failed:
                lines.append(
                    f"| `{record.key}` | {record.status} "
                    f"| {record.error} |"
                )

        stats = self.summary()
        lines.extend([
            "",
            "---",
            "",
            f"共 {stats['total']} 条，成功 {stats['completed']}，"
            f"失败 {stats['failed']}，"
            f"平均覆盖率 {stats['avg_coverage']:.0%}",
            "",
        ])

        return "\n".join(lines)

    def _update_index(self) -> None:
        """
        写 index.md
        """
        try:
            ensure_state_dir() if self.root == STATE_DIR \
                else self.root.mkdir(parents=True, exist_ok=True)

            path = INDEX_PATH if self.root == STATE_DIR \
                else self.root / INDEX_PATH.name

            path.write_text(self.render_index(), encoding="utf-8")
        except Exception as e:
            print(f"写 index.md 失败: {e}")

    def render_record(self, record: LearningRecord) -> str:
        """
        只渲染正文（不含 frontmatter），用于其他场景
        """
        return render_body(record)
