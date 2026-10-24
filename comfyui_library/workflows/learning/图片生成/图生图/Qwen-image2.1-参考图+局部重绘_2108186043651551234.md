---
key: 图片生成/图生图/Qwen-image2.1-参考图+局部重绘_2108186043651551234.json
name: Qwen-image2.1-参考图+局部重绘_2108186043651551234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-参考图+局部重绘_2108186043651551234.json
hash: 242cd707adc146fd
coverage: 0.896552
learned_at: 2026-10-23 11:18:26
nodes: [SaveImage, Mask Fill Holes, InpaintModelConditioning, VAEDecode, Image Comparer (rgthree), KSampler, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImage21, LoadImage, UNETLoader, CLIPLoader, VAELoader, KSampler, VAEDecode, Image Comparer (rgthree), CLIPLoader, TextEncodeQwenImage21, KSampler, VAELoader, UNETLoader, Mask Fill Holes, LayerUtility: ImageScaleByAspectRatio V2, InpaintModelConditioning, LoadImage, LoadImage, TextEncodeQwenImage21, Image Comparer (rgthree), VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 55631978567268, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-参考图+局部重绘_2108186043651551234.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-参考图+局部重绘_2108186043651551234.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `SaveImage`
- `Mask Fill Holes`
- `InpaintModelConditioning`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImage21`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `Mask Fill Holes`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `InpaintModelConditioning`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `55631978567268`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`SaveImage`、`Mask Fill Holes`、`InpaintModelConditioning`、`VAEDecode`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImage21`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、InpaintModelConditioning
