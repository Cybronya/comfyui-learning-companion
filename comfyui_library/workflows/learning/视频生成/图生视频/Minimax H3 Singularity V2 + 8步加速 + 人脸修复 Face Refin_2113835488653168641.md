---
key: 视频生成/图生视频/Minimax H3 Singularity V2 + 8步加速 + 人脸修复 Face Refin_2113835488653168641.json
name: Minimax H3 Singularity V2 + 8步加速 + 人脸修复 Face Refin_2113835488653168641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax H3 Singularity V2 + 8步加速 + 人脸修复 Face Refin_2113835488653168641.json
hash: 9f1b40c0ba194d3d
coverage: 0.689189
learned_at: 2026-10-26 22:13:37
nodes: [ModelAttentionBackend, VAELoader, MiniMaxH3SigmaShift, KSamplerSelect, ConditioningZeroOut, BasicScheduler, SelfLiftH3Sampler, VAEDecodeAudio, VHS_VideoCombine, ComfyMathExpression, VOSR2ModelLoader, VOSR2Upscale, VHS_VideoCombine, PreviewAny, VHS_VideoCombine, ImageScaleToTotalPixels, H3FaceTrackCrop, PrimitiveStringMultiline, PrimitiveFloat, MiniMaxH3ReferenceToVideo, VAELoader, VAEDecode, LoadImage, VAELoader, VAELoader, BasicScheduler, ConditioningZeroOut, VAEDecodeAudio, VAEDecode, SelfLiftH3Sampler, KSamplerSelect, BlockSparseAttention, ImageScaleToTotalPixels, VHS_VideoCombine, PrimitiveStringMultiline, Note, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), MarkdownNote, MarkdownNote, PrimitiveNode, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, PrimitiveNode, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MiniMaxH3ReferenceToVideo, LoadImage, CLIPLoader, UNETLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, CLIPLoader, UNETLoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, BlockSparseAttention, H3FaceStitch, MarkdownNote, MarkdownNote, MarkdownNote, ComfyMathExpression, PrimitiveFloat, ResolutionSelector, ResolutionSelector]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax H3 Singularity V2 + 8步加速 + 人脸修复 Face Refin_2113835488653168641.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax H3 Singularity V2 + 8步加速 + 人脸修复 Face Refin_2113835488653168641.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（74 个）：
- `ModelAttentionBackend`
- `VAELoader`
- `MiniMaxH3SigmaShift`
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `BasicScheduler`
- `SelfLiftH3Sampler` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `VOSR2ModelLoader`
- `VOSR2Upscale`
- `VHS_VideoCombine`
- `PreviewAny`
- `VHS_VideoCombine`
- `ImageScaleToTotalPixels`
- `H3FaceTrackCrop`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `VAELoader`
- `VAEDecode` ★核心
- `LoadImage`
- `VAELoader`
- `VAELoader`
- `BasicScheduler`
- `ConditioningZeroOut`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SelfLiftH3Sampler` ★核心
- `KSamplerSelect` ★核心
- `BlockSparseAttention`
- `ImageScaleToTotalPixels`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `Note`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveNode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveNode`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BlockSparseAttention`
- `H3FaceStitch`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `ResolutionSelector`
- `ResolutionSelector`

## 知识

覆盖率 **69%**（51/74）

**有卡**：`ModelAttentionBackend`、`VAELoader`、`MiniMaxH3SigmaShift`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`SelfLiftH3Sampler`、`VAEDecodeAudio`、`VHS_VideoCombine`、`ComfyMathExpression`、`VOSR2ModelLoader`、`VOSR2Upscale`、`ImageScaleToTotalPixels`、`H3FaceTrackCrop`、`MiniMaxH3ReferenceToVideo`、`VAEDecode`、`LoadImage`、`BlockSparseAttention`、`Label (rgthree)`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`H3FaceStitch`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
