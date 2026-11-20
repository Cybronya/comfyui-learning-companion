---
name: image_to_image_lora_sampler_clip_81
type: Image To Image
frequency: 4
level: strong
coverage: 0.8895
common_nodes: [AddLabel, CLIPLoader, CLIPTextEncode, EmptyFlux2LatentImage, EmptySD3LatentImage, Flux2Scheduler, ImageConcanate, ImageScaleToTotalPixels, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, String Literal, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/2512 _ Flux 2 _ Z-Image _ Klein对比测试_2012077264858521602.json, 图片生成/文生图/2512 vs z-image vs flux2_2006771390493499393.json, 图片生成/文生图/4B_9B_Base vs Qwen 2511 多图对比_2013130226275983361.json, 图片生成/文生图/4B_9B_Base vs Qwen 2511单图对比_2013130253551542274.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_81

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/文生图/2512 _ Flux 2 _ Z-Image _ Klein对比测试_2012077264858521602.json、图片生成/文生图/2512 vs z-image vs flux2_2006771390493499393.json、图片生成/文生图/4B_9B_Base vs Qwen 2511 多图对比_2013130226275983361.json、图片生成/文生图/4B_9B_Base vs Qwen 2511单图对比_2013130253551542274.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
- `AddLabel`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyFlux2LatentImage`
- `EmptySD3LatentImage`
- `Flux2Scheduler`
- `ImageConcanate`
- `ImageScaleToTotalPixels`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `String Literal`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGGuider` —— 3/4 个有
- `ConditioningZeroOut` —— 3/4 个有
- `BasicGuider` —— 2/4 个有
- `CFGNorm` —— 2/4 个有
- `Float` —— 2/4 个有
- `FluxGuidance` —— 2/4 个有
- `FluxKontextMultiReferenceLatentMethod` —— 2/4 个有
- `GetImageSize` —— 2/4 个有
- `GetImageSize+` —— 2/4 个有
- `PrimitiveStringMultiline` —— 2/4 个有
- `TextEncodeQwenImageEditPlus` —— 2/4 个有
- `VAEDecodeTiled` —— 2/4 个有
- `easy seed` —— 2/4 个有
- `Image Comparer (rgthree)` —— 1/4 个有
- `PrimitiveInt` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 6 | 4 - 8 | 4 | 67% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 100% |
| 调度器 | simple | - | 4 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 10/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 6，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 100%
- 调度器 最常用 simple，4 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（10/4 个样本）：Steps较低可能导致细节不足
