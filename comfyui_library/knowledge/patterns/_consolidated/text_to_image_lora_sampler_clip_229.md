---
name: text_to_image_lora_sampler_clip_229
type: Text To Image
frequency: 3
level: weak
coverage: 0.902667
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, CR Text, ColorMatch, ConditioningKrea2Rebalance, ConditioningZeroOut, EmptyFlux2LatentImage, EmptyLatentImage, Flux2Scheduler, GetImageSize, GetNode, Image Comparer (rgthree), KSampler, KSamplerSelect, LCSColorAnchor, LCSLoadData, LCSSharpnessCalibrate, LCSSharpnessIntervene, LoraLoaderModelOnly, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, SetNode, TTResolutionSelector, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Krea2影视资产生成V1_2103524349650235394.json, 图片生成/文生图/Krea2影视资产生成工作流，文生图影视素材快速产出工具_2103978065222266882.json, 数字人/数字人/krea2影视资产生成四视图_2094753229727944705.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_229

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/Krea2影视资产生成V1_2103524349650235394.json、图片生成/文生图/Krea2影视资产生成工作流，文生图影视素材快速产出工具_2103978065222266882.json、数字人/数字人/krea2影视资产生成四视图_2094753229727944705.json）

- **类型**：Text To Image
- **样本数**：3
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `ColorMatch`
- `ConditioningKrea2Rebalance`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `EmptyLatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerSelect`
- `LCSColorAnchor`
- `LCSLoadData`
- `LCSSharpnessCalibrate`
- `LCSSharpnessIntervene`
- `LoraLoaderModelOnly`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `SetNode`
- `TTResolutionSelector`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `ImageScaleBy` —— 2/3 个有
- `ModelAttentionBackend` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 1/3 个有
- `JjkText` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LatentUpscaleBy` —— 1/3 个有
- `MultiTextConcatenate` —— 1/3 个有
- `solarL_SaveImagesToZip` —— 1/3 个有
- `孤海注释` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 3 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 4.5 | 3 | 24% |
| 采样算法 | euler | - | 3 | 67% |
| 调度器 | simple | - | 3 | 67% |
| 重绘幅度 | 1 | 0.43 - 1 | 3 | 67% |
| 宽度 | 1024 | 80 - 1024 | 3 | 37% |
| 高度 | 1024 | 80 - 1024 | 3 | 37% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，3 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4.5，3 个样本，取值分散，一致性仅 24%
- 采样算法 最常用 euler，3 个样本，一致性 67%
- 调度器 最常用 simple，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 0.43 - 1，3 个样本
- 宽度 中位数 1024，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 37%
- 高度 中位数 1024，观测区间 80 - 1024，3 个样本，取值分散，一致性仅 37%
- 高发问题（5/3 个样本）：Steps较低可能导致细节不足
