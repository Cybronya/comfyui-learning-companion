---
key: 图片生成/图生图/图片编辑换头局部重绘Qwen Image 2.1工作流，换脸图生图处理工具_2107925759909253121.json
name: 图片编辑换头局部重绘Qwen Image 2.1工作流，换脸图生图处理工具_2107925759909253121
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片编辑换头局部重绘Qwen Image 2.1工作流，换脸图生图处理工具_2107925759909253121.json
hash: 70f912fd4d4daedb
coverage: 0.695279
learned_at: 2026-10-21 00:51:26
nodes: [VOSR2ModelLoader, VOSR2Upscale, Images to RGB, Reroute, easy cleanGpuUsed, easy cleanGpuUsed, ImageStitch, ImageStitch, Reroute, Reroute, Reroute, ImageScaleToMaxDimension, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Reroute, easy cleanGpuUsed, LoadImage, Image Comparer (rgthree), LoadImage, Reroute, Reroute, ComfyMathExpression, ImagePadForOutpaint, InvertMask, SAM3_Detect, Mask Crop Region, Mask Paste Region, MaskToImage, CheckpointLoaderSimple, CLIPTextEncode, ImageCropByMask, SAM3_Detect, AILab_Preview, ImageToMask, AILab_Preview, Mask Paste Region, MaskToImage, ImagePadForOutpaint, Mask Crop Region, ComfyMathExpression, ImageCropByMask, ImageResizeKJv2, ImageResizeKJv2, ImageToMask, AILab_Preview, AILab_Preview, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, GrowMaskWithBlur, ComfyMathExpression, ComfyMathExpression, GrowMaskWithBlur, ImageCropByMask, ImageToMask, ImageCropByMask, ImageToMask, Reroute, Reroute, easy int, ImageResizeKJv2, ImageResizeKJv2, GetImageSizeAndCount, GetImageSizeAndCount, ImageResizeKJv2, ImageResizeKJv2, Reroute, Reroute, Reroute, MaskToImage, ImageBlend, InvertMask, Reroute, MaskToImage, ImageBlend, PreviewAny, ComfyNumberConvert, ComfyMathExpression, GetImageSizeAndCount, ModelAttentionBackend, AIO_Preprocessor, QwenImage21Cache, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, SamplerCustomAdvanced, easy cleanGpuUsed, VAEDecode, easy cleanGpuUsed, Reroute, Reroute, Reroute, AILab_ImagePreview, GrowMaskWithBlur, FaceEmbedDistance, FaceAnalysisModels, PreviewImage, Reroute, Reroute, Reroute, INTConstant, Image Comparer (rgthree), Reroute, Reroute, Reroute, GrowMaskWithBlur, ModelAttentionBackend, QwenImage21Cache, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, FaceAnalysisModels, FaceEmbedDistance, INTConstant, SamplerCustomAdvanced, easy cleanGpuUsed, VAEDecode, Image Comparer (rgthree), PreviewImage, easy cleanGpuUsed, Reroute, GetImageSizeAndCount, ImageBlend, AILab_ImagePreview, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, SaveImage, ImageCropByMask, Mask Crop Region, Image Paste Crop, Reroute, Reroute, Reroute, FaceEmbedDistance, FaceAnalysisModels, PreviewImage, Image Comparer (rgthree), Reroute, AILab_ImagePreview, Mask Crop Region, Image Paste Crop, ImageCropByMask, Reroute, BatchImagesNode, Reroute, AILab_ImagePreview, Reroute, FaceAnalysisModels, FaceEmbedDistance, PreviewImage, Image Comparer (rgthree), AILab_ImagePreview, Reroute, FaceAnalysisModels, FaceEmbedDistance, PreviewImage, Image Comparer (rgthree), Reroute, UNETLoader, InpaintModelConditioning, AIO_Preprocessor, UNETLoader, GetImageSizeAndCount, Reroute, Reroute, Reroute, PreviewImage, Reroute, PreviewImage, CLIPLoader, VAELoader, AILab_Preview, AILab_ImagePreview, AILab_ImagePreview, CLIPLoader, VAELoader, AILab_Preview, AILab_ImagePreview, AILab_ImagePreview, TextEncodeQwenImage21, TextEncodeQwenImage21, InpaintModelConditioning, GetImageSizeAndCount, GetImageSizeAndCount, GetImageSizeAndCount, INTConstant, INTConstant, Reroute, Seed (rgthree), Seed (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/图片编辑换头局部重绘Qwen Image 2.1工作流，换脸图生图处理工具_2107925759909253121.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片编辑换头局部重绘Qwen Image 2.1工作流，换脸图生图处理工具_2107925759909253121.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（233 个）：
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
- `LoadImage`
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
- `CLIPTextEncode` ★核心
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
- `ModelAttentionBackend`
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
- `ModelAttentionBackend`
- `QwenImage21Cache`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `INTConstant`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `PreviewImage`
- `easy cleanGpuUsed`
- `Reroute`
- `GetImageSizeAndCount`
- `ImageBlend`
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
- `PreviewImage`
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
- `TextEncodeQwenImage21`
- `TextEncodeQwenImage21`
- `InpaintModelConditioning`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `INTConstant`
- `INTConstant`
- `Reroute`
- `Seed (rgthree)`
- `Seed (rgthree)`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **70%**（162/233）

**有卡**：`VOSR2ModelLoader`、`VOSR2Upscale`、`Images to RGB`、`easy cleanGpuUsed`、`ImageStitch`、`ImageScaleToMaxDimension`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`LoadImage`、`ComfyMathExpression`、`ImagePadForOutpaint`、`InvertMask`、`SAM3_Detect`、`Mask Crop Region`、`Mask Paste Region`、`MaskToImage`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`ImageCropByMask`、`AILab_Preview`、`ImageToMask`、`ImageResizeKJv2`、`GrowMaskWithBlur`、`easy int`、`GetImageSizeAndCount`、`ImageBlend`、`ComfyNumberConvert`、`ModelAttentionBackend`、`AIO_Preprocessor`、`QwenImage21Cache`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`AILab_ImagePreview`、`FaceEmbedDistance`、`FaceAnalysisModels`、`INTConstant`、`SaveImage`、`Image Paste Crop`、`BatchImagesNode`、`UNETLoader`、`InpaintModelConditioning`、`CLIPLoader`、`VAELoader`、`TextEncodeQwenImage21`、`Seed (rgthree)`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
