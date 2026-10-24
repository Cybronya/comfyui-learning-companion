"""经验表 + 节点反向索引表 死键清理（2026-10-23）

背景：2026-10-16 裸 id 改名 + 去重时，WorkflowRepository.rename 改了 workflows 行，
但 experiences 与 node_used_in 两张以 workflow_id 为键的表没全部跟着对账，
留下 4,466 条经验死键、3,805 个 junction 死 workflow_id（含 74,152 行）。
这些死键把「文件带 id 但无名字段」的旧键带进归纳，导致图谱 matches 只匹配 76%。

数据证明删除安全（见预检）：
- experiences 死键 4,466：映射到的新键经验行全部已存在（孤儿），需迁移 0；
- node_used_in 死键 3,805：3,792 改名孤儿（新键已有节点行）+ 13 工作流已删，需迁移 0。
即删除不丢任何真实工作流的经验或节点覆盖。

执行前已 VACUUM INTO 留完整备份：workflow_database.pre_expfix.sqlite。
独占访问（无其它管线在跑），单事务 DELETE + commit + VACUUM。
"""
import os
import re
import sqlite3
import sys
import time

STOR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                    "comfyui_library", "database", "storage")
DB = os.path.join(STOR, "workflow_database.sqlite")

# 先确认无外来管线（护栏：两条同写 sqlite 会互相覆盖）
import subprocess
ps = subprocess.run(
    ["powershell", "-NoProfile", "-Command",
     "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | "
     "Where-Object { $_.CommandLine -match 'learn_pipeline|finalize_phase|build_graph' } | "
     "ForEach-Object { $_.ProcessId }"],
    capture_output=True, text=True, timeout=40)
others = [int(x) for x in ps.stdout.split() if x.strip().isdigit() and int(x) != os.getpid()]
if others:
    print(f"[中止] 检测到外来管线进程 {others}，不执行清理", flush=True)
    sys.exit(9)

bak = os.path.join(STOR, "workflow_database.pre_expfix.sqlite")
if not os.path.exists(bak):
    print("[中止] 备份文件不存在，拒绝在无备份情况下清理", flush=True)
    sys.exit(9)

ID_RE = re.compile(r"(\d{12,})\.json$")
con = sqlite3.connect(DB)
wf = {r[0] for r in con.execute("SELECT id FROM workflows")}
t0 = time.time()

exp_dead = [r[0] for r in con.execute("SELECT workflow_id FROM experiences") if r[0] not in wf]
nu_all = {r[0] for r in con.execute("SELECT DISTINCT workflow_id FROM node_used_in")}
nu_dead = sorted(nu_all - wf)
print(f"待清：experiences {len(exp_dead)} 条 / node_used_in {len(nu_dead)} 个 workflow_id", flush=True)


def chunks(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


con.execute("PRAGMA journal_mode=WAL")
cur = con.cursor()
n_exp = n_nu = 0
for c in chunks(exp_dead, 900):
    ph = ",".join("?" * len(c))
    cur.execute(f"DELETE FROM experiences WHERE workflow_id IN ({ph})", c)
    n_exp += cur.rowcount
for c in chunks(nu_dead, 500):
    ph = ",".join("?" * len(c))
    cur.execute(f"DELETE FROM node_used_in WHERE workflow_id IN ({ph})", c)
    n_nu += cur.rowcount
con.commit()
print(f"[删除] experiences 行 {n_exp} / node_used_in 行 {n_nu}，提交耗时 {time.time()-t0:.0f}s", flush=True)

# 一致性核查
wf2 = {r[0] for r in con.execute("SELECT id FROM workflows")}
exp2 = {r[0] for r in con.execute("SELECT workflow_id FROM experiences")}
nu2 = {r[0] for r in con.execute("SELECT DISTINCT workflow_id FROM node_used_in")}
print(f"核查 workflows={len(wf2)}  experiences={len(exp2)}  "
      f"junction引用={len(nu2)}", flush=True)
print(f"  经验死键残留 {len(exp2 - wf2)}  节点死键残留 {len(nu2 - wf2)}", flush=True)

# VACUUM 回收空洞（删了 7.4 万+行）
size_before = os.path.getsize(DB) / 2**20
t1 = time.time()
con.execute("VACUUM")
con.commit()
size_after = os.path.getsize(DB) / 2**20
print(f"[VACUUM] {size_before:.0f}MB → {size_after:.0f}MB，耗时 {time.time()-t1:.0f}s", flush=True)
con.close()

print(f"[完成] 死键清理 总耗时 {time.time()-t0:.0f}s", flush=True)
