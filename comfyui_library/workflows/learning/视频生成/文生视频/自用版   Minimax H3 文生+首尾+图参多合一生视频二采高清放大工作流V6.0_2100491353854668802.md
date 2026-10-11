---
key: 视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V6.0_2100491353854668802.json
name: 自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V6.0_2100491353854668802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V6.0_2100491353854668802.json
hash: 645f7cd9a3813463
coverage: 0.333333
learned_at: 2026-10-11 22:12:55
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, GetNode, LoadAudio, GetNode, SetNode, SetNode, SetNode, 孤海注释, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, VAELoader, ComfyMathExpression, SetNode, GetNode, GetNode, GetNode, GetNode, 布尔孤海, 孤海注释, 孤海注释, VAELoader, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, SetNode, ImpactConditionalBranch, GetNode, GetNode, GetNode, GetNode, GetNode, ConditioningZeroOut, GetNode, GetNode, GetNode, GetNode, GetNode, Any Switch (rgthree), VAEDecodeAudio, 孤海注释, 孤海注释, SetNode, PrimitiveFloat, 孤海注释, 孤海注释, MiniMaxH3ImageToVideo, MiniMaxH3ReferenceToVideo, GetNode, 忽略多组孤海, MarkdownNote, CLIPLoader, 忽略多组孤海, ImageResizeKJv2, ImageResizeKJv2, VHS_VideoCombine, LoadImage, VRGDG_MiniMaxH3AudioDrive, Any Switch (rgthree), PrimitiveFloat, ResolutionSelector, 孤海注释, VAEDecode, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, Int, KSamplerSelect, BasicScheduler, SelfLiftH3Sampler, 孤海注释, MathExpression|pysssss, 孤海注释, SetNode, ModelPreviewOverrideKJ, MiniMaxChunkFeedForward, MiniMaxH3SigmaShift, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, LoadImage]
patterns: []
missing: [MathExpression|pysssss, 布尔孤海, 忽略多组孤海, 忽略多组孤海]
discoveries: [次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `布尔孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V6.0_2100491353854668802.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V6.0_2100491353854668802.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（108 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `GetNode`
- `LoadAudio`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `孤海注释`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAELoader`
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `布尔孤海`
- `孤海注释`
- `孤海注释`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `ImpactConditionalBranch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ConditioningZeroOut`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `VAEDecodeAudio` ★核心
- `孤海注释`
- `孤海注释`
- `SetNode`
- `PrimitiveFloat`
- `孤海注释`
- `孤海注释`
- `MiniMaxH3ImageToVideo`
- `MiniMaxH3ReferenceToVideo`
- `GetNode`
- `忽略多组孤海`
- `MarkdownNote`
- `CLIPLoader`
- `忽略多组孤海`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `LoadImage`
- `VRGDG_MiniMaxH3AudioDrive`
- `Any Switch (rgthree)`
- `PrimitiveFloat`
- `ResolutionSelector`
- `孤海注释`
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `Int`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `SelfLiftH3Sampler` ★核心
- `孤海注释`
- `MathExpression|pysssss`
- `孤海注释`
- `SetNode`
- `ModelPreviewOverrideKJ`
- `MiniMaxChunkFeedForward`
- `MiniMaxH3SigmaShift`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxLowVRAMAttention`
- `LoadImage`

## 知识

覆盖率 **33%**（36/108）

**有卡**：`LoadImage`、`VHS_LoadVideo`、`LoadAudio`、`VAELoader`、`ComfyMathExpression`、`ImpactConditionalBranch`、`ConditioningZeroOut`、`VAEDecodeAudio`、`MiniMaxH3ImageToVideo`、`MiniMaxH3ReferenceToVideo`、`CLIPLoader`、`ImageResizeKJv2`、`VHS_VideoCombine`、`VRGDG_MiniMaxH3AudioDrive`、`ResolutionSelector`、`VAEDecode`、`UNETLoader`、`Int`、`KSamplerSelect`、`BasicScheduler`、`SelfLiftH3Sampler`、`ModelPreviewOverrideKJ`、`MiniMaxChunkFeedForward`、`MiniMaxH3SigmaShift`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxLowVRAMAttention`

**缺卡**（4）：`MathExpression|pysssss`、`布尔孤海`、`忽略多组孤海`、`忽略多组孤海`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `布尔孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
