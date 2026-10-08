"""
批量学习管理

design 第九节给的「完整运行逻辑」是一段 10 行的 for 循环，
实际用起来缺三样东西：进度可见、失败隔离、可重复运行的安全性。
这里封装成 BatchWorkflowLearner.learn_folder()。

    扫描目录 → 查登记表 → 跳过已学的 → 逐个学习
             → 写报告 → 存经验 → 更新登记表 → 汇总

    （接了 database 时，每条记录同时镜像进 WorkflowDatabase，
      见 database_bridge —— Markdown 仍是记录正身，库是查询层）

幂等：同一批文件反复跑，第二次应全部跳过；
改了内容的文件应被识别为「需重学」并重新学习。
"""

from pathlib import Path
from typing import Any, Dict, List, Optional

from .learning_record import (
    LearningRecord,
    STATUS_COMPLETED,
    STATUS_FAILED,
)
from .workflow_scanner import WorkflowScanner
from .workflow_learner import WorkflowLearner
from .learning_store import LearningStore
from .database_bridge import sync_record, sync_all
from .paths import WORKFLOWS_DIR, relative_to_project


class BatchWorkflowLearner:
    """
    批量 workflow 学习器
    """

    def __init__(
        self,
        learner: WorkflowLearner,
        store=None,
        scanner: WorkflowScanner = None,
        verbose: bool = True,
        database=None
    ) -> None:
        """
        初始化批量学习器

        Args:
            learner: 单文件学习器
            store: LearningStore（记录读写与统计都归它）
            scanner: 目录扫描器
            verbose: 是否打印进度
            database: WorkflowDatabase；传入则每条学习结果
                      镜像进库（workflow 记录 + 经验载荷）。
                      None 时不接库，行为与旧版一致
        """
        self.learner = learner
        # 批量模式开启 index 延迟渲染：learn_folder 批内只标脏，
        # 结束时 flush_index() 统一渲染一次（默认 store 也生效；
        # 外部传入的 store 会被就地开启，批次结束恢复原状）
        self.store = store or LearningStore()
        self._store_defer_owned = store is None or not getattr(
            store, "defer_index", False
        )
        self.scanner = scanner or WorkflowScanner()
        self.verbose = verbose
        self.database = database

    # 兼容旧属性名：registry / experience 曾是两个独立存储，
    # 现在合并为一个 store，指向同一份 Markdown 记录
    @property
    def registry(self):
        return self.store

    @property
    def experience(self):
        return self.store

    def learn_folder(
        self,
        folder: str = None,
        force: bool = False,
        prune: bool = True
    ) -> Dict[str, Any]:
        """
        批量学习一个目录下的所有 workflow

        Args:
            folder: 目录路径；None 时用统一位置
                   `comfyui_library/workflows/`
            force: 忽略已有记录，强制全部重学
            prune: 是否清理已删除文件对应的记录

        Returns:
            批次摘要 {
                "folder", "total_found", "learned", "skipped",
                "failed", "records", "skipped_keys", "pruned",
                "elapsed_ms"
            }
        """
        import time

        if folder is None:
            folder = WORKFLOWS_DIR

        started = time.perf_counter()

        files = self.scanner.scan(folder)

        if not self.verbose:
            pass
        else:
            print(f"扫描 {folder}：找到 {len(files)} 个 workflow 文件")

        if not files:
            return self._summary(
                folder=folder,
                learned=[],
                total=0,
                skipped=0,
                failed=0,
                started=started,
            )

        learned: List[LearningRecord] = []
        skipped: List[str] = []

        # 批量镜像时关掉逐条落盘（库 20MB+ 时逐条全量写是主要瓶颈），
        # 循环结束统一 save 一次；异常也要保证落盘，不能丢整批
        if self.database is not None:
            self.database.auto_save = False

        # 批量模式下 index 延迟渲染，结束统一 flush（见 __init__ 注释）
        store = self.store
        if self._store_defer_owned and hasattr(store, "defer_index"):
            prev_defer = store.defer_index
            store.defer_index = True

        try:
            for item in files:
                key = item["key"]
                path = item["path"]

                if not force:
                    content_hash = self._peek_hash(path)
                    if self.store.exists(key, content_hash):
                        skipped.append(key)
                        if self.verbose:
                            print(f"  跳过 {key}（已学习）")
                        continue

                record = self.learner.learn(path, key=key)

                # 记录本身就是完整报告（frontmatter + 正文），
                # 写进去就同时完成了「登记」与「出报告」
                record_path = self.store.write(record)
                if record_path:
                    record.report_path = record_path

                # Markdown 落盘成功后镜像进数据库（失败只提示不中断）
                if record_path and self.database is not None:
                    sync_record(record, self.database, verbose=self.verbose)

                if record.status == STATUS_COMPLETED:
                    learned.append(record)
                    if self.verbose:
                        print(
                            f"  学习 {key}：{len(record.nodes)} 节点，"
                            f"覆盖 {record.coverage:.0%}"
                        )
                else:
                    if self.verbose:
                        print(f"  失败 {key}：{record.error}")
        finally:
            if self.database is not None:
                self.database.save()
                self.database.auto_save = True
            # index.md 批内只标脏，批次结束统一渲染一次
            if self._store_defer_owned and hasattr(store, "defer_index"):
                store.defer_index = prev_defer
            store.flush_index()

        # 清理已删除文件的记录
        pruned = []
        if prune:
            pruned = self.store.prune_missing(
                [f["key"] for f in files]
            )
            if pruned and self.verbose:
                print(f"  清理失效记录 {len(pruned)} 条")

        return self._summary(
            folder=folder,
            learned=learned,
            total=len(files),
            skipped=len(skipped),
            failed=len(files) - len(learned) - len(skipped),
            started=started,
            skipped_keys=skipped,
            pruned=pruned,
        )

    def learn_file(self, path: str, key: str = "", force: bool = False) -> LearningRecord:
        """
        学习单个文件

        Args:
            path: 文件路径
            key: 标识键
            force: 忽略登记表

        Returns:
            LearningRecord
        """
        record_key = key or Path(path).name

        if not force:
            content_hash = self._peek_hash(path)
            if self.store.exists(record_key, content_hash):
                if self.verbose:
                    print(f"跳过 {record_key}（已学习）")
                return LearningRecord(
                    workflow_name=Path(path).stem,
                    file_path=relative_to_project(path),
                    key=record_key,
                    status="skipped",
                )

        record = self.learner.learn(path, key=record_key)

        record_path = self.store.write(record)
        if record_path:
            record.report_path = record_path

        if record_path and self.database is not None:
            sync_record(record, self.database, verbose=self.verbose)

        return record

    def sync_database(self, database=None) -> Dict[str, int]:
        """
        全量镜像：把 LearningStore 里的存量记录补进数据库

        数据库是后建的，先学的记录不会自动出现在库里 ——
        用这个方法做一次性迁移。幂等，重复跑只是覆盖。

        Args:
            database: 目标库；None 时用构造时传入的 self.database

        Returns:
            {"synced", "skipped", "failed"}
        """
        target = database if database is not None else self.database
        if target is None:
            raise RuntimeError(
                "未指定数据库：构造时传 database= 或在此传入"
            )
        return sync_all(self.store, target, verbose=self.verbose)

    def pending(self, folder: str) -> List[Dict[str, Any]]:
        """
        查出哪些文件还没学 / 需要重学

        Args:
            folder: 目录路径

        Returns:
            待学习文件列表
        """
        pending = []

        for item in self.scanner.scan(folder):
            content_hash = self._peek_hash(item["path"])
            if not self.store.exists(item["key"], content_hash):
                pending.append(item)

        return pending

    # ---------- 内部 ----------

    @staticmethod
    def _peek_hash(path: str) -> str:
        """
        取文件指纹用于比对（失败返回空串，交给 exists 处理）
        """
        try:
            return WorkflowLearner._hash_file(Path(path))
        except Exception:
            return ""

    @staticmethod
    def _summary(
        folder: str,
        learned: List[LearningRecord],
        total: int,
        skipped: int,
        failed: int,
        started: float,
        skipped_keys: List[str] = None,
        pruned: List[str] = None,
    ) -> Dict[str, Any]:
        """汇总批次结果"""
        import time

        return {
            "folder": relative_to_project(folder),
            "total_found": total,
            "learned": len(learned),
            "skipped": skipped,
            "failed": failed,
            "records": [r.to_dict() for r in learned],
            "record_paths": [r.report_path for r in learned],
            "skipped_keys": skipped_keys or [],
            "pruned": pruned or [],
            "elapsed_ms": round(
                (time.perf_counter() - started) * 1000, 1
            ),
        }
