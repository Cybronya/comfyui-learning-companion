---
key: 图片生成/文生图/Wan2.2剪辑师出图工作流V1+放大+面部修复_1995824387368574978.json
name: Wan2.2剪辑师出图工作流V1+放大+面部修复_1995824387368574978
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2剪辑师出图工作流V1+放大+面部修复_1995824387368574978.json
hash: 9a1f61cf82107430
coverage: 0.568182
learned_at: 2026-10-19 21:32:44
nodes: [easy int, easy int, GetNode, VAEEncode, GroundingDinoModelLoader (segment anything), SAMLoader, VAELoader, CLIPLoader, GroundingDinoSAMSegment (segment anything), GrowMask, ImageScaleBy, UNETLoader, SetNode, SetNode, SetNode, LoraLoaderModelOnly, PathchSageAttentionKJ, ImageUpscaleWithModel, UpscaleModelLoader, GetNode, GetNode, SetNode, GetNode, GetNode, MaskBoundingBox+, ImageCrop, GroundingDinoSAMSegment (segment anything), GrowMaskWithBlur, SetNode, SetNode, SetNode, SetNode, SetNode, KSampler, SetLatentNoiseMask, SetNode, GetNode, GetNode, VAEDecode, PreviewImage, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, PreviewImage, MaskPreview, ImageCompositeMasked, GetNode, GetNode, GetNode, VAEDecode, easy getNode, LoadImage, SaveImage, SaveImage, Image Comparer (rgthree), Note, Note, CLIPTextEncode, CLIPTextEncode, FastFilmGrain, GetNode, CLIPTextEncode, CLIPTextEncode, SetNode, SetNode, GetNode, WanVideoNAG, ModelSamplingSD3, SetNode, Note, VAEEncode, ImageResizeKJv2, KSampler, GetNode, GetNode, Note, SaveImage, UNETLoader, CLIPLoader, VAELoader, easy setNode, LoraLoader, VAEDecode, EmptyHunyuanLatentVideo, PathchSageAttentionKJ, RHHiddenNodes]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.25000000000000006, "lora_name": "FastWan_T2V_14B_480p_lora_rank_128_bf16.safetensors", "sampler_name": "uni_pc", "scheduler": "simple", "seed": 633945303626011, "steps": 8, "strength_clip": 1.0000000000000002, "strength_model": 1.0000000000000002}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Wan2.2剪辑师出图工作流V1+放大+面部修复_1995824387368574978.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2剪辑师出图工作流V1+放大+面部修复_1995824387368574978.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `easy int`
- `easy int`
- `GetNode`
- `VAEEncode` ★核心
- `GroundingDinoModelLoader (segment anything)`
- `SAMLoader`
- `VAELoader`
- `CLIPLoader`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMask`
- `ImageScaleBy`
- `UNETLoader` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `MaskBoundingBox+`
- `ImageCrop`
- `GroundingDinoSAMSegment (segment anything)`
- `GrowMaskWithBlur`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `KSampler` ★核心
- `SetLatentNoiseMask`
- `SetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `PreviewImage`
- `MaskPreview`
- `ImageCompositeMasked`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecode` ★核心
- `easy getNode`
- `LoadImage`
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `FastFilmGrain`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoNAG`
- `ModelSamplingSD3`
- `SetNode`
- `Note`
- `VAEEncode` ★核心
- `ImageResizeKJv2`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `Note`
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `easy setNode`
- `LoraLoader` ★核心
- `VAEDecode` ★核心
- `EmptyHunyuanLatentVideo`
- `PathchSageAttentionKJ`
- `RHHiddenNodes`

**识别到的模式**：image_to_image、lora

## 关键参数

- `seed` = `633945303626011`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `uni_pc`
- `scheduler` = `simple`
- `denoise` = `0.25000000000000006`
- `lora_name` = `FastWan_T2V_14B_480p_lora_rank_128_bf16.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `1.0000000000000002`

## 知识

覆盖率 **57%**（50/88）

**有卡**：`easy int`、`VAEEncode`、`GroundingDinoModelLoader (segment anything)`、`SAMLoader`、`VAELoader`、`CLIPLoader`、`GroundingDinoSAMSegment (segment anything)`、`GrowMask`、`ImageScaleBy`、`UNETLoader`、`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`MaskBoundingBox+`、`ImageCrop`、`GrowMaskWithBlur`、`KSampler`、`SetLatentNoiseMask`、`VAEDecode`、`ImageResizeKJv2`、`MaskPreview`、`ImageCompositeMasked`、`easy getNode`、`LoadImage`、`SaveImage`、`CLIPTextEncode`、`FastFilmGrain`、`WanVideoNAG`、`ModelSamplingSD3`、`easy setNode`、`LoraLoader`、`EmptyHunyuanLatentVideo`、`RHHiddenNodes`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
