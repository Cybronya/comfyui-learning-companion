---
key: 视频生成/图生视频/10Eros-Max 8步极速4视图生视频 v2.0_2087352692522962945.json
name: 10Eros-Max 8步极速4视图生视频 v2.0_2087352692522962945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/10Eros-Max 8步极速4视图生视频 v2.0_2087352692522962945.json
hash: eaa763f4c3794e39
coverage: 0.88
learned_at: 2026-10-16 21:27:25
nodes: [VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicGuider, RandomNoise, MarkdownNote, CreateVideo, CLIPLoader, MiniMaxH3AVDecodeT8, SaveLatent, SaveLatent, VAELoader, VAELoader, SamplerCustomAdvanced, UNETLoader, ComfyMathExpression, PrimitiveFloat, LoadImage, MiniMaxH3ReferenceToVideo, BasicScheduler, ResolutionSelector, LoraLoaderModelOnly, MmuuaiGroupBypass, SaveVideo, JjkText]
patterns: []
missing: []
---

# 视频生成/图生视频/10Eros-Max 8步极速4视图生视频 v2.0_2087352692522962945.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/10Eros-Max 8步极速4视图生视频 v2.0_2087352692522962945.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（25 个）：
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicGuider`
- `RandomNoise`
- `MarkdownNote`
- `CreateVideo`
- `CLIPLoader`
- `MiniMaxH3AVDecodeT8`
- `SaveLatent`
- `SaveLatent`
- `VAELoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `ComfyMathExpression`
- `PrimitiveFloat`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `BasicScheduler`
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心
- `MmuuaiGroupBypass`
- `SaveVideo`
- `JjkText`

## 知识

覆盖率 **88%**（22/25）

**有卡**：`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicGuider`、`RandomNoise`、`CreateVideo`、`CLIPLoader`、`MiniMaxH3AVDecodeT8`、`SaveLatent`、`VAELoader`、`SamplerCustomAdvanced`、`UNETLoader`、`ComfyMathExpression`、`LoadImage`、`MiniMaxH3ReferenceToVideo`、`BasicScheduler`、`ResolutionSelector`、`LoraLoaderModelOnly`、`MmuuaiGroupBypass`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
