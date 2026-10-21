---
key: 图片生成/图生图/Flux-2-Kelin_零色差局部重绘二合一(手动蒙板+Sam3.1语义蒙板)_2085185293929504770.json
name: Flux-2-Kelin_零色差局部重绘二合一(手动蒙板+Sam3.1语义蒙板)_2085185293929504770
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Flux-2-Kelin_零色差局部重绘二合一(手动蒙板+Sam3.1语义蒙板)_2085185293929504770.json
hash: 1dd8c2220a0eb119
coverage: 0.870968
learned_at: 2026-10-21 00:39:29
nodes: [ImpactInt, Text, UNETLoader, CLIPLoader, VAELoader, LayerUtility: ImageScaleByAspectRatio V2, PreviewAny, RH_Translator, CLIPTextEncode, VAEEncode, ReferenceLatent, ConditioningZeroOut, ReferenceLatent, InpaintModelConditioning, KSampler, LayerUtility: PurgeVRAM V2, VAEDecode, ImageCompositeMasked, SaveImage, CheckpointLoaderSimple, RH_Translator, MaskFillHoles, INPAINT_ExpandMask, CLIPTextEncode, SAM3_Detect, ImpactSwitch, ImpactInt, Note, LoadImage, Image Comparer (rgthree), Text]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 552289331191871, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Flux-2-Kelin_零色差局部重绘二合一(手动蒙板+Sam3.1语义蒙板)_2085185293929504770.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Flux-2-Kelin_零色差局部重绘二合一(手动蒙板+Sam3.1语义蒙板)_2085185293929504770.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `ImpactInt`
- `Text`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewAny`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `ReferenceLatent`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `InpaintModelConditioning`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `VAEDecode` ★核心
- `ImageCompositeMasked`
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `RH_Translator`
- `MaskFillHoles`
- `INPAINT_ExpandMask`
- `CLIPTextEncode` ★核心
- `SAM3_Detect`
- `ImpactSwitch`
- `ImpactInt`
- `Note`
- `LoadImage`
- `Image Comparer (rgthree)`
- `Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `552289331191871`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`ImpactInt`、`Text`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`RH_Translator`、`CLIPTextEncode`、`VAEEncode`、`ReferenceLatent`、`ConditioningZeroOut`、`InpaintModelConditioning`、`KSampler`、`LayerUtility: PurgeVRAM V2`、`VAEDecode`、`ImageCompositeMasked`、`SaveImage`、`CheckpointLoaderSimple`、`MaskFillHoles`、`INPAINT_ExpandMask`、`SAM3_Detect`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
