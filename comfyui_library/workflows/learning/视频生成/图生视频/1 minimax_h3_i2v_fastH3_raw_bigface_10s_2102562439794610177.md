---
key: 视频生成/图生视频/1 minimax_h3_i2v_fastH3_raw_bigface_10s_2102562439794610177.json
name: 1 minimax_h3_i2v_fastH3_raw_bigface_10s_2102562439794610177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1 minimax_h3_i2v_fastH3_raw_bigface_10s_2102562439794610177.json
hash: 94cb72072e4e9997
coverage: 0.791667
learned_at: 2026-10-17 02:28:41
nodes: [VAEDecode, VAEDecodeAudio, VAELoader, MiniMaxH3ImageToVideo, PrimitiveFloat, CLIPLoader, ComfyMathExpression, SamplerCustomAdvanced, KSamplerSelect, MarkdownNote, MarkdownNote, BasicGuider, RandomNoise, VAELoader, UNETLoader, MiniMaxH3SigmaShift, ModelAttentionBackend, BlockSparseAttention, BasicScheduler, VHS_VideoCombine, PrimitiveStringMultiline, ResolutionSelector, PrimitiveNode, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/1 minimax_h3_i2v_fastH3_raw_bigface_10s_2102562439794610177.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1 minimax_h3_i2v_fastH3_raw_bigface_10s_2102562439794610177.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（24 个）：
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VAELoader`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `CLIPLoader`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `BasicGuider`
- `RandomNoise`
- `VAELoader`
- `UNETLoader` ★核心
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `BasicScheduler`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `PrimitiveNode`
- `LoadImage`

## 知识

覆盖率 **79%**（19/24）

**有卡**：`VAEDecode`、`VAEDecodeAudio`、`VAELoader`、`MiniMaxH3ImageToVideo`、`CLIPLoader`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`UNETLoader`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`BlockSparseAttention`、`BasicScheduler`、`VHS_VideoCombine`、`ResolutionSelector`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
