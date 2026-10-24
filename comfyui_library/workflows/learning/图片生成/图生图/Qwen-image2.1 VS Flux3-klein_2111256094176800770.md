---
key: 图片生成/图生图/Qwen-image2.1 VS Flux3-klein_2111256094176800770.json
name: Qwen-image2.1 VS Flux3-klein_2111256094176800770
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1 VS Flux3-klein_2111256094176800770.json
hash: 4fb834828cc27e66
coverage: 0.923077
learned_at: 2026-10-23 11:18:19
nodes: [VAELoader, CLIPLoader, UNETLoader, CLIPLoader, VAEDecode, PreviewImage, KSampler, KSampler, CLIPTextEncode, ReferenceMultiLatent, VAELoader, TextEncodeQwenImage21, PreviewImage, AddLabel, AddLabel, LayerUtility: ImageScaleByAspectRatio V2, AddLabel, AddLabel, LoadImage, CR Prompt Text, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, ImageConcatMulti, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 148123286242585, "steps": 16}
---

# 图片生成/图生图/Qwen-image2.1 VS Flux3-klein_2111256094176800770.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1 VS Flux3-klein_2111256094176800770.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `PreviewImage`
- `KSampler` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceMultiLatent`
- `VAELoader`
- `TextEncodeQwenImage21`
- `PreviewImage`
- `AddLabel`
- `AddLabel`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `AddLabel`
- `AddLabel`
- `LoadImage`
- `CR Prompt Text`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `ImageConcatMulti`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `148123286242585`
- `steps` = `16`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（24/26）

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`VAEDecode`、`KSampler`、`CLIPTextEncode`、`ReferenceMultiLatent`、`TextEncodeQwenImage21`、`AddLabel`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`CR Prompt Text`、`ImageConcatMulti`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader
