---
key: 视频生成/图生视频/H3 Character Swap 1.5｜SAM 3.1 精准角色替换·VDN8 加速版_2114606057728335873.json
name: H3 Character Swap 1.5｜SAM 3.1 精准角色替换·VDN8 加速版_2114606057728335873
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/H3 Character Swap 1.5｜SAM 3.1 精准角色替换·VDN8 加速版_2114606057728335873.json
hash: 02d40bdbc3c8eac7
coverage: 0.706897
learned_at: 2026-10-30 17:57:18
nodes: [UNETLoader, CLIPLoader, VAELoader, VAELoader, LoraLoaderModelOnly, MiniMaxH3SigmaShift, MiniMaxH3VDNModelComposerT8Advanced, SAM3_VideoTrack, VHS_LoadVideo, ImageResizeKJv2, ResolutionSelector, ResolutionSelector, PrimitiveNode, CheckpointLoaderSimple, CLIPTextEncode, SAM3_TrackToMask, MVEx_MaskCleanup, MVEx_SubjectCrop, MVEx_MaskToLatentSpace, VAEEncode, SetLatentNoiseMask, LTXVConcatAVLatent, VAEEncodeAudio, SolidMask, SetLatentNoiseMask, SAM3_TrackPreview, MiniMaxH3ReferenceToVideo, Anything Everywhere3, LoadImage, PrimitiveInt, ComfyMathExpression, MiniMaxH3VDNExecutionPlanT8Advanced, ModelPreviewOverrideKJ, BasicGuider, SamplerCustomAdvanced, RandomNoise, VAEDecode, VAEDecodeAudio, MVEx_SubjectUncrop, VHS_VideoCombine, DrawBBoxes, PreviewAnimation, ResizeImageMaskNode, PreviewAnimation, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, Reroute, PrimitiveStringMultiline, MarkdownNote, MarkdownNote, Reroute, Reroute, Reroute, Reroute]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_Multiplex_fp16.safetensors"}
---

# 视频生成/图生视频/H3 Character Swap 1.5｜SAM 3.1 精准角色替换·VDN8 加速版_2114606057728335873.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/H3 Character Swap 1.5｜SAM 3.1 精准角色替换·VDN8 加速版_2114606057728335873.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（58 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3SigmaShift`
- `MiniMaxH3VDNModelComposerT8Advanced`
- `SAM3_VideoTrack`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `ResolutionSelector`
- `ResolutionSelector`
- `PrimitiveNode`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心
- `SAM3_TrackToMask`
- `MVEx_MaskCleanup`
- `MVEx_SubjectCrop`
- `MVEx_MaskToLatentSpace`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `VAEEncodeAudio` ★核心
- `SolidMask`
- `SetLatentNoiseMask`
- `SAM3_TrackPreview`
- `MiniMaxH3ReferenceToVideo`
- `Anything Everywhere3`
- `LoadImage`
- `PrimitiveInt`
- `ComfyMathExpression`
- `MiniMaxH3VDNExecutionPlanT8Advanced`
- `ModelPreviewOverrideKJ`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `MVEx_SubjectUncrop`
- `VHS_VideoCombine`
- `DrawBBoxes`
- `PreviewAnimation`
- `ResizeImageMaskNode`
- `PreviewAnimation`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `MarkdownNote`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`

## 关键参数

- `checkpoint` = `sam3.1_Multiplex_fp16.safetensors`

## 知识

覆盖率 **71%**（41/58）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`MiniMaxH3SigmaShift`、`MiniMaxH3VDNModelComposerT8Advanced`、`SAM3_VideoTrack`、`VHS_LoadVideo`、`ImageResizeKJv2`、`ResolutionSelector`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`SAM3_TrackToMask`、`MVEx_MaskCleanup`、`MVEx_SubjectCrop`、`MVEx_MaskToLatentSpace`、`VAEEncode`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`VAEEncodeAudio`、`SolidMask`、`SAM3_TrackPreview`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`ComfyMathExpression`、`MiniMaxH3VDNExecutionPlanT8Advanced`、`ModelPreviewOverrideKJ`、`BasicGuider`、`SamplerCustomAdvanced`、`RandomNoise`、`VAEDecode`、`VAEDecodeAudio`、`MVEx_SubjectUncrop`、`VHS_VideoCombine`、`DrawBBoxes`、`PreviewAnimation`、`ResizeImageMaskNode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader、ResolutionSelector
