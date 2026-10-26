---
key: 视频生成/图生视频/H3 Character Swap 1.5升级｜SAM 3.1精准换角色VDN8加速视频替换_2113441647387303937.json
name: H3 Character Swap 1.5升级｜SAM 3.1精准换角色VDN8加速视频替换_2113441647387303937
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/H3 Character Swap 1.5升级｜SAM 3.1精准换角色VDN8加速视频替换_2113441647387303937.json
hash: c6204f2dc361b23e
coverage: 0.920455
learned_at: 2026-10-26 22:11:17
nodes: [CheckpointLoaderSimple, SAM3_TrackPreview, CLIPLoader, VAELoader, SamplerCustomAdvanced, VAEDecodeAudio, VAEDecode, RandomNoise, BasicGuider, ResizeImageMaskNode, SolidMask, VAEEncodeAudio, SetLatentNoiseMask, MVEx_SubjectUncrop, PreviewAnimation, VAELoader, PreviewAnimation, MiniMaxH3SigmaShift, ImageResizeKJv2, SAM3_VideoTrack, MVEx_MaskCleanup, MVEx_MaskToLatentSpace, SetLatentNoiseMask, LTXVConcatAVLatent, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNExecutionPlanT8Advanced, SAM3_TrackToMask, ModelPreviewOverrideKJ, ComfyMathExpression, DrawBBoxes, ResolutionSelector, ResolutionSelector, MiniMaxH3ReferenceToVideo, MVEx_SubjectCrop, VAEEncode, LoadImage, PrimitiveNode, CLIPTextEncode, LoraLoaderModelOnly, LoadImage, PrimitiveStringMultiline, VHS_VideoCombine, PrimitiveFloat, VHS_LoadVideo, UNETLoader, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "sam3.1_multiplex_fp16.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/H3 Character Swap 1.5升级｜SAM 3.1精准换角色VDN8加速视频替换_2113441647387303937.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/H3 Character Swap 1.5升级｜SAM 3.1精准换角色VDN8加速视频替换_2113441647387303937.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（88 个）：
- `CheckpointLoaderSimple` ★核心
- `SAM3_TrackPreview`
- `CLIPLoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `RandomNoise`
- `BasicGuider`
- `ResizeImageMaskNode`
- `SolidMask`
- `VAEEncodeAudio` ★核心
- `SetLatentNoiseMask`
- `MVEx_SubjectUncrop`
- `PreviewAnimation`
- `VAELoader`
- `PreviewAnimation`
- `MiniMaxH3SigmaShift`
- `ImageResizeKJv2`
- `SAM3_VideoTrack`
- `MVEx_MaskCleanup`
- `MVEx_MaskToLatentSpace`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `MiniMaxH3VDNExecutionPlanT8Advanced`
- `SAM3_TrackToMask`
- `ModelPreviewOverrideKJ`
- `ComfyMathExpression`
- `DrawBBoxes`
- `ResolutionSelector`
- `ResolutionSelector`
- `MiniMaxH3ReferenceToVideo`
- `MVEx_SubjectCrop`
- `VAEEncode` ★核心
- `LoadImage`
- `PrimitiveNode`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `PrimitiveFloat`
- `VHS_LoadVideo`
- `UNETLoader` ★核心
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **92%**（81/88）

**有卡**：`CheckpointLoaderSimple`、`SAM3_TrackPreview`、`CLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`VAEDecode`、`RandomNoise`、`BasicGuider`、`ResizeImageMaskNode`、`SolidMask`、`VAEEncodeAudio`、`SetLatentNoiseMask`、`MVEx_SubjectUncrop`、`PreviewAnimation`、`MiniMaxH3SigmaShift`、`ImageResizeKJv2`、`SAM3_VideoTrack`、`MVEx_MaskCleanup`、`MVEx_MaskToLatentSpace`、`LTXVConcatAVLatent`、`MiniMaxH3VDNModelComposerT8Advanced`、`MiniMaxH3VDNExecutionPlanT8Advanced`、`SAM3_TrackToMask`、`ModelPreviewOverrideKJ`、`ComfyMathExpression`、`DrawBBoxes`、`ResolutionSelector`、`MiniMaxH3ReferenceToVideo`、`MVEx_SubjectCrop`、`VAEEncode`、`LoadImage`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`VHS_LoadVideo`、`UNETLoader`、`EmptyLatentImage`、`KSampler`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
