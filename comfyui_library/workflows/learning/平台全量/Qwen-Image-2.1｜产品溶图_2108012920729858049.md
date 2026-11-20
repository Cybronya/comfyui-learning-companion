---
key: 平台全量/Qwen-Image-2.1｜产品溶图_2108012920729858049.json
name: Qwen-Image-2.1｜产品溶图_2108012920729858049
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-Image-2.1｜产品溶图_2108012920729858049.json
hash: 1063ca71896dd3e0
coverage: 0.933333
learned_at: 2026-11-14 00:51:36
nodes: [ImageUpscaleWithModel, LoadImage, UpscaleModelLoader, UNETLoader, LoraLoaderModelOnly, KSamplerAdvanced, VAEDecode, SaveImage, Image Comparer (rgthree), SaveImageAdvanced, TextEncodeQwenImage21, CLIPLoader, ImageScaleToTotalPixels, VAELoader, CR Prompt Text]
patterns: []
missing: []
parameters: {"cfg": 40, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 平台全量/Qwen-Image-2.1｜产品溶图_2108012920729858049.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-Image-2.1｜产品溶图_2108012920729858049.json`

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

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
