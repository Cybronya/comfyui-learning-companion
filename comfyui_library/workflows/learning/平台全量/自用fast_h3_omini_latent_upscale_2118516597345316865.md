---
key: 平台全量/自用fast_h3_omini_latent_upscale_2118516597345316865.json
name: 自用fast_h3_omini_latent_upscale_2118516597345316865
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/自用fast_h3_omini_latent_upscale_2118516597345316865.json
hash: 44e2765da99cd528
coverage: 0.522388
learned_at: 2026-11-14 02:31:51
nodes: [MarkdownNote, MarkdownNote, ComfyMathExpression, SetNode, CLIPLoader, VAELoader, SetNode, ResolutionSelector, SetNode, GetNode, GetNode, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, PrimitiveFloat, LoraLoaderModelOnly, SetNode, GetNode, GetNode, KSamplerSelect, GetNode, ConditioningZeroOut, GetNode, SetNode, BasicScheduler, VAEDecode, GetNode, VAEDecodeAudio, VHS_VideoCombine, SelfLiftH3Sampler, VAELoader, UNETLoader, SetNode, ModelAttentionBackend, BlockSparseAttention, PrimitiveStringMultiline, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoadAudio, LoadImage, Note, SetNode, ImageScaleToTotalPixels, GetNode, LoadImage, LoraLoaderModelOnly, CM_FloatToInt, LoadAudio, LoadImage, ImageScaleToTotalPixels, UNETLoader, LoadImage, ImageScaleToTotalPixels, PrimitiveNode]
patterns: []
missing: []
---

# 平台全量/自用fast_h3_omini_latent_upscale_2118516597345316865.json

> 来源文件 `comfyui_library/workflows/平台全量/自用fast_h3_omini_latent_upscale_2118516597345316865.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（67 个）：
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `SetNode`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `ResolutionSelector`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageScaleToTotalPixels`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `ConditioningZeroOut`
- `GetNode`
- `SetNode`
- `BasicScheduler`
- `VAEDecode` ★核心
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `SelfLiftH3Sampler` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `SetNode`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `PrimitiveStringMultiline`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadAudio`
- `LoadImage`
- `Note`
- `SetNode`
- `ImageScaleToTotalPixels`
- `GetNode`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `CM_FloatToInt`
- `LoadAudio`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `LoadImage`
- `ImageScaleToTotalPixels`
- `PrimitiveNode`

## 知识

覆盖率 **52%**（35/67）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`SelfLiftH3Sampler`、`UNETLoader`、`ModelAttentionBackend`、`BlockSparseAttention`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ReferenceToVideo`、`LoadAudio`、`LoadImage`、`CM_FloatToInt`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
