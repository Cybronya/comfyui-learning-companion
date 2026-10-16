---
key: 视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2086152939638452226.json
name: video_minimax_h3_i2v_turbo_lora_2086152939638452226
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2086152939638452226.json
hash: ebc32cca83c11185
coverage: 0.833333
learned_at: 2026-10-16 21:07:35
nodes: [ComfyMathExpression, ImageScaleToTotalPixels, GetImageSize, VAEDecode, VAEDecodeAudio, CLIPLoader, VAELoader, VAELoader, PrimitiveFloat, SamplerCustomAdvanced, RandomNoise, VHS_VideoCombine, LoadImage, MiniMaxH3ImageToVideo, MarkdownNote, MarkdownNote, MarkdownNote, UNETLoader, PathchSageAttentionKJ, KSamplerSelect, BasicScheduler, CFGGuider, ConditioningZeroOut, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2086152939638452226.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2086152939638452226.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（24 个）：
- `ComfyMathExpression`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `PrimitiveFloat`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `VHS_VideoCombine`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `PathchSageAttentionKJ`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `CFGGuider`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **83%**（20/24）

**有卡**：`ComfyMathExpression`、`ImageScaleToTotalPixels`、`GetImageSize`、`VAEDecode`、`VAEDecodeAudio`、`CLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`RandomNoise`、`VHS_VideoCombine`、`LoadImage`、`MiniMaxH3ImageToVideo`、`UNETLoader`、`PathchSageAttentionKJ`、`KSamplerSelect`、`BasicScheduler`、`CFGGuider`、`ConditioningZeroOut`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider
