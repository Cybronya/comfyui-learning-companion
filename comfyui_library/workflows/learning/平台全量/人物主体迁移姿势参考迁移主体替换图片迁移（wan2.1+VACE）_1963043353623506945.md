---
key: 平台全量/人物主体迁移姿势参考迁移主体替换图片迁移（wan2.1+VACE）_1963043353623506945.json
name: 人物主体迁移姿势参考迁移主体替换图片迁移（wan2.1+VACE）_1963043353623506945
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/人物主体迁移姿势参考迁移主体替换图片迁移（wan2.1+VACE）_1963043353623506945.json
hash: e71f2f8f546d12a2
coverage: 0.774648
learned_at: 2026-11-14 01:36:58
nodes: [UNETLoader, LoraLoaderModelOnly, PathchSageAttentionKJ, UpscaleModelLoader, GetNode, LayerUtility: ImageScaleByAspectRatio V2, ImageUpscaleWithModel, GetNode, GetNode, VAEEncode, WanVideoNAG, PreviewImage, VAEDecode, KSampler, LoraLoaderModelOnly, UNETLoader, VAEDecode, LoraLoaderModelOnly, VAELoader, PreviewImage, ColorMatch, DownloadAndLoadSAM2Model, DownloadAndLoadQwenModel, Sam2Segmentation, Text Multiline, ModelSamplingSD3, KSampler, SaveImage, Image Comparer (rgthree), Image Comparer (rgthree), PreviewImage, easy imageRemBg, SetNode, SetNode, SetNode, LayerUtility: ImageScaleByAspectRatio V2, RBGImageStitchPlus, CLIPLoader, CLIPTextEncode, PathchSageAttentionKJ, WanVideoNAG, TrimVideoLatent, WanVaceToVideo, GetImageRangeFromBatch, LayerUtility: ImageBlend, GetImageSize, ImageResizeKJ, PreviewImage, PreviewImage, InpaintPreprocessor, RH_Captioner, RH_Captioner, ImpactInt, SaveImageAndMetadata_, LoadImage, LayerMask: SegmentAnythingUltra V2, GrowMaskWithBlur, AIO_Preprocessor, VHS_DuplicateMasks, RepeatImageBatch, CLIPTextEncode, Text Multiline, QwenVLDetection, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, easy showAnything, Text Concatenate, easy showAnything, ImpactSwitch, SaveImageAndMetadata_, ReActorFaceSwap]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "beta", "seed": 617251345262790, "steps": 10}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/人物主体迁移姿势参考迁移主体替换图片迁移（wan2.1+VACE）_1963043353623506945.json

> 来源文件 `comfyui_library/workflows/平台全量/人物主体迁移姿势参考迁移主体替换图片迁移（wan2.1+VACE）_1963043353623506945.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（71 个）：
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `UpscaleModelLoader`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageUpscaleWithModel`
- `GetNode`
- `GetNode`
- `VAEEncode` ★核心
- `WanVideoNAG`
- `PreviewImage`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `PreviewImage`
- `ColorMatch`
- `DownloadAndLoadSAM2Model`
- `DownloadAndLoadQwenModel`
- `Sam2Segmentation`
- `Text Multiline`
- `ModelSamplingSD3`
- `KSampler` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `easy imageRemBg`
- `SetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `RBGImageStitchPlus`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `PathchSageAttentionKJ`
- `WanVideoNAG`
- `TrimVideoLatent`
- `WanVaceToVideo`
- `GetImageRangeFromBatch`
- `LayerUtility: ImageBlend`
- `GetImageSize`
- `ImageResizeKJ`
- `PreviewImage`
- `PreviewImage`
- `InpaintPreprocessor`
- `RH_Captioner`
- `RH_Captioner`
- `ImpactInt`
- `SaveImageAndMetadata_`
- `LoadImage`
- `LayerMask: SegmentAnythingUltra V2`
- `GrowMaskWithBlur`
- `AIO_Preprocessor`
- `VHS_DuplicateMasks`
- `RepeatImageBatch`
- `CLIPTextEncode` ★核心
- `Text Multiline`
- `QwenVLDetection`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `easy showAnything`
- `Text Concatenate`
- `easy showAnything`
- `ImpactSwitch`
- `SaveImageAndMetadata_`
- `ReActorFaceSwap`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `617251345262790`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **77%**（55/71）

**有卡**：`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`UpscaleModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageUpscaleWithModel`、`VAEEncode`、`WanVideoNAG`、`VAEDecode`、`KSampler`、`VAELoader`、`ColorMatch`、`DownloadAndLoadSAM2Model`、`DownloadAndLoadQwenModel`、`Sam2Segmentation`、`Text Multiline`、`ModelSamplingSD3`、`SaveImage`、`easy imageRemBg`、`RBGImageStitchPlus`、`CLIPLoader`、`CLIPTextEncode`、`TrimVideoLatent`、`WanVaceToVideo`、`GetImageRangeFromBatch`、`LayerUtility: ImageBlend`、`GetImageSize`、`ImageResizeKJ`、`InpaintPreprocessor`、`RH_Captioner`、`ImpactInt`、`SaveImageAndMetadata_`、`LoadImage`、`LayerMask: SegmentAnythingUltra V2`、`GrowMaskWithBlur`、`AIO_Preprocessor`、`VHS_DuplicateMasks`、`RepeatImageBatch`、`QwenVLDetection`、`Text Concatenate`、`ReActorFaceSwap`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
