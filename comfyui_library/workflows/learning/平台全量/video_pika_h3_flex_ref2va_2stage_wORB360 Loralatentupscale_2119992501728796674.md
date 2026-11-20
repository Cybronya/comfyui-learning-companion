---
key: 平台全量/video_pika_h3_flex_ref2va_2stage_wORB360 Loralatentupscale_2119992501728796674.json
name: video_pika_h3_flex_ref2va_2stage_wORB360 Loralatentupscale_2119992501728796674
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/video_pika_h3_flex_ref2va_2stage_wORB360 Loralatentupscale_2119992501728796674.json
hash: 2e6adf76c8b46e91
coverage: 0.857143
learned_at: 2026-11-14 01:18:47
nodes: [ResolutionSelector, MarkdownNote, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, CLIPLoader, ComfyMathExpression, PrimitiveFloat, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, LoadImage, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, BlockSparseAttention, SelfLiftH3Sampler, BasicScheduler, ConditioningZeroOut, UNETLoader, LoraLoaderModelOnly, MarkdownNote, LoraLoaderModelOnly, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/video_pika_h3_flex_ref2va_2stage_wORB360 Loralatentupscale_2119992501728796674.json

> 来源文件 `comfyui_library/workflows/平台全量/video_pika_h3_flex_ref2va_2stage_wORB360 Loralatentupscale_2119992501728796674.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（28 个）：
- `ResolutionSelector`
- `MarkdownNote`
- `VAELoader`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `LoadImage`
- `VHS_VideoCombine`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BlockSparseAttention`
- `SelfLiftH3Sampler` ★核心
- `BasicScheduler`
- `ConditioningZeroOut`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **86%**（24/28）

**有卡**：`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`CLIPLoader`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BlockSparseAttention`、`SelfLiftH3Sampler`、`BasicScheduler`、`ConditioningZeroOut`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
