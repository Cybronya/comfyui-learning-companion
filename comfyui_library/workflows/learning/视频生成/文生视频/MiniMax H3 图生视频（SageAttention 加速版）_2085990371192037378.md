---
key: 视频生成/文生视频/MiniMax H3 图生视频（SageAttention 加速版）_2085990371192037378.json
name: MiniMax H3 图生视频（SageAttention 加速版）_2085990371192037378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 图生视频（SageAttention 加速版）_2085990371192037378.json
hash: 7557b0c986579fb2
coverage: 0.826087
learned_at: 2026-10-15 22:45:38
nodes: [VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, CLIPLoader, RandomNoise, CreateVideo, ComfyMathExpression, MarkdownNote, SaveVideo, LoadImage, ResolutionSelector, MarkdownNote, MarkdownNote, MiniMaxH3ImageToVideo, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, LoadImage, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 图生视频（SageAttention 加速版）_2085990371192037378.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 图生视频（SageAttention 加速版）_2085990371192037378.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
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
- `ComfyMathExpression`
- `MarkdownNote`
- `SaveVideo`
- `LoadImage`
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `MiniMaxH3ImageToVideo`
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoadImage`
- `PrimitiveFloat`

## 知识

覆盖率 **83%**（19/23）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`SaveVideo`、`LoadImage`、`ResolutionSelector`、`MiniMaxH3ImageToVideo`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
