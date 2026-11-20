---
key: 视频生成/图生视频/10eros_singularity_latent_upscale_James_2115355904576147458.json
name: 10eros_singularity_latent_upscale_James_2115355904576147458
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/10eros_singularity_latent_upscale_James_2115355904576147458.json
hash: 0fc0386d5fd7a6fc
coverage: 0.403846
learned_at: 2026-10-30 17:57:09
nodes: [MarkdownNote, MarkdownNote, ComfyMathExpression, SetNode, PrimitiveNode, CLIPLoader, VAELoader, SetNode, ResolutionSelector, SetNode, GetNode, GetNode, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, PrimitiveFloat, SetNode, GetNode, GetNode, KSamplerSelect, GetNode, ConditioningZeroOut, GetNode, SetNode, BasicScheduler, VAEDecode, GetNode, VAEDecodeAudio, VHS_VideoCombine, SelfLiftH3Sampler, VAELoader, UNETLoader, LoadImage, SetNode, ModelAttentionBackend, BlockSparseAttention, PrimitiveStringMultiline, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, LoadImage, ImageScaleToTotalPixels, SetNode, GetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/10eros_singularity_latent_upscale_James_2115355904576147458.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/10eros_singularity_latent_upscale_James_2115355904576147458.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（52 个）：
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
- `LoadImage`
- `ImageScaleToTotalPixels`
- `SetNode`
- `GetNode`

## 知识

覆盖率 **40%**（21/52）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`ImageScaleToTotalPixels`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`SelfLiftH3Sampler`、`UNETLoader`、`LoadImage`、`ModelAttentionBackend`、`BlockSparseAttention`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ReferenceToVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
