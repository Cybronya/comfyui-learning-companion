---
key: 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086288381553762305.json
name: MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086288381553762305
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086288381553762305.json
hash: 67743b70f24a8b3b
coverage: 0.846154
learned_at: 2026-10-10 23:01:47
nodes: [VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, RandomNoise, CreateVideo, VAELoader, VAELoader, CLIPLoader, ComfyMathExpression, ResolutionSelector, SaveVideo, MiniMaxH3ImageToVideo, MarkdownNote, MarkdownNote, PrimitiveFloat, MarkdownNote, UNETLoader, KSamplerSelect, BasicScheduler, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086288381553762305.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086288381553762305.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `RandomNoise`
- `CreateVideo`
- `VAELoader`
- `VAELoader`
- `CLIPLoader`
- `ComfyMathExpression`
- `ResolutionSelector`
- `SaveVideo`
- `MiniMaxH3ImageToVideo`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveFloat`
- `MarkdownNote`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心

## 知识

覆盖率 **85%**（22/26）

**有卡**：`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`CreateVideo`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`ResolutionSelector`、`SaveVideo`、`MiniMaxH3ImageToVideo`、`UNETLoader`、`KSamplerSelect`、`BasicScheduler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
