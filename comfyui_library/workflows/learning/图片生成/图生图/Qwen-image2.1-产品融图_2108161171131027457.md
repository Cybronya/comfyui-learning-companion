---
key: 图片生成/图生图/Qwen-image2.1-产品融图_2108161171131027457.json
name: Qwen-image2.1-产品融图_2108161171131027457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-产品融图_2108161171131027457.json
hash: 7c6f6f2947e4c27a
coverage: 0.933333
learned_at: 2026-10-21 00:43:25
nodes: [Image Comparer (rgthree), UNETLoader, CLIPLoader, VAEDecode, SaveImage, VAELoader, LoraLoaderModelOnly, KSampler, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, TextEncodeQwenImage21, FastCanvas, LoadImage, InspyrenetRembg, FastCanvasTool]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 842521063773959, "steps": 25}
---

# 图片生成/图生图/Qwen-image2.1-产品融图_2108161171131027457.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-image2.1-产品融图_2108161171131027457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（15 个）：
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecode` ★核心
- `SaveImage`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `TextEncodeQwenImage21`
- `FastCanvas`
- `LoadImage`
- `InspyrenetRembg`
- `FastCanvasTool`

## 关键参数

- `seed` = `842521063773959`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（14/15）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAEDecode`、`SaveImage`、`VAELoader`、`LoraLoaderModelOnly`、`KSampler`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`TextEncodeQwenImage21`、`FastCanvas`、`InspyrenetRembg`、`FastCanvasTool`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader
