---
key: 平台全量/Minimax_H3｜单人 & 多人中选一人替换｜+ 遮罩选人 + Character Swap V1.5 人物替换 LoRA_2106890082614603777.json
name: Minimax_H3｜单人 & 多人中选一人替换｜+ 遮罩选人 + Character Swap V1.5 人物替换 LoRA_2106890082614603777
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Minimax_H3｜单人 & 多人中选一人替换｜+ 遮罩选人 + Character Swap V1.5 人物替换 LoRA_2106890082614603777.json
hash: b56b5739e66d5ec2
coverage: 0.690722
learned_at: 2026-11-14 00:46:17
nodes: [SamplerCustomAdvanced, ModelAttentionBackend, MiniMaxH3SigmaShift, CLIPLoader, LoraLoaderModelOnly, UNETLoader, VAELoader, VAELoader, BlockSparseAttention, VAEDecode, KSamplerSelect, BasicGuider, BasicScheduler, VAEDecodeAudio, Note, Label (rgthree), LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, MarkdownNote, ImageResizeKJv2, VHS_LoadVideo, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, Label (rgthree), ResolutionSelector, PrimitiveFloat, SamplerCustomAdvanced, VAELoader, UNETLoader, CLIPLoader, LoraLoaderModelOnly, VAELoader, PrimitiveFloat, SAM3_VideoTrack, MVEx_MaskCleanup, ImageResizeKJv2, BasicGuider, BasicScheduler, VAEDecode, VAEDecodeAudio, KSamplerSelect, MVEx_SubjectUncrop, MiniMaxH3ReferenceToVideo, VHS_VideoCombine, LoadImage, VHS_LoadVideo, MarkdownNote, SAM3_TrackToMask, PreviewAnimation, MarkdownNote, MarkdownNote, MarkdownNote, DrawBBoxes, MVEx_SubjectCrop, VAEEncode, SetLatentNoiseMask, MarkdownNote, MarkdownNote, MVEx_MaskToLatentSpace, VAEEncodeAudio, SetLatentNoiseMask, LTXVConcatAVLatent, SolidMask, MarkdownNote, PreviewAnimation, SAM3_TrackPreview, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, ResolutionSelector, MarkdownNote, MarkdownNote, MarkdownNote, PrimitiveNode, MarkdownNote, MarkdownNote, LoraLoaderModelOnly, CheckpointLoaderSimple, ModelAttentionBackend, MiniMaxH3SigmaShift, MarkdownNote, ComfyMathExpression, ResolutionSelector, ComfyMathExpression, RandomNoise, RandomNoise, Label (rgthree), CLIPTextEncode, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/Minimax_H3｜单人 & 多人中选一人替换｜+ 遮罩选人 + Character Swap V1.5 人物替换 LoRA_2106890082614603777.json

> 来源文件 `comfyui_library/workflows/平台全量/Minimax_H3｜单人 & 多人中选一人替换｜+ 遮罩选人 + Character Swap V1.5 人物替换 LoRA_2106890082614603777.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Other

**节点**（97 个）：
- `SamplerCustomAdvanced` ★核心
- `ModelAttentionBackend`
- `MiniMaxH3SigmaShift`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `BlockSparseAttention`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `BasicScheduler`
- `VAEDecodeAudio` ★核心
- `Note`
- `Label (rgthree)`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3ReferenceToVideo`
- `MarkdownNote`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Label (rgthree)`
- `ResolutionSelector`
- `PrimitiveFloat`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `PrimitiveFloat`
- `SAM3_VideoTrack`
- `MVEx_MaskCleanup`
- `ImageResizeKJv2`
- `BasicGuider`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `KSamplerSelect` ★核心
- `MVEx_SubjectUncrop`
- `MiniMaxH3ReferenceToVideo`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`
- `MarkdownNote`
- `SAM3_TrackToMask`
- `PreviewAnimation`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `DrawBBoxes`
- `MVEx_SubjectCrop`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `MarkdownNote`
- `MarkdownNote`
- `MVEx_MaskToLatentSpace`
- `VAEEncodeAudio` ★核心
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `SolidMask`
- `MarkdownNote`
- `PreviewAnimation`
- `SAM3_TrackPreview`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveNode`
- `MarkdownNote`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `CheckpointLoaderSimple` ★核心
- `ModelAttentionBackend`
- `MiniMaxH3SigmaShift`
- `MarkdownNote`
- `ComfyMathExpression`
- `ResolutionSelector`
- `ComfyMathExpression`
- `RandomNoise`
- `RandomNoise`
- `Label (rgthree)`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **69%**（67/97）

**有卡**：`SamplerCustomAdvanced`、`ModelAttentionBackend`、`MiniMaxH3SigmaShift`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`BlockSparseAttention`、`VAEDecode`、`KSamplerSelect`、`BasicGuider`、`BasicScheduler`、`VAEDecodeAudio`、`Label (rgthree)`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`ImageResizeKJv2`、`VHS_LoadVideo`、`ResolutionSelector`、`SAM3_VideoTrack`、`MVEx_MaskCleanup`、`MVEx_SubjectUncrop`、`VHS_VideoCombine`、`SAM3_TrackToMask`、`PreviewAnimation`、`DrawBBoxes`、`MVEx_SubjectCrop`、`VAEEncode`、`SetLatentNoiseMask`、`MVEx_MaskToLatentSpace`、`VAEEncodeAudio`、`LTXVConcatAVLatent`、`SolidMask`、`SAM3_TrackPreview`、`CheckpointLoaderSimple`、`ComfyMathExpression`、`RandomNoise`、`CLIPTextEncode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPLoader、CLIPTextEncode、ResolutionSelector
