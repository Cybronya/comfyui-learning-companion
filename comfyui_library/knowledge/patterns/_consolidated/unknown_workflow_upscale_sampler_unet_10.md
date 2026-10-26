---
name: unknown_workflow_upscale_sampler_unet_10
type: Unknown Workflow
frequency: 4
level: strong
coverage: 0.68
common_nodes: [BasicScheduler, CFGGuider, CLIPLoader, ComfyMathExpression, FaceAnalysisModels, FaceEmbedDistance, GetImageSizeAndCount, Image Comparer (rgthree), ImageResizeKJv2, ImageStitch, Images to RGB, KSamplerSelect, LoadImage, ModelAttentionBackend, PreviewImage, QwenImage21Cache, RandomNoise, ResizeImageMaskNode, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/图片编辑-最强换头-QwenImage2.1_2103523615542173698.json, 图片生成/图生图/图片编辑-角色四视图-QwenImage2.1_2103843745719472130.json, 图片生成/图生图/图片编辑-角色四视图-QwenImage2.1_2108737086558916609.json, 图片生成/图生图/图片编辑-角色四视图-QwenImage2.1_2110184896168812546.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_sampler_unet_10

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/图片编辑-最强换头-QwenImage2.1_2103523615542173698.json、图片生成/图生图/图片编辑-角色四视图-QwenImage2.1_2103843745719472130.json、图片生成/图生图/图片编辑-角色四视图-QwenImage2.1_2108737086558916609.json、图片生成/图生图/图片编辑-角色四视图-QwenImage2.1_2110184896168812546.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：强结论
- **平均知识覆盖**：68%

## 共有节点

全部 4 个 workflow 都包含：
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `ComfyMathExpression`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `GetImageSizeAndCount`
- `Image Comparer (rgthree)`
- `ImageResizeKJv2`
- `ImageStitch`
- `Images to RGB`
- `KSamplerSelect`
- `LoadImage`
- `ModelAttentionBackend`
- `PreviewImage`
- `QwenImage21Cache`
- `RandomNoise`
- `ResizeImageMaskNode`
- `SamplerCustomAdvanced`
- `SaveImage`
- `Seed (rgthree)`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `AILab_ImageCrop` —— 3/4 个有
- `AutoCropFaces` —— 3/4 个有
- `Bounded Image Crop with Mask` —— 3/4 个有
- `CLIPTextEncode` —— 3/4 个有
- `CheckpointLoaderSimple` —— 3/4 个有
- `EmptyLatentImage` —— 3/4 个有
- `INTConstant` —— 3/4 个有
- `ImageBatchMulti` —— 3/4 个有
- `ImageBlend` —— 3/4 个有
- `ImagePadForOutpaint` —— 3/4 个有
- `ImageToMask` —— 3/4 个有
- `MaskToImage` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `ResolutionSelector` —— 3/4 个有
- `SAM3_VideoTrack` —— 3/4 个有
- `SCAIL2ColoredMask` —— 3/4 个有
- `AIO_Preprocessor` —— 1/4 个有
- `ImageScaleToMaxDimension` —— 1/4 个有
- `easy float` —— 1/4 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1024 | 3 | 100% |
| 高度 | 1024 | 1024 - 1024 | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1024，3 个样本，取值集中（一致性 100%）
