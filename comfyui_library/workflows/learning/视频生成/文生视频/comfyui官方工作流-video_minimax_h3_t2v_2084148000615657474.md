---
key: 视频生成/文生视频/comfyui官方工作流-video_minimax_h3_t2v_2084148000615657474.json
name: comfyui官方工作流-video_minimax_h3_t2v_2084148000615657474
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/comfyui官方工作流-video_minimax_h3_t2v_2084148000615657474.json
hash: cd58226f6a97ca3d
coverage: 0.761905
learned_at: 2026-10-15 22:47:18
nodes: [SaveVideo, ResolutionSelector, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, ComfyMathExpression, PrimitiveFloat, MarkdownNote, MarkdownNote, MarkdownNote, CreateVideo, MiniMaxH3ImageToVideo, JjkText]
patterns: []
missing: []
---

# 视频生成/文生视频/comfyui官方工作流-video_minimax_h3_t2v_2084148000615657474.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/comfyui官方工作流-video_minimax_h3_t2v_2084148000615657474.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `SaveVideo`
- `ResolutionSelector`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `CreateVideo`
- `MiniMaxH3ImageToVideo`
- `JjkText`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`SaveVideo`、`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`ComfyMathExpression`、`CreateVideo`、`MiniMaxH3ImageToVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、UNETLoader、KSamplerSelect、SamplerCustomAdvanced、VAEDecodeAudio
