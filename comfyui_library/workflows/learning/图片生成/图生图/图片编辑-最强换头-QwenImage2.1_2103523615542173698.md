---
key: 图片生成/图生图/图片编辑-最强换头-QwenImage2.1_2103523615542173698.json
name: 图片编辑-最强换头-QwenImage2.1_2103523615542173698
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图片编辑-最强换头-QwenImage2.1_2103523615542173698.json
hash: 4f5d18ed15720144
coverage: 0.623188
learned_at: 2026-10-21 00:51:24
nodes: [ModelAttentionBackend, QwenImage21Cache, KSamplerSelect, RandomNoise, CFGGuider, BasicScheduler, Seed (rgthree), FaceAnalysisModels, SamplerCustomAdvanced, easy cleanGpuUsed, VAEDecode, PreviewImage, VOSR2ModelLoader, VOSR2Upscale, Images to RGB, easy cleanGpuUsed, easy cleanGpuUsed, PreviewImage, easy cleanGpuUsed, Reroute, Reroute, ImageStitch, ImageStitch, Reroute, Reroute, Reroute, Reroute, Reroute, ImageScaleToMaxDimension, Reroute, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, Reroute, easy cleanGpuUsed, PreviewImage, Reroute, PreviewImage, Reroute, Reroute, LoadImage, PreviewImage, UNETLoader, CLIPLoader, Reroute, SaveImage, Image Comparer (rgthree), FaceEmbedDistance, Reroute, Reroute, Image Comparer (rgthree), LoadImage, Reroute, LoadImage, ComfyMathExpression, ComfyMathExpression, easy float, easy cleanGpuUsed, ResizeImageMaskNode, ResizeImageMaskNode, ImageResizeKJv2, TextEncodeQwenImage21, GetImageSizeAndCount, VAELoader, PreviewImage, GetImageSizeAndCount, AIO_Preprocessor, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/图片编辑-最强换头-QwenImage2.1_2103523615542173698.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图片编辑-最强换头-QwenImage2.1_2103523615542173698.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `ModelAttentionBackend`
- `QwenImage21Cache`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `BasicScheduler`
- `Seed (rgthree)`
- `FaceAnalysisModels`
- `SamplerCustomAdvanced` ★核心
- `easy cleanGpuUsed`
- `VAEDecode` ★核心
- `PreviewImage`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `Images to RGB`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `PreviewImage`
- `easy cleanGpuUsed`
- `Reroute`
- `Reroute`
- `ImageStitch`
- `ImageStitch`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageScaleToMaxDimension`
- `Reroute`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `Reroute`
- `easy cleanGpuUsed`
- `PreviewImage`
- `Reroute`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `LoadImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Reroute`
- `SaveImage`
- `Image Comparer (rgthree)`
- `FaceEmbedDistance`
- `Reroute`
- `Reroute`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Reroute`
- `LoadImage`
- `ComfyMathExpression`
- `ComfyMathExpression`
- `easy float`
- `easy cleanGpuUsed`
- `ResizeImageMaskNode`
- `ResizeImageMaskNode`
- `ImageResizeKJv2`
- `TextEncodeQwenImage21`
- `GetImageSizeAndCount`
- `VAELoader`
- `PreviewImage`
- `GetImageSizeAndCount`
- `AIO_Preprocessor`
- `PreviewImage`

## 知识

覆盖率 **62%**（43/69）

**有卡**：`ModelAttentionBackend`、`QwenImage21Cache`、`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`BasicScheduler`、`Seed (rgthree)`、`FaceAnalysisModels`、`SamplerCustomAdvanced`、`easy cleanGpuUsed`、`VAEDecode`、`VOSR2ModelLoader`、`VOSR2Upscale`、`Images to RGB`、`ImageStitch`、`ImageScaleToMaxDimension`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`SaveImage`、`FaceEmbedDistance`、`ComfyMathExpression`、`easy float`、`ResizeImageMaskNode`、`ImageResizeKJv2`、`TextEncodeQwenImage21`、`GetImageSizeAndCount`、`VAELoader`、`AIO_Preprocessor`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader、CFGGuider
