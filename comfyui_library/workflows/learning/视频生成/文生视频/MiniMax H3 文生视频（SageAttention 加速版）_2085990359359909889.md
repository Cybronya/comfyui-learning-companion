---
key: 视频生成/文生视频/MiniMax H3 文生视频（SageAttention 加速版）_2085990359359909889.json
name: MiniMax H3 文生视频（SageAttention 加速版）_2085990359359909889
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 文生视频（SageAttention 加速版）_2085990359359909889.json
hash: e1bbd03466c1889e
coverage: 0.809524
learned_at: 2026-10-15 22:45:42
nodes: [VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, RandomNoise, CreateVideo, VAELoader, VAELoader, CLIPLoader, ComfyMathExpression, ResolutionSelector, SaveVideo, MiniMaxH3ImageToVideo, MarkdownNote, MarkdownNote, PrimitiveFloat, MarkdownNote, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 文生视频（SageAttention 加速版）_2085990359359909889.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 文生视频（SageAttention 加速版）_2085990359359909889.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
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
- `MiniMaxH3MemoryEfficientSageAttentionPatch`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`RandomNoise`、`CreateVideo`、`VAELoader`、`CLIPLoader`、`ComfyMathExpression`、`ResolutionSelector`、`SaveVideo`、`MiniMaxH3ImageToVideo`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
