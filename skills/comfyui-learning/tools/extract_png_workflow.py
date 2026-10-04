#!/usr/bin/env python3
"""extract_png_workflow.py — 从 ComfyUI 生成的 PNG 中提取内嵌 workflow 元数据。

用法:
    python extract_png_workflow.py <image.png> [输出目录]

输出:
    在输出目录生成 _workflow.json (UI 格式) / _prompt.json (API 格式)
只依赖 Python 标准库。
"""
from __future__ import annotations

import json
import struct
import sys
import zlib
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def extract_text_chunks(png_path: str) -> dict[str, str]:
    data = Path(png_path).read_bytes()
    if data[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("不是有效的 PNG 文件")
    pos = 8
    found: dict[str, str] = {}
    while pos < len(data):
        length = struct.unpack(">I", data[pos:pos + 4])[0]
        ctype = data[pos + 4:pos + 8].decode("latin1")
        chunk = data[pos + 8:pos + 8 + length]
        if ctype == "tEXt":
            key, _, val = chunk.partition(b"\x00")
            found.setdefault(key.decode("latin1"), val.decode("latin1", errors="replace"))
        elif ctype == "iTXt":
            key, _, rest = chunk.partition(b"\x00")
            comp_flag = rest[0]
            rest = rest[2:]  # 跳过 compression_flag + compression_method
            _lang, _, rest = rest.partition(b"\x00")
            _tkey, _, text = rest.partition(b"\x00")
            if comp_flag == 0:
                found.setdefault(key.decode("latin1"), text.decode("utf-8", errors="replace"))
            else:
                found.setdefault(key.decode("latin1"),
                                 zlib.decompress(text).decode("utf-8", errors="replace"))
        elif ctype == "zTXt":
            key, _, rest = chunk.partition(b"\x00")
            found.setdefault(key.decode("latin1"),
                             zlib.decompress(rest[1:]).decode("latin1", errors="replace"))
        pos += 8 + length + 4
        if ctype == "IEND":
            break
    return found


def main() -> int:
    if len(sys.argv) < 2:
        print(__doc__)
        return 1
    png_path = sys.argv[1]
    out_dir = Path(sys.argv[2]) if len(sys.argv) > 2 else Path(png_path).parent
    out_dir.mkdir(parents=True, exist_ok=True)

    found = extract_text_chunks(png_path)
    print(f"PNG: {png_path} ({Path(png_path).stat().st_size} bytes)")
    print(f"text chunks: {list(found.keys()) or '无（未内嵌工作流元数据）'}")

    saved = []
    for key, value in found.items():
        safe = key.replace("/", "_")
        out_path = out_dir / f"_{safe}.json"
        try:
            parsed = json.loads(value)
            out_path.write_text(json.dumps(parsed, ensure_ascii=False, indent=2),
                                encoding="utf-8")
            saved.append((key, out_path, len(value)))
        except json.JSONDecodeError:
            # 不是 JSON（如参数表），也落盘备查
            out_path.write_text(value, encoding="utf-8")
            saved.append((key, out_path, len(value)))
    for key, out_path, size in saved:
        print(f"saved {key} ({size} chars) -> {out_path}")
    if not saved:
        print("该 PNG 未内嵌任何工作流元数据。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
