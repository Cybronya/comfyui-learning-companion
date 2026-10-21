---
key: 图片生成/图生图/图片编辑-换脸(局部重绘)-QwenImage2.1_2107759133796683777.json
name: 图片编辑-换脸(局部重绘)-QwenImage2.1_2107759133796683777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片编辑-换脸(局部重绘)-QwenImage2.1_2107759133796683777.json
hash: 2e4716215c5430b7
coverage: 0.642458
learned_at: 2026-10-21 00:51:23
nodes: [Reroute, Reroute, AILab_ImagePreview, GetImageSizeAndCount, ComfyMathExpression, AutoCropFaces, ImagePadForOutpaint, ImageScaleToTotalPixels, InvertMask, AutoCropFaces, Image Paste Crop, ImageToMask, AILab_Preview, ImagePadForOutpaint, Reroute, Reroute, AILab_ImagePreview, GetImageSizeAndCount, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, AutoCropFaces, ComfyMathExpression, ImageScaleToTotalPixels, AILab_Preview, QwenImage21Cache, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, InpaintModelConditioning, SamplerCustomAdvanced, easy cleanGpuUsed, VAEDecode, easy cleanGpuUsed, Image Comparer (rgthree), Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Image Paste Crop, ImageCropByMask, FaceAnalysisModels, FaceEmbedDistance, PreviewImage, Image Comparer (rgthree), TextEncodeQwenImage21, Reroute, Reroute, Reroute, AILab_Preview, InpaintModelConditioning, INTConstant, QwenImage21Cache, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, FaceAnalysisModels, FaceEmbedDistance, SamplerCustomAdvanced, easy cleanGpuUsed, PreviewImage, VAEDecode, Image Comparer (rgthree), easy cleanGpuUsed, Reroute, Reroute, Reroute, Reroute, FaceAnalysisModels, FaceEmbedDistance, PreviewImage, TextEncodeQwenImage21, Reroute, SAM3_Detect, MaskToImage, AILab_ImagePreview, AILab_ImagePreview, AILab_ImagePreview, AILab_ImagePreview, AILab_ImagePreview, Image Comparer (rgthree), AILab_ImagePreview, AILab_ImagePreview, AILab_ImagePreview, Image Paste Crop, ImageCropByMask, FaceAnalysisModels, FaceEmbedDistance, PreviewImage, AILab_ImagePreview, Image Comparer (rgthree), Reroute, AIO_Preprocessor, GetImageSizeAndCount, AILab_ImagePreview, Reroute, Reroute, BatchImagesNode, Reroute, SaveImage, ImageStitch, ImageStitch, Reroute, Reroute, Reroute, ImageScaleToMaxDimension, VOSR2ModelLoader, VOSR2Upscale, Images to RGB, Reroute, easy cleanGpuUsed, easy cleanGpuUsed, FaceAnalysisModels, PreviewImage, AILab_ImagePreview, FaceEmbedDistance, Image Comparer (rgthree), Reroute, AILab_ImagePreview, FaceAnalysisModels, FaceAlign, AutoCropFaces, LoadImage, LoadImage, Reroute, Reroute, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Reroute, easy cleanGpuUsed, Reroute, Reroute, Reroute, Reroute, PreviewImage, Image Comparer (rgthree), UNETLoader, CLIPLoader, VAELoader, UNETLoader, CLIPLoader, VAELoader, Reroute, Reroute, LoadImage, Seed (rgthree), MaskToImage, SAM3_Detect, CheckpointLoaderSimple, CLIPTextEncode, GetImageSizeAndCount, ImageBlend, ColorMatchV2, ImageBlend, OpenposePreprocessor, SetNode, PrimitiveFloat, GetNode, ImageBlend, INTConstant, Seed (rgthree), MarkdownNote, QwenImage21SpectrumT8, ModelAttentionBackend, MarkdownNote, QwenImage21SpectrumT8, ModelAttentionBackend, PreviewImage, Reroute]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 图片生成/图生图/图片编辑-换脸(局部重绘)-QwenImage2.1_2107759133796683777.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片编辑-换脸(局部重绘)-QwenImage2.1_2107759133796683777.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（179 个）：
- `Reroute`
- `Reroute`
- `AILab_ImagePreview`
- `GetImageSizeAndCount`
- `ComfyMathExpression`
- `AutoCropFaces`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `InvertMask`
- `AutoCropFaces`
- `Image Paste Crop`
- `ImageToMask`
- `AILab_Preview`
- `ImagePadForOutpaint`
- `Reroute`
- `Reroute`
- `AILab_ImagePreview`
- `GetImageSizeAndCount`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `AutoCropFaces`
- `ComfyMathExpression`
- `ImageScaleToTotalPixels`
- `AILab_Preview`
- `QwenImage21Cache`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `InpaintModelConditioning`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Image Paste Crop`
- `ImageCropByMask`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `Reroute`
- `Reroute`
- `Reroute`
- `AILab_Preview`
- `InpaintModelConditioning`
- `INTConstant`
- `QwenImage21Cache`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `PreviewImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `Reroute`
- `SAM3_Detect`
- `MaskToImage`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `Image Comparer (rgthree)`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `Image Paste Crop`
- `ImageCropByMask`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `PreviewImage`
- `AILab_ImagePreview`
- `Image Comparer (rgthree)`
- `Reroute`
- `AIO_Preprocessor`
- `GetImageSizeAndCount`
- `AILab_ImagePreview`
- `Reroute`
- `Reroute`
- `BatchImagesNode`
- `Reroute`
- `SaveImage`
- `ImageStitch`
- `ImageStitch`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageScaleToMaxDimension`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `Images to RGB`
- `Reroute`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `FaceAnalysisModels`
- `PreviewImage`
- `AILab_ImagePreview`
- `FaceEmbedDistance`
- `Image Comparer (rgthree)`
- `Reroute`
- `AILab_ImagePreview`
- `FaceAnalysisModels`
- `FaceAlign`
- `AutoCropFaces`
- `LoadImage`
- `LoadImage`
- `Reroute`
- `Reroute`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Reroute`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `Reroute`
- `LoadImage`
- `Seed (rgthree)`
- `MaskToImage`
- `SAM3_Detect`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `GetImageSizeAndCount`
- `ImageBlend`
- `ColorMatchV2`
- `ImageBlend`
- `OpenposePreprocessor`
- `SetNode`
- `PrimitiveFloat`
- `GetNode`
- `ImageBlend`
- `INTConstant`
- `Seed (rgthree)`
- `MarkdownNote`
- `QwenImage21SpectrumT8`
- `ModelAttentionBackend`
- `MarkdownNote`
- `QwenImage21SpectrumT8`
- `ModelAttentionBackend`
- `PreviewImage`
- `Reroute`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **64%**（115/179）

**有卡**：`AILab_ImagePreview`、`GetImageSizeAndCount`、`ComfyMathExpression`、`AutoCropFaces`、`ImagePadForOutpaint`、`ImageScaleToTotalPixels`、`InvertMask`、`Image Paste Crop`、`ImageToMask`、`AILab_Preview`、`QwenImage21Cache`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`BasicScheduler`、`InpaintModelConditioning`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`、`VAEDecode`、`ImageCropByMask`、`FaceAnalysisModels`、`FaceEmbedDistance`、`TextEncodeQwenImage21`、`INTConstant`、`SAM3_Detect`、`MaskToImage`、`AIO_Preprocessor`、`BatchImagesNode`、`SaveImage`、`ImageStitch`、`ImageScaleToMaxDimension`、`VOSR2ModelLoader`、`VOSR2Upscale`、`Images to RGB`、`FaceAlign`、`LoadImage`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`Seed (rgthree)`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`ImageBlend`、`ColorMatchV2`、`OpenposePreprocessor`、`QwenImage21SpectrumT8`、`ModelAttentionBackend`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage
