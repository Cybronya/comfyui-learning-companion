---
name: unknown_workflow_sampler_clip_unet_292
type: Unknown Workflow
frequency: 5
level: weak
coverage: 0.949
common_nodes: [CLIPTextEncode, ConditioningZeroOut, DualCLIPLoader, EmptySD3LatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux.1 IPAdapter 风格迁移_1994257493721284609.json, 图片生成/文生图/F.1 Krea [dev] 文生图lora_简单工作流-可在线本地使用_1910297443941187586.json, 图片生成/文生图/F.1玄金金箔美学_2008505998876614657.json, 图片生成/文生图/Flux-Krea文生图（降低AI感的新模型）_1950928691515817986.json, 图片生成/文生图/极速4步采样生图——SoilsihgStudio_1895380500704002050.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_292

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Flux.1 IPAdapter 风格迁移_1994257493721284609.json、图片生成/文生图/F.1 Krea [dev] 文生图lora_简单工作流-可在线本地使用_1910297443941187586.json、图片生成/文生图/F.1玄金金箔美学_2008505998876614657.json、图片生成/文生图/Flux-Krea文生图（降低AI感的新模型）_1950928691515817986.json、图片生成/文生图/极速4步采样生图——SoilsihgStudio_1895380500704002050.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DualCLIPLoader`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `LoadImage` —— 2/5 个有
- `ModelSamplingFlux` —— 2/5 个有
- `PreviewImage` —— 2/5 个有
- `RH_Translator` —— 2/5 个有
- `ApplyIPAdapterFlux` —— 1/5 个有
- `FluxGuidance` —— 1/5 个有
- `IPAdapterFluxLoader` —— 1/5 个有
- `easy cleanGpuUsed` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 4 - 30 | 5 | 47% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 5 | 0% |
| 采样算法 | euler | - | 5 | 100% |
| 调度器 | simple | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 4 - 30，5 个样本，取值分散，一致性仅 47%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 100%
- 调度器 最常用 simple，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
