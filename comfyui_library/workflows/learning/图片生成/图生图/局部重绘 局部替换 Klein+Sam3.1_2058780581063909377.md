---
key: 图片生成/图生图/局部重绘 局部替换 Klein+Sam3.1_2058780581063909377.json
name: 局部重绘 局部替换 Klein+Sam3.1_2058780581063909377
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/局部重绘 局部替换 Klein+Sam3.1_2058780581063909377.json
hash: e979a750ffb0ca4d
coverage: 0.828571
learned_at: 2026-10-23 12:49:48
nodes: [VAEDecode, VAELoader, CLIPLoader, KSampler, LayerUtility: PurgeVRAM V2, PreviewImage, CLIPTextEncode, PreviewAny, PreviewAny, VAEEncode, ConditioningZeroOut, ReferenceLatent, CheckpointLoaderSimple, RH_Translator, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, ImageCompositeMasked, RH_Translator, CLIPTextEncode, SeedVR2LoadDiTModel, SeedVR2VideoUpscaler, SeedVR2LoadVAEModel, ReferenceLatent, UNETLoader, SAM3_Detect, InpaintModelConditioning, ImageAndMaskPreview, INPAINT_ExpandMask, LoadImage, Text, Text, Fast Groups Muter (rgthree), SaveImage, Fast Groups Muter (rgthree), SaveImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 774156943689120, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/局部重绘 局部替换 Klein+Sam3.1_2058780581063909377.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/局部重绘 局部替换 Klein+Sam3.1_2058780581063909377.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `PreviewAny`
- `PreviewAny`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `CheckpointLoaderSimple` ★核心
- `RH_Translator`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageCompositeMasked`
- `RH_Translator`
- `CLIPTextEncode` ★核心
- `SeedVR2LoadDiTModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadVAEModel`
- `ReferenceLatent`
- `UNETLoader` ★核心
- `SAM3_Detect`
- `InpaintModelConditioning`
- `ImageAndMaskPreview`
- `INPAINT_ExpandMask`
- `LoadImage`
- `Text`
- `Text`
- `Fast Groups Muter (rgthree)`
- `SaveImage`
- `Fast Groups Muter (rgthree)`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `774156943689120`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **83%**（29/35）

**有卡**：`VAEDecode`、`VAELoader`、`CLIPLoader`、`KSampler`、`LayerUtility: PurgeVRAM V2`、`CLIPTextEncode`、`VAEEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`CheckpointLoaderSimple`、`RH_Translator`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageCompositeMasked`、`SeedVR2LoadDiTModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadVAEModel`、`UNETLoader`、`SAM3_Detect`、`InpaintModelConditioning`、`ImageAndMaskPreview`、`INPAINT_ExpandMask`、`LoadImage`、`Text`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
