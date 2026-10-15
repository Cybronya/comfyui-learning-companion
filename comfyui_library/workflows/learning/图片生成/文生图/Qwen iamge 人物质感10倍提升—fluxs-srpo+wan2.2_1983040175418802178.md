---
key: 图片生成/文生图/Qwen iamge 人物质感10倍提升—fluxs-srpo+wan2.2_1983040175418802178.json
name: Qwen iamge 人物质感10倍提升—fluxs-srpo+wan2.2_1983040175418802178
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen iamge 人物质感10倍提升—fluxs-srpo+wan2.2_1983040175418802178.json
hash: b83bbfa6b6cbbb62
coverage: 0.677419
learned_at: 2026-10-15 22:27:06
nodes: [CLIPLoader, easy cleanGpuUsed, GetNode, ConditioningZeroOut, CLIPTextEncode, EmptyLatentImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, VAELoader, DualCLIPLoader, VAEDecode, UNETLoader, VAELoader, SetNode, SetNode, SaveImage, Image Comparer (rgthree), CFGZeroStarAndInit, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, RH_Translator, VAELoader, CLIPLoader, CLIPTextEncode, FluxGuidance, ImageUpscaleWithModel, GetNode, ImageScaleBy, UpscaleModelLoader, SetNode, GetNode, Reroute, Reroute, UNETLoader, GetNode, CLIPTextEncode, RH_Translator, ConditioningZeroOut, VAEEncode, GetNode, Reroute, Reroute, VAEEncode, PreviewImage, SetNode, CLIPTextEncode, SeCVideoSegmentation, DrawMaskOnImage, GetNode, GetNode, FluxResolutionNode, KSampler, VAEDecode, LayerMask: SegmentAnythingUltra V3, GrowMaskWithBlur, RH_Translator, DrawMaskOnImage, SeCVideoSegmentation, ColorMatch, SeCModelLoader, KSampler, VAEDecode, GrowMaskWithBlur, AddMask, GetNode, LayerMask: SegmentAnythingUltra V3, LayerMask: LoadSegmentAnythingModels, GetNode, SetNode, PreviewImage, ImageResizeKJ, UNETLoader, LoraLoaderModelOnly, LayerUtility: CropByMask, PreviewImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, LayerUtility: RestoreCropBox, ImpactSwitch, PreviewImage, PreviewImage, easy showAnything, CR Text, RH_LLMAPI_NODE, GetNode, Image Comparer (rgthree), SaveImage, LoadImage, LayerUtility: ImageScaleByAspectRatio, PreviewImage]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.20000000000000004, "height": 512, "sampler_name": "euler", "scheduler": "beta", "seed": 1114020293191043, "steps": 10, "width": 512}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen iamge 人物质感10倍提升—fluxs-srpo+wan2.2_1983040175418802178.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen iamge 人物质感10倍提升—fluxs-srpo+wan2.2_1983040175418802178.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（93 个）：
- `CLIPLoader`
- `easy cleanGpuUsed`
- `GetNode`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `VAELoader`
- `DualCLIPLoader`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `SetNode`
- `SetNode`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CFGZeroStarAndInit`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `SetNode`
- `RH_Translator`
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ImageUpscaleWithModel`
- `GetNode`
- `ImageScaleBy`
- `UpscaleModelLoader`
- `SetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `UNETLoader` ★核心
- `GetNode`
- `CLIPTextEncode` ★核心
- `RH_Translator`
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `GetNode`
- `Reroute`
- `Reroute`
- `VAEEncode` ★核心
- `PreviewImage`
- `SetNode`
- `CLIPTextEncode` ★核心
- `SeCVideoSegmentation`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `FluxResolutionNode`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `LayerMask: SegmentAnythingUltra V3`
- `GrowMaskWithBlur`
- `RH_Translator`
- `DrawMaskOnImage`
- `SeCVideoSegmentation`
- `ColorMatch`
- `SeCModelLoader`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `GrowMaskWithBlur`
- `AddMask`
- `GetNode`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerMask: LoadSegmentAnythingModels`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `ImageResizeKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: CropByMask`
- `PreviewImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LayerUtility: RestoreCropBox`
- `ImpactSwitch`
- `PreviewImage`
- `PreviewImage`
- `easy showAnything`
- `CR Text`
- `RH_LLMAPI_NODE`
- `GetNode`
- `Image Comparer (rgthree)`
- `SaveImage`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio`
- `PreviewImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `512`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `1114020293191043`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **68%**（63/93）

**有卡**：`CLIPLoader`、`easy cleanGpuUsed`、`ConditioningZeroOut`、`CLIPTextEncode`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`VAELoader`、`DualCLIPLoader`、`VAEDecode`、`UNETLoader`、`SaveImage`、`CFGZeroStarAndInit`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`RH_Translator`、`FluxGuidance`、`ImageUpscaleWithModel`、`ImageScaleBy`、`UpscaleModelLoader`、`VAEEncode`、`SeCVideoSegmentation`、`DrawMaskOnImage`、`FluxResolutionNode`、`KSampler`、`LayerMask: SegmentAnythingUltra V3`、`GrowMaskWithBlur`、`ColorMatch`、`SeCModelLoader`、`AddMask`、`LayerMask: LoadSegmentAnythingModels`、`ImageResizeKJ`、`LayerUtility: CropByMask`、`LayerUtility: RestoreCropBox`、`CR Text`、`RH_LLMAPI_NODE`、`LoadImage`、`LayerUtility: ImageScaleByAspectRatio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
