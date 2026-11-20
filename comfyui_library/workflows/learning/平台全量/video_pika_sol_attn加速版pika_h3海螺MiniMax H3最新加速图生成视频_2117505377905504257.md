---
key: 平台全量/video_pika_sol_attn加速版pika_h3海螺MiniMax H3最新加速图生成视频_2117505377905504257.json
name: video_pika_sol_attn加速版pika_h3海螺MiniMax H3最新加速图生成视频_2117505377905504257
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/video_pika_sol_attn加速版pika_h3海螺MiniMax H3最新加速图生成视频_2117505377905504257.json
hash: ffb489b8ba445eba
coverage: 0.833333
learned_at: 2026-11-14 01:18:48
nodes: [MarkdownNote, LoadImage, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, SamplerCustomAdvanced, BasicGuider, CLIPLoader, RandomNoise, MiniMaxH3ImageToVideo, ComfyMathExpression, PrimitiveFloat, ManualSigmas, VHS_VideoCombine, ResolutionSelector, ImageResizeKJv2, BlockSparseAttention, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, LoraLoaderModelOnly, 孤海注释, 孤海注释]
patterns: []
missing: []
---

# 平台全量/video_pika_sol_attn加速版pika_h3海螺MiniMax H3最新加速图生成视频_2117505377905504257.json

> 来源文件 `comfyui_library/workflows/平台全量/video_pika_sol_attn加速版pika_h3海螺MiniMax H3最新加速图生成视频_2117505377905504257.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（24 个）：
- `MarkdownNote`
- `LoadImage`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `CLIPLoader`
- `RandomNoise`
- `MiniMaxH3ImageToVideo`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `ManualSigmas`
- `VHS_VideoCombine`
- `ResolutionSelector`
- `ImageResizeKJv2`
- `BlockSparseAttention`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `孤海注释`

## 知识

覆盖率 **83%**（20/24）

**有卡**：`LoadImage`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`CLIPLoader`、`RandomNoise`、`MiniMaxH3ImageToVideo`、`ComfyMathExpression`、`ManualSigmas`、`VHS_VideoCombine`、`ResolutionSelector`、`ImageResizeKJv2`、`BlockSparseAttention`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
