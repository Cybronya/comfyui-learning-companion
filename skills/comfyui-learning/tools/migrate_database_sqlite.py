#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""migrate_database_sqlite.py — 旧 JSON 主库 → sqlite（流式解析，内存恒定）。

背景（2026-10-14，AGENTS.md 待办 21）：主库 workflow_database.json 涨到
1310MB 后，json.load 全量读入在 24GB 内存机器上直接 MemoryError，
WorkflowDatabase() 的自动迁移（同样全量加载，守卫 200MB）也会拒绝 ——
本工具用流式解析逐条搬，内存恒定（约 50MB）。

用法（仓库根目录）：
    python -X utf8 skills/comfyui-learning/tools/migrate_database_sqlite.py
    python -X utf8 skills/comfyui-learning/tools/migrate_database_sqlite.py "路径/workflow_database.json"

行为：
    - 物理库落在同名 .sqlite（与 WorkflowDatabase._sqlite_path 一致，
      迁移后 WorkflowDatabase(path) 直接打开，无需再动）
    - 单事务 + synchronous=OFF + journal_mode=OFF（一次性迁移，速度优先）
    - experiences.data_json 走 zlib 压缩（与 database.py 同级 6，实测 3.06x）
    - 成功后旧 JSON 改名 .bak（留作恢复源；.bak 在则不会重复迁移）
    - 幂等：.sqlite 已存在时拒绝执行（防覆盖已有库）
    - 字段映射与 database._import_payload 完全一致（schema 直接复用）
"""

import argparse
import codecs
import json
import os
import sqlite3
import sys
import time
import zlib
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(line_buffering=True)

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))

from comfyui_library.database.database import _ensure_schema  # noqa: E402

DEFAULT_JSON = (
    ROOT / "comfyui_library" / "database" / "storage" / "workflow_database.json"
)

#: 单个 JSON 值的体积上限（本库单条记录最大约数百 KB；
#: 超限视为文件损坏，避免坏文件把缓冲吃爆）
MAX_VALUE_BYTES = 64 * 1024 * 1024

_WS = " \t\r\n\ufeff"  # \ufeff：兼容带 BOM 的旧文件


class JsonSectionStreamer:
    """单文件 JSON 顶层对象的流式读取器（只用标准库，内存恒定）

    针对本项目的库结构：

        {"version": N, "workflows": {...}, "nodes": {...},
         "patterns": {...}, "experiences": {...}}

    - 二进制分块读 + 增量 UTF-8 解码（不用 TextIOWrapper —— 实测
      tell() 病态慢约 22ms/次；二进制 read 无此问题）
    - 键名与值用 raw_decode 在缓冲上解析，缓冲不够长自动续读，
      块大小逐倍扩（1MB → 16MB 封顶）避免大值反复重扫
    - 每条值解析完立即交付，缓冲只保留未消费的尾巴；
      消费点过块界后砍掉头部，缓冲不再增长
    """

    MAX_CHUNK = 16 * 1024 * 1024

    def __init__(self, path, chunk_size=1024 * 1024):
        self._decoder = json.JSONDecoder()
        self._chunk = chunk_size
        self._buf = ""
        self._pos = 0
        self._inc = codecs.getincrementaldecoder("utf-8")()
        self._file = open(path, "rb")
        self._eof = False

    def close(self):
        if self._file is not None:
            self._file.close()
            self._file = None

    # ---------- 底层 ----------

    def _refill(self) -> bool:
        """再读一块；返回是否拿到新字符"""
        while not self._eof:
            chunk = self._file.read(self._chunk)
            if not chunk:
                self._eof = True
                tail = self._inc.decode(b"", final=True)
                if tail:
                    self._buf += tail
                    return True
                return False
            text = self._inc.decode(chunk)
            if text:
                self._buf += text
                return True
            # 整块都是被截断的多字节序列，继续读下一块
        return False

    def _compact(self):
        """消费点过块界后砍掉缓冲头部（防无限增长）"""
        if self._pos >= self._chunk:
            self._buf = self._buf[self._pos:]
            self._pos = 0

    def skip_ws(self) -> bool:
        """跳过空白；返回 False = 文件读完"""
        while True:
            while self._pos < len(self._buf) and self._buf[self._pos] in _WS:
                self._pos += 1
            if self._pos < len(self._buf):
                return True
            if not self._refill():
                return False
            self._compact()

    def expect(self, char: str):
        """断言当前位置是指定字符并消费它"""
        if not self.skip_ws() or self._buf[self._pos] != char:
            if self._pos < len(self._buf):
                found = self._buf[self._pos:self._pos + 20]
            else:
                found = "<EOF>"
            raise ValueError(
                f"JSON 结构与预期不符：期望 {char!r}，实际 {found!r}"
            )
        self._pos += 1

    def parse_value(self):
        """解析当前位置起的一个完整 JSON 值（自动续读，块大小逐倍扩）"""
        if not self.skip_ws():
            raise ValueError("JSON 提前结束：期待值")
        while True:
            try:
                value, end = self._decoder.raw_decode(self._buf, self._pos)
                if (
                    end >= len(self._buf)
                    and isinstance(value, (int, float))
                    and not isinstance(value, bool)
                    and not self._eof
                ):
                    # 数字可能被块边界截断（如 12345 只读到 1234），
                    # 续读一块后重解；字符串/对象有终止符无此问题
                    if self._refill():
                        continue
                self._pos = end
                self._compact()
                return value
            except json.JSONDecodeError:
                if len(self._buf) > MAX_VALUE_BYTES:
                    raise ValueError(
                        "单个 JSON 值超过 64MB，文件疑似损坏，终止迁移"
                    )
                if self._chunk < self.MAX_CHUNK:
                    self._chunk = min(self._chunk * 2, self.MAX_CHUNK)
                if not self._refill():
                    raise

    def parse_object_items(self):
        """当前位置起解析一个 JSON 对象，逐条产出 (key, value)

        假定调用方已消费掉开头的 '{'。值逐条 raw_decode，
        不整体物化 —— 这是内存恒定的关键。
        """
        if not self.skip_ws():
            raise ValueError("JSON 提前结束：对象未闭合")
        if self._buf[self._pos] == "}":
            self._pos += 1
            return
        while True:
            if not self.skip_ws():
                raise ValueError("JSON 提前结束：对象未闭合")
            key = self.parse_value()  # 键名（字符串）
            self.expect(":")
            yield key, self.parse_value()
            if not self.skip_ws():
                raise ValueError("JSON 提前结束：对象未闭合")
            ch = self._buf[self._pos]
            self._pos += 1
            if ch == "}":
                return
            if ch != ",":
                raise ValueError(f"对象成员分隔符异常：{ch!r}")


# ---------- 各 section 的逐条插入（与 database._import_payload 同映射） ----------


def _make_workflow_inserter(conn, counts):
    def insert(wid, rec):
        conn.execute(
            "INSERT OR REPLACE INTO workflows VALUES (?,?,?,?,?,?,?,?,?,?)",
            (
                wid,
                rec.get("name", ""),
                rec.get("file_path", ""),
                rec.get("status", "unlearned"),
                rec.get("type", rec.get("workflow_type", "")),
                json.dumps(rec.get("nodes", []), ensure_ascii=False),
                json.dumps(rec.get("patterns", []), ensure_ascii=False),
                rec.get("report", ""),
                rec.get("content_hash", ""),
                1 if rec.get("official") else 0,
            ),
        )
        counts["workflows"] += 1
    return insert


def _make_node_inserter(conn, counts):
    def insert(name, entry):
        conn.execute(
            "INSERT OR REPLACE INTO nodes(name, category) VALUES (?,?)",
            (name, entry.get("category", "")),
        )
        counts["nodes"] += 1
        for wid in entry.get("used_in", []):
            conn.execute(
                "INSERT OR IGNORE INTO node_used_in(node, workflow_id)"
                " VALUES (?,?)",
                (name, wid),
            )
            counts["node_used_in"] += 1
    return insert


def _make_pattern_inserter(conn, counts):
    def insert(name, pat):
        conn.execute(
            "INSERT OR REPLACE INTO patterns(name, workflows_json, description)"
            " VALUES (?,?,?)",
            (
                name,
                json.dumps(pat.get("workflows", []), ensure_ascii=False),
                pat.get("description", ""),
            ),
        )
        counts["patterns"] += 1
    return insert


def _make_experience_inserter(conn, counts):
    def insert(wid, exp):
        conn.execute(
            "INSERT OR REPLACE INTO experiences(workflow_id, content, tags_json,"
            " data_json) VALUES (?,?,?,?)",
            (
                wid,
                exp.get("content", ""),
                json.dumps(exp.get("tags", []), ensure_ascii=False),
                zlib.compress(
                    json.dumps(exp.get("data", {}), ensure_ascii=False).encode(
                        "utf-8"
                    ),
                    6,
                ),
            ),
        )
        counts["experiences"] += 1
    return insert


# ---------- 主流程 ----------


def migrate(json_path: Path, verbose: bool = True,
            chunk_size: int = 1024 * 1024) -> dict:
    """旧 JSON → sqlite（流式）；返回各类条数统计

    Args:
        chunk_size: 流式读取的初始块大小（测试用小值压边界；
                    解析大值时自动逐倍扩到 16MB 封顶）
    """
    json_path = Path(json_path)
    sqlite_path = json_path.with_suffix(".sqlite")
    if sqlite_path.exists():
        raise SystemExit(f"物理库已存在，拒绝覆盖: {sqlite_path}")
    if not json_path.exists():
        raise SystemExit(f"找不到旧 JSON: {json_path}")

    size_mb = json_path.stat().st_size / (1024 * 1024)
    if verbose:
        print(f"迁移开始: {json_path}（{size_mb:.0f}MB）→ {sqlite_path}")

    counts = dict.fromkeys(
        ("workflows", "nodes", "node_used_in", "patterns", "experiences"), 0
    )
    conn = sqlite3.connect(str(sqlite_path))
    try:
        # 单事务一次性迁移：同步与日志全关，速度优先
        conn.execute("PRAGMA synchronous=OFF")
        conn.execute("PRAGMA journal_mode=OFF")
        _ensure_schema(conn)

        inserters = {
            "workflows": _make_workflow_inserter(conn, counts),
            "nodes": _make_node_inserter(conn, counts),
            "patterns": _make_pattern_inserter(conn, counts),
            "experiences": _make_experience_inserter(conn, counts),
        }
        streamer = JsonSectionStreamer(json_path, chunk_size=chunk_size)
        t0 = time.time()
        try:
            streamer.expect("{")
            while True:
                if not streamer.skip_ws():
                    raise ValueError("JSON 提前结束：顶层对象未闭合")
                if streamer._buf[streamer._pos] == "}":
                    streamer._pos += 1
                    break
                key = streamer.parse_value()
                streamer.expect(":")
                if key == "version":
                    version = streamer.parse_value()
                    if version != 1:
                        raise SystemExit(
                            f"源库 version={version}（预期 1），结构可能不兼容，"
                            f"拒绝迁移（与自动迁移守卫同一口径）"
                        )
                elif key in inserters:
                    streamer.expect("{")
                    for item_key, value in streamer.parse_object_items():
                        inserters[key](item_key, value)
                        if verbose and counts[key] % 5000 == 0 and counts[key]:
                            print(
                                f"  [{key}] {counts[key]} 条"
                                f"（{time.time() - t0:.0f}s）"
                            )
                else:
                    value = streamer.parse_value()
                    print(
                        f"⚠ 未知顶层键 {key!r} 已跳过"
                        f"（值类型 {type(value).__name__}）"
                    )
                # 统一消费顶层成员分隔符（, 或 }）：三个分支都要 ——
                # section 的闭 } 由 parse_object_items 消费，
                # 但其后的顶层 , 或 }（含最后一个 section 后的 }）在这里处理
                if not streamer.skip_ws():
                    raise ValueError("JSON 提前结束：顶层对象未闭合")
                ch = streamer._buf[streamer._pos]
                streamer._pos += 1
                if ch == "}":
                    break
                if ch != ",":
                    raise ValueError(f"顶层成员分隔符异常：{ch!r}")
            conn.commit()
        finally:
            streamer.close()
    finally:
        conn.close()

    # 旧文件改名 .bak（sqlite 是新正身；.bak 留作恢复源，防重复迁移）
    bak = json_path.with_name(json_path.name + ".bak")
    os.replace(json_path, bak)

    if verbose:
        dt = time.time() - t0
        print(
            f"迁移完成: {counts['workflows']} workflow / "
            f"{counts['nodes']} node / {counts['node_used_in']} used_in / "
            f"{counts['patterns']} pattern / {counts['experiences']} experience"
            f"（{dt:.0f}s）"
        )
        print(f"旧 JSON 已改名: {bak.name}（确认无误后可删）")
    return counts


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="旧 JSON 主库 → sqlite 流式迁移（内存恒定）"
    )
    parser.add_argument(
        "json_path",
        nargs="?",
        default=str(DEFAULT_JSON),
        help="旧 JSON 路径（默认本仓库主库）",
    )
    args = parser.parse_args(argv)
    migrate(Path(args.json_path))


if __name__ == "__main__":
    main()
