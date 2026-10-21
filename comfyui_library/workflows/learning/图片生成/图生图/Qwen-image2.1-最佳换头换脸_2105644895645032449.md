---
key: 图片生成/图生图/Qwen-image2.1-最佳换头换脸_2105644895645032449.json
name: Qwen-image2.1-最佳换头换脸_2105644895645032449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-最佳换头换脸_2105644895645032449.json
hash: 425b62532c086c0a
coverage: 0.923077
learned_at: 2026-10-21 00:43:27
nodes: [LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, PreviewImage, VAELoader, KSampler, CLIPLoader, UNETLoader, TextEncodeQwenImage21, SaveImage, LoraLoaderModelOnly, CR Prompt Text, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 559547218310275, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-最佳换头换脸_2105644895645032449.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-最佳换头换脸_2105644895645032449.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `PreviewImage`
- `VAELoader`
- `KSampler` ★核心
- `CLIPLoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `559547218310275`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`VAELoader`、`KSampler`、`CLIPLoader`、`UNETLoader`、`TextEncodeQwenImage21`、`SaveImage`、`LoraLoaderModelOnly`、`CR Prompt Text`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
