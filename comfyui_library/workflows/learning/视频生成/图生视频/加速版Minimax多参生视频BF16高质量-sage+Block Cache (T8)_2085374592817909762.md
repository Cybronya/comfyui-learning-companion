---
key: 视频生成/图生视频/加速版Minimax多参生视频BF16高质量-sage+Block Cache (T8)_2085374592817909762.json
name: 加速版Minimax多参生视频BF16高质量-sage+Block Cache (T8)_2085374592817909762
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/加速版Minimax多参生视频BF16高质量-sage+Block Cache (T8)_2085374592817909762.json
hash: dc1769b057e87bd7
coverage: 0.821429
learned_at: 2026-10-16 20:50:49
nodes: [MarkdownNote, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, CLIPLoader, RandomNoise, CreateVideo, UNETLoader, MiniMaxH3ReferenceToVideo, MiniMaxH3BlockCacheT8, PathchSageAttentionKJ, SaveVideo, LoadImage, LoadImage, LoadAudio, ComfyMathExpression, MarkdownNote, MarkdownNote, ResolutionSelector, LoadImage, VHS_LoadVideo, PrimitiveFloat, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/加速版Minimax多参生视频BF16高质量-sage+Block Cache (T8)_2085374592817909762.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/加速版Minimax多参生视频BF16高质量-sage+Block Cache (T8)_2085374592817909762.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（28 个）：
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `CLIPLoader`
- `RandomNoise`
- `CreateVideo`
- `UNETLoader` ★核心
- `MiniMaxH3ReferenceToVideo`
- `MiniMaxH3BlockCacheT8`
- `PathchSageAttentionKJ`
- `SaveVideo`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `ComfyMathExpression`
- `MarkdownNote`
- `MarkdownNote`
- `ResolutionSelector`
- `LoadImage`
- `VHS_LoadVideo`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **82%**（23/28）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`UNETLoader`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3BlockCacheT8`、`PathchSageAttentionKJ`、`SaveVideo`、`LoadImage`、`LoadAudio`、`ComfyMathExpression`、`ResolutionSelector`、`VHS_LoadVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
