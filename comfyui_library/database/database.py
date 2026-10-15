r"""
WorkflowDatabase —— 统一持久化核心（sqlite 后端）

背景（2026-10-14）：旧后端是单文件 JSON，主库涨到 1.25GB 后
json.load 全量读入在 24GB 内存机器上直接 MemoryError，批量学习
逐条全量写盘也慢到不可用。改用标准库 sqlite3：

- 按行存取：按 id 查一条约 0.1-2ms，内存不再随库大小增长
- experiences.data_json 走 zlib 压缩（实测 3.06x：压后 3.0KB/条、
  压前 9.2KB/条，30616 条合计 39MB）
- 写入走增量事务，不再有「每加一条全量重写整库」的问题

实测体积构成（2026-10-15 VACUUM 后 235MB，29554 workflow / 773075 条 junction 行）：
    node_used_in（junction 表 + 主键索引）  138.7MB (59%)  ← 最大头
      原因：workflow_id 是长路径文本（均值 67 字节，中文路径 UTF-8 更长），
      表与主键索引各存一份
    experiences（data_json 39MB + content 7MB + 索引）  68.4MB (29%)
    workflows + nodes + patterns                      约 27MB (12%)
  即：1.25GB JSON → 419MB sqlite → VACUUM 后 235MB，其中 165MB 是
  INSERT OR REPLACE 留下的空洞（已回收）。剩下唯一的大头是 junction 表，
  要再砍得把 workflow_id 换成整数外键（SCHEMA_VERSION 升 2，
  见 AGENTS.md 9.3 待办 22）。

兼容性（老调用方无感）：

- path 参数与默认值不变（storage/workflow_database.json）；
  物理库落在同名 .sqlite 文件，db.path 仍是逻辑 .json 路径
- 打开时若只有旧 JSON（无 .sqlite）自动迁入并把旧文件改名 .bak；
  超过体积守卫的旧 JSON 拒绝自动迁移（json.load 需要 3-5 倍内存，
  1310MB 的主库会 MemoryError），提示先跑迁移工具（流式解析，内存恒定）
- .data 保留为只读兼容视图（每次访问重新物化；仅旧测试在用，
  生产代码请走四个仓库）
- summary() 改走 SQL COUNT，不再物化全库

连接生命周期（Windows 实测）：

- 打开的连接不关，TemporaryDirectory 清理会 PermissionError
  （WinError 32）—— 测试在 with TemporaryDirectory 里建库不 close
- auto_save=True（默认）：每个写操作短连接，用完即关（约 2ms/次，
  与持久连接只差 0.5ms，可忽略）
- auto_save=False（批量）：持有连接累积事务，save() 一次提交并关闭；
  close()/__del__ 兜底
"""

import json
import os
import sqlite3
import zlib
from pathlib import Path

from .workflow_repository import WorkflowRepository
from .node_repository import NodeRepository
from .pattern_repository import PatternRepository
from .experience_repository import ExperienceRepository
from .index_manager import IndexManager

#: 存储格式版本。结构不兼容变更时 +1，
#: 打开时会拒绝读旧版本而不是给出莫名其妙的错。
SCHEMA_VERSION = 1

#: 数据库的四个 section（.data 兼容视图与旧 JSON 迁移用）
SECTIONS = ("workflows", "nodes", "patterns", "experiences")

#: 默认逻辑路径（本包 storage/ 下，与调用方 cwd 无关）。
#: 物理库是同名 .sqlite；保留 .json 逻辑路径，老调用方显式传路径也无感。
DEFAULT_PATH = (
    Path(__file__).resolve().parent / "storage" / "workflow_database.json"
)

#: 旧 JSON 超过这个体积就拒绝自动迁移（json.load 需要约 3-5 倍内存，
#: 1310MB 的主库会 MemoryError），提示先跑迁移工具
MAX_AUTO_MIGRATE_BYTES = 200 * 1024 * 1024

#: 建表语句（逐条 execute，不用 executescript —— 它会隐式 COMMIT，
#: 打断批量模式的事务累积）
_SCHEMA_STATEMENTS = (
    """
    CREATE TABLE IF NOT EXISTS meta (
        key TEXT PRIMARY KEY,
        value TEXT
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS workflows (
        id TEXT PRIMARY KEY,
        name TEXT NOT NULL DEFAULT '',
        file_path TEXT NOT NULL DEFAULT '',
        status TEXT NOT NULL DEFAULT 'unlearned',
        type TEXT NOT NULL DEFAULT '',
        nodes_json TEXT NOT NULL DEFAULT '[]',
        patterns_json TEXT NOT NULL DEFAULT '[]',
        report TEXT NOT NULL DEFAULT '',
        content_hash TEXT NOT NULL DEFAULT '',
        official INTEGER NOT NULL DEFAULT 0
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS nodes (
        name TEXT PRIMARY KEY,
        category TEXT NOT NULL DEFAULT ''
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS node_used_in (
        node TEXT NOT NULL,
        workflow_id TEXT NOT NULL,
        PRIMARY KEY (node, workflow_id)
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS patterns (
        name TEXT PRIMARY KEY,
        workflows_json TEXT NOT NULL DEFAULT '[]',
        description TEXT NOT NULL DEFAULT ''
    )
    """,
    """
    CREATE TABLE IF NOT EXISTS experiences (
        workflow_id TEXT PRIMARY KEY,
        content TEXT NOT NULL DEFAULT '',
        tags_json TEXT NOT NULL DEFAULT '[]',
        data_json BLOB
    )
    """,
)


def _ensure_schema(conn):
    """建表（幂等）+ 版本号入库"""
    for stmt in _SCHEMA_STATEMENTS:
        conn.execute(stmt)
    conn.execute(
        "INSERT OR IGNORE INTO meta(key, value) VALUES('version', ?)",
        (str(SCHEMA_VERSION),),
    )


def _decode_data(raw):
    """data_json BLOB → dict；zlib 解压失败按裸 JSON 兼容（原型期未压缩）"""
    if raw is None:
        return {}
    if isinstance(raw, str):
        return json.loads(raw)
    try:
        raw = zlib.decompress(raw)
    except zlib.error:
        pass
    return json.loads(raw.decode("utf-8"))


def _record_dict(row):
    """workflows 行 → 外部 dict 契约（workflow_type 落库为 type 列）"""
    return {
        "id": row["id"],
        "name": row["name"],
        "file_path": row["file_path"],
        "status": row["status"],
        "type": row["type"],
        "nodes": json.loads(row["nodes_json"]),
        "patterns": json.loads(row["patterns_json"]),
        "report": row["report"],
        "content_hash": row["content_hash"],
        "official": bool(row["official"]),
    }


def _import_payload(conn, data):
    """把旧 JSON payload 的四个 section 批量导入 sqlite（单事务内调用）"""
    for wid, rec in data["workflows"].items():
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
    for name, entry in data["nodes"].items():
        conn.execute(
            "INSERT OR REPLACE INTO nodes(name, category) VALUES (?,?)",
            (name, entry.get("category", "")),
        )
        for wid in entry.get("used_in", []):
            conn.execute(
                "INSERT OR IGNORE INTO node_used_in(node, workflow_id) VALUES (?,?)",
                (name, wid),
            )
    for name, pat in data["patterns"].items():
        conn.execute(
            "INSERT OR REPLACE INTO patterns(name, workflows_json, description)"
            " VALUES (?,?,?)",
            (
                name,
                json.dumps(pat.get("workflows", []), ensure_ascii=False),
                pat.get("description", ""),
            ),
        )
    for wid, exp in data["experiences"].items():
        conn.execute(
            "INSERT OR REPLACE INTO experiences(workflow_id, content, tags_json,"
            " data_json) VALUES (?,?,?,?)",
            (
                wid,
                exp.get("content", ""),
                json.dumps(exp.get("tags", []), ensure_ascii=False),
                zlib.compress(
                    json.dumps(exp.get("data", {}), ensure_ascii=False).encode("utf-8"),
                    6,
                ),
            ),
        )


class WorkflowDatabase:
    """workflow / node / pattern / experience 四类数据的统一存储"""

    def __init__(self, path=None):
        """
        Args:
            path: 逻辑数据库路径；None 时用本包 storage/workflow_database.json。
                  物理库是同名 .sqlite 文件；发现旧 JSON 时自动迁移。
        """
        self.path = Path(path) if path is not None else DEFAULT_PATH
        # 每次写操作后是否立即提交。True（默认）= 短连接即时提交；
        # False = 批量模式，持有连接累积事务，save() 一次提交并关闭。
        self.auto_save = True
        self._conn = None  # 批量模式持有的连接
        self._schema_ready = False

        # 便捷入口：db.workflows.add(...) 即可，不必再手工 new 仓库
        self.workflows = WorkflowRepository(self)
        self.nodes = NodeRepository(self)
        self.patterns = PatternRepository(self)
        self.experiences = ExperienceRepository(self)
        self.indexes = IndexManager(self)

        self._open_backend()

    # ---------- 后端打开与迁移 ----------

    @property
    def _sqlite_path(self) -> Path:
        """物理库路径（与逻辑路径同目录同名，扩展名 .sqlite）"""
        return self.path.with_suffix(".sqlite")

    def _open_backend(self):
        """打开后端：物理库在则查版本；只有旧 JSON 则先迁移"""
        if self._sqlite_path.exists():
            self._check_version()
            return
        if self.path.exists() and self.path.resolve() != self._sqlite_path.resolve():
            self._migrate_legacy_json()

    def _check_version(self):
        """物理库版本守卫（GraphStore 踩过的坑：无版本号旧结构会被误读）"""
        conn = self._connect()
        try:
            self._ensure_schema_once(conn)
            conn.commit()
            row = conn.execute(
                "SELECT value FROM meta WHERE key='version'"
            ).fetchone()
        finally:
            conn.close()
        if row is not None and row["value"] != str(SCHEMA_VERSION):
            raise ValueError(
                f"数据库版本不支持：文件 version={row['value']}，"
                f"当前支持 {SCHEMA_VERSION}，请重建或迁移: {self._sqlite_path}"
            )

    def _migrate_legacy_json(self):
        """旧单文件 JSON → sqlite（一次性；成功后旧文件改名 .bak）"""
        size = self.path.stat().st_size
        if size > MAX_AUTO_MIGRATE_BYTES:
            raise ValueError(
                f"数据库 JSON 过大（{size / (1024 * 1024):.0f}MB），"
                f"自动迁移需要全量加载，可能内存不足。请先运行迁移工具：\n"
                f"    python -X utf8 skills/comfyui-learning/tools/"
                f'migrate_database_sqlite.py "{self.path}"\n'
                f"（流式解析，内存恒定）"
            )
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

        conn = self._connect()
        try:
            conn.execute("PRAGMA synchronous=OFF")  # 一次性迁移，速度优先
            self._ensure_schema_once(conn)
            _import_payload(conn, data)
            conn.commit()
        finally:
            conn.close()

        # 旧文件改名 .bak（sqlite 是新正身；.bak 留作恢复源，防重复迁移）
        os.replace(self.path, self.path.with_name(self.path.name + ".bak"))

    # ---------- 连接管理 ----------

    def _connect(self):
        """新短连接（读或写皆可）；调用方负责 close"""
        self._sqlite_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(str(self._sqlite_path))
        conn.row_factory = sqlite3.Row
        conn.execute("PRAGMA synchronous=NORMAL")
        return conn

    def _ensure_schema_once(self, conn):
        """建表每实例只跑一次（CREATE IF NOT EXISTS 幂等，省每连接开销）"""
        if self._schema_ready:
            return
        _ensure_schema(conn)
        self._schema_ready = True

    def _begin_write(self):
        """写操作入口：返回连接（短连接或批量持有连接）"""
        if self._conn is not None:
            return self._conn
        conn = self._connect()
        self._ensure_schema_once(conn)
        if self.auto_save:
            return conn  # 短连接：调用方 _end_write 提交并关闭
        self._conn = conn  # 批量：持有，save() 提交并关闭
        return self._conn

    def _end_write(self, conn):
        """写操作收尾：短连接提交并关闭；批量持有连接只累积"""
        if conn is not self._conn:
            conn.commit()
            conn.close()

    def _read(self):
        """读连接：库不存在返回 None（调用方按空处理）"""
        if self._conn is not None:
            return self._conn
        if not self._sqlite_path.exists():
            return None
        conn = self._connect()
        self._ensure_schema_once(conn)
        return conn

    def _end_read(self, conn):
        if conn is not None and conn is not self._conn:
            conn.close()

    # ---------- 兼容视图 ----------

    @property
    def data(self):
        """只读兼容视图：物化快照（每次访问重新物化）

        仅旧测试在用（生产代码请走四个仓库）。保留它是为了旧断言
        语义不变：db.data["nodes"]["KSampler"]["used_in"] 等。
        """
        snapshot = {"version": SCHEMA_VERSION}
        conn = self._read()
        if conn is None:
            for section in SECTIONS:
                snapshot[section] = {}
            return snapshot
        try:
            snapshot["workflows"] = {
                row["id"]: _record_dict(row)
                for row in conn.execute("SELECT * FROM workflows ORDER BY rowid")
            }
            nodes = {}
            for row in conn.execute(
                "SELECT name, category FROM nodes ORDER BY rowid"
            ):
                nodes[row["name"]] = {"category": row["category"], "used_in": []}
            for node, wid in conn.execute(
                "SELECT node, workflow_id FROM node_used_in ORDER BY rowid"
            ):
                if node in nodes:
                    nodes[node]["used_in"].append(wid)
            snapshot["nodes"] = nodes
            snapshot["patterns"] = {
                row["name"]: {
                    "workflows": json.loads(row["workflows_json"]),
                    "description": row["description"],
                }
                for row in conn.execute("SELECT * FROM patterns ORDER BY rowid")
            }
            snapshot["experiences"] = {
                row["workflow_id"]: {
                    "content": row["content"],
                    "tags": json.loads(row["tags_json"]),
                    "data": _decode_data(row["data_json"]),
                }
                for row in conn.execute(
                    "SELECT * FROM experiences ORDER BY rowid"
                )
            }
        finally:
            self._end_read(conn)
        return snapshot

    # ---------- 读 / 写 / 汇总 ----------

    def load(self):
        """兼容方法：重新打开后端（旧版从磁盘全量读入）"""
        self._open_backend()

    def save(self):
        """提交并落盘：批量模式在这里一次性提交并关闭持有连接"""
        if self._conn is not None:
            try:
                self._conn.commit()
            finally:
                self._conn.close()
                self._conn = None
            return
        # 即时模式：写操作已逐条提交；确保库文件存在（与旧版 save 后落盘一致）
        conn = self._connect()
        try:
            self._ensure_schema_once(conn)
            conn.commit()
        finally:
            conn.close()

    def close(self):
        """关闭批量持有连接（未提交的回滚）"""
        if self._conn is not None:
            try:
                self._conn.rollback()
            finally:
                self._conn.close()
                self._conn = None

    def vacuum(self, force: bool = False) -> dict:
        """
        压缩库文件、回收空洞，返回 {"before_mb", "after_mb", "freed_mb"}

        `INSERT OR REPLACE` 是「删旧插新」，每次重学都在文件里留空洞；
        批量学习几千条后空洞能占三成以上（实测 419MB 里 38% 是空洞）。
        VACUUM 一次性归还磁盘，代价是重写整个库（几十秒）。

        Args:
            force: False 时只在空洞超过 10% 才真跑（省一次重写）
        """
        conn = self._read()
        if conn is None:
            return {"before_mb": 0.0, "after_mb": 0.0, "freed_mb": 0.0}
        try:
            page_count = conn.execute("PRAGMA page_count").fetchone()[0]
            freelist = conn.execute("PRAGMA freelist_count").fetchone()[0]
            page_size = conn.execute("PRAGMA page_size").fetchone()[0]
        finally:
            self._end_read(conn)
        before = page_count * page_size
        if not force and freelist < page_count * 0.1:
            return {
                "before_mb": round(before / 1048576, 1),
                "after_mb": round(before / 1048576, 1),
                "freed_mb": 0.0,
            }
        # VACUUM 不能在事务里跑：批量模式先提交释放连接
        if self._conn is not None:
            self.save()
        conn = self._connect()
        try:
            conn.execute("VACUUM")
            after = conn.execute("PRAGMA page_count").fetchone()[0] * page_size
        finally:
            conn.close()
        return {
            "before_mb": round(before / 1048576, 1),
            "after_mb": round(after / 1048576, 1),
            "freed_mb": round((before - after) / 1048576, 1),
        }

    def __del__(self):
        try:
            self.close()
        except Exception:
            pass

    def summary(self) -> str:
        """一行摘要（SQL COUNT，不再物化全库）"""
        conn = self._read()
        if conn is None:
            counts = {s: 0 for s in SECTIONS}
        else:
            try:
                counts = {
                    section: conn.execute(
                        f"SELECT COUNT(*) FROM {table}"
                    ).fetchone()[0]
                    for table, section in (
                        ("workflows", "workflows"),
                        ("nodes", "nodes"),
                        ("patterns", "patterns"),
                        ("experiences", "experiences"),
                    )
                }
            finally:
                self._end_read(conn)
        return (
            f"{self.path}：{counts['workflows']} workflow / "
            f"{counts['nodes']} node / {counts['patterns']} pattern / "
            f"{counts['experiences']} experience"
        )
