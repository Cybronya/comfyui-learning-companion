---
key: 平台全量/Qwen-image 2.1 图片一键去水印_2096414733749538818.json
name: Qwen-image 2.1 图片一键去水印_2096414733749538818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen-image 2.1 图片一键去水印_2096414733749538818.json
hash: 43cef3c648a554dd
coverage: 1
learned_at: 2026-11-14 00:52:03
nodes: [LoadImage, LoadImage, QwenImage21SpectrumT8, UNETLoader, LayerUtility: ImageScaleByAspectRatio V2, QwenImage21SageAttentionT8, DrawMaskOnImage, TextEncodeQwenImage21, SaveImage, KSampler, CLIPLoader, VAELoader, MaskFillHoles, QwenImage21BlockCacheT8, LoadImage, VAEDecode, easy imageColorMatch]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 131842672221476, "steps": 30}
---

# 平台全量/Qwen-image 2.1 图片一键去水印_2096414733749538818.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen-image 2.1 图片一键去水印_2096414733749538818.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `LoadImage`
- `LoadImage`
- `QwenImage21SpectrumT8`
- `UNETLoader` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `QwenImage21SageAttentionT8`
- `DrawMaskOnImage`
- `TextEncodeQwenImage21`
- `SaveImage`
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `MaskFillHoles`
- `QwenImage21BlockCacheT8`
- `LoadImage`
- `VAEDecode` ★核心
- `easy imageColorMatch`

## 关键参数

- `seed` = `131842672221476`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（17/17）

**有卡**：`LoadImage`、`QwenImage21SpectrumT8`、`UNETLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`QwenImage21SageAttentionT8`、`DrawMaskOnImage`、`TextEncodeQwenImage21`、`SaveImage`、`KSampler`、`CLIPLoader`、`VAELoader`、`MaskFillHoles`、`QwenImage21BlockCacheT8`、`VAEDecode`、`easy imageColorMatch`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、SaveImage
