---
key: 视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V6.1_2098342858284691457.json
name: 自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V6.1_2098342858284691457
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V6.1_2098342858284691457.json
hash: 9be3c8de3cea4ac9
coverage: 0.37963
learned_at: 2026-10-15 22:48:59
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, SetNode, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, GetNode, LoadAudio, GetNode, SetNode, SetNode, SetNode, 孤海注释, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, VAELoader, ComfyMathExpression, SetNode, ModelPreviewOverrideKJ, GetNode, GetNode, GetNode, 孤海注释, GetNode, 布尔孤海, 孤海注释, 孤海注释, 孤海注释, ResolutionSelector, VAELoader, GetNode, GetNode, GetNode, SetNode, GetNode, SetNode, GetNode, SetNode, SetNode, ImpactConditionalBranch, GetNode, GetNode, GetNode, GetNode, GetNode, ConditioningZeroOut, GetNode, GetNode, GetNode, GetNode, Any Switch (rgthree), VAEDecode, VAEDecodeAudio, 孤海注释, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxLowVRAMAttention, 孤海注释, SetNode, PrimitiveFloat, 孤海注释, 孤海注释, MiniMaxH3ImageToVideo, MiniMaxH3ReferenceToVideo, GetNode, 忽略多组孤海, MarkdownNote, CLIPLoader, 忽略多组孤海, ImageResizeKJv2, ImageResizeKJv2, 孤海注释, VHS_VideoCombine, PrimitiveStringMultiline, LoadImage, VRGDG_MiniMaxH3AudioDrive, Any Switch (rgthree), Int, 孤海注释, PrimitiveFloat, LoadImage, SelfLiftH3Sampler, 孤海注释, MiniMaxChunkFeedForward, LoraLoaderModelOnly, UNETLoader, SetNode, MiniMaxH3SigmaShift, MathExpression|pysssss, BasicScheduler, KSamplerSelect]
patterns: []
missing: []
---

# 视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V6.1_2098342858284691457.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/自用版   Minimax H3 文生+首尾+图参多合一生视频二采高清放大工作流V6.1_2098342858284691457.json`

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
- `ModelPreviewOverrideKJ`
- `GetNode`
- `GetNode`
- `GetNode`
- `孤海注释`
- `GetNode`
- `布尔孤海`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `ResolutionSelector`
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
- `Any Switch (rgthree)`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `孤海注释`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxLowVRAMAttention`
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
- `孤海注释`
- `VHS_VideoCombine`
- `PrimitiveStringMultiline`
- `LoadImage`
- `VRGDG_MiniMaxH3AudioDrive`
- `Any Switch (rgthree)`
- `Int`
- `孤海注释`
- `PrimitiveFloat`
- `LoadImage`
- `SelfLiftH3Sampler` ★核心
- `孤海注释`
- `MiniMaxChunkFeedForward`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `MiniMaxH3SigmaShift`
- `MathExpression|pysssss`
- `BasicScheduler`
- `KSamplerSelect` ★核心

## 知识

覆盖率 **38%**（41/108）

**有卡**：`LoadImage`、`VHS_LoadVideo`、`LoadAudio`、`VAELoader`、`ComfyMathExpression`、`ModelPreviewOverrideKJ`、`布尔孤海`、`ResolutionSelector`、`ImpactConditionalBranch`、`ConditioningZeroOut`、`VAEDecode`、`VAEDecodeAudio`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxLowVRAMAttention`、`MiniMaxH3ImageToVideo`、`MiniMaxH3ReferenceToVideo`、`忽略多组孤海`、`CLIPLoader`、`ImageResizeKJv2`、`VHS_VideoCombine`、`VRGDG_MiniMaxH3AudioDrive`、`Int`、`SelfLiftH3Sampler`、`MiniMaxChunkFeedForward`、`LoraLoaderModelOnly`、`UNETLoader`、`MiniMaxH3SigmaShift`、`MathExpression|pysssss`、`BasicScheduler`、`KSamplerSelect`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
