"""收尾阶段 2：知识图谱全量重建（消费阶段1落盘的新模式卡与三索引）

build_graph() 从三个数据源建图并原子落盘：
    LearningStore.completed_records()（74,208 条）
    KnowledgeStore.load_all()（阶段1 新归纳的模式）
    node_index.json（7,248 张卡）
独立进程：图谱（上次 1GB 级落盘 + 150 万边）内存峰值不与归纳叠加。
上次水位：61,832 顶点 / 1,433,196 边 / 696s（库 44k 时）；本次库 74k，预计 20-40 分钟。
"""
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

t0 = time.time()
print("[0] 开始重建知识图谱…", flush=True)

from engine.knowledge_graph import build_graph

qy = build_graph(verbose=True)
print(f"[完成] 阶段2 图谱重建 总耗时 {time.time()-t0:.0f}s", flush=True)
