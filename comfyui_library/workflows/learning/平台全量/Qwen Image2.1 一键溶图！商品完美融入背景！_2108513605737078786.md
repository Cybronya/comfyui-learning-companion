---
key: 平台全量/Qwen Image2.1 一键溶图！商品完美融入背景！_2108513605737078786.json
name: Qwen Image2.1 一键溶图！商品完美融入背景！_2108513605737078786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen Image2.1 一键溶图！商品完美融入背景！_2108513605737078786.json
hash: 23c3959987ff0502
coverage: 0.733333
learned_at: 2026-11-14 00:50:18
nodes: [UNETLoader, SetNode, ImageUpscaleWithModel, UpscaleModelLoader, LoadImage, LoraLoaderModelOnly, ImageScaleToTotalPixels, GetNode, GetNode, LoraLoaderModelOnly, AnySwitch, LoraLoaderModelOnly, KSampler (Efficient), CLIPLoader, KSamplerAdvanced, CR Prompt Text, SeedNode, SetNode, GetNode, VAELoader, UNETLoader, TextEncodeQwenImage21, SaveImage, VAEDecode, KSamplerAdvanced, FluxGuidance, Image Comparer (rgthree), 孤海注释, 孤海注释, 忽略多组孤海]
patterns: []
missing: []
parameters: {"cfg": 82, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 平台全量/Qwen Image2.1 一键溶图！商品完美融入背景！_2108513605737078786.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen Image2.1 一键溶图！商品完美融入背景！_2108513605737078786.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `UNETLoader` ★核心
- `SetNode`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `ImageScaleToTotalPixels`
- `GetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `AnySwitch`
- `LoraLoaderModelOnly` ★核心
- `KSampler (Efficient)` ★核心
- `CLIPLoader`
- `KSamplerAdvanced` ★核心
- `CR Prompt Text`
- `SeedNode`
- `SetNode`
- `GetNode`
- `VAELoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `SaveImage`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `FluxGuidance`
- `Image Comparer (rgthree)`
- `孤海注释`
- `孤海注释`
- `忽略多组孤海`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `82`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **73%**（22/30）

**有卡**：`UNETLoader`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`LoadImage`、`LoraLoaderModelOnly`、`ImageScaleToTotalPixels`、`AnySwitch`、`KSampler (Efficient)`、`CLIPLoader`、`KSamplerAdvanced`、`CR Prompt Text`、`SeedNode`、`VAELoader`、`TextEncodeQwenImage21`、`SaveImage`、`VAEDecode`、`FluxGuidance`、`忽略多组孤海`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、FluxGuidance
