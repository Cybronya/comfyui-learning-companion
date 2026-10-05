# 归纳出的 Workflow 模式

本目录由 `engine/knowledge_consolidation/` **自动生成**，请勿手改 ——
下次运行 `consolidate()` 会被整体覆盖。

## 这里是什么

把「一堆学过的 workflow」提炼成「几条通用规律」。

```
workflows/learning/*.md（每个 workflow 一份学习记录）
    ↓ 按 workflow_type 分组 + Jaccard 相似度聚类
    ↓ 逐模式统计参数（不跨模式混算）
    ↓ 聚合各 workflow 的参数体检结论 → 常见问题
comfyui_library/knowledge/patterns/_consolidated/
```

与 `knowledge_evolution` 的分工（并存，不重复）：

| 模块 | 数据源 | 回答的问题 |
|---|---|---|
| `knowledge_evolution` | 参数**改动**记录 | 「改这个参数会怎样」 |
| `knowledge_consolidation`（本目录） | 完整 **workflow** | 「这类流程长什么样、常用什么参数、容易踩什么坑」 |

## 怎么用

```python
from engine.knowledge_consolidation import create_consolidation_engine

engine = create_consolidation_engine()
knowledge = engine.consolidate()          # 从 workflows/learning/ 读
print(engine.render_report(knowledge))
```

参数：`similarity`（默认 0.6，聚类阈值）、`min_frequency`（默认 2，模式最小成员数）。

## 文件结构

- `index.md` —— 汇总表，一行一个模式，带链接
- `<pattern>.md` —— 单个模式：
  - frontmatter：`frequency` / `level` / `common_nodes` / `problems` / `missing` / `members`
  - 正文：共有节点与可变部分、典型参数表、常见问题表、建议与风险

参数统计**不在** frontmatter 里（嵌套 dict 无法用行内列表表达），
只存在正文的表格中，需要时从正文解析回来。

## 可信度分级

| level | 含义 |
|---|---|
| `strong` | ≥3 个样本，且参数一致性 ≥85% |
| `moderate` | ≥3 个样本但取值分散，或无可统计参数 |
| `weak` | 样本 <3 —— 建议只是噪声，不要据此调参 |

样本不足时建议里会明写「仅 N 个样本，建议积累到 5 个以上再据此调参」。

## 检索

纯文本，可直接 grep：

```bash
grep -rl "ControlNet 权重" comfyui_library/knowledge/patterns/_consolidated/
# → 哪些模式用到 ControlNet 权重

grep -rl "风险" comfyui_library/knowledge/patterns/_consolidated/
# → 哪些模式有参数超阈值
```
