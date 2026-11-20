---
key: 平台全量/video_pika_h3_flex_fl2va_sol_attn_2117787644636782594.json
name: video_pika_h3_flex_fl2va_sol_attn_2117787644636782594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/video_pika_h3_flex_fl2va_sol_attn_2117787644636782594.json
hash: ac91bc00f541f05c
coverage: 0.909091
learned_at: 2026-11-14 01:18:44
nodes: [MarkdownNote, LoadImage, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, SamplerCustomAdvanced, BasicGuider, CLIPLoader, RandomNoise, MiniMaxH3ImageToVideo, ComfyMathExpression, PrimitiveFloat, ManualSigmas, VHS_VideoCombine, ResolutionSelector, ImageResizeKJv2, BlockSparseAttention, MiniMaxH3MemoryEfficientSageAttentionPatch, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 平台全量/video_pika_h3_flex_fl2va_sol_attn_2117787644636782594.json

> 来源文件 `comfyui_library/workflows/平台全量/video_pika_h3_flex_fl2va_sol_attn_2117787644636782594.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（22 个）：
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

## 知识

覆盖率 **91%**（20/22）

**有卡**：`LoadImage`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`CLIPLoader`、`RandomNoise`、`MiniMaxH3ImageToVideo`、`ComfyMathExpression`、`ManualSigmas`、`VHS_VideoCombine`、`ResolutionSelector`、`ImageResizeKJv2`、`BlockSparseAttention`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
