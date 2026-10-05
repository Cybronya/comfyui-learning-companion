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

        Args:
            folder: 目录路径

        Returns:
            [{"name", "path", "key", "kind", "size"}]
            key 是相对路径（用 / 分隔，跨平台一致）
        """
        root = Path(folder)
        if not root.exists():
            return []

        workflows = []

        for file in sorted(root.rglob("*")):
            if not file.is_file():
                continue

            # 跳过状态目录（learning/）：里面放的是 registry.json /
            # experience.json / reports，不是 workflow，不能拿去"学习"。
            # 否则每次跑批量学习都会把自己的学习记录当成新 workflow，
            # 产出 report、coverage 100%、然后把自己写进 registry，无限循环。
            if self._in_state_dir(file, root):
                continue

            suffix = file.suffix.lower()
            if suffix not in self.extensions:
                continue

            if not self.include_sidecars and self._is_sidecar(file):
                continue

            relative = file.relative_to(root).as_posix()

            workflows.append({
                "name": file.stem,
                # 存绝对路径供立即读取，但一并给相对路径便于持久化
                "path": str(file),
                "rel_path": relative_to_project(file),
                "key": relative,
                "kind": SOURCE_KIND.get(suffix, suffix.lstrip(".")),
                "size": file.stat().st_size,
            })

        return workflows

    @staticmethod
    def _is_sidecar(file: Path) -> bool:
        """
        判断是否为 ComfyUI 导出的伴生文件
        """
        if file.stem.startswith(SIDECAR_PREFIX):
            return True
        return file.stem.lower() in SIDECAR_NAMES

    @staticmethod
    def _in_state_dir(file: Path, root: Path) -> bool:
        """
        判断文件是否位于状态目录内

        Args:
            file: 待判断文件
            root: 扫描根目录

        Returns:
            是否在状态目录内
        """
        try:
            relative = file.relative_to(root)
        except ValueError:
            return False

        # 目录层级里任一段命中 learning 即视为状态文件
        return any(
            part in SKIPPED_DIR_NAMES
            for part in relative.parts[:-1]
        )


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
