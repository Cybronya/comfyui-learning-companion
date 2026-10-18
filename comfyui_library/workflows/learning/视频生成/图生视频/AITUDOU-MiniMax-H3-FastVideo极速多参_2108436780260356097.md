---
key: 视频生成/图生视频/AITUDOU-MiniMax-H3-FastVideo极速多参_2108436780260356097.json
name: AITUDOU-MiniMax-H3-FastVideo极速多参_2108436780260356097
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AITUDOU-MiniMax-H3-FastVideo极速多参_2108436780260356097.json
hash: 61361e482fbb8f54
coverage: 0.402597
learned_at: 2026-10-17 22:17:12
nodes: [SetNode, SetNode, SetNode, LoadImage, LoadImage, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, LoadImage, LoadImage, SetNode, SetNode, LoadImage, LoadImage, GetNode, GetNode, SetNode, SetNode, MarkdownNote, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, ComfyMathExpression, SetNode, SetNode, VAEDecode, SetNode, Label (rgthree), Label (rgthree), VAELoader, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, MiniMaxH3ReferenceToVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, RandomNoise, SamplerCustomAdvanced, GetNode, BasicGuider, BasicScheduler, Label (rgthree), KSamplerSelect, ModelAttentionBackend, MiniMaxH3MemoryEfficientSageAttentionPatch, BlockSparseAttention, SetNode, VHS_VideoCombine, CLIPLoader, UNETLoader, easy float, PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), LoadImage, LoadImage, LoadImage, ResolutionSelector]
patterns: []
missing: []
---

# 视频生成/图生视频/AITUDOU-MiniMax-H3-FastVideo极速多参_2108436780260356097.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/AITUDOU-MiniMax-H3-FastVideo极速多参_2108436780260356097.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（77 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `MarkdownNote`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `VAELoader`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
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
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `BasicGuider`
- `BasicScheduler`
- `Label (rgthree)`
- `KSamplerSelect` ★核心
- `ModelAttentionBackend`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BlockSparseAttention`
- `SetNode`
- `VHS_VideoCombine`
- `CLIPLoader`
- `UNETLoader` ★核心
- `easy float`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`

## 知识

覆盖率 **40%**（31/77）

**有卡**：`LoadImage`、`VAEDecodeAudio`、`ComfyMathExpression`、`VAEDecode`、`Label (rgthree)`、`VAELoader`、`MiniMaxH3ReferenceToVideo`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicGuider`、`BasicScheduler`、`KSamplerSelect`、`ModelAttentionBackend`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BlockSparseAttention`、`VHS_VideoCombine`、`CLIPLoader`、`UNETLoader`、`easy float`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
