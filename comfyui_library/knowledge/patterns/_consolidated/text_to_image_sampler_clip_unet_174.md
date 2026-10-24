---
name: text_to_image_sampler_clip_unet_174
type: Text To Image
frequency: 3
level: strong
coverage: 0.970333
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Prompt Text, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, EmptySD3LatentImage, Flux2Scheduler, KSampler, KSamplerSelect, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM, ModelSamplingAuraFlow, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/001.Z-image生图巅峰004.多模型文生图对比.json_2033721684305387521.json, 图片生成/文生图/Flux2-Klein出图对比_2013969753559277569.json, 图片生成/文生图/Flux2-Klein横向出图对比（四种模型）_2012011167622893570.json]
source: knowledge_consolidation
---

# text_to_image_sampler_clip_unet_174

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/001.Z-image生图巅峰004.多模型文生图对比.json_2033721684305387521.json、图片生成/文生图/Flux2-Klein出图对比_2013969753559277569.json、图片生成/文生图/Flux2-Klein横向出图对比（四种模型）_2012011167622893570.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：97%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `EmptySD3LatentImage`
- `Flux2Scheduler`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: PurgeVRAM`
- `ModelSamplingAuraFlow`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 2/3 个有
- `KOOK_ImageCompression` —— 2/3 个有
- `KOOK_SaveJPGImage` —— 2/3 个有
- `LoraLoaderModelOnly` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `RH_LLMAPI_NODE` —— 2/3 个有
- `easy showAnything` —— 2/3 个有
- `CheckpointLoaderSimple` —— 1/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `KSamplerAdvanced` —— 1/3 个有
- `LatentUpscaleBy` —— 1/3 个有
- `easy imageChooser` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 3 | 29% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 宽度 | 512 | 512 - 512 | 3 | 100% |
| 高度 | 512 | 512 - 512 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，3 个样本，取值分散，一致性仅 29%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高度 中位数 512，观测区间 512 - 512，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
