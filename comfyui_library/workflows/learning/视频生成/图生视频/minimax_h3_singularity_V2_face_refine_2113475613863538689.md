---
key: 视频生成/图生视频/minimax_h3_singularity_V2_face_refine_2113475613863538689.json
name: minimax_h3_singularity_V2_face_refine_2113475613863538689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax_h3_singularity_V2_face_refine_2113475613863538689.json
hash: 7cad6db67293cbf6
coverage: 0.409091
learned_at: 2026-10-26 22:14:48
nodes: [MarkdownNote, MarkdownNote, ComfyMathExpression, SetNode, CLIPLoader, VAELoader, SetNode, SetNode, GetNode, GetNode, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, VAELoader, SetNode, GetNode, GetNode, GetNode, PrimitiveFloat, GetNode, GetNode, GetNode, ConditioningZeroOut, GetNode, SetNode, GetNode, LoadImage, PrimitiveNode, UNETLoader, SelfLiftH3Sampler, ResolutionSelector, GetNode, VOSR2ModelLoader, H3FaceStitch, VAEDecode, SetNode, VAEDecodeAudio, PreviewAny, VHS_VideoCombine, VOSR2Upscale, GetNode, SetNode, SetNode, GetNode, GetNode, VHS_VideoCombine, SetNode, GetNode, MiniMaxH3SigmaShift, SetNode, SetNode, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, SetNode, VHS_VideoCombine, H3FaceTrackCrop, KSamplerSelect, BasicScheduler, ModelAttentionBackend, LoraLoaderModelOnly, BlockSparseAttention, MiniMaxH3MemoryEfficientSageAttentionPatch]
patterns: []
missing: []
---

# 视频生成/图生视频/minimax_h3_singularity_V2_face_refine_2113475613863538689.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax_h3_singularity_V2_face_refine_2113475613863538689.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（66 个）：
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `GetNode`
- `SetNode`
- `GetNode`
- `LoadImage`
- `PrimitiveNode`
- `UNETLoader` ★核心
- `SelfLiftH3Sampler` ★核心
- `ResolutionSelector`
- `GetNode`
- `VOSR2ModelLoader`
- `H3FaceStitch`
- `VAEDecode` ★核心
- `SetNode`
- `VAEDecodeAudio` ★核心
- `PreviewAny`
- `VHS_VideoCombine`
- `VOSR2Upscale`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `MiniMaxH3SigmaShift`
- `SetNode`
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `SetNode`
- `VHS_VideoCombine`
- `H3FaceTrackCrop`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ModelAttentionBackend`
- `LoraLoaderModelOnly` ★核心
- `BlockSparseAttention`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`

## 知识

覆盖率 **41%**（27/66）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`ConditioningZeroOut`、`LoadImage`、`UNETLoader`、`SelfLiftH3Sampler`、`ResolutionSelector`、`VOSR2ModelLoader`、`H3FaceStitch`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`VOSR2Upscale`、`MiniMaxH3SigmaShift`、`MiniMaxH3ReferenceToVideo`、`H3FaceTrackCrop`、`KSamplerSelect`、`BasicScheduler`、`ModelAttentionBackend`、`LoraLoaderModelOnly`、`BlockSparseAttention`、`MiniMaxH3MemoryEfficientSageAttentionPatch`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
