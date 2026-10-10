---
key: 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086407187261378562.json
name: MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086407187261378562
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086407187261378562.json
hash: a0a4020f7d288d58
coverage: 0.833333
learned_at: 2026-10-10 23:01:48
nodes: [VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, RandomNoise, CreateVideo, VAELoader, VAELoader, CLIPLoader, ComfyMathExpression, SaveVideo, MarkdownNote, MarkdownNote, PrimitiveFloat, MarkdownNote, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, KSamplerSelect, BasicScheduler, ResolutionSelector, LoraLoaderBypassModelOnly, MiniMaxH3ImageToVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086407187261378562.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 文生视频（SageAttention+LoRA 双重加速）_2086407187261378562.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
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
- `SaveVideo`
- `MarkdownNote`
- `MarkdownNote`
- `PrimitiveFloat`
- `MarkdownNote`
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `ResolutionSelector`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3ImageToVideo`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`CreateVideo`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`SaveVideo`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderBypassModelOnly`、`KSamplerSelect`、`BasicScheduler`、`ResolutionSelector`、`MiniMaxH3ImageToVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
