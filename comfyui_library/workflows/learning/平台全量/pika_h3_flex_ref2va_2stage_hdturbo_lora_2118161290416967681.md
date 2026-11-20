---
key: 平台全量/pika_h3_flex_ref2va_2stage_hdturbo_lora_2118161290416967681.json
name: pika_h3_flex_ref2va_2stage_hdturbo_lora_2118161290416967681
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/pika_h3_flex_ref2va_2stage_hdturbo_lora_2118161290416967681.json
hash: fde8fbce9a98b02a
coverage: 0.857143
learned_at: 2026-11-14 01:15:42
nodes: [ResolutionSelector, MarkdownNote, VAELoader, VAELoader, VAEDecodeAudio, VAEDecode, KSamplerSelect, CLIPLoader, ComfyMathExpression, PrimitiveFloat, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, LoadImage, VHS_VideoCombine, MiniMaxH3MemoryEfficientSageAttentionPatch, BlockSparseAttention, SelfLiftH3Sampler, BasicScheduler, ConditioningZeroOut, UNETLoader, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 平台全量/pika_h3_flex_ref2va_2stage_hdturbo_lora_2118161290416967681.json

> 来源文件 `comfyui_library/workflows/平台全量/pika_h3_flex_ref2va_2stage_hdturbo_lora_2118161290416967681.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（21 个）：
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

## 知识

覆盖率 **86%**（18/21）

**有卡**：`ResolutionSelector`、`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`CLIPLoader`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`VHS_VideoCombine`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BlockSparseAttention`、`SelfLiftH3Sampler`、`BasicScheduler`、`ConditioningZeroOut`、`UNETLoader`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
