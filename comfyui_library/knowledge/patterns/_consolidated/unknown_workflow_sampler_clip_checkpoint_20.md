---
name: unknown_workflow_sampler_clip_checkpoint_20
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.661
common_nodes: [CLIPTextEncodeSDXL, CLIPTextEncodeSDXLRefiner, CheckpointLoaderSimple, EmptyLatentImage, KSamplerAdvanced, PreviewImage, SaveImage, VAEDecode]
problems: []
missing: [MathExpression|pysssss, Label (rgthree)]
members: [图片生成/文生图/1925579019461283841.json, 图片生成/文生图/1964348804235411457.json, 图片生成/文生图/1964382898122014721.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_checkpoint_20

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1925579019461283841.json、图片生成/文生图/1964348804235411457.json、图片生成/文生图/1964382898122014721.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPTextEncodeSDXL`
- `CLIPTextEncodeSDXLRefiner`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `KSamplerAdvanced`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`

**可变部分**（部分 workflow 才有）：
- `Label (rgthree)` —— 2/3 个有
- `SDXLPromptStylerAdvanced` —— 2/3 个有
- `MathExpression|pysssss` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 100% |
| Prompt 约束强度(CFG) | 30 | 30 - 40 | 3 | 86% |
| 采样算法 | 8 | 8 - 8 | 3 | 100% |
| 调度器 | euler | - | 3 | 67% |
| 重绘幅度 | simple | - | 3 | 67% |
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 30，观测区间 30 - 40，3 个样本，取值集中（一致性 86%）
- 采样算法 中位数 8，观测区间 8 - 8，3 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，3 个样本，一致性 67%
- 重绘幅度 最常用 simple，3 个样本，一致性 67%
- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 风险：Prompt 约束强度(CFG) 观测到 40，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 这些节点还没有知识卡，系统对它们的理解有限：MathExpression|pysssss、Label (rgthree)
