---
key: 视频生成/图生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json
name: Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json
hash: d602eaacc398a02e
coverage: 0.554054
learned_at: 2026-10-10 22:53:53
nodes: [SetNode, SetNode, SetNode, SetNode, PrimitiveFloat, GetNode, PathchSageAttentionKJ, SetNode, GetNode, GetNode, GetNode, SetNode, MarkdownNote, MiniMaxH3ReferenceToVideo, VAEDecode, SeedNode, SetNode, ResolutionSelector, GetNode, KSamplerSelect, GetNode, RandomNoise, SamplerCustomAdvanced, BasicGuider, GetNode, ImageResizeKJv2, easy cleanGpuUsed, easy clearCacheAll, RandomNoise, Note, Note, VAEDecode, VAEDecodeAudio, VAEDecodeTiled, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, ImageConcatMulti, VHS_VideoCombine, GetNode, CLIPLoader, VAELoader, VAELoader, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxChunkFeedForward, ModelPatchTorchSettings, MiniMaxH3SigmaShift, SetNode, Note, VHS_VideoCombine, ComfyMathExpression, SetNode, PrimitiveFloat, PrimitiveFloat, Label (rgthree), LoadImage, VHS_LoadVideo, ImageResizeKJv2, UNETLoader, PrimitiveStringMultiline, LoraLoaderModelOnly, BasicScheduler, ResolutionSelector, LoraLoaderModelOnly, MMH3UltimateUpscale, MMH3TemporalSplitParams, Note, MMH3LatentUpscaleWithModelParams, MMH3SpatialSplitParams, KSamplerSelect, BasicScheduler]
patterns: []
missing: [Label (rgthree), easy cleanGpuUsed, easy clearCacheAll]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 视频生成/图生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Minimax_H3_Character_Swap 角色替换_参考到视频工作流_2106641143629959169.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（74 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `GetNode`
- `PathchSageAttentionKJ`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `MarkdownNote`
- `MiniMaxH3ReferenceToVideo`
- `VAEDecode` ★核心
- `SeedNode`
- `SetNode`
- `ResolutionSelector`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `GetNode`
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `RandomNoise`
- `Note`
- `Note`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `GetNode`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxChunkFeedForward`
- `ModelPatchTorchSettings`
- `MiniMaxH3SigmaShift`
- `SetNode`
- `Note`
- `VHS_VideoCombine`
- `ComfyMathExpression`
- `SetNode`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `Label (rgthree)`
- `LoadImage`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `UNETLoader` ★核心
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心
- `MMH3UltimateUpscale`
- `MMH3TemporalSplitParams`
- `Note`
- `MMH3LatentUpscaleWithModelParams`
- `MMH3SpatialSplitParams`
- `KSamplerSelect` ★核心
- `BasicScheduler`

## 知识

覆盖率 **55%**（41/74）

**有卡**：`PathchSageAttentionKJ`、`MiniMaxH3ReferenceToVideo`、`VAEDecode`、`SeedNode`、`ResolutionSelector`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`BasicGuider`、`ImageResizeKJv2`、`VAEDecodeAudio`、`VAEDecodeTiled`、`VHS_VideoCombine`、`ImageConcatMulti`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxChunkFeedForward`、`ModelPatchTorchSettings`、`MiniMaxH3SigmaShift`、`ComfyMathExpression`、`LoadImage`、`VHS_LoadVideo`、`UNETLoader`、`BasicScheduler`、`MMH3UltimateUpscale`、`MMH3TemporalSplitParams`、`MMH3LatentUpscaleWithModelParams`、`MMH3SpatialSplitParams`

**缺卡**（3）：`Label (rgthree)`、`easy cleanGpuUsed`、`easy clearCacheAll`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
