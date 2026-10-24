---
name: image_to_image_lora_sampler_unet_219
type: Image To Image
frequency: 2
level: weak
coverage: 0.9605
common_nodes: [CFGNorm, CLIPLoader, CR Text, FluxKontextImageScale, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, SaveImage, SeedVR2, SeedVR2BlockSwap, TextEncodeQwenImageEditPlus, UNETLoader, VAEDecode, VAEEncode, VAELoader, easy int]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图像编辑-FireRed-image-edit1.1_2032731253379702785.json, 图片生成/图生图/角色换头-单人版-图生图-FireRed-image-edit1.1-换脸_2035907829818724353.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_unet_219

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图像编辑-FireRed-image-edit1.1_2032731253379702785.json、图片生成/图生图/角色换头-单人版-图生图-FireRed-image-edit1.1-换脸_2035907829818724353.json）

- **类型**：Image To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CR Text`
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `KSampler`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Bjornulf_IfElse` —— 1/2 个有
- `ClothesSegment` —— 1/2 个有
- `ConstrainImage|pysssss` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `LayerUtility: CropByMask V2` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `LazySwitch1way` —— 1/2 个有
- `PreviewAny` —— 1/2 个有
- `RH_LLMAPI_NODE` —— 1/2 个有
- `UnetLoaderGGUF` —— 1/2 个有
- `easy boolean` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 9 | - | 2 | 89% |
| Prompt 约束强度(CFG) | 1 | - | 2 | 100% |
| 采样算法 | euler | - | 2 | 100% |
| 调度器 | simple | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 9，样本不足，未给区间，2 个样本，取值集中（一致性 89%）
- Prompt 约束强度(CFG) 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，2 个样本，一致性 100%
- 调度器 最常用 simple，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（1/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
