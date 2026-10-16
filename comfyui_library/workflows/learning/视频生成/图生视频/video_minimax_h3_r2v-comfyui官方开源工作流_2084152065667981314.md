---
key: 视频生成/图生视频/video_minimax_h3_r2v-comfyui官方开源工作流_2084152065667981314.json
name: video_minimax_h3_r2v-comfyui官方开源工作流_2084152065667981314
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/video_minimax_h3_r2v-comfyui官方开源工作流_2084152065667981314.json
hash: 34a187bc46635787
coverage: 0.782609
learned_at: 2026-10-16 19:52:24
nodes: [SaveVideo, ResolutionSelector, MarkdownNote, MarkdownNote, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, CreateVideo, ComfyMathExpression, PrimitiveFloat, MiniMaxH3ReferenceToVideo, MarkdownNote, LoadImage, LoadImage, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 视频生成/图生视频/video_minimax_h3_r2v-comfyui官方开源工作流_2084152065667981314.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/video_minimax_h3_r2v-comfyui官方开源工作流_2084152065667981314.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（23 个）：
- `SaveVideo`
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
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
- `CreateVideo`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `MarkdownNote`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`SaveVideo`、`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
