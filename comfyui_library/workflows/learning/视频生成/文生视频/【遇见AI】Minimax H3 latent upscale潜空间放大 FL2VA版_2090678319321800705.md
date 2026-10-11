---
key: 视频生成/文生视频/【遇见AI】Minimax H3 latent upscale潜空间放大 FL2VA版_2090678319321800705.json
name: 【遇见AI】Minimax H3 latent upscale潜空间放大 FL2VA版_2090678319321800705
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/【遇见AI】Minimax H3 latent upscale潜空间放大 FL2VA版_2090678319321800705.json
hash: 381765e73e2ff586
coverage: 0.944444
learned_at: 2026-10-11 21:19:52
nodes: [VAEDecodeAudio, VAEDecodeAudio, ComfyMathExpression, VAEDecode, KSamplerSelect, BasicGuider, CreateVideo, LTXVConcatAVLatent, BasicGuider, LTXVSeparateAVLatent, RandomNoise, RandomNoise, ManualSigmas, ManualSigmas, VAEDecode, SamplerCustomAdvanced, ModelAttentionBackend, SplitSigmas, BasicScheduler, ManualSigmas, SamplerCustomAdvanced, MiniMaxH3ImageToVideo, ResolutionSelector, MiniMaxH3SigmaShift, PrimitiveFloat, VHS_VideoCombine, MarkdownNote, LoadImage, LoadImage, UNETLoader, CLIPLoader, VAELoader, VAELoader, LoraLoaderModelOnly, SaveVideo, MinimaxH3LatentUpscaler3D]
patterns: []
missing: []
---

# 视频生成/文生视频/【遇见AI】Minimax H3 latent upscale潜空间放大 FL2VA版_2090678319321800705.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/【遇见AI】Minimax H3 latent upscale潜空间放大 FL2VA版_2090678319321800705.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `VAEDecodeAudio` ★核心
- `VAEDecodeAudio` ★核心
- `ComfyMathExpression`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `CreateVideo`
- `LTXVConcatAVLatent`
- `BasicGuider`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `RandomNoise`
- `ManualSigmas`
- `ManualSigmas`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `ModelAttentionBackend`
- `SplitSigmas`
- `BasicScheduler`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3ImageToVideo`
- `ResolutionSelector`
- `MiniMaxH3SigmaShift`
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `SaveVideo`
- `MinimaxH3LatentUpscaler3D`

## 知识

覆盖率 **94%**（34/36）

**有卡**：`VAEDecodeAudio`、`ComfyMathExpression`、`VAEDecode`、`KSamplerSelect`、`BasicGuider`、`CreateVideo`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`RandomNoise`、`ManualSigmas`、`SamplerCustomAdvanced`、`ModelAttentionBackend`、`SplitSigmas`、`BasicScheduler`、`MiniMaxH3ImageToVideo`、`ResolutionSelector`、`MiniMaxH3SigmaShift`、`VHS_VideoCombine`、`LoadImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`SaveVideo`、`MinimaxH3LatentUpscaler3D`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
