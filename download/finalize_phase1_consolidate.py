"""收尾阶段 1：全量重归纳（74k 条经验 → 模式卡覆盖 _consolidated/ 并写回库）

装配方式复用 learn_pipeline 已验证口径：
    WorkflowDatabase(auto_save=False) → create_consolidation_engine(database=db)
    → consolidate() → db.save() + indexes.save_all() + vacuum()
独立进程运行：归纳的内存峰值不与图谱阶段叠加。
上次水位：44,368 条 550.8s → 5,777 模式；本次 74,208 条，预计 15 分钟内。
"""
import os
import sys
import time

# 脚本方式运行时 sys.path[0] 是 download/，需把仓库根加进来
# （同 2026-10-16 rename_library_workflows 踩过的坑）
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

t0 = time.time()
print("[0] 打开数据库…", flush=True)

from comfyui_library.database.database import WorkflowDatabase
from engine.knowledge_consolidation import create_consolidation_engine

db = WorkflowDatabase()
db.auto_save = False
print(f"[0] 数据库就绪 {time.time()-t0:.1f}s", flush=True)

try:
    engine = create_consolidation_engine(database=db)
    t1 = time.time()
    result = engine.consolidate()
    print(f"[1] 归纳完成 {time.time()-t1:.1f}s："
          f"{len(result.patterns)} 个模式 / 未归类 {result.ungrouped} / "
          f"来源 {result.source_count} 条", flush=True)
finally:
    t2 = time.time()
    db.save()
    db.indexes.save_all()
    print(f"[2] 主库与三索引落盘 {time.time()-t2:.1f}s", flush=True)
    db.auto_save = True
    vac = db.vacuum()
    if vac["freed_mb"]:
        print(f"[3] 库整理 {vac['before_mb']}MB → {vac['after_mb']}MB"
              f"（回收 {vac['freed_mb']}MB 空洞）", flush=True)

print(f"[完成] 阶段1 全量重归纳 总耗时 {time.time()-t0:.0f}s", flush=True)
