---
key: 平台全量/video_pika_h3_flex_fl2va_2stage_OBR360_sampling_2117496708174270465.json
name: video_pika_h3_flex_fl2va_2stage_OBR360_sampling_2117496708174270465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/video_pika_h3_flex_fl2va_2stage_OBR360_sampling_2117496708174270465.json
hash: 0e6fe36e90c63c1a
coverage: 0.875
learned_at: 2026-11-14 01:18:42
nodes: [MarkdownNote, LoadImage, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, CLIPLoader, MiniMaxH3ImageToVideo, ComfyMathExpression, PrimitiveFloat, ManualSigmas, VHS_VideoCombine, ResolutionSelector, ImageResizeKJv2, BlockSparseAttention, MiniMaxH3MemoryEfficientSageAttentionPatch, SelfLiftH3Sampler, ConditioningZeroOut, BasicScheduler, UNETLoader, LoraLoaderModelOnly, MarkdownNote, LoadImage]
patterns: []
missing: []
---

# 平台全量/video_pika_h3_flex_fl2va_2stage_OBR360_sampling_2117496708174270465.json

> 来源文件 `comfyui_library/workflows/平台全量/video_pika_h3_flex_fl2va_2stage_OBR360_sampling_2117496708174270465.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（24 个）：
- `MarkdownNote`
- `LoadImage`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `MiniMaxH3ImageToVideo`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `ManualSigmas`
- `VHS_VideoCombine`
- `ResolutionSelector`
- `ImageResizeKJv2`
- `BlockSparseAttention`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SelfLiftH3Sampler` ★核心
- `ConditioningZeroOut`
- `BasicScheduler`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `LoadImage`

## 知识

覆盖率 **88%**（21/24）

**有卡**：`LoadImage`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`CLIPLoader`、`MiniMaxH3ImageToVideo`、`ComfyMathExpression`、`ManualSigmas`、`VHS_VideoCombine`、`ResolutionSelector`、`ImageResizeKJv2`、`BlockSparseAttention`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`SelfLiftH3Sampler`、`ConditioningZeroOut`、`BasicScheduler`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
