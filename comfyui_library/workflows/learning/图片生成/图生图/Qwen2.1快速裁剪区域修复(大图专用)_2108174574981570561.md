---
key: 图片生成/图生图/Qwen2.1快速裁剪区域修复(大图专用)_2108174574981570561.json
name: Qwen2.1快速裁剪区域修复(大图专用)_2108174574981570561
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1快速裁剪区域修复(大图专用)_2108174574981570561.json
hash: 90d7ffedd51ab1ff
coverage: 0.928571
learned_at: 2026-10-21 00:43:40
nodes: [InpaintStitchImproved, VAEDecode, Label (rgthree), InpaintModelConditioning, KSampler, VAELoader, CLIPLoader, InpaintCropImproved, MaskPreview+, SaveImage, LoadImage, Image Comparer (rgthree), UNETLoader, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 49613014137239, "steps": 25}
---

# 图片生成/图生图/Qwen2.1快速裁剪区域修复(大图专用)_2108174574981570561.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1快速裁剪区域修复(大图专用)_2108174574981570561.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（14 个）：
- `InpaintStitchImproved`
- `VAEDecode` ★核心
- `Label (rgthree)`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `InpaintCropImproved`
- `MaskPreview+`
- `SaveImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `49613014137239`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **93%**（13/14）

**有卡**：`InpaintStitchImproved`、`VAEDecode`、`Label (rgthree)`、`InpaintModelConditioning`、`KSampler`、`VAELoader`、`CLIPLoader`、`InpaintCropImproved`、`MaskPreview+`、`SaveImage`、`LoadImage`、`UNETLoader`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、UNETLoader、InpaintModelConditioning
