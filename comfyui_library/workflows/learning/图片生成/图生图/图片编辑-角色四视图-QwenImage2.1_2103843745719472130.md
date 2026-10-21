---
key: 图片生成/图生图/图片编辑-角色四视图-QwenImage2.1_2103843745719472130.json
name: 图片编辑-角色四视图-QwenImage2.1_2103843745719472130
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片编辑-角色四视图-QwenImage2.1_2103843745719472130.json
hash: c0bba01a7af17f7e
coverage: 0.69863
learned_at: 2026-10-21 00:51:24
nodes: [Reroute, ResizeImageMaskNode, ModelAttentionBackend, ResolutionSelector, QwenImage21Cache, Seed (rgthree), PrimitiveStringMultiline, ResizeImageMaskNode, PrimitiveStringMultiline, EmptyLatentImage, RandomNoise, CFGGuider, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, easy cleanGpuUsed, FaceAnalysisModels, FaceEmbedDistance, VAEDecode, Image Comparer (rgthree), easy cleanGpuUsed, PreviewImage, SCAIL2ColoredMask, Reroute, Reroute, Reroute, ImageStitch, GetImageSizeAndCount, GetImageSizeAndCount, ComfyMathExpression, AILab_ImageCrop, Reroute, Reroute, Reroute, CLIPTextEncode, SAM3_VideoTrack, Bounded Image Crop with Mask, ImageToMask, Reroute, Image Comparer (rgthree), INTConstant, AILab_ImageCrop, Reroute, ModelAttentionBackend, QwenImage21Cache, easy cleanGpuUsed, VAEDecode, Reroute, Seed (rgthree), SamplerCustomAdvanced, VOSR2ModelLoader, VOSR2Upscale, easy cleanGpuUsed, easy cleanGpuUsed, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, FaceAnalysisModels, PreviewImage, ResizeImageMaskNode, SCAIL2ColoredMask, CLIPTextEncode, SCAIL2ColoredMask, FaceEmbedDistance, ResizeImageMaskNode, SCAIL2ColoredMask, SAM3_VideoTrack, Bounded Image Crop with Mask, INTConstant, Bounded Image Crop with Mask, AutoCropFaces, ResizeImageMaskNode, ResizeImageMaskNode, ImageToMask, ImageResizeKJv2, ImageToMask, ImageResizeKJv2, Bounded Image Crop with Mask, ImageToMask, ImageBatchMulti, TextEncodeQwenImage21, ImagePadForOutpaint, GetImageSizeAndCount, TextEncodeQwenImage21, ComfyMathExpression, MaskToImage, Reroute, ImageStitch, Reroute, SCAIL2ColoredMask, ImageToMask, Bounded Image Crop with Mask, ImageResizeKJv2, INTConstant, ImageResizeKJv2, easy cleanGpuUsed, UNETLoader, CLIPLoader, VAELoader, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Reroute, easy cleanGpuUsed, Image Comparer (rgthree), PreviewImage, PreviewImage, PreviewImage, UNETLoader, CLIPLoader, VAELoader, CheckpointLoaderSimple, CheckpointLoaderSimple, Reroute, Reroute, PreviewImage, easy cleanGpuUsed, Images to RGB, AutoCropFaces, ImageBlend, PreviewImage, PreviewImage, PreviewImage, GetImageSizeAndCount, PreviewImage, Reroute, SaveImage, PreviewImage, Reroute, Reroute, Reroute, Reroute, Reroute, ImageResizeKJv2, ImageResizeKJv2, Reroute, Reroute, PreviewImage, Reroute, LoadImage, Reroute, LoadImage, Images to RGB, PreviewImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "height": 1024, "width": 1024}
---

# 图片生成/图生图/图片编辑-角色四视图-QwenImage2.1_2103843745719472130.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片编辑-角色四视图-QwenImage2.1_2103843745719472130.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（146 个）：
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
- `LoadImage`
- `Images to RGB`
- `PreviewImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **70%**（102/146）

**有卡**：`ResizeImageMaskNode`、`ModelAttentionBackend`、`ResolutionSelector`、`QwenImage21Cache`、`Seed (rgthree)`、`EmptyLatentImage`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`、`FaceAnalysisModels`、`FaceEmbedDistance`、`VAEDecode`、`SCAIL2ColoredMask`、`ImageStitch`、`GetImageSizeAndCount`、`ComfyMathExpression`、`AILab_ImageCrop`、`CLIPTextEncode`、`SAM3_VideoTrack`、`Bounded Image Crop with Mask`、`ImageToMask`、`INTConstant`、`VOSR2ModelLoader`、`VOSR2Upscale`、`AutoCropFaces`、`ImageResizeKJv2`、`ImageBatchMulti`、`TextEncodeQwenImage21`、`ImagePadForOutpaint`、`MaskToImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`CheckpointLoaderSimple`、`Images to RGB`、`ImageBlend`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage
