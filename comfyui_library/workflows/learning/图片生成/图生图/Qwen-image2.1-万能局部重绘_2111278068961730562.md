---
key: 图片生成/图生图/Qwen-image2.1-万能局部重绘_2111278068961730562.json
name: Qwen-image2.1-万能局部重绘_2111278068961730562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-万能局部重绘_2111278068961730562.json
hash: e183618e4e7fb5e2
coverage: 0.846154
learned_at: 2026-10-23 11:18:24
nodes: [UNETLoader, LoadImage, SaveImage, Mask Fill Holes, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, InpaintModelConditioning, KSampler, VAEDecode, CLIPLoader, Image Comparer (rgthree), TextEncodeQwenImage21, JjkText]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 525433261427328, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-万能局部重绘_2111278068961730562.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-万能局部重绘_2111278068961730562.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `UNETLoader` ★核心
- `LoadImage`
- `SaveImage`
- `Mask Fill Holes`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImage21`
- `JjkText`

## 关键参数

- `seed` = `525433261427328`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **85%**（11/13）

**有卡**：`UNETLoader`、`LoadImage`、`SaveImage`、`Mask Fill Holes`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`InpaintModelConditioning`、`KSampler`、`VAEDecode`、`CLIPLoader`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、InpaintModelConditioning
