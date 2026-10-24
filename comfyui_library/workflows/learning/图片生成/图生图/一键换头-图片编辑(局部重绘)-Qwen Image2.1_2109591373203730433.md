---
key: 图片生成/图生图/一键换头-图片编辑(局部重绘)-Qwen Image2.1_2109591373203730433.json
name: 一键换头-图片编辑(局部重绘)-Qwen Image2.1_2109591373203730433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/一键换头-图片编辑(局部重绘)-Qwen Image2.1_2109591373203730433.json
hash: 2343653f8eef53d5
coverage: 0.669856
learned_at: 2026-10-23 11:56:08
nodes: [VOSR2ModelLoader, VOSR2Upscale, Images to RGB, Reroute, easy cleanGpuUsed, easy cleanGpuUsed, ImageStitch, ImageStitch, Reroute, Reroute, Reroute, ImageScaleToMaxDimension, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Reroute, easy cleanGpuUsed, Image Comparer (rgthree), LoadImage, Reroute, Reroute, ComfyMathExpression, ImagePadForOutpaint, InvertMask, SAM3_Detect, Mask Crop Region, Mask Paste Region, MaskToImage, CheckpointLoaderSimple, ImageCropByMask, SAM3_Detect, AILab_Preview, ImageToMask, AILab_Preview, Mask Paste Region, MaskToImage, ImagePadForOutpaint, Mask Crop Region, ComfyMathExpression, ImageCropByMask, ImageResizeKJv2, ImageResizeKJv2, ImageToMask, AILab_Preview, AILab_Preview, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, GrowMaskWithBlur, ComfyMathExpression, ComfyMathExpression, GrowMaskWithBlur, ImageCropByMask, ImageToMask, ImageCropByMask, ImageToMask, Reroute, Reroute, easy int, ImageResizeKJv2, ImageResizeKJv2, GetImageSizeAndCount, GetImageSizeAndCount, ImageResizeKJv2, ImageResizeKJv2, Reroute, Reroute, Reroute, MaskToImage, ImageBlend, InvertMask, Reroute, MaskToImage, ImageBlend, PreviewAny, ComfyNumberConvert, ComfyMathExpression, GetImageSizeAndCount, AIO_Preprocessor, QwenImage21Cache, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, SamplerCustomAdvanced, easy cleanGpuUsed, VAEDecode, easy cleanGpuUsed, Reroute, Reroute, Reroute, AILab_ImagePreview, GrowMaskWithBlur, FaceEmbedDistance, FaceAnalysisModels, PreviewImage, Reroute, Reroute, Reroute, INTConstant, Image Comparer (rgthree), Reroute, Reroute, Reroute, GrowMaskWithBlur, QwenImage21Cache, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, FaceAnalysisModels, FaceEmbedDistance, SamplerCustomAdvanced, easy cleanGpuUsed, VAEDecode, Image Comparer (rgthree), PreviewImage, easy cleanGpuUsed, Reroute, GetImageSizeAndCount, AILab_ImagePreview, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, SaveImage, ImageCropByMask, Mask Crop Region, Image Paste Crop, Reroute, Reroute, Reroute, FaceEmbedDistance, FaceAnalysisModels, PreviewImage, Image Comparer (rgthree), Reroute, AILab_ImagePreview, Mask Crop Region, Image Paste Crop, ImageCropByMask, Reroute, BatchImagesNode, Reroute, AILab_ImagePreview, Reroute, FaceAnalysisModels, FaceEmbedDistance, PreviewImage, Image Comparer (rgthree), AILab_ImagePreview, Reroute, FaceAnalysisModels, FaceEmbedDistance, PreviewImage, Image Comparer (rgthree), Reroute, UNETLoader, InpaintModelConditioning, AIO_Preprocessor, UNETLoader, GetImageSizeAndCount, Reroute, Reroute, Reroute, Reroute, PreviewImage, CLIPLoader, VAELoader, AILab_Preview, AILab_ImagePreview, AILab_ImagePreview, CLIPLoader, VAELoader, AILab_Preview, AILab_ImagePreview, AILab_ImagePreview, InpaintModelConditioning, GetImageSizeAndCount, GetImageSizeAndCount, GetImageSizeAndCount, INTConstant, INTConstant, Seed (rgthree), Seed (rgthree), CLIPTextEncode, TextEncodeQwenImage21, INTConstant, ImageBlend, QwenImage21SpectrumT8, MarkdownNote, ModelAttentionBackend, TextEncodeQwenImage21, MarkdownNote, QwenImage21SpectrumT8, ModelAttentionBackend, PreviewImage, Reroute, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 图片生成/图生图/一键换头-图片编辑(局部重绘)-Qwen Image2.1_2109591373203730433.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/一键换头-图片编辑(局部重绘)-Qwen Image2.1_2109591373203730433.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（209 个）：
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `Images to RGB`
- `Reroute`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageStitch`
- `ImageStitch`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageScaleToMaxDimension`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Reroute`
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Reroute`
- `Reroute`
- `ComfyMathExpression`
- `ImagePadForOutpaint`
- `InvertMask`
- `SAM3_Detect`
- `Mask Crop Region`
- `Mask Paste Region`
- `MaskToImage`
- `CheckpointLoaderSimple` ★核心
- `ImageCropByMask`
- `SAM3_Detect`
- `AILab_Preview`
- `ImageToMask`
- `AILab_Preview`
- `Mask Paste Region`
- `MaskToImage`
- `ImagePadForOutpaint`
- `Mask Crop Region`
- `ComfyMathExpression`
- `ImageCropByMask`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `ImageToMask`
- `AILab_Preview`
- `AILab_Preview`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `GrowMaskWithBlur`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `GrowMaskWithBlur`
- `ImageCropByMask`
- `ImageToMask`
- `ImageCropByMask`
- `ImageToMask`
- `Reroute`
- `Reroute`
- `easy int`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Reroute`
- `Reroute`
- `Reroute`
- `MaskToImage`
- `ImageBlend`
- `InvertMask`
- `Reroute`
- `MaskToImage`
- `ImageBlend`
- `PreviewAny`
- `ComfyNumberConvert`
- `ComfyMathExpression`
- `GetImageSizeAndCount`
- `AIO_Preprocessor`
- `QwenImage21Cache`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `Reroute`
- `AILab_ImagePreview`
- `GrowMaskWithBlur`
- `FaceEmbedDistance`
- `FaceAnalysisModels`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `INTConstant`
- `Image Comparer (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `GrowMaskWithBlur`
- `QwenImage21Cache`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `easy cleanGpuUsed`
- `Reroute`
- `GetImageSizeAndCount`
- `AILab_ImagePreview`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `SaveImage`
- `ImageCropByMask`
- `Mask Crop Region`
- `Image Paste Crop`
- `Reroute`
- `Reroute`
- `Reroute`
- `FaceEmbedDistance`
- `FaceAnalysisModels`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Reroute`
- `AILab_ImagePreview`
- `Mask Crop Region`
- `Image Paste Crop`
- `ImageCropByMask`
- `Reroute`
- `BatchImagesNode`
- `Reroute`
- `AILab_ImagePreview`
- `Reroute`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `AILab_ImagePreview`
- `Reroute`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Reroute`
- `UNETLoader` ★核心
- `InpaintModelConditioning`
- `AIO_Preprocessor`
- `UNETLoader` ★核心
- `GetImageSizeAndCount`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `CLIPLoader`
- `VAELoader`
- `AILab_Preview`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `CLIPLoader`
- `VAELoader`
- `AILab_Preview`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `InpaintModelConditioning`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `INTConstant`
- `INTConstant`
- `Seed (rgthree)`
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `TextEncodeQwenImage21`
- `INTConstant`
- `ImageBlend`
- `QwenImage21SpectrumT8`
- `MarkdownNote`
- `ModelAttentionBackend`
- `TextEncodeQwenImage21`
- `MarkdownNote`
- `QwenImage21SpectrumT8`
- `ModelAttentionBackend`
- `PreviewImage`
- `Reroute`
- `LoadImage`
- `LoadImage`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **67%**（140/209）

**有卡**：`VOSR2ModelLoader`、`VOSR2Upscale`、`Images to RGB`、`easy cleanGpuUsed`、`ImageStitch`、`ImageScaleToMaxDimension`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`LoadImage`、`ComfyMathExpression`、`ImagePadForOutpaint`、`InvertMask`、`SAM3_Detect`、`Mask Crop Region`、`Mask Paste Region`、`MaskToImage`、`CheckpointLoaderSimple`、`ImageCropByMask`、`AILab_Preview`、`ImageToMask`、`ImageResizeKJv2`、`GrowMaskWithBlur`、`easy int`、`GetImageSizeAndCount`、`ImageBlend`、`ComfyNumberConvert`、`AIO_Preprocessor`、`QwenImage21Cache`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`AILab_ImagePreview`、`FaceEmbedDistance`、`FaceAnalysisModels`、`INTConstant`、`SaveImage`、`Image Paste Crop`、`BatchImagesNode`、`UNETLoader`、`InpaintModelConditioning`、`CLIPLoader`、`VAELoader`、`Seed (rgthree)`、`CLIPTextEncode`、`TextEncodeQwenImage21`、`QwenImage21SpectrumT8`、`ModelAttentionBackend`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage
