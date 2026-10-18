---
key: 视频生成/图生视频/minimax_h3_i2v_fastH3_trim_multiframe_2109449722762190850.json
name: minimax_h3_i2v_fastH3_trim_multiframe_2109449722762190850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax_h3_i2v_fastH3_trim_multiframe_2109449722762190850.json
hash: f9be3f007e939246
coverage: 0.657895
learned_at: 2026-10-18 00:24:05
nodes: [VAEDecode, VAEDecodeAudio, VAELoader, CLIPLoader, ComfyMathExpression, SamplerCustomAdvanced, KSamplerSelect, MarkdownNote, MarkdownNote, BasicGuider, RandomNoise, VAELoader, UNETLoader, MiniMaxH3SigmaShift, ModelAttentionBackend, BlockSparseAttention, BasicScheduler, ResolutionSelector, VHS_VideoCombine, SetNode, SetNode, SetNode, SetNode, MiniMaxH3ImageToVideo, PrimitiveFloat, SetNode, SetNode, PrimitiveNode, PrimitiveStringMultiline, MiniMaxH3AddGuide, MiniMaxH3AddGuide, PreviewAny, MiniMaxH3AddGuide, GetNode, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/minimax_h3_i2v_fastH3_trim_multiframe_2109449722762190850.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax_h3_i2v_fastH3_trim_multiframe_2109449722762190850.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（38 个）：
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VAELoader`
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
- `ResolutionSelector`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `PrimitiveNode`
- `PrimitiveStringMultiline`
- `MiniMaxH3AddGuide`
- `MiniMaxH3AddGuide`
- `PreviewAny`
- `MiniMaxH3AddGuide`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **66%**（25/38）

**有卡**：`VAEDecode`、`VAEDecodeAudio`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`UNETLoader`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`BlockSparseAttention`、`BasicScheduler`、`ResolutionSelector`、`VHS_VideoCombine`、`MiniMaxH3ImageToVideo`、`MiniMaxH3AddGuide`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
