---
key: 视频生成/文生视频/MiniMax H3 图生视频（SageAttention+LoRA 双重加速）_2086288398037372929.json
name: MiniMax H3 图生视频（SageAttention+LoRA 双重加速）_2086288398037372929
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 图生视频（SageAttention+LoRA 双重加速）_2086288398037372929.json
hash: ea125fbc6460093f
coverage: 0.846154
learned_at: 2026-10-11 20:53:40
nodes: [VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, BasicGuider, CLIPLoader, RandomNoise, CreateVideo, ComfyMathExpression, MarkdownNote, SaveVideo, LoadImage, ResolutionSelector, MarkdownNote, MiniMaxH3ImageToVideo, UNETLoader, LoadImage, PrimitiveFloat, LoraLoaderBypassModelOnly, MarkdownNote, LoraLoaderBypassModelOnly, LoraLoaderBypassModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, KSamplerSelect]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 图生视频（SageAttention+LoRA 双重加速）_2086288398037372929.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 图生视频（SageAttention+LoRA 双重加速）_2086288398037372929.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `CLIPLoader`
- `RandomNoise`
- `CreateVideo`
- `ComfyMathExpression`
- `MarkdownNote`
- `SaveVideo`
- `LoadImage`
- `ResolutionSelector`
- `MarkdownNote`
- `MiniMaxH3ImageToVideo`
- `UNETLoader` ★核心
- `LoadImage`
- `PrimitiveFloat`
- `LoraLoaderBypassModelOnly` ★核心
- `MarkdownNote`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BasicScheduler`
- `KSamplerSelect` ★核心

## 知识

覆盖率 **85%**（22/26）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`BasicGuider`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`SaveVideo`、`LoadImage`、`ResolutionSelector`、`MiniMaxH3ImageToVideo`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`KSamplerSelect`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
