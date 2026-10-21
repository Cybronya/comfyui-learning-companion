---
key: 图片生成/图生图/Qwen-image2.1-万能局部重绘_2108164582689824769.json
name: Qwen-image2.1-万能局部重绘_2108164582689824769
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-万能局部重绘_2108164582689824769.json
hash: 5cec202eebbb2987
coverage: 0.916667
learned_at: 2026-10-21 00:43:24
nodes: [UNETLoader, LoadImage, SaveImage, Mask Fill Holes, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, InpaintModelConditioning, KSampler, VAEDecode, CLIPLoader, TextEncodeQwenImage21, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 299641957731073, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-万能局部重绘_2108164582689824769.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-万能局部重绘_2108164582689824769.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
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
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`

## 关键参数

- `seed` = `299641957731073`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`UNETLoader`、`LoadImage`、`SaveImage`、`Mask Fill Holes`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`InpaintModelConditioning`、`KSampler`、`VAEDecode`、`CLIPLoader`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、InpaintModelConditioning
