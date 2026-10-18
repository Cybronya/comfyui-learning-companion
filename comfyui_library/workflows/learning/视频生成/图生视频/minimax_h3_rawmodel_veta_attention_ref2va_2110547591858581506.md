---
key: 视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va_2110547591858581506.json
name: minimax_h3_rawmodel_veta_attention_ref2va_2110547591858581506
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va_2110547591858581506.json
hash: e9699979d3e6a056
coverage: 0.5
learned_at: 2026-10-18 00:24:05
nodes: [GetNode, MarkdownNote, MarkdownNote, ComfyMathExpression, SetNode, RandomNoise, SetNode, GetNode, GetNode, GetNode, GetNode, BasicGuider, KSamplerSelect, GetNode, SetNode, SamplerCustomAdvanced, ResolutionSelector, PrimitiveFloat, BasicScheduler, BlockSparseAttention, MiniMaxH3MemoryEfficientSageAttentionPatch, VAEDecode, SetNode, VAEDecodeAudio, SetNode, CLIPLoader, SetNode, VAELoader, VAELoader, SetNode, SetNode, VHS_VideoCombine, PrimitiveNode, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, LoraLoaderModelOnly, VedaSparseAttention, SetNode, LoadImage, UNETLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va_2110547591858581506.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va_2110547591858581506.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（40 个）：
- `GetNode`
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `SetNode`
- `RandomNoise`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `GetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `ResolutionSelector`
- `PrimitiveFloat`
- `BasicScheduler`
- `BlockSparseAttention`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VAEDecode` ★核心
- `SetNode`
- `VAEDecodeAudio` ★核心
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `PrimitiveNode`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `VedaSparseAttention`
- `SetNode`
- `LoadImage`
- `UNETLoader` ★核心

## 知识

覆盖率 **50%**（20/40）

**有卡**：`ComfyMathExpression`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`ResolutionSelector`、`BasicScheduler`、`BlockSparseAttention`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VAEDecode`、`VAEDecodeAudio`、`CLIPLoader`、`VAELoader`、`VHS_VideoCombine`、`MiniMaxH3ReferenceToVideo`、`LoraLoaderModelOnly`、`VedaSparseAttention`、`LoadImage`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
