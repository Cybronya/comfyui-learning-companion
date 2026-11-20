---
key: 平台全量/qwen-image2.1一键抠图_2117504818246934529.json
name: qwen-image2.1一键抠图_2117504818246934529
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen-image2.1一键抠图_2117504818246934529.json
hash: 7b707b2991f8649c
coverage: 0.9375
learned_at: 2026-11-14 01:16:25
nodes: [UNETLoader, CLIPLoader, VAELoader, CFGGuider, RandomNoise, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, VAEDecode, SaveImage, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, Image Comparer (rgthree), TextEncodeQwenImage21, GetImageSize, EmptyLatentImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 平台全量/qwen-image2.1一键抠图_2117504818246934529.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen-image2.1一键抠图_2117504818246934529.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGGuider`
- `RandomNoise`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `GetImageSize`
- `EmptyLatentImage` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGGuider`、`RandomNoise`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`SaveImage`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImage21`、`GetImageSize`、`EmptyLatentImage`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、UNETLoader、CFGGuider
