---
key: 视频生成/文生视频/Minimax H3多参 Taomate 3 steplora 二采生视频_2100938444443832322.json
name: Minimax H3多参 Taomate 3 steplora 二采生视频_2100938444443832322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Minimax H3多参 Taomate 3 steplora 二采生视频_2100938444443832322.json
hash: 176203c9bc4860a8
coverage: 0.85
learned_at: 2026-10-15 22:46:36
nodes: [VAELoader, VAELoader, VAEDecode, VAEDecodeAudio, LTXVConcatAVLatent, ModelPreviewOverrideKJ, VAEDecodeAudio, SamplerCustomAdvanced, KSamplerSelect, VAEDecode, MarkdownNote, MarkdownNote, UNETLoader, RandomNoise, ComfyMathExpression, CreateVideo, SaveVideo, LoadImage, PrimitiveFloat, MiniMaxH3SigmaShift, ModelAttentionBackend, BasicGuider, ManualSigmas, MinimaxH3LatentUpscaler3D, ClownsharKSampler_Beta, ClownsharKSampler_Beta, MarkdownNote, MarkdownNote, SeedGenerator, ConditioningZeroOut, LTXVSeparateAVLatent, MiniMaxH3ReferenceToVideo, Text, PrimitiveFloat, ResolutionSelector, LoraLoaderModelOnly, LoraLoaderModelOnly, CreateVideo, SaveVideo, CLIPLoader]
patterns: []
missing: []
parameters: {"cfg": 7, "denoise": 1, "sampler_name": 3, "scheduler": 1, "seed": 0.3, "steps": "simple"}
---

# 视频生成/文生视频/Minimax H3多参 Taomate 3 steplora 二采生视频_2100938444443832322.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Minimax H3多参 Taomate 3 steplora 二采生视频_2100938444443832322.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（40 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `LTXVConcatAVLatent`
- `ModelPreviewOverrideKJ`
- `VAEDecodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `VAEDecode` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `RandomNoise`
- `ComfyMathExpression`
- `CreateVideo`
- `SaveVideo`
- `LoadImage`
- `PrimitiveFloat`
- `MiniMaxH3SigmaShift`
- `ModelAttentionBackend`
- `BasicGuider`
- `ManualSigmas`
- `MinimaxH3LatentUpscaler3D`
- `ClownsharKSampler_Beta` ★核心
- `ClownsharKSampler_Beta` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `SeedGenerator`
- `ConditioningZeroOut`
- `LTXVSeparateAVLatent`
- `MiniMaxH3ReferenceToVideo`
- `Text`
- `PrimitiveFloat`
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CreateVideo`
- `SaveVideo`
- `CLIPLoader`

## 关键参数

- `seed` = `0.3`
- `steps` = `simple`
- `cfg` = `7`
- `sampler_name` = `3`
- `scheduler` = `1`
- `denoise` = `1`

## 知识

覆盖率 **85%**（34/40）

**有卡**：`VAELoader`、`VAEDecode`、`VAEDecodeAudio`、`LTXVConcatAVLatent`、`ModelPreviewOverrideKJ`、`SamplerCustomAdvanced`、`KSamplerSelect`、`UNETLoader`、`RandomNoise`、`ComfyMathExpression`、`CreateVideo`、`SaveVideo`、`LoadImage`、`MiniMaxH3SigmaShift`、`ModelAttentionBackend`、`BasicGuider`、`ManualSigmas`、`MinimaxH3LatentUpscaler3D`、`ClownsharKSampler_Beta`、`SeedGenerator`、`ConditioningZeroOut`、`LTXVSeparateAVLatent`、`MiniMaxH3ReferenceToVideo`、`Text`、`ResolutionSelector`、`LoraLoaderModelOnly`、`CLIPLoader`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
