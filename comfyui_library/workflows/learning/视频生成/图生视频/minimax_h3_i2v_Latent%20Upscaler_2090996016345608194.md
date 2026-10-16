---
key: 视频生成/图生视频/minimax_h3_i2v_Latent%20Upscaler_2090996016345608194.json
name: minimax_h3_i2v_Latent%20Upscaler_2090996016345608194
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/minimax_h3_i2v_Latent%20Upscaler_2090996016345608194.json
hash: 725fbc94ba45d6c2
coverage: 0.846154
learned_at: 2026-10-16 22:30:51
nodes: [VAEDecodeAudio, VAELoader, VAEDecode, VAELoader, LTXVConcatAVLatent, ManualSigmas, KSamplerSelect, ManualSigmas, MarkdownNote, MarkdownNote, BasicGuider, BasicGuider, MarkdownNote, MiniMaxH3SigmaShift, UNETLoader, CLIPLoader, VAEDecodeAudio, SamplerCustomAdvanced, ComfyMathExpression, BasicScheduler, SplitSigmas, ManualSigmas, VHS_VideoCombine, PrimitiveFloat, PrimitiveFloat, RandomNoise, MiniMaxH3ImageToVideo, MiniMaxH3ImageToVideo, LoraLoaderModelOnly, ModelPreviewOverrideKJ, ImageResizeKJv2, LTXVSeparateAVLatent, SamplerCustomAdvanced, MinimaxH3LatentUpscaler3D, ModelAttentionBackend, ResolutionSelector, ResolutionSelector, PrimitiveStringMultiline, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/minimax_h3_i2v_Latent%20Upscaler_2090996016345608194.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/minimax_h3_i2v_Latent%20Upscaler_2090996016345608194.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（39 个）：
- `VAEDecodeAudio` ★核心
- `VAELoader`
- `VAEDecode` ★核心
- `VAELoader`
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `MarkdownNote`
- `MarkdownNote`
- `BasicGuider`
- `BasicGuider`
- `MarkdownNote`
- `MiniMaxH3SigmaShift`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `ComfyMathExpression`
- `BasicScheduler`
- `SplitSigmas`
- `ManualSigmas`
- `VHS_VideoCombine`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `RandomNoise`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ImageToVideo`
- `LoraLoaderModelOnly` ★核心
- `ModelPreviewOverrideKJ`
- `ImageResizeKJv2`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `MinimaxH3LatentUpscaler3D`
- `ModelAttentionBackend`
- `ResolutionSelector`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `LoadImage`

## 知识

覆盖率 **85%**（33/39）

**有卡**：`VAEDecodeAudio`、`VAELoader`、`VAEDecode`、`LTXVConcatAVLatent`、`ManualSigmas`、`KSamplerSelect`、`BasicGuider`、`MiniMaxH3SigmaShift`、`UNETLoader`、`CLIPLoader`、`SamplerCustomAdvanced`、`ComfyMathExpression`、`BasicScheduler`、`SplitSigmas`、`VHS_VideoCombine`、`RandomNoise`、`MiniMaxH3ImageToVideo`、`LoraLoaderModelOnly`、`ModelPreviewOverrideKJ`、`ImageResizeKJv2`、`LTXVSeparateAVLatent`、`MinimaxH3LatentUpscaler3D`、`ModelAttentionBackend`、`ResolutionSelector`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
