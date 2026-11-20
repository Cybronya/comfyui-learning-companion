---
key: 平台全量/MiniMax_H3_SelfLift_Avatar_GlobalStream_NovelFlow_Mapped_API_2117454242343636994.json
name: MiniMax_H3_SelfLift_Avatar_GlobalStream_NovelFlow_Mapped_API_2117454242343636994
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/MiniMax_H3_SelfLift_Avatar_GlobalStream_NovelFlow_Mapped_API_2117454242343636994.json
hash: 36fb4ccef20a1dd0
coverage: 0.939394
learned_at: 2026-11-14 00:45:02
nodes: [ResolutionSelector, VAEDecodeAudio, VAEDecode, KSamplerSelect, BasicScheduler, UNETLoader, CLIPLoader, ComfyMathExpression, PrimitiveFloat, MiniMaxH3ReferenceToVideo, LoraLoaderModelOnly, H3SigmaRefiner, ModelAttentionBackend, LoadImage, ModelPreviewOverrideKJ, LoadImage, easy float, ConditioningZeroOut, VHS_VideoCombine, VAELoader, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, VAELoader, PrimitiveStringMultiline, LoadImage, LoadImage, LoadImage, LoadImage, SelfLiftAvatarH3Sampler, BlockSparseAttention, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 平台全量/MiniMax_H3_SelfLift_Avatar_GlobalStream_NovelFlow_Mapped_API_2117454242343636994.json

> 来源文件 `comfyui_library/workflows/平台全量/MiniMax_H3_SelfLift_Avatar_GlobalStream_NovelFlow_Mapped_API_2117454242343636994.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（33 个）：
- `ResolutionSelector`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `LoraLoaderModelOnly` ★核心
- `H3SigmaRefiner`
- `ModelAttentionBackend`
- `LoadImage`
- `ModelPreviewOverrideKJ`
- `LoadImage`
- `easy float`
- `ConditioningZeroOut`
- `VHS_VideoCombine`
- `VAELoader`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `VAELoader`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SelfLiftAvatarH3Sampler` ★核心
- `BlockSparseAttention`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`ResolutionSelector`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`BasicScheduler`、`UNETLoader`、`CLIPLoader`、`ComfyMathExpression`、`MiniMaxH3ReferenceToVideo`、`LoraLoaderModelOnly`、`H3SigmaRefiner`、`ModelAttentionBackend`、`LoadImage`、`ModelPreviewOverrideKJ`、`easy float`、`ConditioningZeroOut`、`VHS_VideoCombine`、`VAELoader`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`SelfLiftAvatarH3Sampler`、`BlockSparseAttention`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
