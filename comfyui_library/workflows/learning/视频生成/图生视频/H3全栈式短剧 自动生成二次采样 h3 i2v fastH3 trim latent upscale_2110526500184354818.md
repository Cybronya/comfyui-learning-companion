---
key: 视频生成/图生视频/H3全栈式短剧 自动生成二次采样 h3 i2v fastH3 trim latent upscale_2110526500184354818.json
name: H3全栈式短剧 自动生成二次采样 h3 i2v fastH3 trim latent upscale_2110526500184354818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/H3全栈式短剧 自动生成二次采样 h3 i2v fastH3 trim latent upscale_2110526500184354818.json
hash: 76845534bbbc88f8
coverage: 0.833333
learned_at: 2026-10-18 00:23:01
nodes: [ManualSigmas, VAELoader, MiniMaxH3ImageToVideo, PrimitiveFloat, CLIPLoader, ComfyMathExpression, SamplerCustomAdvanced, SamplerCustomAdvanced, KSamplerSelect, MarkdownNote, MarkdownNote, BasicGuider, BasicGuider, RandomNoise, VAELoader, UNETLoader, MiniMaxH3SigmaShift, ModelAttentionBackend, BlockSparseAttention, MiniMaxH3ImageToVideo, BasicScheduler, ResolutionSelector, ManualSigmas, SplitSigmas, ManualSigmas, PrimitiveFloat, LTXVSeparateAVLatent, LTXVConcatAVLatent, ResolutionSelector, MinimaxH3LatentUpscaler3D, PrimitiveNode, PrimitiveStringMultiline, LoadImage, VAEDecode, VAEDecodeAudio, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/H3全栈式短剧 自动生成二次采样 h3 i2v fastH3 trim latent upscale_2110526500184354818.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/H3全栈式短剧 自动生成二次采样 h3 i2v fastH3 trim latent upscale_2110526500184354818.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（36 个）：
- `ManualSigmas`
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
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `ResolutionSelector`
- `MinimaxH3LatentUpscaler3D`
- `PrimitiveNode`
- `PrimitiveStringMultiline`
- `LoadImage`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`

## 知识

覆盖率 **83%**（30/36）

**有卡**：`ManualSigmas`、`VAELoader`、`MiniMaxH3ImageToVideo`、`CLIPLoader`、`ComfyMathExpression`、`SamplerCustomAdvanced`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`UNETLoader`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`BlockSparseAttention`、`BasicScheduler`、`ResolutionSelector`、`SplitSigmas`、`LTXVSeparateAVLatent`、`LTXVConcatAVLatent`、`MinimaxH3LatentUpscaler3D`、`LoadImage`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
