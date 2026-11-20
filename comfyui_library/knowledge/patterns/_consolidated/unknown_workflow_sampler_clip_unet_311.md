---
name: unknown_workflow_sampler_clip_unet_311
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8918
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, KSampler, MOSSMergePreset, PrimitiveStringMultiline, ResolutionSelector, SaveImage, SkipLayerGuidanceDiTSimple, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Moss_image-文生图-洗图_2116427620094144513.json, 图片生成/文生图/Moss_image-文生图-洗图_2116677999922864130.json, 图片生成/文生图/Moss_image-文生图-洗图_2116688974679994370.json, 图片生成/文生图/Moss_动漫风格_8步文生图_2116046335290990594.json, 图片生成/文生图/moss 融合模型工作流_2115023859698192385.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_311

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Moss_image-文生图-洗图_2116427620094144513.json、图片生成/文生图/Moss_image-文生图-洗图_2116677999922864130.json、图片生成/文生图/Moss_image-文生图-洗图_2116688974679994370.json、图片生成/文生图/Moss_动漫风格_8步文生图_2116046335290990594.json、图片生成/文生图/moss 融合模型工作流_2115023859698192385.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `KSampler`
- `MOSSMergePreset`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `SaveImage`
- `SkipLayerGuidanceDiTSimple`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 4/5 个有
- `LoraLoaderModelOnly` —— 4/5 个有
- `GoohaiDisplayAny` —— 3/5 个有
- `RHLLMChatNode` —— 3/5 个有
- `忽略多组孤海` —— 3/5 个有
- `AddLabel` —— 1/5 个有
- `ModelSamplingAuraFlow` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 30 | 8 - 35 | 5 | 64% |
| Prompt 约束强度(CFG) | 3 | 1 - 3.5 | 5 | 68% |
| 采样算法 | er_sde | - | 5 | 80% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 30，观测区间 8 - 35，5 个样本
- Prompt 约束强度(CFG) 中位数 3，观测区间 1 - 3.5，5 个样本
- 采样算法 最常用 er_sde，5 个样本，一致性 80%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
