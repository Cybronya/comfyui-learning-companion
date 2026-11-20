---
key: 视频生成/图生视频/Minimax_Fasth3_Ominiref_Solarrenderer 视频到视频工作流_2114749514438504449.json
name: Minimax_Fasth3_Ominiref_Solarrenderer 视频到视频工作流_2114749514438504449
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax_Fasth3_Ominiref_Solarrenderer 视频到视频工作流_2114749514438504449.json
hash: bffdb35867467c88
coverage: 0.47541
learned_at: 2026-10-30 17:58:30
nodes: [MarkdownNote, ComfyMathExpression, SetNode, PrimitiveNode, CLIPLoader, VAELoader, SetNode, ResolutionSelector, SetNode, GetNode, GetNode, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, PrimitiveFloat, LoraLoaderModelOnly, SetNode, GetNode, GetNode, KSamplerSelect, GetNode, ConditioningZeroOut, GetNode, SetNode, BasicScheduler, VAEDecode, GetNode, VAEDecodeAudio, VHS_VideoCombine, SelfLiftH3Sampler, VAELoader, UNETLoader, SetNode, PrimitiveStringMultiline, MiniMaxH3ReferenceToVideo, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxChunkFeedForward, ModelPatchTorchSettings, MiniMaxH3SigmaShift, BlockSparseAttention, VHS_LoadVideo, AIO_Preprocessor, VHS_VideoCombine, ModelAttentionBackend, LoadImage, SetNode, GetNode, LoraLoaderModelOnly, Note, Note, Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/图生视频/Minimax_Fasth3_Ominiref_Solarrenderer 视频到视频工作流_2114749514438504449.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax_Fasth3_Ominiref_Solarrenderer 视频到视频工作流_2114749514438504449.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Other

**节点**（61 个）：
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
- `SetNode`
- `PrimitiveStringMultiline`
- `MiniMaxH3ReferenceToVideo`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxChunkFeedForward`
- `ModelPatchTorchSettings`
- `MiniMaxH3SigmaShift`
- `BlockSparseAttention`
- `VHS_LoadVideo`
- `AIO_Preprocessor`
- `VHS_VideoCombine`
- `ModelAttentionBackend`
- `LoadImage`
- `SetNode`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `Note`
- `Label (rgthree)`

## 知识

覆盖率 **48%**（29/61）

**有卡**：`ComfyMathExpression`、`CLIPLoader`、`VAELoader`、`ResolutionSelector`、`ImageScaleToTotalPixels`、`LoraLoaderModelOnly`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`VAEDecode`、`VAEDecodeAudio`、`VHS_VideoCombine`、`SelfLiftH3Sampler`、`UNETLoader`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxChunkFeedForward`、`ModelPatchTorchSettings`、`MiniMaxH3SigmaShift`、`BlockSparseAttention`、`VHS_LoadVideo`、`AIO_Preprocessor`、`ModelAttentionBackend`、`LoadImage`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
