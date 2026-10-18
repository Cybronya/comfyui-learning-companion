---
key: 视频生成/图生视频/minimax+taomate_workflow_2099426301223456770.json
name: minimax+taomate_workflow_2099426301223456770
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax+taomate_workflow_2099426301223456770.json
hash: 20dac58752a54aa3
coverage: 0.475
learned_at: 2026-10-17 01:44:52
nodes: [GetNode, GetNode, MarkdownNote, MarkdownNote, ComfyMathExpression, SetNode, RandomNoise, SetNode, GetNode, GetNode, GetNode, GetNode, BasicGuider, KSamplerSelect, GetNode, SetNode, SamplerCustomAdvanced, PrimitiveFloat, VAEDecode, SetNode, VAEDecodeAudio, SetNode, CLIPLoader, SetNode, VAELoader, VAELoader, SetNode, SetNode, SetNode, LoadImage, VHS_VideoCombine, PrimitiveNode, PrimitiveStringMultiline, LoraLoaderModelOnly, BasicScheduler, ResolutionSelector, MiniMaxH3MemoryEfficientSageAttentionPatch, BlockSparseAttention, MiniMaxH3ReferenceToVideo, UNETLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/minimax+taomate_workflow_2099426301223456770.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax+taomate_workflow_2099426301223456770.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（40 个）：
- `GetNode`
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
- `PrimitiveFloat`
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
- `SetNode`
- `LoadImage`
- `VHS_VideoCombine`
- `PrimitiveNode`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `ResolutionSelector`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BlockSparseAttention`
- `MiniMaxH3ReferenceToVideo`
- `UNETLoader` ★核心

## 知识

覆盖率 **48%**（19/40）

**有卡**：`ComfyMathExpression`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEDecodeAudio`、`CLIPLoader`、`VAELoader`、`LoadImage`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`BasicScheduler`、`ResolutionSelector`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BlockSparseAttention`、`MiniMaxH3ReferenceToVideo`、`UNETLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
