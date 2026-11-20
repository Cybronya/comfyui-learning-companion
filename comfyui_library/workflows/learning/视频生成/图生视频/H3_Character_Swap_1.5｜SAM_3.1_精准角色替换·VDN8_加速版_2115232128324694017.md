---
key: 视频生成/图生视频/H3_Character_Swap_1.5｜SAM_3.1_精准角色替换·VDN8_加速版_2115232128324694017.json
name: H3_Character_Swap_1.5｜SAM_3.1_精准角色替换·VDN8_加速版_2115232128324694017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/H3_Character_Swap_1.5｜SAM_3.1_精准角色替换·VDN8_加速版_2115232128324694017.json
hash: e3e0871d744371aa
coverage: 0.893617
learned_at: 2026-10-30 17:57:22
nodes: [CheckpointLoaderSimple, MarkdownNote, SAM3_TrackPreview, CLIPLoader, VAELoader, SamplerCustomAdvanced, VAEDecodeAudio, VAEDecode, RandomNoise, BasicGuider, ResizeImageMaskNode, SolidMask, VAEEncodeAudio, SetLatentNoiseMask, MVEx_SubjectUncrop, PreviewAnimation, VAELoader, PreviewAnimation, MiniMaxH3SigmaShift, ImageResizeKJv2, SAM3_VideoTrack, MVEx_MaskCleanup, MVEx_MaskToLatentSpace, SetLatentNoiseMask, LTXVConcatAVLatent, MiniMaxH3VDNModelComposerT8Advanced, MiniMaxH3VDNExecutionPlanT8Advanced, SAM3_TrackToMask, ModelPreviewOverrideKJ, MarkdownNote, ComfyMathExpression, DrawBBoxes, ResolutionSelector, ResolutionSelector, MiniMaxH3ReferenceToVideo, MVEx_SubjectCrop, VAEEncode, LoadImage, PrimitiveNode, CLIPTextEncode, LoraLoaderModelOnly, LoadImage, PrimitiveStringMultiline, VHS_VideoCombine, PrimitiveFloat, VHS_LoadVideo, UNETLoader]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 视频生成/图生视频/H3_Character_Swap_1.5｜SAM_3.1_精准角色替换·VDN8_加速版_2115232128324694017.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/H3_Character_Swap_1.5｜SAM_3.1_精准角色替换·VDN8_加速版_2115232128324694017.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（47 个）：
- `CheckpointLoaderSimple` ★核心
- `MarkdownNote`
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
- `MarkdownNote`
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

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **89%**（42/47）

**有卡**：`CheckpointLoaderSimple`、`SAM3_TrackPreview`、`CLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`VAEDecode`、`RandomNoise`、`BasicGuider`、`ResizeImageMaskNode`、`SolidMask`、`VAEEncodeAudio`、`SetLatentNoiseMask`、`MVEx_SubjectUncrop`、`PreviewAnimation`、`MiniMaxH3SigmaShift`、`ImageResizeKJv2`、`SAM3_VideoTrack`、`MVEx_MaskCleanup`、`MVEx_MaskToLatentSpace`、`LTXVConcatAVLatent`、`MiniMaxH3VDNModelComposerT8Advanced`、`MiniMaxH3VDNExecutionPlanT8Advanced`、`SAM3_TrackToMask`、`ModelPreviewOverrideKJ`、`ComfyMathExpression`、`DrawBBoxes`、`ResolutionSelector`、`MiniMaxH3ReferenceToVideo`、`MVEx_SubjectCrop`、`VAEEncode`、`LoadImage`、`CLIPTextEncode`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`VHS_LoadVideo`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、ResolutionSelector
