---
key: 视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2sampling_2086306419887923201.json
name: video_minimax_h3_i2v_turbo_lora_2sampling_2086306419887923201
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2sampling_2086306419887923201.json
hash: 3d25d70704ab6e0d
coverage: 0.857143
learned_at: 2026-10-16 21:07:35
nodes: [MarkdownNote, MarkdownNote, ImageScaleToTotalPixels, MarkdownNote, GetImageSize, CLIPLoader, VAELoader, VAELoader, PrimitiveFloat, ComfyMathExpression, PathchSageAttentionKJ, UNETLoader, LoraLoaderModelOnly, RandomNoise, CFGGuider, KSamplerSelect, BasicScheduler, SplitSigmas, CFGGuider, DisableNoise, SamplerCustomAdvanced, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, ConditioningZeroOut, LoadImage, MiniMaxH3ImageToVideo, SamplerCustomAdvanced]
patterns: []
missing: []
---

# 视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2sampling_2086306419887923201.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/video_minimax_h3_i2v_turbo_lora_2sampling_2086306419887923201.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（28 个）：
- `MarkdownNote`
- `MarkdownNote`
- `ImageScaleToTotalPixels`
- `MarkdownNote`
- `GetImageSize`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `PathchSageAttentionKJ`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SplitSigmas`
- `CFGGuider`
- `DisableNoise`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `ConditioningZeroOut`
- `LoadImage`
- `MiniMaxH3ImageToVideo`
- `SamplerCustomAdvanced` ★核心

## 知识

覆盖率 **86%**（24/28）

**有卡**：`ImageScaleToTotalPixels`、`GetImageSize`、`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`PathchSageAttentionKJ`、`UNETLoader`、`LoraLoaderModelOnly`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`BasicScheduler`、`SplitSigmas`、`DisableNoise`、`SamplerCustomAdvanced`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`ConditioningZeroOut`、`LoadImage`、`MiniMaxH3ImageToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、LoadImage、UNETLoader、CFGGuider
