---
key: 视频生成/图生视频/10eros_singularity_base james02_2115355058022993921.json
name: 10eros_singularity_base james02_2115355058022993921
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/10eros_singularity_base james02_2115355058022993921.json
hash: 92dee9420bad91ca
coverage: 0.4
learned_at: 2026-10-30 17:57:07
nodes: [MarkdownNote, MarkdownNote, ComfyMathExpression, SetNode, PrimitiveNode, CLIPLoader, VAELoader, SetNode, SetNode, GetNode, GetNode, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, PrimitiveFloat, GetNode, VHS_VideoCombine, LoadImage, PrimitiveStringMultiline, VAELoader, RandomNoise, BasicScheduler, GetNode, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, GetNode, GetNode, SamplerCustomAdvanced, SetNode, BlockSparseAttention, MiniMaxH3ReferenceToVideo, GetNode, GetNode, KSamplerSelect, BasicGuider, ResolutionSelector, ModelAttentionBackend, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode]
patterns: []
missing: []
---

# 视频生成/图生视频/10eros_singularity_base james02_2115355058022993921.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/10eros_singularity_base james02_2115355058022993921.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（50 个）：
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `SetNode`
- `PrimitiveNode`
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
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `GetNode`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveStringMultiline`
- `VAELoader`
- `RandomNoise`
- `BasicScheduler`
- `GetNode`
- `SetNode`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `BlockSparseAttention`
- `MiniMaxH3ReferenceToVideo`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ResolutionSelector`
- `ModelAttentionBackend`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SetNode`

## 知识

覆盖率 **40%**（20/50）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`VHS_VideoCombine`、`LoadImage`、`RandomNoise`、`BasicScheduler`、`UNETLoader`、`VAEDecode`、`VAEDecodeAudio`、`SamplerCustomAdvanced`、`BlockSparseAttention`、`MiniMaxH3ReferenceToVideo`、`KSamplerSelect`、`BasicGuider`、`ResolutionSelector`、`ModelAttentionBackend`、`MiniMaxH3MemoryEfficientSageAttentionPatch`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
