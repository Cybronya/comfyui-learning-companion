---
key: 平台全量/【遇见AI】Minimax H3 latent upscale潜空间放大 REF2VA版_2090678350456123394.json
name: 【遇见AI】Minimax H3 latent upscale潜空间放大 REF2VA版_2090678350456123394
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【遇见AI】Minimax H3 latent upscale潜空间放大 REF2VA版_2090678350456123394.json
hash: c1a2f31ba435a3c1
coverage: 0.945946
learned_at: 2026-11-14 01:25:35
nodes: [VAEDecodeAudio, VAEDecodeAudio, ComfyMathExpression, VAEDecode, KSamplerSelect, BasicGuider, CreateVideo, LTXVConcatAVLatent, ResolutionSelector, BasicGuider, LTXVSeparateAVLatent, RandomNoise, RandomNoise, ManualSigmas, ManualSigmas, VAEDecode, SamplerCustomAdvanced, MiniMaxH3SigmaShift, ModelAttentionBackend, SplitSigmas, BasicScheduler, ManualSigmas, SamplerCustomAdvanced, PrimitiveFloat, VHS_VideoCombine, MiniMaxH3ReferenceToVideo, MarkdownNote, LoadImage, LoadImage, LoadImage, CLIPLoader, VAELoader, VAELoader, LoraLoaderModelOnly, UNETLoader, MinimaxH3LatentUpscaler3D, SaveVideo]
patterns: []
missing: []
---

# 平台全量/【遇见AI】Minimax H3 latent upscale潜空间放大 REF2VA版_2090678350456123394.json

> 来源文件 `comfyui_library/workflows/平台全量/【遇见AI】Minimax H3 latent upscale潜空间放大 REF2VA版_2090678350456123394.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `VAEDecodeAudio` ★核心
- `VAEDecodeAudio` ★核心
- `ComfyMathExpression`
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `CreateVideo`
- `LTXVConcatAVLatent`
- `ResolutionSelector`
- `BasicGuider`
- `LTXVSeparateAVLatent`
- `RandomNoise`
- `RandomNoise`
- `ManualSigmas`
- `ManualSigmas`
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `SplitSigmas`
- `BasicScheduler`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveFloat`
- `VHS_VideoCombine`
- `MiniMaxH3ReferenceToVideo`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `MinimaxH3LatentUpscaler3D`
- `SaveVideo`

## 知识

覆盖率 **95%**（35/37）

**有卡**：`VAEDecodeAudio`、`ComfyMathExpression`、`VAEDecode`、`KSamplerSelect`、`BasicGuider`、`CreateVideo`、`LTXVConcatAVLatent`、`ResolutionSelector`、`LTXVSeparateAVLatent`、`RandomNoise`、`ManualSigmas`、`SamplerCustomAdvanced`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`SplitSigmas`、`BasicScheduler`、`VHS_VideoCombine`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`UNETLoader`、`MinimaxH3LatentUpscaler3D`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
