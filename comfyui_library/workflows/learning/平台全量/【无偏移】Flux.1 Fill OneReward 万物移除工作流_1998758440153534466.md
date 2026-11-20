---
key: 平台全量/【无偏移】Flux.1 Fill OneReward 万物移除工作流_1998758440153534466.json
name: 【无偏移】Flux.1 Fill OneReward 万物移除工作流_1998758440153534466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【无偏移】Flux.1 Fill OneReward 万物移除工作流_1998758440153534466.json
hash: 4a70605e45f42e16
coverage: 0.833333
learned_at: 2026-11-14 01:24:21
nodes: [Image Comparer (rgthree), ToBinaryMask, Mask Fill Holes, SaveImage, PreviewImage, ImpactInt, 孤海图像缩放按像素, UNETLoader, LoraLoaderModelOnly, DualCLIPLoader, VAELoader, LayerUtility: RestoreCropBox, LayerUtility: CropByMask V2, LayerMask: MaskPreview, LayerMask: MaskPreview, DifferentialDiffusion, LayerMask: MaskGrow, GrowMaskWithBlur, PreviewImage, VAEDecode, KSamplerAdvanced, ConditioningZeroOut, CLIPTextEncode, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, Note, InpaintModelConditioning, PreviewImage, FluxGuidance]
patterns: []
missing: []
parameters: {"cfg": 8, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 平台全量/【无偏移】Flux.1 Fill OneReward 万物移除工作流_1998758440153534466.json

> 来源文件 `comfyui_library/workflows/平台全量/【无偏移】Flux.1 Fill OneReward 万物移除工作流_1998758440153534466.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（30 个）：
- `Image Comparer (rgthree)`
- `ToBinaryMask`
- `Mask Fill Holes`
- `SaveImage`
- `PreviewImage`
- `ImpactInt`
- `孤海图像缩放按像素`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `LayerUtility: RestoreCropBox`
- `LayerUtility: CropByMask V2`
- `LayerMask: MaskPreview`
- `LayerMask: MaskPreview`
- `DifferentialDiffusion`
- `LayerMask: MaskGrow`
- `GrowMaskWithBlur`
- `PreviewImage`
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`
- `InpaintModelConditioning`
- `PreviewImage`
- `FluxGuidance`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `8`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（25/30）

**有卡**：`ToBinaryMask`、`Mask Fill Holes`、`SaveImage`、`ImpactInt`、`孤海图像缩放按像素`、`UNETLoader`、`LoraLoaderModelOnly`、`DualCLIPLoader`、`VAELoader`、`LayerUtility: RestoreCropBox`、`LayerUtility: CropByMask V2`、`LayerMask: MaskPreview`、`DifferentialDiffusion`、`LayerMask: MaskGrow`、`GrowMaskWithBlur`、`VAEDecode`、`KSamplerAdvanced`、`ConditioningZeroOut`、`CLIPTextEncode`、`LoadImage`、`InpaintModelConditioning`、`FluxGuidance`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
