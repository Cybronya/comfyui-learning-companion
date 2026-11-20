"""
项目内临时工作区（**禁止使用 C 盘 / 系统临时目录**）

规则（2026-11-20 用户明确要求）
--------------------------------
所有任务、测试、工具产生的临时文件、临时目录、临时数据库、临时工作副本，
**只能在本项目目录内创建、使用、删除**。不得写入：

- ``C:\\Users\\<user>\\AppData\\Local\\Temp``（系统 TEMP）
- ``C:\\Windows\\Temp``
- 任何系统盘上的临时/缓存目录
- 任何项目目录之外的位置

原因
----
1. **可审计**：临时产物留在项目内，出问题能直接翻目录查；
   散落到系统 Temp 里出问题后基本无法复盘。
2. **不污染系统盘**：跑一次全量学习/推送就可能产生 GB 级临时文件，
   写系统盘会挤占用户空间且清理不可控。
3. **可清理**：项目内临时目录可以整体删除并加进 ``.gitignore``，
   系统 Temp 里的残留只能靠人工翻。

用法
----
测试文件把标准库的导入换成项目内的：

.. code-block:: python

    # 原来
    from tempfile import TemporaryDirectory

    # 改成
    from engine.tmp_workspace import TemporaryDirectory

``TemporaryDirectory`` 是标准库同名类的**下位替身**，API 兼容
（``with`` 上下文管理、``.name`` 属性、退出时自动递归删除），
但根目录固定在 ``<项目根>/.tmp/`` 下。

命令行工具直接用：

.. code-block:: python

    from engine.tmp_workspace import project_temp_dir, temp_path

    with project_temp_dir("my_task") as d:
        ...          # d 在项目内 .tmp/my_task-xxxx/

也可以直接调 ``temp_path("名字.扩展名")`` 得到项目内的临时文件路径。
"""

from __future__ import annotations

import shutil
import tempfile
from pathlib import Path
from types import TracebackType

__all__ = [
    "PROJECT_ROOT",
    "TMP_ROOT",
    "project_temp_dir",
    "temp_path",
    "TemporaryDirectory",
]


# ---- 项目根定位 ----------------------------------------------------
# 本文件位于 <项目根>/engine/tmp_workspace.py
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# 统一的临时工作区根目录：<项目根>/.tmp
TMP_ROOT = PROJECT_ROOT / ".tmp"


def _ensure_tmp_root() -> Path:
    """确保项目内临时根目录存在并可用。"""
    TMP_ROOT.mkdir(parents=True, exist_ok=True)
    return TMP_ROOT


def project_temp_dir(prefix: str = "task", suffix: str = "") -> Path:
    """
    在项目内 ``.tmp/`` 下创建一个**独立**临时目录（不自动删除）。

    与 :class:`TemporaryDirectory` 不同，这个不负责清理 ——
    适合长跑任务（下载/学习/推送）需要跨进程保留中间态的场景。

    Args:
        prefix: 目录名前缀，便于事后辨认用途
        suffix: 目录名后缀

    Returns:
        新建的目录路径（已在项目内）
    """
    root = _ensure_tmp_root()
    return Path(tempfile.mkdtemp(prefix=f"{prefix}-", suffix=suffix, dir=str(root)))


def temp_path(name: str = "tmp.bin", subdir: str = "") -> Path:
    """
    返回项目内的一个临时文件路径（**不创建文件**）。

    Args:
        name: 文件名
        subdir: ``.tmp/`` 下的子目录（可为空）

    Returns:
        完整路径（父目录会被确保存在）
    """
    root = _ensure_tmp_root()
    base = root / subdir if subdir else root
    base.mkdir(parents=True, exist_ok=True)
    return base / name


class TemporaryDirectory:
    """
    标准库 ``tempfile.TemporaryDirectory`` 的项目内替身。

    行为差异只有一处：**根目录固定在 ``<项目根>/.tmp/``**，
    而不是系统 TEMP。其余 API（``with``、``.name``、退出自动清理）完全一致。

    Example:
        >>> with TemporaryDirectory() as tmp:
        ...     p = Path(tmp) / "x.db"
        ...     p.write_text("hi")
    """

    def __init__(self, suffix: str | None = None, prefix: str | None = None,
                 dir: str | None = None) -> None:
        """
        Args:
            suffix: 目录名后缀
            prefix: 目录名前缀
            dir: **忽略**。保留此参数只为兼容标准库签名；
                出于「临时目录只能在项目内」的规则，本实现拒绝在项目外创建。
        """
        if dir is not None:
            root = Path(dir).resolve()
            try:
                root.relative_to(PROJECT_ROOT)
            except ValueError:
                raise ValueError(
                    f"临时目录必须位于项目内（{PROJECT_ROOT}）之下，"
                    f"拒绝使用：{root}"
                ) from None
        self._prefix = prefix if prefix is not None else "tmp-"
        self._suffix = suffix if suffix is not None else ""
        self._finalizer = None
        self.name = str(project_temp_dir(prefix=self._prefix, suffix=self._suffix))

    # ---- 上下文管理器 ----
    def __enter__(self) -> str:
        return self.name

    def __exit__(self, exc_type: type[BaseException] | None,
                 exc_val: BaseException | None,
                 exc_tb: TracebackType | None) -> bool:
        self.cleanup()
        return False

    # ---- 清理 ----
    def cleanup(self) -> None:
        """递归删除临时目录（幂等）。"""
        p = Path(self.name)
        if p.exists():
            shutil.rmtree(p, ignore_errors=True)

    # ---- 与标准库一致的其它接口 ----
    def __repr__(self) -> str:
        return f"<TemporaryDirectory {self.name!r}>"
