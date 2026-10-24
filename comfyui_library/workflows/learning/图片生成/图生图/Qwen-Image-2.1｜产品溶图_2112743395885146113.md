---
key: 图片生成/图生图/Qwen-Image-2.1｜产品溶图_2112743395885146113.json
name: Qwen-Image-2.1｜产品溶图_2112743395885146113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1｜产品溶图_2112743395885146113.json
hash: a0eefbdbf137de18
coverage: 0.933333
learned_at: 2026-10-23 11:16:33
nodes: [ImageUpscaleWithModel, LoadImage, UpscaleModelLoader, UNETLoader, LoraLoaderModelOnly, KSamplerAdvanced, VAEDecode, SaveImage, Image Comparer (rgthree), SaveImageAdvanced, TextEncodeQwenImage21, CLIPLoader, ImageScaleToTotalPixels, VAELoader, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 40, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/Qwen-Image-2.1｜产品溶图_2112743395885146113.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1｜产品溶图_2112743395885146113.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `ImageUpscaleWithModel`
- `LoadImage`
- `UpscaleModelLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `SaveImageAdvanced`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `VAELoader`
- `CR Prompt Text`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `40`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`ImageUpscaleWithModel`、`LoadImage`、`UpscaleModelLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`KSamplerAdvanced`、`VAEDecode`、`SaveImage`、`SaveImageAdvanced`、`TextEncodeQwenImage21`、`CLIPLoader`、`ImageScaleToTotalPixels`、`VAELoader`、`CR Prompt Text`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
