---
key: 图片生成/图生图/角色四视图一键生成 QwenImage2.1超高一致性图生图_2104301701854486529.json
name: 角色四视图一键生成 QwenImage2.1超高一致性图生图_2104301701854486529
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/角色四视图一键生成 QwenImage2.1超高一致性图生图_2104301701854486529.json
hash: c23f97ba33800a8d
coverage: 0.724138
learned_at: 2026-10-21 00:56:17
nodes: [Reroute, ResizeImageMaskNode, ModelAttentionBackend, ResolutionSelector, QwenImage21Cache, Seed (rgthree), PrimitiveStringMultiline, ResizeImageMaskNode, PrimitiveStringMultiline, EmptyLatentImage, RandomNoise, CFGGuider, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, easy cleanGpuUsed, FaceAnalysisModels, FaceEmbedDistance, VAEDecode, Image Comparer (rgthree), easy cleanGpuUsed, PreviewImage, SCAIL2ColoredMask, Reroute, Reroute, Reroute, ImageStitch, GetImageSizeAndCount, GetImageSizeAndCount, ComfyMathExpression, AILab_ImageCrop, Reroute, Reroute, Reroute, CLIPTextEncode, SAM3_VideoTrack, Bounded Image Crop with Mask, ImageToMask, Reroute, Image Comparer (rgthree), INTConstant, AILab_ImageCrop, Reroute, ModelAttentionBackend, QwenImage21Cache, easy cleanGpuUsed, VAEDecode, Reroute, Seed (rgthree), SamplerCustomAdvanced, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed, easy cleanGpuUsed, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, FaceAnalysisModels, PreviewImage, ResizeImageMaskNode, SCAIL2ColoredMask, CLIPTextEncode, SCAIL2ColoredMask, FaceEmbedDistance, ResizeImageMaskNode, SCAIL2ColoredMask, SAM3_VideoTrack, Bounded Image Crop with Mask, INTConstant, Bounded Image Crop with Mask, AutoCropFaces, ResizeImageMaskNode, ResizeImageMaskNode, ImageToMask, ImageResizeKJv2, ImageToMask, ImageResizeKJv2, Bounded Image Crop with Mask, ImageToMask, ImageBatchMulti, TextEncodeQwenImage21, ImagePadForOutpaint, GetImageSizeAndCount, TextEncodeQwenImage21, ComfyMathExpression, MaskToImage, Reroute, ImageStitch, Reroute, SCAIL2ColoredMask, ImageToMask, Bounded Image Crop with Mask, ImageResizeKJv2, INTConstant, ImageResizeKJv2, easy cleanGpuUsed, UNETLoader, CLIPLoader, VAELoader, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Reroute, easy cleanGpuUsed, Image Comparer (rgthree), PreviewImage, PreviewImage, PreviewImage, UNETLoader, CLIPLoader, VAELoader, CheckpointLoaderSimple, CheckpointLoaderSimple, Reroute, Reroute, PreviewImage, easy cleanGpuUsed, Images to RGB, AutoCropFaces, ImageBlend, PreviewImage, PreviewImage, PreviewImage, GetImageSizeAndCount, PreviewImage, Reroute, SaveImage, PreviewImage, Reroute, Reroute, Reroute, Reroute, Reroute, ImageResizeKJv2, ImageResizeKJv2, Reroute, Reroute, PreviewImage, Reroute, LoadImage, Reroute, Images to RGB, PreviewImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/角色四视图一键生成 QwenImage2.1超高一致性图生图_2104301701854486529.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/角色四视图一键生成 QwenImage2.1超高一致性图生图_2104301701854486529.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（174 个）：
- `Reroute`
- `ResizeImageMaskNode`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `QwenImage21Cache`
- `Seed (rgthree)`
- `PrimitiveStringMultiline`
- `ResizeImageMaskNode`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `FaceAnalysisModels`
- `FaceEmbedDistance`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `easy cleanGpuUsed`
- `PreviewImage`
- `SCAIL2ColoredMask`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageStitch`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `ComfyMathExpression`
- `AILab_ImageCrop`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPTextEncode` ★核心
- `SAM3_VideoTrack`
- `Bounded Image Crop with Mask`
- `ImageToMask`
- `Reroute`
- `Image Comparer (rgthree)`
- `INTConstant`
- `AILab_ImageCrop`
- `Reroute`
- `ModelAttentionBackend`
- `QwenImage21Cache`
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `Reroute`
- `Seed (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `FaceAnalysisModels`
- `PreviewImage`
- `ResizeImageMaskNode`
- `SCAIL2ColoredMask`
- `CLIPTextEncode` ★核心
- `SCAIL2ColoredMask`
- `FaceEmbedDistance`
- `ResizeImageMaskNode`
- `SCAIL2ColoredMask`
- `SAM3_VideoTrack`
- `Bounded Image Crop with Mask`
- `INTConstant`
- `Bounded Image Crop with Mask`
- `AutoCropFaces`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ImageToMask`
- `ImageResizeKJv2`
- `ImageToMask`
- `ImageResizeKJv2`
- `Bounded Image Crop with Mask`
- `ImageToMask`
- `ImageBatchMulti`
- `TextEncodeQwenImage21`
- `ImagePadForOutpaint`
- `GetImageSizeAndCount`
- `TextEncodeQwenImage21`
- `ComfyMathExpression`
- `MaskToImage`
- `Reroute`
- `ImageStitch`
- `Reroute`
- `SCAIL2ColoredMask`
- `ImageToMask`
- `Bounded Image Crop with Mask`
- `ImageResizeKJv2`
- `INTConstant`
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Reroute`
- `easy cleanGpuUsed`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CheckpointLoaderSimple` ★核心
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `Reroute`
- `PreviewImage`
- `easy cleanGpuUsed`
- `Images to RGB`
- `AutoCropFaces`
- `ImageBlend`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `GetImageSizeAndCount`
- `PreviewImage`
- `Reroute`
- `SaveImage`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `Reroute`
- `LoadImage`
- `Reroute`
- `Images to RGB`
- `PreviewImage`
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

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **72%**（126/174）

**有卡**：`ResizeImageMaskNode`、`ModelAttentionBackend`、`ResolutionSelector`、`QwenImage21Cache`、`Seed (rgthree)`、`EmptyLatentImage`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`、`FaceAnalysisModels`、`FaceEmbedDistance`、`VAEDecode`、`SCAIL2ColoredMask`、`ImageStitch`、`GetImageSizeAndCount`、`ComfyMathExpression`、`AILab_ImageCrop`、`CLIPTextEncode`、`SAM3_VideoTrack`、`Bounded Image Crop with Mask`、`ImageToMask`、`INTConstant`、`VOSR2ModelLoader`、`VOSR2Upscale`、`AutoCropFaces`、`ImageResizeKJv2`、`ImageBatchMulti`、`TextEncodeQwenImage21`、`ImagePadForOutpaint`、`MaskToImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`CheckpointLoaderSimple`、`Images to RGB`、`ImageBlend`、`SaveImage`、`LoadImage`、`LoraLoaderModelOnly`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
