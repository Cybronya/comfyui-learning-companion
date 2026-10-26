---
key: 数字人/数字人/极速生视频 Fast_h3_omini_latent_upscale精品_2114537045958942722.json
name: 极速生视频 Fast_h3_omini_latent_upscale精品_2114537045958942722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/极速生视频 Fast_h3_omini_latent_upscale精品_2114537045958942722.json
hash: dac1fa2b4dbe8f97
coverage: 0.433962
learned_at: 2026-10-26 22:10:52
nodes: [MarkdownNote, MarkdownNote, ComfyMathExpression, SetNode, PrimitiveNode, CLIPLoader, VAELoader, SetNode, ResolutionSelector, SetNode, GetNode, GetNode, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, PrimitiveFloat, LoraLoaderModelOnly, SetNode, GetNode, GetNode, KSamplerSelect, GetNode, ConditioningZeroOut, GetNode, SetNode, BasicScheduler, VAEDecode, GetNode, VAEDecodeAudio, VHS_VideoCombine, SelfLiftH3Sampler, VAELoader, UNETLoader, LoadImage, SetNode, ModelAttentionBackend, BlockSparseAttention, PrimitiveStringMultiline, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, QwenH3PromptLocal, LoadImage, ImageScaleToTotalPixels, PrimitiveStringMultiline]
patterns: []
missing: []
---

# 数字人/数字人/极速生视频 Fast_h3_omini_latent_upscale精品_2114537045958942722.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/极速生视频 Fast_h3_omini_latent_upscale精品_2114537045958942722.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（53 个）：
- `MarkdownNote`
- `MarkdownNote`
- `ComfyMathExpression`
- `SetNode`
- `PrimitiveNode`
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
- `LoadImage`
- `SetNode`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `PrimitiveStringMultiline`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `QwenH3PromptLocal`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `PrimitiveStringMultiline`

## 知识

覆盖率 **43%**（23/53）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`SelfLiftH3Sampler`、`UNETLoader`、`LoadImage`、`ModelAttentionBackend`、`BlockSparseAttention`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ReferenceToVideo`、`QwenH3PromptLocal`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
