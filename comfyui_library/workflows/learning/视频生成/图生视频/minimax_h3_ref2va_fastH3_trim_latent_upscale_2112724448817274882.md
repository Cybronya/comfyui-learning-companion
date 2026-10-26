---
key: 视频生成/图生视频/minimax_h3_ref2va_fastH3_trim_latent_upscale_2112724448817274882.json
name: minimax_h3_ref2va_fastH3_trim_latent_upscale_2112724448817274882
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax_h3_ref2va_fastH3_trim_latent_upscale_2112724448817274882.json
hash: 02b97851b1e5d4fd
coverage: 0.833333
learned_at: 2026-10-26 22:14:47
nodes: [ManualSigmas, VAEDecode, VAEDecodeAudio, PrimitiveFloat, CLIPLoader, SamplerCustomAdvanced, SamplerCustomAdvanced, KSamplerSelect, MarkdownNote, MarkdownNote, BasicGuider, BasicGuider, VAELoader, UNETLoader, MiniMaxH3SigmaShift, ModelAttentionBackend, BlockSparseAttention, LTXVConcatAVLatent, BasicScheduler, ManualSigmas, SplitSigmas, ManualSigmas, PrimitiveFloat, PrimitiveNode, VAELoader, LoadImage, ResolutionSelector, ComfyMathExpression, LTXVSeparateAVLatent, MinimaxH3LatentUpscaler3D, RandomNoise, ResolutionSelector, MiniMaxH3ReferenceToVideo, MiniMaxH3ReferenceToVideo, VHS_VideoCombine, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/minimax_h3_ref2va_fastH3_trim_latent_upscale_2112724448817274882.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax_h3_ref2va_fastH3_trim_latent_upscale_2112724448817274882.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（36 个）：
- `ManualSigmas`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `PrimitiveFloat`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `BasicGuider`
- `BasicGuider`
- `VAELoader`
- `UNETLoader` ★核心
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `LTXVConcatAVLatent`
- `BasicScheduler`
- `ManualSigmas`
- `SplitSigmas`
- `ManualSigmas`
- `PrimitiveFloat`
- `PrimitiveNode`
- `VAELoader`
- `LoadImage`
- `ResolutionSelector`
- `ComfyMathExpression`
- `LTXVSeparateAVLatent`
- `MinimaxH3LatentUpscaler3D`
- `RandomNoise`
- `ResolutionSelector`
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3ReferenceToVideo`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`ManualSigmas`、`VAEDecode`、`VAEDecodeAudio`、`CLIPLoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`VAELoader`、`UNETLoader`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`BlockSparseAttention`、`LTXVConcatAVLatent`、`BasicScheduler`、`SplitSigmas`、`LoadImage`、`ResolutionSelector`、`ComfyMathExpression`、`LTXVSeparateAVLatent`、`MinimaxH3LatentUpscaler3D`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
