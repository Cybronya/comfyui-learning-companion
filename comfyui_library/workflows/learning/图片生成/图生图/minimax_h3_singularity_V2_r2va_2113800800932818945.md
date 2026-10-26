---
key: 图片生成/图生图/minimax_h3_singularity_V2_r2va_2113800800932818945.json
name: minimax_h3_singularity_V2_r2va_2113800800932818945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/minimax_h3_singularity_V2_r2va_2113800800932818945.json
hash: 8a9ef4224fd9a09a
coverage: 0.411765
learned_at: 2026-10-26 22:04:12
nodes: [MarkdownNote, MarkdownNote, ComfyMathExpression, SetNode, PrimitiveNode, CLIPLoader, VAELoader, SetNode, ResolutionSelector, SetNode, GetNode, GetNode, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, PrimitiveFloat, LoraLoaderModelOnly, SetNode, GetNode, GetNode, KSamplerSelect, GetNode, ConditioningZeroOut, GetNode, SetNode, BasicScheduler, VAEDecode, GetNode, VAEDecodeAudio, VHS_VideoCombine, SelfLiftH3Sampler, VAELoader, UNETLoader, LoadImage, SetNode, ModelAttentionBackend, BlockSparseAttention, PrimitiveStringMultiline, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, EmptyImage, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/minimax_h3_singularity_V2_r2va_2113800800932818945.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/minimax_h3_singularity_V2_r2va_2113800800932818945.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `SetNode`
- `PrimitiveNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `ResolutionSelector`
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
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `ConditioningZeroOut`
- `GetNode`
- `SetNode`
- `BasicScheduler`
- `VAEDecode` ★核心
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `SelfLiftH3Sampler` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `SetNode`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `PrimitiveStringMultiline`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `EmptyImage`
- `PreviewImage`

## 知识

覆盖率 **41%**（21/51）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`SelfLiftH3Sampler`、`UNETLoader`、`LoadImage`、`ModelAttentionBackend`、`BlockSparseAttention`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ReferenceToVideo`、`EmptyImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
