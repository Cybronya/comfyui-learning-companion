---
key: 图片生成/文生图/图片编辑-QwenImage2.1_2101963695487283202.json
name: 图片编辑-QwenImage2.1_2101963695487283202
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图片编辑-QwenImage2.1_2101963695487283202.json
hash: 99ba4fc44a8481a8
coverage: 0.647059
learned_at: 2026-10-20 01:52:26
nodes: [QwenImage21Cache, VAEDecode, ResolutionSelector, TextEncodeQwenImage21, ModelAttentionBackend, SamplerCustomAdvanced, RandomNoise, CFGGuider, KSamplerSelect, BasicScheduler, easy cleanGpuUsed, PrimitiveStringMultiline, PrimitiveBoolean, Seed (rgthree), GetImageSizeAndCount, ResizeImageMaskNode, VOSR2ModelLoader, VOSR2Upscale, Images to RGB, Reroute, Reroute, Reroute, Reroute, Reroute, easy cleanGpuUsed, ResizeImageMaskNode, Reroute, Reroute, StringConcatenate, SeedVR2LoadVAEModel, PreviewImage, SeedVR2LoadDiTModel, easy cleanGpuUsed, PrimitiveStringMultiline, PrimitiveStringMultiline, PrimitiveStringMultiline, ComfySwitchNode, StringConcatenate, TextGenerate, TextGenerate, UNETLoader, CLIPLoader, VAELoader, Reroute, Reroute, ShowText|pysssss, Image Comparer (rgthree), Reroute, Reroute, Image Comparer (rgthree), PreviewImage, SaveImage, ComfyOrNode, ComfySwitchNode, EmptyLatentImage, LoadImage, ImageResizeKJv2, ImageScaleToMaxDimension, easy cleanGpuUsed, SeedVR2VideoUpscaler, Reroute, easy cleanGpuUsed, INTConstant, JsonExtractString, PrimitiveStringMultiline, PrimitiveBoolean, CLIPLoader, CLIPLoader]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/文生图/图片编辑-QwenImage2.1_2101963695487283202.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图片编辑-QwenImage2.1_2101963695487283202.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `TextEncodeQwenImage21`
- `ModelAttentionBackend`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `easy cleanGpuUsed`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `Seed (rgthree)`
- `GetImageSizeAndCount`
- `ResizeImageMaskNode`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `Images to RGB`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy cleanGpuUsed`
- `ResizeImageMaskNode`
- `Reroute`
- `Reroute`
- `StringConcatenate`
- `SeedVR2LoadVAEModel`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `easy cleanGpuUsed`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `StringConcatenate`
- `TextGenerate`
- `TextGenerate`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Reroute`
- `Reroute`
- `ShowText|pysssss`
- `Image Comparer (rgthree)`
- `Reroute`
- `Reroute`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `SaveImage`
- `ComfyOrNode`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `ImageResizeKJv2`
- `ImageScaleToMaxDimension`
- `easy cleanGpuUsed`
- `SeedVR2VideoUpscaler`
- `Reroute`
- `easy cleanGpuUsed`
- `INTConstant`
- `JsonExtractString`
- `PrimitiveStringMultiline`
- `PrimitiveBoolean`
- `CLIPLoader`
- `CLIPLoader`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **65%**（44/68）

**有卡**：`QwenImage21Cache`、`VAEDecode`、`ResolutionSelector`、`TextEncodeQwenImage21`、`ModelAttentionBackend`、`SamplerCustomAdvanced`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`easy cleanGpuUsed`、`PrimitiveBoolean`、`Seed (rgthree)`、`GetImageSizeAndCount`、`ResizeImageMaskNode`、`VOSR2ModelLoader`、`VOSR2Upscale`、`Images to RGB`、`StringConcatenate`、`SeedVR2LoadVAEModel`、`SeedVR2LoadDiTModel`、`TextGenerate`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`SaveImage`、`ComfyOrNode`、`EmptyLatentImage`、`LoadImage`、`ImageResizeKJv2`、`ImageScaleToMaxDimension`、`SeedVR2VideoUpscaler`、`INTConstant`、`JsonExtractString`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage、QwenImage21Cache
