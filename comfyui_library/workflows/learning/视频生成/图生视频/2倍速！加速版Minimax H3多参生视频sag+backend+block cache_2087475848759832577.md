---
key: 视频生成/图生视频/2倍速！加速版Minimax H3多参生视频sag+backend+block cache_2087475848759832577.json
name: 2倍速！加速版Minimax H3多参生视频sag+backend+block cache_2087475848759832577
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2倍速！加速版Minimax H3多参生视频sag+backend+block cache_2087475848759832577.json
hash: d77d42a00cf0039e
coverage: 0.909091
learned_at: 2026-10-16 21:27:26
nodes: [VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, CLIPLoader, CreateVideo, VAELoader, LoadImage, LoadImage, LoadImage, ComfyMathExpression, ResolutionSelector, PrimitiveFloat, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveStringMultiline, TrimAudioDuration, RandomNoise, MiniMaxH3ReferenceToVideo, LoadAudio, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, MiniMaxH3BlockCacheT8, UNETLoader, MarkdownNote, LoadImage, SaveVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/2倍速！加速版Minimax H3多参生视频sag+backend+block cache_2087475848759832577.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2倍速！加速版Minimax H3多参生视频sag+backend+block cache_2087475848759832577.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（33 个）：
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `CLIPLoader`
- `CreateVideo`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ComfyMathExpression`
- `ResolutionSelector`
- `PrimitiveFloat`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `TrimAudioDuration`
- `RandomNoise`
- `MiniMaxH3ReferenceToVideo`
- `LoadAudio`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `MiniMaxH3BlockCacheT8`
- `UNETLoader` ★核心
- `MarkdownNote`
- `LoadImage`
- `SaveVideo`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`CLIPLoader`、`CreateVideo`、`LoadImage`、`ComfyMathExpression`、`ResolutionSelector`、`TrimAudioDuration`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`LoadAudio`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`MiniMaxH3BlockCacheT8`、`UNETLoader`、`SaveVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
