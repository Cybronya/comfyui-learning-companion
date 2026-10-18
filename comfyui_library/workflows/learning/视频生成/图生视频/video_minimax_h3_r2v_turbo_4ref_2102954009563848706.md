---
key: 视频生成/图生视频/video_minimax_h3_r2v_turbo_4ref_2102954009563848706.json
name: video_minimax_h3_r2v_turbo_4ref_2102954009563848706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/video_minimax_h3_r2v_turbo_4ref_2102954009563848706.json
hash: 0e077445ceba0e97
coverage: 0.807692
learned_at: 2026-10-17 02:29:34
nodes: [SaveVideo, ResolutionSelector, MarkdownNote, MarkdownNote, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, BasicScheduler, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, CreateVideo, ComfyMathExpression, PrimitiveFloat, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, MarkdownNote, MiniMaxH3TurboLoRA, MiniMaxH3TurboSampler, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/video_minimax_h3_r2v_turbo_4ref_2102954009563848706.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/video_minimax_h3_r2v_turbo_4ref_2102954009563848706.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（26 个）：
- `SaveVideo`
- `ResolutionSelector`
- `MarkdownNote`
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
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
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `MiniMaxH3TurboLoRA`
- `MiniMaxH3TurboSampler` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **81%**（21/26）

**有卡**：`SaveVideo`、`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3TurboLoRA`、`MiniMaxH3TurboSampler`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、SamplerCustomAdvanced、MiniMaxH3TurboSampler
