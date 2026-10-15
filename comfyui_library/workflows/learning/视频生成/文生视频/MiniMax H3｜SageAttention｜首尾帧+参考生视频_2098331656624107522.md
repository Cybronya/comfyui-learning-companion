---
key: 视频生成/文生视频/MiniMax H3｜SageAttention｜首尾帧+参考生视频_2098331656624107522.json
name: MiniMax H3｜SageAttention｜首尾帧+参考生视频_2098331656624107522
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3｜SageAttention｜首尾帧+参考生视频_2098331656624107522.json
hash: f3e20f90e3272069
coverage: 0.9
learned_at: 2026-10-15 22:46:11
nodes: [MarkdownNote, MarkdownNote, BasicScheduler, VAEDecode, VAELoader, CLIPLoader, SamplerCustomAdvanced, RandomNoise, BasicGuider, KSamplerSelect, VAEDecodeAudio, VAELoader, MiniMaxH3AudioConditioningT8, SaveVideo, CreateVideo, LoadImage, LoadImage, UNETLoader, UNETLoader, PathchSageAttentionKJ]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3｜SageAttention｜首尾帧+参考生视频_2098331656624107522.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3｜SageAttention｜首尾帧+参考生视频_2098331656624107522.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（20 个）：
- `MarkdownNote`
- `MarkdownNote`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAEDecodeAudio` ★核心
- `VAELoader`
- `MiniMaxH3AudioConditioningT8`
- `SaveVideo`
- `CreateVideo`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`

## 知识

覆盖率 **90%**（18/20）

**有卡**：`BasicScheduler`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`SamplerCustomAdvanced`、`RandomNoise`、`BasicGuider`、`KSamplerSelect`、`VAEDecodeAudio`、`MiniMaxH3AudioConditioningT8`、`SaveVideo`、`CreateVideo`、`LoadImage`、`UNETLoader`、`PathchSageAttentionKJ`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
