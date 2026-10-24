---
name: image_to_image_lora_sampler_clip_42
type: Image To Image
frequency: 7
level: strong
coverage: 0.509286
common_nodes: [CLIPLoader, CLIPTextEncode, CR Text, CR Text Concatenate, ConditioningZeroOut, EmptySD3LatentImage, Fast Groups Bypasser (rgthree), GetImageSize, Image Comparer (rgthree), ImageConcatMulti, ImageScaleBy, ImageScaleToTotalPixels, Int, KSampler, KSamplerAdvanced, LayerColor: RGB, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingAuraFlow, MuyeTextEditOutput, PathchSageAttentionKJ, PreviewImage, RH_Captioner, SaveImage, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, Seed_, SetNode, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy imageConcat, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/洗图仿图-双种采样反推Z-Image bf16+turbo+klein_2016731833764941825.json, 图片生成/图生图/洗图仿图-双种采样反推Z-Image bf16+turbo+klein_2022159702238437378.json, 图片生成/图生图/洗图仿图-双种采样反推Z-Image bf16+turbo+klein_2065231993989849090.json, 图片生成/图生图/洗图仿图-双种采样反推Z-Image bf16+turbo+klein_2065350366732050434.json, 图片生成/图生图/洗图仿图-双种采样反推Z-Image bf16+turbo+klein_2066321899495444481.json, 图片生成/图生图/洗图仿图-双种采样反推Z-Image bf16+turbo+klein_2070432103707267073.json, 图片生成/图生图/洗图仿图-双种采样反推Z-Image+bf16+turbo+klein_2067491946037338114.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_42

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/洗图仿图-双种采样反推Z-Image bf16+turbo+klein_2016731833764941825.json、图片生成/图生图/洗图仿图-双种采样反推Z-Image bf16+turbo+klein_2022159702238437378.json、图片生成/图生图/洗图仿图-双种采样反推Z-Image bf16+turbo+klein_2065231993989849090.json、图片生成/图生图/洗图仿图-双种采样反推Z-Image bf16+turbo+klein_2065350366732050434.json、图片生成/图生图/洗图仿图-双种采样反推Z-Image bf16+turbo+klein_2066321899495444481.json…）

- **类型**：Image To Image
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：51%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Text`
- `CR Text Concatenate`
- `ConditioningZeroOut`
- `EmptySD3LatentImage`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageConcatMulti`
- `ImageScaleBy`
- `ImageScaleToTotalPixels`
- `Int`
- `KSampler`
- `KSamplerAdvanced`
- `LayerColor: RGB`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingAuraFlow`
- `MuyeTextEditOutput`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `RH_Captioner`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `Seed_`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy imageConcat`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 6 - 6 | 7 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 7 | 100% |
| 采样算法 | euler | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 0.6 | 0.6 - 0.6 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 7/7 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 6 - 6，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 0.6，观测区间 0.6 - 0.6，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：Steps较低可能导致细节不足
