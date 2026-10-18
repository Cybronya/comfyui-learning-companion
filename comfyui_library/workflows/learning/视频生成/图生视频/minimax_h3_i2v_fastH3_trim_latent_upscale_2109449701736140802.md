---
key: 视频生成/图生视频/minimax_h3_i2v_fastH3_trim_latent_upscale_2109449701736140802.json
name: minimax_h3_i2v_fastH3_trim_latent_upscale_2109449701736140802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax_h3_i2v_fastH3_trim_latent_upscale_2109449701736140802.json
hash: c57ff097b92f9a2b
coverage: 0.833333
learned_at: 2026-10-18 00:24:05
nodes: [ManualSigmas, VAEDecode, VAEDecodeAudio, VAELoader, MiniMaxH3ImageToVideo, PrimitiveFloat, CLIPLoader, ComfyMathExpression, SamplerCustomAdvanced, SamplerCustomAdvanced, KSamplerSelect, MarkdownNote, MarkdownNote, BasicGuider, BasicGuider, RandomNoise, PrimitiveStringMultiline, VAELoader, UNETLoader, MiniMaxH3SigmaShift, ModelAttentionBackend, BlockSparseAttention, MiniMaxH3ImageToVideo, BasicScheduler, ResolutionSelector, ManualSigmas, SplitSigmas, ManualSigmas, PrimitiveFloat, VHS_VideoCombine, PrimitiveNode, LoadImage, LTXVSeparateAVLatent, LTXVConcatAVLatent, ResolutionSelector, MinimaxH3LatentUpscaler3D]
patterns: []
missing: []
---

# 视频生成/图生视频/minimax_h3_i2v_fastH3_trim_latent_upscale_2109449701736140802.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax_h3_i2v_fastH3_trim_latent_upscale_2109449701736140802.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（36 个）：
- `ManualSigmas`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VAELoader`
- `MiniMaxH3ImageToVideo`
- `PrimitiveFloat`
- `CLIPLoader`
- `ComfyMathExpression`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `BasicGuider`
- `BasicGuider`
- `RandomNoise`
- `PrimitiveStringMultiline`
- `VAELoader`
- `UNETLoader` ★核心
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `MiniMaxH3ImageToVideo`
- `BasicScheduler`
- `ResolutionSelector`
- `ManualSigmas`
- `SplitSigmas`
- `ManualSigmas`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `PrimitiveNode`
- `LoadImage`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `ResolutionSelector`
- `MinimaxH3LatentUpscaler3D`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`ManualSigmas`、`VAEDecode`、`VAEDecodeAudio`、`VAELoader`、`MiniMaxH3ImageToVideo`、`CLIPLoader`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`UNETLoader`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`BlockSparseAttention`、`BasicScheduler`、`ResolutionSelector`、`SplitSigmas`、`VHS_VideoCombine`、`LoadImage`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`MinimaxH3LatentUpscaler3D`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
