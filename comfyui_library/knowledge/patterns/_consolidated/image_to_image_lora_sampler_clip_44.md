---
name: image_to_image_lora_sampler_clip_44
type: Image To Image
frequency: 6
level: weak
coverage: 0.896667
common_nodes: [CFGGuider, CFGNorm, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, FluxKontextMultiReferenceLatentMethod, GetImageSize, Image Comparer (rgthree), ImageScaleToTotalPixels, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2511 风格迁移（线稿+参考图）_2032768346655039489.json, 图片生成/图生图/Qwen-Image-Edit 2511 高斯泼溅3D摄像机移动_2011085906899374081.json, 图片生成/图生图/Qwen-Image-Edit 2511 高斯泼溅3D摄像机移动_2066158379487293441.json, 图片生成/图生图/【CQ808】2511人物替换-_2037378323537469442.json, 图片生成/图生图/线稿上色 风格迁移 自动转线稿 （Qwen2511大熊版）_2032958830627266562.json, 图片生成/图生图/风格迁移 自动转线稿 大熊版_2032950491176509441.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_44

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2511 风格迁移（线稿+参考图）_2032768346655039489.json、图片生成/图生图/Qwen-Image-Edit 2511 高斯泼溅3D摄像机移动_2011085906899374081.json、图片生成/图生图/Qwen-Image-Edit 2511 高斯泼溅3D摄像机移动_2066158379487293441.json、图片生成/图生图/【CQ808】2511人物替换-_2037378323537469442.json、图片生成/图生图/线稿上色 风格迁移 自动转线稿 （Qwen2511大熊版）_2032958830627266562.json…）

- **类型**：Image To Image
- **样本数**：6
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CFGGuider`
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `FluxKontextMultiReferenceLatentMethod`
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 5/6 个有
- `CR Seed` —— 3/6 个有
- `PrimitiveBoolean` —— 3/6 个有
- `Switch image [Crystools]` —— 3/6 个有
- `Text` —— 3/6 个有
- `Fast Groups Bypasser (rgthree)` —— 2/6 个有
- `LayerUtility: ImageReel` —— 2/6 个有
- `LayerUtility: ImageReelComposit` —— 2/6 个有
- `QwenImageIntegratedKSampler` —— 2/6 个有
- `easy imageSize` —— 2/6 个有
- `AIO_Preprocessor` —— 1/6 个有
- `FluxKontextImageScale` —— 1/6 个有
- `RHHiddenNodes` —— 1/6 个有
- `easy seed` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 50% |
| 调度器 | simple | - | 6 | 50% |
| 重绘幅度 | 1 | 1 - 5.59066e+14 | 6 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 6/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 50%
- 调度器 最常用 simple，6 个样本，一致性 50%
- 重绘幅度 中位数 1，观测区间 1 - 5.59066e+14，6 个样本，取值分散，一致性仅 0%
- 风险：重绘幅度 观测到 5.59066e+14，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
- 高发问题（6/6 个样本）：Steps较低可能导致细节不足
