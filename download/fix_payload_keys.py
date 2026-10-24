"""经验载荷内嵌 key 修复（2026-10-24）

根因：2026-10-16 裸 id 改名改了 workflows 表、experiences 列键、学习记录三处，
但 experiences 的 data_json 载荷里嵌的 "key" 字段是第五个存放点，漏改了
14,182 条（值为改名前的 目录/裸id.json）。knowledge_consolidation 的
ExperienceLoader 优先取载荷 key（experience_loader.py:176），旧键因此被
带进模式卡成员 → 图谱 matches 匹配率卡在 81%。

修复：列键 workflow_id 昨天已证明与 workflows 表严格一致（74,208=74,208，
死键 0），是正确值。逐条解码载荷，把 data["key"] 覆盖为列键后重压缩写回。
安全门槛：仅当列键以 `_<载荷key尾部id>.json` 结尾才改（防误伤）；
不满足的行跳过上报。

执行前 VACUUM INTO 留新备份 workflow_database.pre_payloadfix.sqlite。
单事务批量 UPDATE，直连 sqlite（不加载 WorkflowDatabase，避免全库物化）。
"""
import json
import os
import re
import sqlite3
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from comfyui_library.database.database import _decode_data
from comfyui_library.database.experience_repository import _zlib_compress_data

STOR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "comfyui_library", "database", "storage")
DB = os.path.join(STOR, "workflow_database.sqlite")
BAK = os.path.join(STOR, "workflow_database.pre_payloadfix.sqlite")

TAIL_ID = re.compile(r"(\d{12,})\.json$")

# 护栏：无外来管线
import subprocess
ps = subprocess.run(
    ["powershell", "-NoProfile", "-Command",
     "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | "
     "Where-Object { $_.CommandLine -match 'learn_pipeline|finalize_phase|build_graph' } | "
     "ForEach-Object { $_.ProcessId }"],
    capture_output=True, text=True, timeout=40)
others = [x for x in ps.stdout.split() if x.strip().isdigit() and int(x) != os.getpid()]
if others:
    print(f"[中止] 检测到外来管线进程 {others}，不执行修复", flush=True)
    sys.exit(9)

t0 = time.time()
con = sqlite3.connect(DB)
print("[备份] VACUUM INTO →", os.path.basename(BAK), flush=True)
con.execute("VACUUM INTO ?", (BAK,))
print(f"[备份] 完成 {os.path.getsize(BAK)/2**20:.0f}MB，{time.time()-t0:.0f}s", flush=True)

changed = skipped = 0
skip_samples = []
updates = []
for wid, dj in con.execute("SELECT workflow_id, data_json FROM experiences"):
    try:
        data = _decode_data(dj) or {}
    except Exception:
        skipped += 1
        continue
    k = data.get("key")
    if not k or k == wid:
        continue
    m = TAIL_ID.search(k)
    if not m or not wid.endswith("_" + m.group(1) + ".json"):
        skipped += 1
        if len(skip_samples) < 5:
            skip_samples.append((wid, k))
        continue
    data["key"] = wid
    updates.append((wid, _zlib_compress_data(data)))

print(f"待改 {len(updates)} 行，跳过 {skipped} 行", flush=True)
for w, k in skip_samples:
    print("   跳过样例:", w[:60], "| payload:", k[:60], flush=True)

t1 = time.time()
con.executemany(
    "UPDATE experiences SET data_json=? WHERE workflow_id=?",
    [(dj, wid) for wid, dj in updates],
)
con.commit()
print(f"[写入] {len(updates)} 行更新提交，耗时 {time.time()-t1:.0f}s", flush=True)

# 复扫验证
bad = 0
for wid, dj in con.execute("SELECT workflow_id, data_json FROM experiences"):
    try:
        data = _decode_data(dj) or {}
    except Exception:
        bad += 1
        continue
    if data.get("key") and data["key"] != wid:
        bad += 1
print(f"[验证] 载荷 key 仍不等于列键的行数: {bad}（应为 0）", flush=True)
con.close()
print(f"[完成] 总耗时 {time.time()-t0:.0f}s", flush=True)
sys.exit(0 if bad == 0 else 8)
