---
name: text_to_image_inpaint_upscale_lora_2
type: Text To Image
frequency: 5
level: strong
coverage: 0.6988
common_nodes: [AILab_ImagePreview, AILab_Preview, AIO_Preprocessor, BasicScheduler, CFGGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, EmptyLatentImage, FaceAnalysisModels, FaceEmbedDistance, GetImageSizeAndCount, INTConstant, Image Comparer (rgthree), Image Paste Crop, ImageBlend, ImageCropByMask, ImagePadForOutpaint, ImageScaleToMaxDimension, ImageStitch, ImageToMask, Images to RGB, InpaintModelConditioning, InvertMask, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MaskToImage, ModelAttentionBackend, PreviewImage, QwenImage21Cache, RandomNoise, SAM3_Detect, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen Image2.1换脸局部重绘｜超高一致性脸部编辑_2108063537095593986.json, 图片生成/图生图/QwenImage2.1图片换头编辑｜局部重绘自然无痕迹_2107666085775503361.json, 图片生成/图生图/图片编辑换头局部重绘Qwen Image 2.1工作流，换脸图生图处理工具_2107925759909253121.json, 图片生成/图生图/图片编辑换头局部重绘QwenImage2.1 人物面部精准替换_2109359488070414338.json, 图片生成/图生图/图片编辑换脸局部重绘Qwen Image 2.1工作流，换脸图生图处理工具_2108315202566578178.json]
source: knowledge_consolidation
---

# text_to_image_inpaint_upscale_lora_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Qwen Image2.1换脸局部重绘｜超高一致性脸部编辑_2108063537095593986.json、图片生成/图生图/QwenImage2.1图片换头编辑｜局部重绘自然无痕迹_2107666085775503361.json、图片生成/图生图/图片编辑换头局部重绘Qwen Image 2.1工作流，换脸图生图处理工具_2107925759909253121.json、图片生成/图生图/图片编辑换头局部重绘QwenImage2.1 人物面部精准替换_2109359488070414338.json、图片生成/图生图/图片编辑换脸局部重绘Qwen Image 2.1工作流，换脸图生图处理工具_2108315202566578178.json）

- **类型**：Text To Image
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
- `AILab_ImagePreview`
- `AILab_Preview`
- `AIO_Preprocessor`
- `BasicScheduler`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `GetImageSizeAndCount`
- `INTConstant`
- `Image Comparer (rgthree)`
- `Image Paste Crop`
- `ImageBlend`
- `ImageCropByMask`
- `ImagePadForOutpaint`
- `ImageScaleToMaxDimension`
- `ImageStitch`
- `ImageToMask`
- `Images to RGB`
- `InpaintModelConditioning`
- `InvertMask`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MaskToImage`
- `ModelAttentionBackend`
- `PreviewImage`
- `QwenImage21Cache`
- `RandomNoise`
- `SAM3_Detect`
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
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 4/5 个有
- `GrowMaskWithBlur` —— 3/5 个有
- `ImageResizeKJv2` —— 3/5 个有
- `ImageScaleToTotalPixels` —— 3/5 个有
- `Mask Crop Region` —— 3/5 个有
- `Mask Paste Region` —— 3/5 个有
- `easy int` —— 3/5 个有
- `AutoCropFaces` —— 2/5 个有
- `ColorMatchV2` —— 2/5 个有
- `ComfyNumberConvert` —— 2/5 个有
- `FaceAlign` —— 2/5 个有
- `GetNode` —— 2/5 个有
- `OpenposePreprocessor` —— 2/5 个有
- `PreviewAny` —— 2/5 个有
- `PrimitiveFloat` —— 2/5 个有
- `SetNode` —— 2/5 个有
- `QwenImage21SpectrumT8` —— 1/5 个有
- `easy float` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 5 | 100% |
| 高度 | 80 | 80 - 80 | 5 | 100% |
| 采样步数 | 4 | 4 - 4 | 5 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 5 | 100% |
| 采样算法 | er_sde | - | 5 | 100% |
| 调度器 | beta | - | 5 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 5 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 5/5 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，5 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，5 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，5 个样本，一致性 100%
- 调度器 最常用 beta，5 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 高发问题（5/5 个样本）：Steps较低可能导致细节不足
