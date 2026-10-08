"""
Workflow 扫描器

扫描目录下的 workflow 文件。支持 .json 与 .png（PNG 内嵌工作流元数据）。

两个容易踩的点：
1. ComfyUI 导出会产生 _workflow.json / _prompt.json 这类伴生文件。
   _prompt.json 是 API 格式（没有 UI 的 nodes[].type 结构），
   拿去喂 WorkflowAnalyzer 会出错。默认跳过。
2. 文件名当键会撞：a/sd15_basic.json 与 b/sd15_basic.json 同名。
   所以同时返回相对路径作为 key。
"""

import json
import struct
import zlib
from pathlib import Path
from typing import List, Dict, Any, Optional

from .paths import SKIPPED_DIR_NAMES, relative_to_project


# 伴生文件前缀（ComfyUI 导出约定）
SIDECAR_PREFIX = "_"

# 伴生文件名（即便没有下划线前缀也跳过）
SIDECAR_NAMES = {"workflow.json", "prompt.json"}

# 扩展名 → 来源类型
SOURCE_KIND = {
    ".json": "json",
    ".png": "png",
}


class WorkflowScanner:
    """
    workflow 文件扫描器
    """

    def __init__(
        self,
        extensions: Optional[List[str]] = None,
        include_sidecars: bool = False
    ) -> None:
        """
        初始化扫描器

        Args:
            extensions: 要扫描的扩展名，默认 [".json", ".png"]
            include_sidecars: 是否包含 _workflow.json / _prompt.json 这类伴生文件
        """
        self.extensions = [
            e.lower() if e.startswith(".") else f".{e.lower()}"
            for e in (extensions or [".json", ".png"])
        ]
        self.include_sidecars = include_sidecars

    def scan(self, folder: str) -> List[Dict[str, Any]]:
        """
        扫描目录

        用 os.walk 而非 rglob：workflows/ 下有约一半文件是 learning/
        里的学习记录（4000+ 个 .md），rglob 无法目录级剪枝，会把它们
        全部 stat 一遍再逐个丢弃 —— 千级文件时扫描就要 8 秒+，
        而剪枝后只碰真正的 workflow 文件。

        Args:
            folder: 目录路径

        Returns:
            [{"name", "path", "rel_path", "key", "kind"}]
            key 是相对路径（用 / 分隔，跨平台一致）。
            不再带 size 字段：无消费方，而逐文件 stat 在 4000+ 个
            文件时是扫描剩余耗时的全部（约 1 秒）；需要大小时对
            单个 path 调 os.stat 即可
        """
        import os

        root = Path(folder)
        if not root.exists():
            return []

        # rel_path 预解析：resolve()/relative_to() 每次都含系统调用与
        # pathlib 开销，3946 个文件要 2 秒+；扫描根只 resolve 一次，
        # 之后用前缀字符串切割（纯内存运算，0.04s）。
        # 根不在仓库内（如临时目录测试）时退回逐个 relative_to_project
        root_resolved = root.resolve()
        try:
            from .paths import PROJECT_ROOT
            project_root_str = str(PROJECT_ROOT)
        except ImportError:
            project_root_str = None

        def _rel_path(file_str: str) -> str:
            if project_root_str:
                s = file_str
                if s.startswith(project_root_str):
                    return s[len(project_root_str) + 1:].replace("\\", "/")
            return relative_to_project(file_str)

        workflows = []

        for dirpath, dirnames, filenames in os.walk(root_resolved):
            # 状态目录（learning/）整枝剪掉：里面是学习记录不是 workflow，
            # 不能拿去"学习"——否则每次批量学习都会把自己的记录当成
            # 新 workflow，产出 report 再写进记录，无限循环
            dirnames[:] = [
                d for d in dirnames if d not in SKIPPED_DIR_NAMES
            ]

            for name in sorted(filenames):
                file = Path(dirpath) / name
                # 后缀与伴生判断只用文件名，不必先构造完整 Path 链
                dot = name.rfind(".")
                suffix = name[dot:].lower() if dot >= 0 else ""
                if suffix not in self.extensions:
                    continue

                if not self.include_sidecars and self._is_sidecar(file):
                    continue

                s = str(file)
                # key/rel_path 都是前缀切割（见 _rel_path 注释）
                rel_to_root = s[len(str(root_resolved)) + 1:].replace(
                    "\\", "/"
                )

                workflows.append({
                    "name": file.stem,
                    # 存绝对路径供立即读取，但一并给相对路径便于持久化
                    "path": s,
                    "rel_path": _rel_path(s),
                    "key": rel_to_root,
                    "kind": SOURCE_KIND.get(suffix, suffix.lstrip(".")),
                })

        workflows.sort(key=lambda w: w["key"])
        return workflows

    @staticmethod
    def _is_sidecar(file: Path) -> bool:
        """
        判断是否为 ComfyUI 导出的伴生文件
        """
        if file.stem.startswith(SIDECAR_PREFIX):
            return True
        return file.stem.lower() in SIDECAR_NAMES


# ============================================================
# PNG 工作流元数据提取
# ============================================================

def extract_text_chunks(png_path: str) -> Dict[str, str]:
    """
    提取 PNG 内嵌的文本块

    逻辑与 skills/comfyui-learning/tools/extract_png_workflow.py 一致
    （纯标准库，不引入 PIL）。ComfyUI 把工作流塞进 tEXt 的
    "workflow" 键（UI 格式）与 "prompt" 键（API 格式）。

    Args:
        png_path: PNG 文件路径

    Returns:
        {键: 值}
    """
    data = Path(png_path).read_bytes()

    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("不是有效的 PNG 文件")

    pos = 8
    found: Dict[str, str] = {}

    while pos < len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        ctype = data[pos + 4:pos + 8].decode("latin1", errors="replace")
        chunk = data[pos + 8:pos + 8 + length]

        if ctype == "tEXt":
            key, _, val = chunk.partition(b"\x00")
            found.setdefault(
                key.decode("latin1", errors="replace"),
                val.decode("latin1", errors="replace"),
            )
        elif ctype == "iTXt":
            key, _, rest = chunk.partition(b"\x00")
            if len(rest) < 2:
                pos += 8 + length + 4
                continue
            comp_flag = rest[0]
            rest = rest[2:]          # 跳过 compression_method
            _lang, _, rest = rest.partition(b"\x00")
            _tkey, _, text = rest.partition(b"\x00")
            if comp_flag == 0:
                found.setdefault(
                    key.decode("latin1", errors="replace"),
                    text.decode("utf-8", errors="replace"),
                )
            else:
                try:
                    found.setdefault(
                        key.decode("latin1", errors="replace"),
                        zlib.decompress(text).decode(
                            "utf-8", errors="replace"
                        ),
                    )
                except zlib.error:
                    pass
        elif ctype == "zTXt":
            key, _, rest = chunk.partition(b"\x00")
            try:
                found.setdefault(
                    key.decode("latin1", errors="replace"),
                    zlib.decompress(rest[1:]).decode(
                        "latin1", errors="replace"
                    ),
                )
            except zlib.error:
                pass

        pos += 8 + length + 4
        if ctype == "IEND":
            break

    return found


def load_png_workflow(png_path: str) -> Optional[Dict]:
    """
    从 PNG 提取 UI 格式的工作流

    Args:
        png_path: PNG 文件路径

    Returns:
        UI 格式 workflow dict；未内嵌则返回 None
    """
    try:
        chunks = extract_text_chunks(png_path)
    except Exception:
        return None

    for key in ("workflow", "Workflow"):
        if key not in chunks:
            continue
        try:
            data = json.loads(chunks[key])
        except (json.JSONDecodeError, TypeError):
            continue

        # UI 格式必须有 nodes 数组且节点带 type 字段；
        # API 格式（prompt 键）用 class_type，两者不能混用
        nodes = data.get("nodes")
        if isinstance(nodes, list) and nodes:
            if any("type" in n for n in nodes if isinstance(n, dict)):
                data["_extracted_from"] = "png"
                return data

    return None
