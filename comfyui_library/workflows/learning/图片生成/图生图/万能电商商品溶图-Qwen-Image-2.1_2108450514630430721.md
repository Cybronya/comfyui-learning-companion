---
key: 图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1_2108450514630430721.json
name: 万能电商商品溶图-Qwen-Image-2.1_2108450514630430721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1_2108450514630430721.json
hash: 706f6b46eeea6ea3
coverage: 0.84
learned_at: 2026-10-23 12:01:33
nodes: [KSamplerAdvanced, TextEncodeQwenImage21, CLIPLoader, VAELoader, ImageUpscaleWithModel, LoraLoaderModelOnly, ImageScaleToTotalPixels, CR Prompt Text, CR Text Concatenate, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, VAEDecode, UpscaleModelLoader, LayerUtility: ImageScaleByAspectRatio V2, FastCanvasTool, InspyrenetRembg, SaveImage, Image Comparer (rgthree), CR Prompt Text, 孤海注释, 孤海注释, Note, LoadImage, FastCanvas]
patterns: []
missing: []
parameters: {"cfg": 40, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1_2108450514630430721.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1_2108450514630430721.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（25 个）：
- `KSamplerAdvanced` ★核心
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `VAELoader`
- `ImageUpscaleWithModel`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `CR Prompt Text`
- `CR Text Concatenate`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `FastCanvasTool`
- `InspyrenetRembg`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CR Prompt Text`
- `孤海注释`
- `孤海注释`
- `Note`
- `LoadImage`
- `FastCanvas`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `40`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **84%**（21/25）

**有卡**：`KSamplerAdvanced`、`TextEncodeQwenImage21`、`CLIPLoader`、`VAELoader`、`ImageUpscaleWithModel`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`、`CR Prompt Text`、`CR Text Concatenate`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`VAEDecode`、`UpscaleModelLoader`、`FastCanvasTool`、`InspyrenetRembg`、`SaveImage`、`FastCanvas`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
