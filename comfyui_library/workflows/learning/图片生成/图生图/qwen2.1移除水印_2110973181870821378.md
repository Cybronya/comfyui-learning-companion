---
key: 图片生成/图生图/qwen2.1移除水印_2110973181870821378.json
name: qwen2.1移除水印_2110973181870821378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1移除水印_2110973181870821378.json
hash: eaca5ff42508953e
coverage: 0.928571
learned_at: 2026-10-23 11:43:01
nodes: [CLIPLoader, TextEncodeQwenImage21, CR Prompt Text, KSamplerAdvanced, UpscaleModelLoader, ImageScaleToTotalPixels, ImageUpscaleWithModel, LoraLoaderModelOnly, VAEDecode, LoadImage, SaveImage, Image Comparer (rgthree), UNETLoader, VAELoader]
patterns: []
missing: []
parameters: {"cfg": 40, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "fixed"}
---

# 图片生成/图生图/qwen2.1移除水印_2110973181870821378.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1移除水印_2110973181870821378.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CLIPLoader`
- `TextEncodeQwenImage21`
- `CR Prompt Text`
- `KSamplerAdvanced` ★核心
- `UpscaleModelLoader`
- `ImageScaleToTotalPixels`
- `ImageUpscaleWithModel`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `LoadImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `VAELoader`

## 关键参数

- `seed` = `enable`
- `steps` = `fixed`
- `cfg` = `40`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`CLIPLoader`、`TextEncodeQwenImage21`、`CR Prompt Text`、`KSamplerAdvanced`、`UpscaleModelLoader`、`ImageScaleToTotalPixels`、`ImageUpscaleWithModel`、`LoraLoaderModelOnly`、`VAEDecode`、`LoadImage`、`SaveImage`、`UNETLoader`、`VAELoader`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、KSamplerAdvanced
