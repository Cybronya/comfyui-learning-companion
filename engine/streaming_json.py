"""
流式 JSON 读写工具

## 为什么需要

项目里有几个**大 JSON 派生文件**（都是几百 MB 量级）：

    engine/knowledge_graph/knowledge_graph.json      848MB / 12.3 万顶点 / 289 万边
    engine/retrieval/retrieval_store.json            593MB / 关键词倒排索引

`json.load()` 会把整个文件读成一个 Python 对象树。对 848MB 的图谱来说，
峰值内存 = 848MB 文本 + 290 万个 dict 对象树 + 已建好的图，
24GB 机器上直接 **MemoryError**。

而且 **`MemoryError` 的 str 是空的** —— 控制台只打出
`读取知识图谱失败:` 四个字，看不出原因，排查时非常费劲
（2026-11-20 真实卡在 `test_knowledge_graph` 的 F2 上）。

标准库没有流式 JSON 解析器，但 `json.JSONDecoder.raw_decode`
可以在缓冲区里解出**一个**完整值。自己拼一个增量解析器即可：

    解出值 → 若解码位置已到缓冲区末尾（值可能被截断，
    比如「12288」其实是「122880」的前半截）→ 补读一块重解
    → 否则位置后移，继续解下一个值

## 提供什么

- `JsonStreamReader` —— 增量解析一个流式 JSON 文件
- `write_json_stream()` —— 逐条写 JSON 数组字段（不先拼整份 payload）
- `stream_array()` —— 把「顶层对象里的某个数组字段」解成迭代器

## 约定

- 读 JSON 一律 `utf-8-sig`（项目约定，Windows 下 ComfyUI 导出带 BOM）
- 写 JSON 用 utf-8 无 BOM
- 临时文件建在**目标同目录**（`os.replace` 原子替换的硬要求），
  不要用系统 `%TEMP%`（AGENTS.md 3.6）
"""

import json
import os
import tempfile
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Optional

#: 分块大小。1MB 足够让 raw_decode 一次吃掉一个数组元素，
#: 又不会让缓冲区本身占多少内存。
DEFAULT_CHUNK = 1 << 20


class JsonStreamReader:
    """
    增量 JSON 读取器

    用法（解析一个顶层对象，某个字段是数组）：

        reader = JsonStreamReader(fp)
        reader.expect("{")
        while True:
            ch = reader.peek()
            if ch == "":
                raise ValueError("文件提前结束")
            if ch == "}":
                reader.pos += 1
                break
            if ch == ",":
                reader.pos += 1
                continue
            key = reader.read_value()
            reader.expect(":")
            if key == "nodes":
                for item in reader.iter_array():
                    ...
            else:
                value = reader.read_value()
    """

    def __init__(self, fp, chunk: int = DEFAULT_CHUNK) -> None:
        self.fp = fp
        self.chunk = chunk
        self.buf = ""
        self.pos = 0
        self.decoder = json.JSONDecoder()

    # ---------- 缓冲 ----------

    def _fill(self) -> bool:
        """再读一块进缓冲区；到 EOF 返回 False"""
        data = self.fp.read(self.chunk)
        if not data:
            return False
        self.buf += data
        return True

    def compact(self) -> None:
        """丢掉已消费的前缀（否则缓冲区会涨到整个文件大小）"""
        if self.pos > self.chunk:
            self.buf = self.buf[self.pos:]
            self.pos = 0

    # ---------- 词法 ----------

    def skip_ws(self) -> None:
        """跳过空白"""
        while True:
            while self.pos < len(self.buf) and self.buf[self.pos] in " \t\r\n":
                self.pos += 1
            if self.pos < len(self.buf):
                return
            if not self._fill():
                return

    def peek(self) -> str:
        """看下一个非空白字符；EOF 返回空串"""
        self.skip_ws()
        if self.pos >= len(self.buf):
            return ""
        return self.buf[self.pos]

    def expect(self, ch: str) -> None:
        """吃掉一个必须出现的字符"""
        got = self.peek()
        if got != ch:
            raise ValueError(f"期望 {ch!r}，实际 {got!r}")
        self.pos += 1

    def read_value(self) -> Any:
        """解出一个完整的 JSON 值"""
        while True:
            self.skip_ws()
            try:
                value, end = self.decoder.raw_decode(self.buf, self.pos)
            except ValueError:
                # 不完整 → 补读再试（真格式错误则会在 EOF 后抛出）
                if self._fill():
                    continue
                raise
            if end >= len(self.buf):
                # 解码正好停在缓冲区末尾：值可能被截断
                # （「12288」可能是「122880」的前半截），
                # 补读后重解。
                if self._fill():
                    continue
            self.pos = end
            return value

    def iter_array(self) -> Iterator[Any]:
        """逐个解出数组元素（数组本身已在当前位置）"""
        self.expect("[")
        while True:
            ch = self.peek()
            if ch == "":
                raise ValueError("数组未正常结束")
            if ch == "]":
                self.pos += 1
                return
            if ch == ",":
                self.pos += 1
                continue
            yield self.read_value()
            self.compact()


def stream_array(
    fp,
    key: str,
    chunk: int = DEFAULT_CHUNK,
) -> Iterator[Any]:
    """
    从一个 JSON 对象里取某个数组字段，逐元素产出

    Args:
        fp: 已打开的文本文件句柄
        key: 数组字段名
        chunk: 分块大小

    Yields:
        数组元素（已解析成 Python 值）

    Raises:
        ValueError: 结构不符合预期
    """
    reader = JsonStreamReader(fp, chunk)
    reader.expect("{")
    found = False
    while True:
        ch = reader.peek()
        if ch == "":
            raise ValueError("文件提前结束")
        if ch == "}":
            reader.pos += 1
            break
        if ch == ",":
            reader.pos += 1
            continue

        name = reader.read_value()
        reader.expect(":")
        if name == key:
            found = True
            for item in reader.iter_array():
                yield item
        else:
            reader.read_value()
        reader.compact()

    if not found:
        raise ValueError(f"文件里没有 {key!r} 字段")


def iter_dict_of_arrays(fp, chunk: int = DEFAULT_CHUNK) -> Iterator[tuple]:
    """
    从一个「顶层对象的每个值都是数组」的 JSON 里逐元素产出

    典型用途：关键词倒排索引 `{关键词: [条目, ...], ...}`。

    Yields:
        `(键, 元素)` 二元组
    """
    reader = JsonStreamReader(fp, chunk)
    reader.expect("{")
    while True:
        ch = reader.peek()
        if ch == "":
            raise ValueError("文件提前结束")
        if ch == "}":
            reader.pos += 1
            return
        if ch == ",":
            reader.pos += 1
            continue

        key = reader.read_value()
        reader.expect(":")
        for item in reader.iter_array():
            yield key, item
        reader.compact()


def write_json_stream(
    path,
    header: Dict[str, Any],
    arrays: List[tuple],
    indent: int = 2,
) -> Path:
    """
    逐条写一个含多个数组字段的 JSON 文件（原子替换）

    **不先拼整份 payload** —— 这是大图能存下来的关键：
    290 万条边如果先 `json.dumps(payload)`，峰值内存直接翻倍。

    Args:
        path: 目标路径
        header: 顶层标量字段（version / stats 等）
        arrays: `[(字段名, 可迭代对象), ...]`，按给定顺序写
        indent: JSON 缩进（仅作用于 header 段）

    Returns:
        目标 Path
    """
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)

    fd, tmp_name = tempfile.mkstemp(
        dir=str(target.parent),
        prefix=target.name + ".",
        suffix=".tmp",
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write("{\n")
            for i, (name, value) in enumerate(header.items()):
                text = json.dumps(value, ensure_ascii=False, indent=indent)
                text = text.replace("\n", "\n  ")
                f.write(f'  "{name}": {text}')
                if i < len(header) - 1 or arrays:
                    f.write(",")
                f.write("\n")

            for i, (name, items) in enumerate(arrays):
                f.write(f'  "{name}": [\n')
                first = True
                for item in items:
                    if not first:
                        f.write(",\n")
                    f.write("    ")
                    f.write(json.dumps(item, ensure_ascii=False))
                    first = False
                if not first:
                    f.write("\n")
                f.write(f'  ]')
                if i < len(arrays) - 1:
                    f.write(",")
                f.write("\n")

            f.write("}\n")
        os.replace(tmp_name, target)
        return target
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise


def write_json_dict_of_arrays(
    path,
    groups,
    indent: int = 4,
) -> Path:
    """
    写一个「顶层对象的每个值都是数组」的 JSON 文件（原子替换）

    Args:
        path: 目标路径
        groups: `[(键, 可迭代元素), ...]`
        indent: 缩进

    Returns:
        目标 Path
    """
    target = Path(path)
    target.parent.mkdir(parents=True, exist_ok=True)

    fd, tmp_name = tempfile.mkstemp(
        dir=str(target.parent),
        prefix=target.name + ".",
        suffix=".tmp",
    )
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as f:
            f.write("{\n")
            first_key = True
            for key, items in groups:
                if not first_key:
                    f.write(",\n")
                first_key = False
                f.write(f"  {json.dumps(key, ensure_ascii=False)}: [\n")
                first_item = True
                for item in items:
                    if not first_item:
                        f.write(",\n")
                    first_item = False
                    text = json.dumps(item, ensure_ascii=False, indent=indent)
                    # 多行 JSON 后续行要跟着缩进，否则格式乱掉
                    f.write("    " + text.replace("\n", "\n    "))
                if not first_item:
                    f.write("\n")
                f.write("  ]")
            f.write("\n}\n")
        os.replace(tmp_name, target)
        return target
    except BaseException:
        try:
            os.unlink(tmp_name)
        except OSError:
            pass
        raise
