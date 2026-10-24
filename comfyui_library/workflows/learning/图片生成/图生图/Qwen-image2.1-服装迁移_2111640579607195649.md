---
key: 图片生成/图生图/Qwen-image2.1-服装迁移_2111640579607195649.json
name: Qwen-image2.1-服装迁移_2111640579607195649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-服装迁移_2111640579607195649.json
hash: 093fb843ccb90f05
coverage: 0.923077
learned_at: 2026-10-23 11:18:27
nodes: [UNETLoader, VAEDecode, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, KSampler, Image Comparer (rgthree), SaveImage, VAELoader, Int, LoraLoaderModelOnly, TextEncodeQwenImage21, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 214979998612474, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-服装迁移_2111640579607195649.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-服装迁移_2111640579607195649.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `SaveImage`
- `VAELoader`
- `Int`
- `LoraLoaderModelOnly` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `214979998612474`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`UNETLoader`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CLIPLoader`、`KSampler`、`SaveImage`、`VAELoader`、`Int`、`LoraLoaderModelOnly`、`TextEncodeQwenImage21`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
