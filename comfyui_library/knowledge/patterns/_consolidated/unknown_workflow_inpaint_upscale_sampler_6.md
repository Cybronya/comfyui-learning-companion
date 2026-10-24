---
name: unknown_workflow_inpaint_upscale_sampler_6
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.663
common_nodes: [AILab_ImagePreview, AILab_Preview, AIO_Preprocessor, BasicScheduler, BatchImagesNode, CFGGuider, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, ComfyMathExpression, FaceAnalysisModels, FaceEmbedDistance, GetImageSizeAndCount, INTConstant, Image Comparer (rgthree), Image Paste Crop, ImageBlend, ImageCropByMask, ImagePadForOutpaint, ImageScaleToMaxDimension, ImageStitch, ImageToMask, Images to RGB, InpaintModelConditioning, InvertMask, KSamplerSelect, LoadImage, MaskToImage, ModelAttentionBackend, PreviewImage, QwenImage21Cache, QwenImage21SpectrumT8, RandomNoise, SAM3_Detect, SamplerCustomAdvanced, SaveImage, Seed (rgthree), SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/一键换头-图片编辑(局部重绘)-Qwen Image2.1_2109591373203730433.json, 图片生成/图生图/一键换头-图片编辑(局部重绘)-Qwen Image2.1_2109601936193441794.json, 图片生成/图生图/图片编辑-换头(局部重绘)-QwenImage2.1_2107437547424145409.json, 图片生成/图生图/图片编辑-换脸(局部重绘)-QwenImage2.1_2107759133796683777.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_upscale_sampler_6

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/一键换头-图片编辑(局部重绘)-Qwen Image2.1_2109591373203730433.json、图片生成/图生图/一键换头-图片编辑(局部重绘)-Qwen Image2.1_2109601936193441794.json、图片生成/图生图/图片编辑-换头(局部重绘)-QwenImage2.1_2107437547424145409.json、图片生成/图生图/图片编辑-换脸(局部重绘)-QwenImage2.1_2107759133796683777.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：66%

## 共有节点

全部 4 个 workflow 都包含：
- `AILab_ImagePreview`
- `AILab_Preview`
- `AIO_Preprocessor`
- `BasicScheduler`
- `BatchImagesNode`
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ComfyMathExpression`
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
- `KSamplerSelect`
- `LoadImage`
- `MaskToImage`
- `ModelAttentionBackend`
- `PreviewImage`
- `QwenImage21Cache`
- `QwenImage21SpectrumT8`
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

**可变部分**（部分 workflow 才有）：
- `ComfyNumberConvert` —— 3/4 个有
- `GrowMaskWithBlur` —— 3/4 个有
- `ImageResizeKJv2` —— 3/4 个有
- `Mask Crop Region` —— 3/4 个有
- `Mask Paste Region` —— 3/4 个有
- `PreviewAny` —— 3/4 个有
- `easy int` —— 3/4 个有
- `AutoCropFaces` —— 1/4 个有
- `ColorMatchV2` —— 1/4 个有
- `FaceAlign` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImageScaleToTotalPixels` —— 1/4 个有
- `OpenposePreprocessor` —— 1/4 个有
- `PrimitiveFloat` —— 1/4 个有
- `SetNode` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
