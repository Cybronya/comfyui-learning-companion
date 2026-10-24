---
key: 图片生成/图生图/人物环境质感提升+脸部修复—fluxs-srpo+wan2.2_1987070189932097537.json
name: 人物环境质感提升+脸部修复—fluxs-srpo+wan2.2_1987070189932097537
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/人物环境质感提升+脸部修复—fluxs-srpo+wan2.2_1987070189932097537.json
hash: 460c5bac7bc71291
coverage: 0.595238
learned_at: 2026-10-23 12:11:05
nodes: [VAELoader, DualCLIPLoader, VAEDecode, SetNode, CFGZeroStarAndInit, VAELoader, FluxGuidance, ImageUpscaleWithModel, ImageScaleBy, GetNode, Reroute, Reroute, UNETLoader, ConditioningZeroOut, VAEEncode, Reroute, Reroute, VAEEncode, DrawMaskOnImage, VAEDecode, SeCVideoSegmentation, ColorMatch, SeCModelLoader, GrowMaskWithBlur, LayerMask: SegmentAnythingUltra V3, PreviewImage, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UpscaleModelLoader, GetNode, LayerUtility: CropByMask, GetNode, SaveImage, LayerUtility: RestoreCropBox, GetNode, PreviewImage, LayerMask: LoadSegmentAnythingModels, GetNode, RH_Translator, ImageResizeKJ, SetNode, Image Comparer (rgthree), SetNode, SetNode, SaveImage, GetNode, GrowMaskWithBlur, AddMask, ImpactSwitch, PreviewImage, CLIPTextEncode, Note, CLIPLoader, PathchSageAttentionKJ, ModelSamplingSD3, PreviewImage, LayerUtility: ImageScaleByAspectRatio, CLIPTextEncode, GetNode, GetNode, SetNode, CLIPTextEncode, GetNode, GetNode, easy showAnything, AILab_QwenVL, LoadImage, PreviewImage, DrawMaskOnImage, SeCVideoSegmentation, LayerMask: SegmentAnythingUltra V3, RH_Translator, Image Comparer (rgthree), JWStringToFloat, JWStringToFloat, Note, KSampler, Note, Note, KSampler, Note, SetNode]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "beta", "seed": 355380877724972, "steps": 10}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/人物环境质感提升+脸部修复—fluxs-srpo+wan2.2_1987070189932097537.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/人物环境质感提升+脸部修复—fluxs-srpo+wan2.2_1987070189932097537.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（84 个）：
- `VAELoader`
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `SetNode`
- `CFGZeroStarAndInit`
- `VAELoader`
- `FluxGuidance`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `GetNode`
- `Reroute`
- `Reroute`
- `UNETLoader` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `Reroute`
- `Reroute`
- `VAEEncode` ★核心
- `DrawMaskOnImage`
- `VAEDecode` ★核心
- `SeCVideoSegmentation`
- `ColorMatch`
- `SeCModelLoader`
- `GrowMaskWithBlur`
- `LayerMask: SegmentAnythingUltra V3`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UpscaleModelLoader`
- `GetNode`
- `LayerUtility: CropByMask`
- `GetNode`
- `SaveImage`
- `LayerUtility: RestoreCropBox`
- `GetNode`
- `PreviewImage`
- `LayerMask: LoadSegmentAnythingModels`
- `GetNode`
- `RH_Translator`
- `ImageResizeKJ`
- `SetNode`
- `Image Comparer (rgthree)`
- `SetNode`
- `SetNode`
- `SaveImage`
- `GetNode`
- `GrowMaskWithBlur`
- `AddMask`
- `ImpactSwitch`
- `PreviewImage`
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPLoader`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPTextEncode` ★核心
- `GetNode`
- `GetNode`
- `easy showAnything`
- `AILab_QwenVL`
- `LoadImage`
- `PreviewImage`
- `DrawMaskOnImage`
- `SeCVideoSegmentation`
- `LayerMask: SegmentAnythingUltra V3`
- `RH_Translator`
- `Image Comparer (rgthree)`
- `JWStringToFloat`
- `JWStringToFloat`
- `Note`
- `KSampler` ★核心
- `Note`
- `Note`
- `KSampler` ★核心
- `Note`
- `SetNode`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `355380877724972`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **60%**（50/84）

**有卡**：`VAELoader`、`DualCLIPLoader`、`VAEDecode`、`CFGZeroStarAndInit`、`FluxGuidance`、`ImageUpscaleWithModel`、`ImageScaleBy`、`UNETLoader`、`ConditioningZeroOut`、`VAEEncode`、`DrawMaskOnImage`、`SeCVideoSegmentation`、`ColorMatch`、`SeCModelLoader`、`GrowMaskWithBlur`、`LayerMask: SegmentAnythingUltra V3`、`LoraLoaderModelOnly`、`UpscaleModelLoader`、`LayerUtility: CropByMask`、`SaveImage`、`LayerUtility: RestoreCropBox`、`LayerMask: LoadSegmentAnythingModels`、`RH_Translator`、`ImageResizeKJ`、`AddMask`、`CLIPTextEncode`、`CLIPLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`LayerUtility: ImageScaleByAspectRatio`、`AILab_QwenVL`、`LoadImage`、`JWStringToFloat`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
