---
name: unknown_workflow_sampler_57
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.705667
common_nodes: [Anything Everywhere3, Efficient Loader, KSampler (Efficient), LoadImage, Prompts Everywhere, SaveImage]
problems: []
missing: []
members: [图片生成/文生图/一键运行：最简扩图 修复 局部重绘 新人必备_1951491900136173570.json, 图片生成/文生图/效率节点极简图生图新人必备_1950463623363792897.json, 图片生成/文生图/最简效率节点局部重绘工作流新人必备_1950483114151825409.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_57

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/一键运行：最简扩图 修复 局部重绘 新人必备_1951491900136173570.json、图片生成/文生图/效率节点极简图生图新人必备_1950463623363792897.json、图片生成/文生图/最简效率节点局部重绘工作流新人必备_1950483114151825409.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：71%

## 共有节点

全部 3 个 workflow 都包含：
- `Anything Everywhere3`
- `Efficient Loader`
- `KSampler (Efficient)`
- `LoadImage`
- `Prompts Everywhere`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `InpaintModelConditioning` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `ImagePadForOutpaint` —— 1/3 个有
- `VAEEncode` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 3 | 100% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 3 | 100% |
| 采样算法 | euler | - | 3 | 100% |
| 调度器 | simple | - | 3 | 100% |
| 重绘幅度 | 1 | 0.5 - 1 | 3 | 72% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，3 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，3 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，3 个样本，一致性 100%
- 调度器 最常用 simple，3 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.5 - 1，3 个样本
