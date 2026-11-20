---
key: 平台全量/Minimax H3+Sam3.1角色自动替换_2095161277223096321.json
name: Minimax H3+Sam3.1角色自动替换_2095161277223096321
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Minimax H3+Sam3.1角色自动替换_2095161277223096321.json
hash: e04f498012c6b49a
coverage: 1
learned_at: 2026-11-14 00:45:31
nodes: [VAEEncodeAudio, UNETLoader, ModelAttentionBackend, LoraLoaderModelOnly, CLIPLoader, VAELoader, VAELoader, LoadBackgroundRemovalModel, RemoveBackground, InvertMask, EmptyImage, ImageFromBatch, ResizeImageMaskNode, GetImageSize, ModelPreviewOverrideKJ, ConditioningZeroOut, ImageCompositeMasked, SolidMask, LTXVConcatAVLatent, VAEDecodeAudio, VAEDecode, CreateVideo, KSampler, SetLatentNoiseMask, SetLatentNoiseMask, SAM3_TrackEditMask, ImageResizeKJv2, SAM3_VideoTrack, CLIPTextEncode, CheckpointLoaderSimple, SCAIL2ColoredMaskV2, VHS_VideoCombine, GrowMask, VHS_LoadVideo, VAEEncode, LoadImage, RH_Translator, Int, SaveVideo, GetImageSize, ComfyMathExpression, MiniMaxH3ReferenceToVideo, ResolutionSelector]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 123, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Minimax H3+Sam3.1角色自动替换_2095161277223096321.json

> 来源文件 `comfyui_library/workflows/平台全量/Minimax H3+Sam3.1角色自动替换_2095161277223096321.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `VAEEncodeAudio` ★核心
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoadBackgroundRemovalModel`
- `RemoveBackground`
- `InvertMask`
- `EmptyImage`
- `ImageFromBatch`
- `ResizeImageMaskNode`
- `GetImageSize`
- `ModelPreviewOverrideKJ`
- `ConditioningZeroOut`
- `ImageCompositeMasked`
- `SolidMask`
- `LTXVConcatAVLatent`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `CreateVideo`
- `KSampler` ★核心
- `SetLatentNoiseMask`
- `SetLatentNoiseMask`
- `SAM3_TrackEditMask`
- `ImageResizeKJv2`
- `SAM3_VideoTrack`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `SCAIL2ColoredMaskV2`
- `VHS_VideoCombine`
- `GrowMask`
- `VHS_LoadVideo`
- `VAEEncode` ★核心
- `LoadImage`
- `RH_Translator`
- `Int`
- `SaveVideo`
- `GetImageSize`
- `ComfyMathExpression`
- `MiniMaxH3ReferenceToVideo`
- `ResolutionSelector`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `123`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **100%**（43/43）

**有卡**：`VAEEncodeAudio`、`UNETLoader`、`ModelAttentionBackend`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`LoadBackgroundRemovalModel`、`RemoveBackground`、`InvertMask`、`EmptyImage`、`ImageFromBatch`、`ResizeImageMaskNode`、`GetImageSize`、`ModelPreviewOverrideKJ`、`ConditioningZeroOut`、`ImageCompositeMasked`、`SolidMask`、`LTXVConcatAVLatent`、`VAEDecodeAudio`、`VAEDecode`、`CreateVideo`、`KSampler`、`SetLatentNoiseMask`、`SAM3_TrackEditMask`、`ImageResizeKJv2`、`SAM3_VideoTrack`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`SCAIL2ColoredMaskV2`、`VHS_VideoCombine`、`GrowMask`、`VHS_LoadVideo`、`VAEEncode`、`LoadImage`、`RH_Translator`、`Int`、`SaveVideo`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
