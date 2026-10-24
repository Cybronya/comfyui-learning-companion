---
key: 图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1-手动版_2112437243515334657.json
name: 万能电商商品溶图-Qwen-Image-2.1-手动版_2112437243515334657
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1-手动版_2112437243515334657.json
hash: 9ea1a086456f13c5
coverage: 0.833333
learned_at: 2026-10-23 12:01:33
nodes: [KSamplerAdvanced, CLIPLoader, VAELoader, ImageUpscaleWithModel, LoraLoaderModelOnly, ImageScaleToTotalPixels, CR Prompt Text, CR Text Concatenate, UNETLoader, VAEDecode, UpscaleModelLoader, Image Comparer (rgthree), CR Prompt Text, 孤海注释, 孤海注释, SaveImage, LoadImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"cfg": 40, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1-手动版_2112437243515334657.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/万能电商商品溶图-Qwen-Image-2.1-手动版_2112437243515334657.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageUpscaleWithModel`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `CR Prompt Text`
- `CR Text Concatenate`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `UpscaleModelLoader`
- `Image Comparer (rgthree)`
- `CR Prompt Text`
- `孤海注释`
- `孤海注释`
- `SaveImage`
- `LoadImage`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `40`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`KSamplerAdvanced`、`CLIPLoader`、`VAELoader`、`ImageUpscaleWithModel`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`、`CR Prompt Text`、`CR Text Concatenate`、`UNETLoader`、`VAEDecode`、`UpscaleModelLoader`、`SaveImage`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
