---
key: 平台全量/qwen image 2.1 溶图_2106220761554968578.json
name: qwen image 2.1 溶图_2106220761554968578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen image 2.1 溶图_2106220761554968578.json
hash: 2dc2389b3017eb6d
coverage: 0.947368
learned_at: 2026-11-14 01:16:00
nodes: [CLIPLoader, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, KSampler, LoraLoaderModelOnly, VAELoader, UNETLoader, Label (rgthree), DF_Text_Box, QwenImage21BlockCacheT8, VAEDecode, TextEncodeQwenImage21GH, LoadImage, Image Comparer (rgthree), DetailTransfer, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, SaveImage, LayerUtility: ImageRemoveAlpha]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 475591575762091, "steps": 30}
---

# 平台全量/qwen image 2.1 溶图_2106220761554968578.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen image 2.1 溶图_2106220761554968578.json`

## 结构

**生成流程**：Model → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `CLIPLoader`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `Label (rgthree)`
- `DF_Text_Box`
- `QwenImage21BlockCacheT8`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21GH`
- `LoadImage`
- `Image Comparer (rgthree)`
- `DetailTransfer`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SaveImage`
- `LayerUtility: ImageRemoveAlpha`

## 关键参数

- `seed` = `475591575762091`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`CLIPLoader`、`QwenImage21SageAttentionT8`、`QwenImage21SpectrumT8`、`KSampler`、`LoraLoaderModelOnly`、`VAELoader`、`UNETLoader`、`Label (rgthree)`、`DF_Text_Box`、`QwenImage21BlockCacheT8`、`VAEDecode`、`TextEncodeQwenImage21GH`、`LoadImage`、`DetailTransfer`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerUtility: ImageRemoveAlpha`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、TextEncodeQwenImage21GH
