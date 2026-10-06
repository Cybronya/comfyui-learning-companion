---
key: 视频生成/图生视频/MiniMax-H3-导演skill-双采2k直出.json
name: MiniMax-H3-导演skill-双采2k直出
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax-H3-导演skill-双采2k直出.json
hash: 44b039619b0400a4
coverage: 0.75
learned_at: 2026-10-07 00:33:19
nodes: [Label (rgthree), MarkdownNote, CLIPLoader, ModelAttentionBackend, MiniMaxH3MemoryEfficientSageAttentionPatch, Label (rgthree), Label (rgthree), MarkdownNote, VAELoader, MiniMaxH3SigmaShift, UNETLoader, MarkdownNote, CLIPLoader, ModelAttentionBackend, MiniMaxH3MemoryEfficientSageAttentionPatch, VAELoader, MiniMaxH3SigmaShift, UNETLoader, ComfyMathExpression, LoraLoaderModelOnly, VAELoader, Reroute, Reroute, KSamplerSelect, BasicScheduler, VAEDecode, VAEDecodeAudio, LoraLoaderModelOnly, ModelPreviewOverrideKJ, ModelPreviewOverrideKJ, ConditioningZeroOut, VAELoader, MiniMaxH3ReferenceToVideo, ConditioningZeroOut, BasicScheduler, VAEDecode, VAEDecodeAudio, VHS_VideoCombine, SelfLiftH3Sampler, ResolutionSelector, VHS_VideoCombine, Label (rgthree), LoadImage, PrimitiveFloat, ResolutionSelector, SelfLiftH3Sampler, H3SigmaRefiner, MiniMaxH3Unified, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, KSamplerSelect, PrimitiveStringMultiline]
patterns: []
missing: [Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree)]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/MiniMax-H3-导演skill-双采2k直出.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax-H3-导演skill-双采2k直出.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Other

**节点**（52 个）：
- `Label (rgthree)`
- `MarkdownNote`
- `CLIPLoader`
- `ModelAttentionBackend`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `Label (rgthree)`
- `Label (rgthree)`
- `MarkdownNote`
- `VAELoader`
- `MiniMaxH3SigmaShift`
- `UNETLoader` ★核心
- `MarkdownNote`
- `CLIPLoader`
- `ModelAttentionBackend`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VAELoader`
- `MiniMaxH3SigmaShift`
- `UNETLoader` ★核心
- `ComfyMathExpression`
- `LoraLoaderModelOnly` ★核心
- `VAELoader`
- `Reroute`
- `Reroute`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelPreviewOverrideKJ`
- `ModelPreviewOverrideKJ`
- `ConditioningZeroOut`
- `VAELoader`
- `MiniMaxH3ReferenceToVideo`
- `ConditioningZeroOut`
- `BasicScheduler`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VHS_VideoCombine`
- `SelfLiftH3Sampler` ★核心
- `ResolutionSelector`
- `VHS_VideoCombine`
- `Label (rgthree)`
- `LoadImage`
- `PrimitiveFloat`
- `ResolutionSelector`
- `SelfLiftH3Sampler` ★核心
- `H3SigmaRefiner`
- `MiniMaxH3Unified`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `KSamplerSelect` ★核心
- `PrimitiveStringMultiline`

## 知识

覆盖率 **75%**（39/52）

**有卡**：`CLIPLoader`、`ModelAttentionBackend`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VAELoader`、`MiniMaxH3SigmaShift`、`UNETLoader`、`ComfyMathExpression`、`LoraLoaderModelOnly`、`KSamplerSelect`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`ModelPreviewOverrideKJ`、`ConditioningZeroOut`、`MiniMaxH3ReferenceToVideo`、`VHS_VideoCombine`、`SelfLiftH3Sampler`、`ResolutionSelector`、`LoadImage`、`H3SigmaRefiner`、`MiniMaxH3Unified`

**缺卡**（4）：`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
