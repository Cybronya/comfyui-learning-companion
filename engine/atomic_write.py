"""
原子写：先写同目录临时文件，成功后 os.replace 覆盖目标

为什么需要（2026-10-17 血泪）：
`Path.write_text()` 是 mode 'w' —— **先截断再写**。写到一半失败时
（磁盘满 / MemoryError / 进程被杀），旧文件已经没了、新文件还是半截，
数据直接丢，而且**报错还看不出原因**。实测事故：

- `knowledge_graph.json` 在 4 万顶点时，`json.dumps` 先拼几百 MB 文本、
  `write_text` 内部再编码一份 bytes，峰值内存翻倍 → OOM；
  而 OOM 发生在截断之后、写入完成之前 → 整张图谱变成 **0 字节**，
  只能重跑 4 分钟重建图（`MemoryError` 的 str 是空的，控制台只打出
  `保存知识图谱失败:` 四个字）。

改成临时文件 + `os.replace` 后：写失败只丢临时文件，目标文件原封不动；
`json.dump` 直接写文件句柄，也不再需要拼整份大字符串（少一份峰值内存）。

约定（AGENTS 3.4）：只用标准库，不引第三方依赖。
读 JSON 一律 utf-8-sig（Windows 下 ComfyUI 导出带 BOM）；写用 utf-8 无 BOM。
"""

import json
import os
import tempfile
from pathlib import Path
from typing import Any, Union

PathLike = Union[str, "os.PathLike[str]"]


def atomic_write_text(
    path: PathLike,
    text: str,
    encoding: str = "utf-8",
    newline: str = "\n",
) -> Path:
    """
    原子写文本（失败时目标文件不变）

    Args:
        path: 目标路径
        text: 内容
        encoding: 写编码（默认 utf-8 无 BOM）
        newline: 换行符（默认 \\n，避免 Windows 写 CRLF）

    Returns:
        目标 Path

    Raises:
        写入过程中的异常原样抛出；临时文件已被清理
    """
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(
        dir=str(target.parent),
        prefix=target.name + ".",
        suffix=".tmp",
    )
    try:
        with os.fdopen(fd, "w", encoding=encoding, newline=newline) as f:
            f.write(text)
        os.replace(tmp_name, target)          # 原子替换，跨平台
        return target
    except BaseException:
        # 任何失败（含 KeyboardInterrupt）都不留半截临时文件
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def atomic_write_json(
    path: PathLike,
    data: Any,
    indent: int = 2,
    ensure_ascii: bool = False,
    encoding: str = "utf-8",
    newline: str = "\n",
) -> Path:
    """
    原子写 JSON（**流式**，不拼整份字符串）

    大对象用 `atomic_write_text(json.dumps(...))` 会同时驻留
    「对象 + 整份文本 + 编码后的 bytes」三份，峰值内存 3 倍。
    这里直接 `json.dump` 写文件句柄，只有对象本身在内存里。

    Args:
        path: 目标路径
        data: 可 JSON 序列化的对象
        indent: 缩进（None / 0 表示紧凑）
        ensure_ascii: 是否把非 ASCII 转义（False 才可读）
        encoding: 写编码
        newline: 换行符

    Returns:
        目标 Path

    Raises:
        序列化失败（TypeError 等）与 IO 错误原样抛出，目标文件不变
    """
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(
        dir=str(target.parent),
        prefix=target.name + ".",
        suffix=".tmp",
    )
    try:
        with os.fdopen(fd, "w", encoding=encoding, newline=newline) as f:
            json.dump(data, f, indent=indent or None, ensure_ascii=ensure_ascii)
            f.write("\n")
        os.replace(tmp_name, target)
        return target
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise