---
name: image_to_image_lora_sampler_clip_64
type: Image To Image
frequency: 4
level: strong
coverage: 0.8115
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, Flux2Scheduler, GrowMaskWithBlur, Image Comparer (rgthree), KSampler, KSamplerSelect, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, PreviewImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Flux2 Klein 最强四合一多功能_2014157990777069569.json, 图片生成/图生图/PS助手【扩图流】_2094046566104526849.json, 图片生成/图生图/QwenEdit2509-FP2换脸（相似度95%-图片会有轻微偏移-人脸与环境光影需二次编辑）林耀_2016711910770610178.json, 图片生成/图生图/flux-2-klein-9b【扩图流】_2104159780033089537.json]
source: knowledge_consolidation
---

# image_to_image_lora_sampler_clip_64

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Flux2 Klein 最强四合一多功能_2014157990777069569.json、图片生成/图生图/PS助手【扩图流】_2094046566104526849.json、图片生成/图生图/QwenEdit2509-FP2换脸（相似度95%-图片会有轻微偏移-人脸与环境光影需二次编辑）林耀_2016711910770610178.json、图片生成/图生图/flux-2-klein-9b【扩图流】_2104159780033089537.json）

- **类型**：Image To Image
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：81%

## 共有节点

全部 4 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `Flux2Scheduler`
- `GrowMaskWithBlur`
- `Image Comparer (rgthree)`
- `KSampler`
- `KSamplerSelect`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PreviewImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CFGNorm` —— 3/4 个有
- `EmptyFlux2LatentImage` —— 3/4 个有
- `GetImageSize` —— 3/4 个有
- `ImagePadForOutpaint` —— 3/4 个有
- `InpaintModelConditioning` —— 3/4 个有
- `TextEncodeQwenImageEditPlus_lrzjason` —— 3/4 个有
- `CR Text` —— 2/4 个有
- `DifferentialDiffusion` —— 2/4 个有
- `Get Image Size` —— 2/4 个有
- `GulfSeaImageMergeMask` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `图像缩放V2_孤海` —— 2/4 个有
- `图像缩放范围孤海` —— 2/4 个有
- `孤海外补画板按方向` —— 2/4 个有
- `ACE_ImageFaceCrop` —— 1/4 个有
- `Anything Everywhere3` —— 1/4 个有
- `CannyEdgePreprocessor` —— 1/4 个有
- `DepthAnythingPreprocessor` —— 1/4 个有
- `ImageAndMaskPreview` —— 1/4 个有
- `LayerUtility: PurgeVRAM` —— 1/4 个有
- `Mask Fill Holes` —— 1/4 个有
- `MaskPreview+` —— 1/4 个有
- `ModelSamplingAuraFlow` —— 1/4 个有
- `RBGImageStitchPlus` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 8 | 4 | 75% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 4 | 100% |
| 采样算法 | euler | - | 4 | 50% |
| 调度器 | simple | - | 4 | 75% |
| 重绘幅度 | 1 | 1 - 1 | 4 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/4 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 8，4 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，4 个样本，一致性 50%
- 调度器 最常用 simple，4 个样本，一致性 75%
- 重绘幅度 中位数 1，观测区间 1 - 1，4 个样本，取值集中（一致性 100%）
- 高发问题（5/4 个样本）：Steps较低可能导致细节不足
