---
key: 平台全量/Anima-aesthetic-v1.1-局部重绘_2078551615627423745.json
name: Anima-aesthetic-v1.1-局部重绘_2078551615627423745
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Anima-aesthetic-v1.1-局部重绘_2078551615627423745.json
hash: c0f025b1e18ec15b
coverage: 1
learned_at: 2026-11-14 00:17:51
nodes: [CLIPTextEncode, UNETLoader, SetLatentNoiseMask, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, MaskFillHoles, VAEEncode, SaveImage, VAEDecode, KSampler, CLIPLoader, VAELoader, AnimaLLLiteApply, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4.5, "denoise": 1, "sampler_name": "er_sde", "scheduler": "beta", "seed": 41371318362260, "steps": 40}
---

# 平台全量/Anima-aesthetic-v1.1-局部重绘_2078551615627423745.json

> 来源文件 `comfyui_library/workflows/平台全量/Anima-aesthetic-v1.1-局部重绘_2078551615627423745.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `SetLatentNoiseMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `MaskFillHoles`
- `VAEEncode` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `VAELoader`
- `AnimaLLLiteApply`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `41371318362260`
- `steps` = `40`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`SetLatentNoiseMask`、`LayerUtility: ImageScaleByAspectRatio V2`、`MaskFillHoles`、`VAEEncode`、`SaveImage`、`VAEDecode`、`KSampler`、`CLIPLoader`、`VAELoader`、`AnimaLLLiteApply`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、LoadImage、UNETLoader、SetLatentNoiseMask
