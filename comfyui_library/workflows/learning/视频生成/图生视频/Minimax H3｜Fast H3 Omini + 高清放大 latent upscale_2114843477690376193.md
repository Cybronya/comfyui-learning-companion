---
key: 视频生成/图生视频/Minimax H3｜Fast H3 Omini + 高清放大 latent upscale_2114843477690376193.json
name: Minimax H3｜Fast H3 Omini + 高清放大 latent upscale_2114843477690376193
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax H3｜Fast H3 Omini + 高清放大 latent upscale_2114843477690376193.json
hash: 47866ef06bc91ce4
coverage: 0.698413
learned_at: 2026-10-30 17:58:26
nodes: [ComfyMathExpression, PrimitiveNode, CLIPLoader, VAELoader, ResolutionSelector, ImageScaleToTotalPixels, PrimitiveFloat, LoraLoaderModelOnly, KSamplerSelect, ConditioningZeroOut, BasicScheduler, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, SelfLiftH3Sampler, VAELoader, UNETLoader, LoadImage, ModelAttentionBackend, BlockSparseAttention, PrimitiveStringMultiline, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, PrimitiveStringMultiline, VAELoader, VHS_VideoCombine, BasicScheduler, BlockSparseAttention, MiniMaxH3ReferenceToVideo, VAELoader, ImageScaleToTotalPixels, ComfyMathExpression, VAEDecodeAudio, KSamplerSelect, ResolutionSelector, CLIPLoader, LoadImage, VAEDecode, BasicGuider, ModelAttentionBackend, PrimitiveNode, PrimitiveFloat, RandomNoise, UNETLoader, SamplerCustomAdvanced, MiniMaxH3MemoryEfficientSageAttentionPatch, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Note, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax H3｜Fast H3 Omini + 高清放大 latent upscale_2114843477690376193.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax H3｜Fast H3 Omini + 高清放大 latent upscale_2114843477690376193.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（63 个）：
- `ComfyMathExpression`
- `PrimitiveNode`
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `ImageScaleToTotalPixels`
- `PrimitiveFloat`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `ConditioningZeroOut`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `SelfLiftH3Sampler` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `ModelAttentionBackend`
- `BlockSparseAttention`
- `PrimitiveStringMultiline`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveStringMultiline`
- `VAELoader`
- `VHS_VideoCombine`
- `BasicScheduler`
- `BlockSparseAttention`
- `MiniMaxH3ReferenceToVideo`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `ComfyMathExpression`
- `VAEDecodeAudio` ★核心
- `KSamplerSelect` ★核心
- `ResolutionSelector`
- `CLIPLoader`
- `LoadImage`
- `VAEDecode` ★核心
- `BasicGuider`
- `ModelAttentionBackend`
- `PrimitiveNode`
- `PrimitiveFloat`
- `RandomNoise`
- `UNETLoader` ★核心
- `SamplerCustomAdvanced` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`

## 知识

覆盖率 **70%**（44/63）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`SelfLiftH3Sampler`、`UNETLoader`、`LoadImage`、`ModelAttentionBackend`、`BlockSparseAttention`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ReferenceToVideo`、`BasicGuider`、`RandomNoise`、`SamplerCustomAdvanced`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
