---
key: 视频生成/文生视频/Wan 2.2 Animate无限循环自动分割 TikTok舞蹈视频原生支持_2090421078559645697.json
name: Wan 2.2 Animate无限循环自动分割 TikTok舞蹈视频原生支持_2090421078559645697
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan 2.2 Animate无限循环自动分割 TikTok舞蹈视频原生支持_2090421078559645697.json
hash: 7809ed20f28f1ce7
coverage: 0.530303
learned_at: 2026-10-15 22:47:05
nodes: [CLIPTextEncode, TrimVideoLatent, VAEDecode, ModelSamplingSD3, WanAnimateToVideo, KSampler, ImageFromBatch, VAEDecode, WanAnimateToVideo, KSampler, TrimVideoLatent, GrowMask, BlockifyMask, DrawMaskOnImage, PreviewImage, MaskPreview, PixelPerfectResolution, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, Reroute, VHS_VideoCombine, easy showAnything, PathchSageAttentionKJ, TorchCompileModel, GroundingDinoSAMSegment (segment anything), SetNode, SetNode, easy forLoopStart, VHS_VideoCombine, GetNode, GetNode, GetNode, MathExpression|pysssss, easy showAnything, easy showAnything, easy showAnything, easy showAnything, ModelSamplingSD3, VHS_GetImageCount, easy showAnything, ImageCropByMaskAndResize, FaceMaskFromPoseKeypoints, easy showAnything, ImageResizeKJv2, PreviewImage, LoadImageFromPath, CLIPVisionEncode, SetNode, SetNode, LoadImage, VHS_LoadVideoPath, GetNode, SetNode, VHS_VideoInfoLoaded, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, CLIPVisionLoader, VAELoader, GroundingDinoModelLoader (segment anything), SAMModelLoader (segment anything), ImageBatch, easy forLoopEnd, GetNode, GetNode, VHS_VideoCombine, DWPreprocessor, VHS_LoadVideo, PrimitiveInt, PrimitiveInt, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, JjkText, solarL_SaveImagesToZip, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/文生视频/Wan 2.2 Animate无限循环自动分割 TikTok舞蹈视频原生支持_2090421078559645697.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan 2.2 Animate无限循环自动分割 TikTok舞蹈视频原生支持_2090421078559645697.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（132 个）：
- `CLIPTextEncode` ★核心
- `TrimVideoLatent`
- `VAEDecode` ★核心
- `ModelSamplingSD3`
- `WanAnimateToVideo`
- `KSampler` ★核心
- `ImageFromBatch`
- `VAEDecode` ★核心
- `WanAnimateToVideo`
- `KSampler` ★核心
- `TrimVideoLatent`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `PreviewImage`
- `MaskPreview`
- `PixelPerfectResolution`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `VHS_VideoCombine`
- `easy showAnything`
- `PathchSageAttentionKJ`
- `TorchCompileModel`
- `GroundingDinoSAMSegment (segment anything)`
- `SetNode`
- `SetNode`
- `easy forLoopStart`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `ModelSamplingSD3`
- `VHS_GetImageCount`
- `easy showAnything`
- `ImageCropByMaskAndResize`
- `FaceMaskFromPoseKeypoints`
- `easy showAnything`
- `ImageResizeKJv2`
- `PreviewImage`
- `LoadImageFromPath`
- `CLIPVisionEncode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `VHS_LoadVideoPath`
- `GetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `GroundingDinoModelLoader (segment anything)`
- `SAMModelLoader (segment anything)`
- `ImageBatch`
- `easy forLoopEnd`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `DWPreprocessor`
- `VHS_LoadVideo`
- `PrimitiveInt`
- `PrimitiveInt`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `JjkText`
- `solarL_SaveImagesToZip`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **53%**（70/132）

**有卡**：`CLIPTextEncode`、`TrimVideoLatent`、`VAEDecode`、`ModelSamplingSD3`、`WanAnimateToVideo`、`KSampler`、`ImageFromBatch`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`MaskPreview`、`PixelPerfectResolution`、`VHS_VideoCombine`、`PathchSageAttentionKJ`、`TorchCompileModel`、`GroundingDinoSAMSegment (segment anything)`、`easy forLoopStart`、`MathExpression|pysssss`、`VHS_GetImageCount`、`ImageCropByMaskAndResize`、`FaceMaskFromPoseKeypoints`、`ImageResizeKJv2`、`LoadImageFromPath`、`CLIPVisionEncode`、`LoadImage`、`VHS_LoadVideoPath`、`VHS_VideoInfoLoaded`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`CLIPVisionLoader`、`VAELoader`、`GroundingDinoModelLoader (segment anything)`、`SAMModelLoader (segment anything)`、`ImageBatch`、`easy forLoopEnd`、`DWPreprocessor`、`VHS_LoadVideo`、`EmptyLatentImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
