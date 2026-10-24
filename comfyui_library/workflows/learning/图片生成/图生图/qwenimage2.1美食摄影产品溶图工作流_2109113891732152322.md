---
key: 图片生成/图生图/qwenimage2.1美食摄影产品溶图工作流_2109113891732152322.json
name: qwenimage2.1美食摄影产品溶图工作流_2109113891732152322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwenimage2.1美食摄影产品溶图工作流_2109113891732152322.json
hash: f71cf403f8506ecb
coverage: 0.8
learned_at: 2026-10-23 11:44:20
nodes: [ImageCropper, CLIPLoader, TTP_Expand_And_Mask, TextEncodeQwenImage21, FastCanvasTool, CR Prompt Text, PreviewImage, InspyrenetRembg, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleToTotalPixels, Image Comparer (rgthree), UNETLoader, LoraLoaderModelOnly, VAELoader, LoadImage, LoadImage, PreviewImage, FastCanvas, LoadImage, Note, Note, VAEDecode, SaveImage, KSamplerAdvanced]
patterns: []
missing: []
parameters: {"cfg": 40, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/qwenimage2.1美食摄影产品溶图工作流_2109113891732152322.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwenimage2.1美食摄影产品溶图工作流_2109113891732152322.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `ImageCropper`
- `CLIPLoader`
- `TTP_Expand_And_Mask`
- `TextEncodeQwenImage21`
- `FastCanvasTool`
- `CR Prompt Text`
- `PreviewImage`
- `InspyrenetRembg`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScaleToTotalPixels`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `FastCanvas`
- `LoadImage`
- `Note`
- `Note`
- `VAEDecode` ★核心
- `SaveImage`
- `KSamplerAdvanced` ★核心

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `40`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **80%**（20/25）

**有卡**：`ImageCropper`、`CLIPLoader`、`TTP_Expand_And_Mask`、`TextEncodeQwenImage21`、`FastCanvasTool`、`CR Prompt Text`、`InspyrenetRembg`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`UNETLoader`、`LoraLoaderModelOnly`、`VAELoader`、`LoadImage`、`FastCanvas`、`VAEDecode`、`SaveImage`、`KSamplerAdvanced`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
