---
key: 平台全量/video_pika_h3_flex_ref2va_sol_atten_2117785731493093377.json
name: video_pika_h3_flex_ref2va_sol_atten_2117785731493093377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/video_pika_h3_flex_ref2va_sol_atten_2117785731493093377.json
hash: 18a049aed1405ff2
coverage: 0.863636
learned_at: 2026-11-14 01:18:48
nodes: [ResolutionSelector, MarkdownNote, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, SamplerCustomAdvanced, BasicGuider, UNETLoader, CLIPLoader, RandomNoise, ComfyMathExpression, PrimitiveFloat, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, LoraLoaderModelOnly, ManualSigmas, LoadImage, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, BlockSparseAttention]
patterns: []
missing: []
---

# 平台全量/video_pika_h3_flex_ref2va_sol_atten_2117785731493093377.json

> 来源文件 `comfyui_library/workflows/平台全量/video_pika_h3_flex_ref2va_sol_atten_2117785731493093377.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（22 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `UNETLoader` ★核心
- `CLIPLoader`
- `RandomNoise`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `ManualSigmas`
- `LoadImage`
- `VHS_VideoCombine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BlockSparseAttention`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`SamplerCustomAdvanced`、`BasicGuider`、`UNETLoader`、`CLIPLoader`、`RandomNoise`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`LoraLoaderModelOnly`、`ManualSigmas`、`LoadImage`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BlockSparseAttention`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
