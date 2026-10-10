---
key: 视频生成/文生视频/MiniMax 文生视频-Sage Attention 加速版工作流_2084924005185843201.json
name: MiniMax 文生视频-Sage Attention 加速版工作流_2084924005185843201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax 文生视频-Sage Attention 加速版工作流_2084924005185843201.json
hash: bb79743e4f223f7b
coverage: 0.809524
learned_at: 2026-10-10 23:03:38
nodes: [VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, CLIPLoader, RandomNoise, CreateVideo, ComfyMathExpression, MarkdownNote, MarkdownNote, MarkdownNote, UNETLoader, ResolutionSelector, PrimitiveFloat, SaveVideo, MiniMaxH3ImageToVideo, PathchSageAttentionKJ]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax 文生视频-Sage Attention 加速版工作流_2084924005185843201.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax 文生视频-Sage Attention 加速版工作流_2084924005185843201.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
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
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `PrimitiveFloat`
- `SaveVideo`
- `MiniMaxH3ImageToVideo`
- `PathchSageAttentionKJ`

## 知识

覆盖率 **81%**（17/21）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`UNETLoader`、`ResolutionSelector`、`SaveVideo`、`MiniMaxH3ImageToVideo`、`PathchSageAttentionKJ`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
