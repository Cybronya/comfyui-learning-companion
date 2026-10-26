---
name: unknown_workflow_lora_sampler_clip_29
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.858909
common_nodes: [AddLabel, CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, DF_Get_latent_size, EmptyFlux2LatentImage, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), Flux2Scheduler, ImageConcatMulti, KSampler, KSamplerSelect, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, PrimitiveStringMultiline, QwenImageLatentAspectRatio, RandomNoise, SamplerCustomAdvanced, SaveImage, ShowAnything|Mie, UNETLoader, VAEDecode, VAELoader, easy cleanGpuUsed]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2012141133685592065.json, 图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2084894059092598786.json, 图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2084901212222218242.json, 图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2084905221939089410.json, 图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2089609097233657858.json, 图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2108479912758833153.json, 图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2108762365310365697.json, 图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2109484821650169857.json, 图片生成/文生图/文生图Qwen+Flux2+Klein多版本+Zimage_2037762719994089474.json, 图片生成/文生图/文生图大全，Flux2多版本 VS Zimage_2012128533153320961.json, 图片生成/文生图/文生图（大漠孤烟直，长河落日圆）_2061330236628885505.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_29

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2012141133685592065.json、图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2084894059092598786.json、图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2084901212222218242.json、图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2084905221939089410.json、图片生成/文生图/文生图Qwen+Flux2 Klein多版本+Zimage_2089609097233657858.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：86%

## 共有节点

全部 11 个 workflow 都包含：
- `AddLabel`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `DF_Get_latent_size`
- `EmptyFlux2LatentImage`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `Flux2Scheduler`
- `ImageConcatMulti`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `QwenImageLatentAspectRatio`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `ShowAnything|Mie`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy cleanGpuUsed`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 11 | 100% |
| 采样算法 | res_multistep | - | 11 | 100% |
| 调度器 | simple | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 13/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 res_multistep，11 个样本，一致性 100%
- 调度器 最常用 simple，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 高发问题（13/11 个样本）：Steps较低可能导致细节不足
