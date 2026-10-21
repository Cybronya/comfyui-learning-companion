---
key: 图片生成/图生图/QwenImage2.1图片换头编辑｜局部重绘自然无痕迹_2107666085775503361.json
name: QwenImage2.1图片换头编辑｜局部重绘自然无痕迹_2107666085775503361
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenImage2.1图片换头编辑｜局部重绘自然无痕迹_2107666085775503361.json
hash: b3daaa8709c858d9
coverage: 0.730159
learned_at: 2026-10-21 00:43:52
nodes: [VOSR2ModelLoader, VOSR2Upscale, Images to RGB, Reroute, easy cleanGpuUsed, easy cleanGpuUsed, PreviewImage, ImageStitch, ImageStitch, Reroute, Reroute, Reroute, ImageScaleToMaxDimension, Reroute, Reroute, Reroute, Reroute, GetImageSizeAndCount, ComfyMathExpression, ImagePadForOutpaint, InvertMask, SAM3_Detect, Mask Crop Region, Mask Paste Region, MaskToImage, CheckpointLoaderSimple, CLIPTextEncode, ImageCropByMask, SAM3_Detect, INTConstant, AILab_Preview, ImageToMask, AILab_Preview, Mask Paste Region, MaskToImage, GetImageSizeAndCount, ImagePadForOutpaint, Mask Crop Region, ComfyMathExpression, ImageCropByMask, InvertMask, ImageResizeKJv2, ImageResizeKJv2, ImageToMask, AILab_Preview, AILab_Preview, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, GrowMaskWithBlur, ComfyMathExpression, ComfyMathExpression, GrowMaskWithBlur, ImageCropByMask, ImageToMask, ImageCropByMask, ImageToMask, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageCropByMask, Mask Crop Region, Image Paste Crop, Reroute, Reroute, Reroute, FaceEmbedDistance, FaceAnalysisModels, PreviewImage, Image Comparer (rgthree), Reroute, Reroute, Reroute, ModelAttentionBackend, AIO_Preprocessor, GetImageSizeAndCount, QwenImage21Cache, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, SamplerCustomAdvanced, easy cleanGpuUsed, VAEDecode, easy cleanGpuUsed, Reroute, Reroute, Reroute, AILab_Preview, AILab_ImagePreview, AILab_ImagePreview, AILab_ImagePreview, TextEncodeQwenImage21, AILab_ImagePreview, InpaintModelConditioning, GrowMaskWithBlur, FaceEmbedDistance, FaceAnalysisModels, PreviewImage, Reroute, Reroute, INTConstant, Reroute, Reroute, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageResizeKJv2, ImageResizeKJv2, easy int, easy float, Reroute, Reroute, Reroute, Reroute, Reroute, ImageResizeKJv2, GetImageSizeAndCount, Reroute, Reroute, Reroute, ModelAttentionBackend, AILab_Preview, InpaintModelConditioning, QwenImage21Cache, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, FaceAnalysisModels, FaceEmbedDistance, INTConstant, SamplerCustomAdvanced, easy cleanGpuUsed, VAEDecode, Image Comparer (rgthree), PreviewImage, easy cleanGpuUsed, AILab_ImagePreview, Reroute, Reroute, ModelAttentionBackend, AILab_Preview, InpaintModelConditioning, INTConstant, GrowMaskWithBlur, AILab_ImagePreview, KSamplerSelect, QwenImage21Cache, RandomNoise, CFGGuider, BasicScheduler, FaceAnalysisModels, FaceEmbedDistance, SamplerCustomAdvanced, easy cleanGpuUsed, PreviewImage, VAEDecode, Image Comparer (rgthree), easy cleanGpuUsed, AILab_ImagePreview, CheckpointLoaderSimple, CLIPTextEncode, SAM3_Detect, MaskToImage, ImageBlend, Reroute, Image Comparer (rgthree), AILab_ImagePreview, AILab_ImagePreview, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Reroute, easy cleanGpuUsed, PreviewImage, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, UNETLoader, CLIPLoader, VAELoader, Reroute, LoadImage, GrowMaskWithBlur, AILab_ImagePreview, TextEncodeQwenImage21, Reroute, Reroute, Reroute, Image Comparer (rgthree), SaveImage, Reroute, LoadImage, Seed (rgthree), Seed (rgthree), Seed (rgthree), 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QwenImage2.1图片换头编辑｜局部重绘自然无痕迹_2107666085775503361.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenImage2.1图片换头编辑｜局部重绘自然无痕迹_2107666085775503361.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（252 个）：
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `Images to RGB`
- `Reroute`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `PreviewImage`
- `ImageStitch`
- `ImageStitch`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageScaleToMaxDimension`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `GetImageSizeAndCount`
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
- `INTConstant`
- `AILab_Preview`
- `ImageToMask`
- `AILab_Preview`
- `Mask Paste Region`
- `MaskToImage`
- `GetImageSizeAndCount`
- `ImagePadForOutpaint`
- `Mask Crop Region`
- `ComfyMathExpression`
- `ImageCropByMask`
- `InvertMask`
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
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
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
- `Reroute`
- `Reroute`
- `ModelAttentionBackend`
- `AIO_Preprocessor`
- `GetImageSizeAndCount`
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
- `AILab_Preview`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `TextEncodeQwenImage21`
- `AILab_ImagePreview`
- `InpaintModelConditioning`
- `GrowMaskWithBlur`
- `FaceEmbedDistance`
- `FaceAnalysisModels`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `INTConstant`
- `Reroute`
- `Reroute`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `easy int`
- `easy float`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `Reroute`
- `Reroute`
- `Reroute`
- `ModelAttentionBackend`
- `AILab_Preview`
- `InpaintModelConditioning`
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
- `AILab_ImagePreview`
- `Reroute`
- `Reroute`
- `ModelAttentionBackend`
- `AILab_Preview`
- `InpaintModelConditioning`
- `INTConstant`
- `GrowMaskWithBlur`
- `AILab_ImagePreview`
- `KSamplerSelect` ★核心
- `QwenImage21Cache`
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
- `AILab_ImagePreview`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `SAM3_Detect`
- `MaskToImage`
- `ImageBlend`
- `Reroute`
- `Image Comparer (rgthree)`
- `AILab_ImagePreview`
- `AILab_ImagePreview`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Reroute`
- `easy cleanGpuUsed`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `LoadImage`
- `GrowMaskWithBlur`
- `AILab_ImagePreview`
- `TextEncodeQwenImage21`
- `Reroute`
- `Reroute`
- `Reroute`
- `Image Comparer (rgthree)`
- `SaveImage`
- `Reroute`
- `LoadImage`
- `Seed (rgthree)`
- `Seed (rgthree)`
- `Seed (rgthree)`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **73%**（184/252）

**有卡**：`VOSR2ModelLoader`、`VOSR2Upscale`、`Images to RGB`、`easy cleanGpuUsed`、`ImageStitch`、`ImageScaleToMaxDimension`、`GetImageSizeAndCount`、`ComfyMathExpression`、`ImagePadForOutpaint`、`InvertMask`、`SAM3_Detect`、`Mask Crop Region`、`Mask Paste Region`、`MaskToImage`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`ImageCropByMask`、`INTConstant`、`AILab_Preview`、`ImageToMask`、`ImageResizeKJv2`、`GrowMaskWithBlur`、`Image Paste Crop`、`FaceEmbedDistance`、`FaceAnalysisModels`、`ModelAttentionBackend`、`AIO_Preprocessor`、`QwenImage21Cache`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`BasicScheduler`、`SamplerCustomAdvanced`、`VAEDecode`、`AILab_ImagePreview`、`TextEncodeQwenImage21`、`InpaintModelConditioning`、`ImageScaleToTotalPixels`、`easy int`、`easy float`、`ImageBlend`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoadImage`、`SaveImage`、`Seed (rgthree)`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
