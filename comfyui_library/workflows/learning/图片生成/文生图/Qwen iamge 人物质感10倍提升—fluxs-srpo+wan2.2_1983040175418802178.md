---
key: 图片生成/文生图/Qwen iamge 人物质感10倍提升—fluxs-srpo+wan2.2_1983040175418802178.json
name: Qwen iamge 人物质感10倍提升—fluxs-srpo+wan2.2_1983040175418802178
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen iamge 人物质感10倍提升—fluxs-srpo+wan2.2_1983040175418802178.json
hash: b83bbfa6b6cbbb62
coverage: 0.591398
learned_at: 2026-10-10 20:58:56
nodes: [CLIPLoader, easy cleanGpuUsed, GetNode, ConditioningZeroOut, CLIPTextEncode, EmptyLatentImage, LoraLoaderModelOnly, ModelSamplingAuraFlow, VAELoader, DualCLIPLoader, VAEDecode, UNETLoader, VAELoader, SetNode, SetNode, SaveImage, Image Comparer (rgthree), CFGZeroStarAndInit, PathchSageAttentionKJ, ModelSamplingSD3, SetNode, RH_Translator, VAELoader, CLIPLoader, CLIPTextEncode, FluxGuidance, ImageUpscaleWithModel, GetNode, ImageScaleBy, UpscaleModelLoader, SetNode, GetNode, Reroute, Reroute, UNETLoader, GetNode, CLIPTextEncode, RH_Translator, ConditioningZeroOut, VAEEncode, GetNode, Reroute, Reroute, VAEEncode, PreviewImage, SetNode, CLIPTextEncode, SeCVideoSegmentation, DrawMaskOnImage, GetNode, GetNode, FluxResolutionNode, KSampler, VAEDecode, LayerMask: SegmentAnythingUltra V3, GrowMaskWithBlur, RH_Translator, DrawMaskOnImage, SeCVideoSegmentation, ColorMatch, SeCModelLoader, KSampler, VAEDecode, GrowMaskWithBlur, AddMask, GetNode, LayerMask: SegmentAnythingUltra V3, LayerMask: LoadSegmentAnythingModels, GetNode, SetNode, PreviewImage, ImageResizeKJ, UNETLoader, LoraLoaderModelOnly, LayerUtility: CropByMask, PreviewImage, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, LayerUtility: RestoreCropBox, ImpactSwitch, PreviewImage, PreviewImage, easy showAnything, CR Text, RH_LLMAPI_NODE, GetNode, Image Comparer (rgthree), SaveImage, LoadImage, LayerUtility: ImageScaleByAspectRatio, PreviewImage]
patterns: [text_to_image, image_to_image]
missing: [CR Text, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3, LayerMask: SegmentAnythingUltra V3, LayerUtility: CropByMask, LayerUtility: ImageScaleByAspectRatio, LayerUtility: RestoreCropBox, easy cleanGpuUsed]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 0.20000000000000004, "height": 512, "sampler_name": "euler", "scheduler": "beta", "seed": 1114020293191043, "steps": 10, "width": 512}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: LoadSegmentAnythingModels` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: SegmentAnythingUltra V3` 知识库中没有该节点类型的任何知识, 次要节点 `LayerMask: SegmentAnythingUltra V3` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: CropByMask` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: RestoreCropBox` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen iamge 人物质感10倍提升—fluxs-srpo+wan2.2_1983040175418802178.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen iamge 人物质感10倍提升—fluxs-srpo+wan2.2_1983040175418802178.json`

## 结构

**节点**（93 个）：
- `CLIPLoader`
- `easy cleanGpuUsed`
- `GetNode`
- `ConditioningZeroOut`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `LoraLoaderModelOnly`
- `ModelSamplingAuraFlow`
- `VAELoader`
- `DualCLIPLoader`
- `VAEDecode`
- `UNETLoader`
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
- `CLIPTextEncode`
- `FluxGuidance`
- `ImageUpscaleWithModel`
- `GetNode`
- `ImageScaleBy`
- `UpscaleModelLoader`
- `SetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `UNETLoader`
- `GetNode`
- `CLIPTextEncode`
- `RH_Translator`
- `ConditioningZeroOut`
- `VAEEncode`
- `GetNode`
- `Reroute`
- `Reroute`
- `VAEEncode`
- `PreviewImage`
- `SetNode`
- `CLIPTextEncode`
- `SeCVideoSegmentation`
- `DrawMaskOnImage`
- `GetNode`
- `GetNode`
- `FluxResolutionNode`
- `KSampler`
- `VAEDecode`
- `LayerMask: SegmentAnythingUltra V3`
- `GrowMaskWithBlur`
- `RH_Translator`
- `DrawMaskOnImage`
- `SeCVideoSegmentation`
- `ColorMatch`
- `SeCModelLoader`
- `KSampler`
- `VAEDecode`
- `GrowMaskWithBlur`
- `AddMask`
- `GetNode`
- `LayerMask: SegmentAnythingUltra V3`
- `LayerMask: LoadSegmentAnythingModels`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `ImageResizeKJ`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LayerUtility: CropByMask`
- `PreviewImage`
- `UNETLoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `KSampler`
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

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `0.20000000000000004`
- `height` = `512`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `seed` = `1114020293191043`
- `steps` = `10`
- `width` = `512`

## 知识

覆盖率 **59%**（55/93）

**有卡**：`CLIPLoader`、`easy cleanGpuUsed`、`GetNode`、`ConditioningZeroOut`、`CLIPTextEncode`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`ModelSamplingAuraFlow`、`VAELoader`、`DualCLIPLoader`、`VAEDecode`、`UNETLoader`、`SetNode`、`SaveImage`、`Image Comparer (rgthree)`、`CFGZeroStarAndInit`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`RH_Translator`、`FluxGuidance`、`ImageUpscaleWithModel`、`ImageScaleBy`、`UpscaleModelLoader`、`Reroute`、`VAEEncode`、`PreviewImage`、`SeCVideoSegmentation`、`DrawMaskOnImage`、`FluxResolutionNode`、`KSampler`、`LayerMask: SegmentAnythingUltra V3`

**缺卡**（8）：`CR Text`、`LayerMask: LoadSegmentAnythingModels`、`LayerMask: SegmentAnythingUltra V3`、`LayerMask: SegmentAnythingUltra V3`、`LayerUtility: CropByMask`、`LayerUtility: ImageScaleByAspectRatio`、`LayerUtility: RestoreCropBox`、`easy cleanGpuUsed`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: LoadSegmentAnythingModels` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: SegmentAnythingUltra V3` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerMask: SegmentAnythingUltra V3` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: CropByMask` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: RestoreCropBox` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
