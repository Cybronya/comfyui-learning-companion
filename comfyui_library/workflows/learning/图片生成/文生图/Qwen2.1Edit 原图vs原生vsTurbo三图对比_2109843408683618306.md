---
key: 图片生成/文生图/Qwen2.1Edit 原图vs原生vsTurbo三图对比_2109843408683618306.json
name: Qwen2.1Edit 原图vs原生vsTurbo三图对比_2109843408683618306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1Edit 原图vs原生vsTurbo三图对比_2109843408683618306.json
hash: 8e25ae8c57c4333c
coverage: 0.892857
learned_at: 2026-10-21 02:54:42
nodes: [UNETLoader, CLIPLoader, VAELoader, INTConstant, INTConstant, StringConstantMultiline, ImageResizeKJv2, TextEncodeQwenImage21, UNETLoader, KSampler, VAEDecode, SaveImage, AddLabel, ManualSigmas, KSamplerSelect, VAEDecode, SaveImage, AddLabel, AddLabel, ImageConcatMulti, SaveImage, Image Comparer (rgthree), Image Comparer (rgthree), Note, INTConstant, SamplerCustom, LoadImage, LayerUtility: ImageRemoveAlpha]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 20261011, "steps": 40}
---

# 图片生成/文生图/Qwen2.1Edit 原图vs原生vsTurbo三图对比_2109843408683618306.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1Edit 原图vs原生vsTurbo三图对比_2109843408683618306.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（28 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `INTConstant`
- `INTConstant`
- `StringConstantMultiline`
- `ImageResizeKJv2`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `AddLabel`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `Note`
- `INTConstant`
- `SamplerCustom` ★核心
- `LoadImage`
- `LayerUtility: ImageRemoveAlpha`

## 关键参数

- `seed` = `20261011`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（25/28）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`INTConstant`、`StringConstantMultiline`、`ImageResizeKJv2`、`TextEncodeQwenImage21`、`KSampler`、`VAEDecode`、`SaveImage`、`AddLabel`、`ManualSigmas`、`KSamplerSelect`、`ImageConcatMulti`、`SamplerCustom`、`LoadImage`、`LayerUtility: ImageRemoveAlpha`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect
