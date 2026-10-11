---
key: 视频生成/文生视频/Minimax-h3-文生、图生视频+双采+Lantent upscale放大_2091360806108745730.json
name: Minimax-h3-文生、图生视频+双采+Lantent upscale放大_2091360806108745730
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax-h3-文生、图生视频+双采+Lantent upscale放大_2091360806108745730.json
hash: 8ed8d39d529d6e2e
coverage: 0.837838
learned_at: 2026-10-11 21:19:48
nodes: [VAEDecode, VAEDecodeAudio, ResolutionSelector, KSamplerSelect, MarkdownNote, MarkdownNote, BasicGuider, MarkdownNote, PrimitiveFloat, LoraLoaderModelOnly, UNETLoader, VAELoader, VAELoader, CLIPLoader, ModelPreviewOverrideKJ, LTXVConcatAVLatent, RandomNoise, SamplerCustomAdvanced, PrimitiveStringMultiline, LTXVSeparateAVLatent, SamplerCustomAdvanced, BasicGuider, ModelAttentionBackend, ManualSigmas, CreateVideo, SaveVideo, ManualSigmas, ManualSigmas, BasicScheduler, SplitSigmas, LoadImage, LoadImage, ComfyMathExpression, PrimitiveFloat, MinimaxH3LatentUpscaler3D, MiniMaxH3ImageToVideo, MiniMaxH3SigmaShift]
patterns: []
missing: []
---

# 视频生成/文生视频/Minimax-h3-文生、图生视频+双采+Lantent upscale放大_2091360806108745730.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax-h3-文生、图生视频+双采+Lantent upscale放大_2091360806108745730.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `ResolutionSelector`
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `BasicGuider`
- `MarkdownNote`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `ModelPreviewOverrideKJ`
- `LTXVConcatAVLatent`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveStringMultiline`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `ModelAttentionBackend`
- `ManualSigmas`
- `CreateVideo`
- `SaveVideo`
- `ManualSigmas`
- `ManualSigmas`
- `BasicScheduler`
- `SplitSigmas`
- `LoadImage`
- `LoadImage`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `MinimaxH3LatentUpscaler3D`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3SigmaShift`

## 知识

覆盖率 **84%**（31/37）

**有卡**：`VAEDecode`、`VAEDecodeAudio`、`ResolutionSelector`、`KSamplerSelect`、`BasicGuider`、`LoraLoaderModelOnly`、`UNETLoader`、`VAELoader`、`CLIPLoader`、`ModelPreviewOverrideKJ`、`LTXVConcatAVLatent`、`RandomNoise`、`SamplerCustomAdvanced`、`LTXVSeparateAVLatent`、`ModelAttentionBackend`、`ManualSigmas`、`CreateVideo`、`SaveVideo`、`BasicScheduler`、`SplitSigmas`、`LoadImage`、`ComfyMathExpression`、`MinimaxH3LatentUpscaler3D`、`MiniMaxH3ImageToVideo`、`MiniMaxH3SigmaShift`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
