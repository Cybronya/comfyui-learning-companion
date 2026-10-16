---
key: 视频生成/图生视频/Minimax-H3-多参图生视频+双采+Lantent upscale放大_2091376603443064833.json
name: Minimax-H3-多参图生视频+双采+Lantent upscale放大_2091376603443064833
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax-H3-多参图生视频+双采+Lantent upscale放大_2091376603443064833.json
hash: 479cf6cd24c6e146
coverage: 0.861111
learned_at: 2026-10-16 22:30:40
nodes: [ManualSigmas, LTXVConcatAVLatent, ModelPreviewOverrideKJ, VAEDecodeAudio, SamplerCustomAdvanced, KSamplerSelect, SamplerCustomAdvanced, ManualSigmas, VAEDecode, BasicGuider, BasicGuider, ManualSigmas, ModelAttentionBackend, MiniMaxH3SigmaShift, LoraLoaderModelOnly, BasicScheduler, SplitSigmas, MinimaxH3LatentUpscaler3D, LTXVSeparateAVLatent, CreateVideo, SaveVideo, MarkdownNote, MarkdownNote, ResolutionSelector, PrimitiveFloat, PrimitiveFloat, LoadImage, LoadImage, ComfyMathExpression, CLIPLoader, VAELoader, VAELoader, UNETLoader, MiniMaxH3ReferenceToVideo, RandomNoise, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax-H3-多参图生视频+双采+Lantent upscale放大_2091376603443064833.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax-H3-多参图生视频+双采+Lantent upscale放大_2091376603443064833.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `ManualSigmas`
- `LTXVConcatAVLatent`
- `ModelPreviewOverrideKJ`
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `ManualSigmas`
- `VAEDecode` ★核心
- `BasicGuider`
- `BasicGuider`
- `ManualSigmas`
- `ModelAttentionBackend`
- `MiniMaxH3SigmaShift`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `SplitSigmas`
- `MinimaxH3LatentUpscaler3D`
- `LTXVSeparateAVLatent`
- `CreateVideo`
- `SaveVideo`
- `MarkdownNote`
- `MarkdownNote`
- `ResolutionSelector`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `LoadImage`
- `LoadImage`
- `ComfyMathExpression`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **86%**（31/36）

**有卡**：`ManualSigmas`、`LTXVConcatAVLatent`、`ModelPreviewOverrideKJ`、`VAEDecodeAudio`、`SamplerCustomAdvanced`、`KSamplerSelect`、`VAEDecode`、`BasicGuider`、`ModelAttentionBackend`、`MiniMaxH3SigmaShift`、`LoraLoaderModelOnly`、`BasicScheduler`、`SplitSigmas`、`MinimaxH3LatentUpscaler3D`、`LTXVSeparateAVLatent`、`CreateVideo`、`SaveVideo`、`ResolutionSelector`、`LoadImage`、`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`MiniMaxH3ReferenceToVideo`、`RandomNoise`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
