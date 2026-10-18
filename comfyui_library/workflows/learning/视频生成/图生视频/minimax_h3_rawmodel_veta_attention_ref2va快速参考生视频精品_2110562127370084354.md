---
key: 视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va快速参考生视频精品_2110562127370084354.json
name: minimax_h3_rawmodel_veta_attention_ref2va快速参考生视频精品_2110562127370084354
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va快速参考生视频精品_2110562127370084354.json
hash: 972ab5680a0014f8
coverage: 0.533333
learned_at: 2026-10-18 00:24:05
nodes: [GetNode, MarkdownNote, MarkdownNote, ComfyMathExpression, SetNode, RandomNoise, SetNode, GetNode, GetNode, GetNode, GetNode, BasicGuider, KSamplerSelect, GetNode, SetNode, SamplerCustomAdvanced, BasicScheduler, BlockSparseAttention, MiniMaxH3MemoryEfficientSageAttentionPatch, VAEDecode, SetNode, VAEDecodeAudio, SetNode, CLIPLoader, SetNode, VAELoader, VAELoader, SetNode, SetNode, VHS_VideoCombine, LoraLoaderModelOnly, SetNode, MiniMaxH3ReferenceToVideo, VedaSparseAttention, UNETLoader, PrimitiveStringMultiline, UNETLoader, LoadImage, LoadImage, LoadImage, QwenH3PromptLocal, PrimitiveStringMultiline, PrimitiveNode, PrimitiveFloat, ResolutionSelector]
patterns: []
missing: []
---

# 视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va快速参考生视频精品_2110562127370084354.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax_h3_rawmodel_veta_attention_ref2va快速参考生视频精品_2110562127370084354.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（45 个）：
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
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `VedaSparseAttention`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `UNETLoader` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenH3PromptLocal`
- `PrimitiveStringMultiline`
- `PrimitiveNode`
- `PrimitiveFloat`
- `ResolutionSelector`

## 知识

覆盖率 **53%**（24/45）

**有卡**：`ComfyMathExpression`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicScheduler`、`BlockSparseAttention`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VAEDecode`、`VAEDecodeAudio`、`CLIPLoader`、`VAELoader`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`MiniMaxH3ReferenceToVideo`、`VedaSparseAttention`、`UNETLoader`、`LoadImage`、`QwenH3PromptLocal`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
