---
key: 图片生成/图生图/局部重绘Flux-Fill最强局部重绘-OneReward-Fill1.0_1985568936228016129.json
name: 局部重绘Flux-Fill最强局部重绘-OneReward-Fill1.0_1985568936228016129
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/局部重绘Flux-Fill最强局部重绘-OneReward-Fill1.0_1985568936228016129.json
hash: b148ee7ada88f9c0
coverage: 0.896552
learned_at: 2026-10-23 12:49:59
nodes: [DualCLIPLoader, FluxGuidance, LayerMask: MaskGrow, GrowMaskWithBlur, VAEDecode, ColorCorrect, InpaintModelConditioning, LayerUtility: RestoreCropBox, ConditioningZeroOut, Mask Fill Holes, ToBinaryMask, easy ifElse, VAELoader, easy boolean, KSampler, LayerUtility: ImageScaleByAspectRatio V2, ImpactInt, DifferentialDiffusion, UNETLoader, SaveImage, LoadImage, LayerUtility: CropByMask V2, CR Text, LoraLoader, CLIPTextEncode, DeepTranslatorTextNode, LoadImage, Note, Image Comparer (rgthree)]
patterns: [lora]
missing: []
parameters: {"cfg": 1, "denoise": 1, "lora_name": "20251018-89931609.safetensors", "sampler_name": "er_sde", "scheduler": "simple", "seed": 534930348728887, "steps": 30, "strength_clip": 1, "strength_model": 1}
---

# 图片生成/图生图/局部重绘Flux-Fill最强局部重绘-OneReward-Fill1.0_1985568936228016129.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/局部重绘Flux-Fill最强局部重绘-OneReward-Fill1.0_1985568936228016129.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `DualCLIPLoader`
- `FluxGuidance`
- `LayerMask: MaskGrow`
- `GrowMaskWithBlur`
- `VAEDecode` ★核心
- `ColorCorrect`
- `InpaintModelConditioning`
- `LayerUtility: RestoreCropBox`
- `ConditioningZeroOut`
- `Mask Fill Holes`
- `ToBinaryMask`
- `easy ifElse`
- `VAELoader`
- `easy boolean`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImpactInt`
- `DifferentialDiffusion`
- `UNETLoader` ★核心
- `SaveImage`
- `LoadImage`
- `LayerUtility: CropByMask V2`
- `CR Text`
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `DeepTranslatorTextNode`
- `LoadImage`
- `Note`
- `Image Comparer (rgthree)`

**识别到的模式**：lora

## 关键参数

- `seed` = `534930348728887`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `er_sde`
- `scheduler` = `simple`
- `denoise` = `1`
- `lora_name` = `20251018-89931609.safetensors`
- `strength_model` = `1`
- `strength_clip` = `1`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`DualCLIPLoader`、`FluxGuidance`、`LayerMask: MaskGrow`、`GrowMaskWithBlur`、`VAEDecode`、`ColorCorrect`、`InpaintModelConditioning`、`LayerUtility: RestoreCropBox`、`ConditioningZeroOut`、`Mask Fill Holes`、`ToBinaryMask`、`VAELoader`、`easy boolean`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImpactInt`、`DifferentialDiffusion`、`UNETLoader`、`SaveImage`、`LoadImage`、`LayerUtility: CropByMask V2`、`CR Text`、`LoraLoader`、`CLIPTextEncode`、`DeepTranslatorTextNode`

**用到的条目**：KSampler、VAEDecode、VAELoader、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、FluxGuidance
