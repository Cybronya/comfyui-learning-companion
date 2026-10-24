---
key: 图片生成/图生图/Qwen-Image-2.1溶图-Viggle加速-V1_2108370950365466626.json
name: Qwen-Image-2.1溶图-Viggle加速-V1_2108370950365466626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1溶图-Viggle加速-V1_2108370950365466626.json
hash: 6f2a0b594ed4c219
coverage: 1
learned_at: 2026-10-23 11:16:30
nodes: [CLIPLoader, VAELoader, UNETLoader, KSamplerAdvanced, LoraLoaderModelOnly, FluxGuidance, VAEDecode, UNETLoader, LoraLoaderModelOnly, KSamplerAdvanced, TextEncodeQwenImage21, CR Prompt Text, ImageUpscaleWithModel, ImageScaleToTotalPixels, UpscaleModelLoader, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 26, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/Qwen-Image-2.1溶图-Viggle加速-V1_2108370950365466626.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1溶图-Viggle加速-V1_2108370950365466626.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `KSamplerAdvanced` ★核心
- `LoraLoaderModelOnly` ★核心
- `FluxGuidance`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerAdvanced` ★核心
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `ImageUpscaleWithModel`
- `ImageScaleToTotalPixels`
- `UpscaleModelLoader`
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `26`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSamplerAdvanced`、`LoraLoaderModelOnly`、`FluxGuidance`、`VAEDecode`、`TextEncodeQwenImage21`、`CR Prompt Text`、`ImageUpscaleWithModel`、`ImageScaleToTotalPixels`、`UpscaleModelLoader`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、FluxGuidance
