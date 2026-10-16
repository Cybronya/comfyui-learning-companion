---
key: 视频生成/图生视频/video_minimax_h3_i2v 开源comfyui 官方版本_2084149773224992770.json
name: video_minimax_h3_i2v 开源comfyui 官方版本_2084149773224992770
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/video_minimax_h3_i2v 开源comfyui 官方版本_2084149773224992770.json
hash: 6f6e3bf76ca1e199
coverage: 0.791667
learned_at: 2026-10-16 19:52:24
nodes: [SaveVideo, ResolutionSelector, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, CreateVideo, ComfyMathExpression, PrimitiveFloat, MarkdownNote, MarkdownNote, ImageScaleToTotalPixels, GetImageSize, MarkdownNote, LoadImage, MiniMaxH3ImageToVideo, VAELoader, JjkText]
patterns: []
missing: []
---

# 视频生成/图生视频/video_minimax_h3_i2v 开源comfyui 官方版本_2084149773224992770.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/video_minimax_h3_i2v 开源comfyui 官方版本_2084149773224992770.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `SaveVideo`
- `ResolutionSelector`
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
- `MarkdownNote`
- `MarkdownNote`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `MarkdownNote`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `VAELoader`
- `JjkText`

## 知识

覆盖率 **79%**（19/24）

**有卡**：`SaveVideo`、`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`CreateVideo`、`ComfyMathExpression`、`ImageScaleToTotalPixels`、`GetImageSize`、`LoadImage`、`MiniMaxH3ImageToVideo`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
