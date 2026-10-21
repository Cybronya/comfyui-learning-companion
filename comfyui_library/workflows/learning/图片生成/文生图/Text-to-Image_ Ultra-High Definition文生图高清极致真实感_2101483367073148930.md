---
key: 图片生成/文生图/Text-to-Image_ Ultra-High Definition文生图高清极致真实感_2101483367073148930.json
name: Text-to-Image_ Ultra-High Definition文生图高清极致真实感_2101483367073148930
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Text-to-Image_ Ultra-High Definition文生图高清极致真实感_2101483367073148930.json
hash: ab1492837b012b74
coverage: 0.725
learned_at: 2026-10-20 01:51:31
nodes: [MarkdownNote, UNETLoader, PrimitiveStringMultiline, StringConcatenate, TextGenerate, PreviewAny, CLIPTextEncode, ConditioningZeroOut, KSampler, EmptyLatentImage, LoraLoaderModelOnly, VAELoader, CLIPLoader, MarkdownNote, VAEDecode, SetNode, SeedVR2LoadVAEModel, ImageResize+, ImageScaleBy, ImageResize+, easy cleanGpuUsed, TTP_Image_Tile_Batch, ImageScaleBy, easy imageSize, easy imageSize, SeedVR2VideoUpscaler, TTP_Tile_image_size, SeedVR2LoadDiTModel, ResolutionSelector, MarkdownNote, SaveImage, SaveImage, GetNode, TTP_Image_Assy, Image Comparer (rgthree), LoadImage, RH_Captioner, PreviewAny, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 310932417485714, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Text-to-Image_ Ultra-High Definition文生图高清极致真实感_2101483367073148930.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Text-to-Image_ Ultra-High Definition文生图高清极致真实感_2101483367073148930.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `MarkdownNote`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `StringConcatenate`
- `TextGenerate`
- `PreviewAny`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `CLIPLoader`
- `MarkdownNote`
- `VAEDecode` ★核心
- `SetNode`
- `SeedVR2LoadVAEModel`
- `ImageResize+`
- `ImageScaleBy`
- `ImageResize+`
- `easy cleanGpuUsed`
- `TTP_Image_Tile_Batch`
- `ImageScaleBy`
- `easy imageSize`
- `easy imageSize`
- `SeedVR2VideoUpscaler`
- `TTP_Tile_image_size`
- `SeedVR2LoadDiTModel`
- `ResolutionSelector`
- `MarkdownNote`
- `SaveImage`
- `SaveImage`
- `GetNode`
- `TTP_Image_Assy`
- `Image Comparer (rgthree)`
- `LoadImage`
- `RH_Captioner`
- `PreviewAny`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `310932417485714`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **72%**（29/40）

**有卡**：`UNETLoader`、`StringConcatenate`、`TextGenerate`、`CLIPTextEncode`、`ConditioningZeroOut`、`KSampler`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`VAELoader`、`CLIPLoader`、`VAEDecode`、`SeedVR2LoadVAEModel`、`ImageResize+`、`ImageScaleBy`、`easy cleanGpuUsed`、`TTP_Image_Tile_Batch`、`easy imageSize`、`SeedVR2VideoUpscaler`、`TTP_Tile_image_size`、`SeedVR2LoadDiTModel`、`ResolutionSelector`、`SaveImage`、`TTP_Image_Assy`、`LoadImage`、`RH_Captioner`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
