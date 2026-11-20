---
key: 平台全量/Wan2.1+Kontext 2阶段换装实验版V1_1947273509502341121.json
name: Wan2.1+Kontext 2阶段换装实验版V1_1947273509502341121
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1+Kontext 2阶段换装实验版V1_1947273509502341121.json
hash: 5ec2649b3ba910ea
coverage: 0.875
learned_at: 2026-11-14 01:04:33
nodes: [CLIPLoader, VAELoader, ModelSamplingSD3, PathchSageAttentionKJ, KSampler, LoraLoaderModelOnly, ImageConcanate, MaskToImage, SaveImage, MathExpression|pysssss, CR Prompt Text, VAELoader, ConditioningZeroOut, PreviewImage, LoadImageOutput, VAEEncode, MarkdownNote, FluxGuidance, ReferenceLatent, ImageStitch, CLIPTextEncode, GoogleTranslateTextNode, DualCLIPLoader, FluxKontextImageScale, PDIMAGE_LongerSize, ImageConcanate, TeaCache, SaveImage, UnetLoaderGGUF, LoraLoaderModelOnly, LoadImage, PDIMAGE_LongerSize, ImageConcanate, GetImageRangeFromBatch, ImageConcanate, SaveImage, LayerUtility: PurgeVRAM, KSampler, PreviewImage, UNETLoader, CLIPTextEncode, SaveImage, TrimVideoLatent, VAEDecode, VHS_VideoCombine, WanVaceToVideo, LayerUtility: ImageScaleByAspectRatio V2, CLIPTextEncode, MaskRepeatBatch, RepeatImageBatch, LoadImage, JWInteger, CR Prompt Text, Note, Note, Note, Note, Mix Color By Mask, PreviewImage, preview_mask, VAEDecode, GrowMaskWithBlur, LayerMask: LoadSegmentAnythingModels, LayerMask: SegmentAnythingUltra V3]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 169374313982370, "steps": 20}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Wan2.1+Kontext 2阶段换装实验版V1_1947273509502341121.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1+Kontext 2阶段换装实验版V1_1947273509502341121.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `CLIPLoader`
- `VAELoader`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageConcanate`
- `MaskToImage`
- `SaveImage`
- `MathExpression|pysssss`
- `CR Prompt Text`
- `VAELoader`
- `ConditioningZeroOut`
- `PreviewImage`
- `LoadImageOutput`
- `VAEEncode` ★核心
- `MarkdownNote`
- `FluxGuidance`
- `ReferenceLatent`
- `ImageStitch`
- `CLIPTextEncode` ★核心
- `GoogleTranslateTextNode`
- `DualCLIPLoader`
- `FluxKontextImageScale`
- `PDIMAGE_LongerSize`
- `ImageConcanate`
- `TeaCache`
- `SaveImage`
- `UnetLoaderGGUF` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `PDIMAGE_LongerSize`
- `ImageConcanate`
- `GetImageRangeFromBatch`
- `ImageConcanate`
- `SaveImage`
- `LayerUtility: PurgeVRAM`
- `KSampler` ★核心
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `SaveImage`
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `WanVaceToVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPTextEncode` ★核心
- `MaskRepeatBatch`
- `RepeatImageBatch`
- `LoadImage`
- `JWInteger`
- `CR Prompt Text`
- `Note`
- `Note`
- `Note`
- `Note`
- `Mix Color By Mask`
- `PreviewImage`
- `preview_mask`
- `VAEDecode` ★核心
- `GrowMaskWithBlur`
- `LayerMask: LoadSegmentAnythingModels`
- `LayerMask: SegmentAnythingUltra V3`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `169374313982370`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（56/64）

**有卡**：`CLIPLoader`、`VAELoader`、`ModelSamplingSD3`、`PathchSageAttentionKJ`、`KSampler`、`LoraLoaderModelOnly`、`ImageConcanate`、`MaskToImage`、`SaveImage`、`MathExpression|pysssss`、`CR Prompt Text`、`ConditioningZeroOut`、`LoadImageOutput`、`VAEEncode`、`FluxGuidance`、`ReferenceLatent`、`ImageStitch`、`CLIPTextEncode`、`GoogleTranslateTextNode`、`DualCLIPLoader`、`FluxKontextImageScale`、`PDIMAGE_LongerSize`、`TeaCache`、`UnetLoaderGGUF`、`LoadImage`、`GetImageRangeFromBatch`、`LayerUtility: PurgeVRAM`、`UNETLoader`、`TrimVideoLatent`、`VAEDecode`、`VHS_VideoCombine`、`WanVaceToVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`MaskRepeatBatch`、`RepeatImageBatch`、`JWInteger`、`Mix Color By Mask`、`preview_mask`、`GrowMaskWithBlur`、`LayerMask: LoadSegmentAnythingModels`、`LayerMask: SegmentAnythingUltra V3`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
