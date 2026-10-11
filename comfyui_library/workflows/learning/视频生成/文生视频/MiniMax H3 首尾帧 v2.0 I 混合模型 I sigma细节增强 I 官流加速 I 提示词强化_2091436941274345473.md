---
key: 视频生成/文生视频/MiniMax H3 首尾帧 v2.0 I 混合模型 I sigma细节增强 I 官流加速 I 提示词强化_2091436941274345473.json
name: MiniMax H3 首尾帧 v2.0 I 混合模型 I sigma细节增强 I 官流加速 I 提示词强化_2091436941274345473
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 首尾帧 v2.0 I 混合模型 I sigma细节增强 I 官流加速 I 提示词强化_2091436941274345473.json
hash: bb37958762d77c37
coverage: 0.459459
learned_at: 2026-10-11 21:19:44
nodes: [MiniMaxH3GenerationTailLoader, Label (rgthree), CLIPLoader, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, ComfyMathExpression, SetNode, SetNode, SetNode, BasicGuider, KSamplerSelect, UniBlockSwap, VAEDecodeAudio, SetNode, VAELoader, Note, KepStringLiteral, MiniMaxH3PromptEnhancer, SetNode, MarkdownNote, VAEDecode, GetImageSize, ComfyMathExpression, SeedVR2, SeedVR2ExtraArgs, SeedVR2BlockSwap, ModelAttentionBackend, SetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, SetNode, RTXVideoSuperResolution, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, SamplerCustomAdvanced, GetNode, GetNode, GetNode, MarkdownNote, Int, GetNode, BasicScheduler, GetNode, SetNode, SetNode, SetNode, ExtendIntermediateSigmas, VHS_VideoCombine, RandomNoise, LoraLoaderModelOnly, GetNode, GetNode, GetNode, GetNode, easy clearCacheAll, MiniMaxH3ImageToVideo, GetNode, GetNode, SetNode, GetNode, GetNode, SetNode, UNETLoader, Label (rgthree), LoadImage, ResizeImageMaskNode, LoadImage, ResizeImageMaskNode, ResolutionSelector, PrimitiveFloat]
patterns: []
missing: [Label (rgthree), Label (rgthree), easy clearCacheAll]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/MiniMax H3 首尾帧 v2.0 I 混合模型 I sigma细节增强 I 官流加速 I 提示词强化_2091436941274345473.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 首尾帧 v2.0 I 混合模型 I sigma细节增强 I 官流加速 I 提示词强化_2091436941274345473.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（74 个）：
- `MiniMaxH3GenerationTailLoader`
- `Label (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `UniBlockSwap`
- `VAEDecodeAudio` ★核心
- `SetNode`
- `VAELoader`
- `Note`
- `KepStringLiteral`
- `MiniMaxH3PromptEnhancer`
- `SetNode`
- `MarkdownNote`
- `VAEDecode` ★核心
- `GetImageSize`
- `ComfyMathExpression`
- `SeedVR2`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `ModelAttentionBackend`
- `SetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SetNode`
- `SetNode`
- `RTXVideoSuperResolution`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `Int`
- `GetNode`
- `BasicScheduler`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ExtendIntermediateSigmas`
- `VHS_VideoCombine`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy clearCacheAll`
- `MiniMaxH3ImageToVideo`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `UNETLoader` ★核心
- `Label (rgthree)`
- `LoadImage`
- `ResizeImageMaskNode`
- `LoadImage`
- `ResizeImageMaskNode`
- `ResolutionSelector`
- `PrimitiveFloat`

## 知识

覆盖率 **46%**（34/74）

**有卡**：`MiniMaxH3GenerationTailLoader`、`CLIPLoader`、`VAELoader`、`ComfyMathExpression`、`BasicGuider`、`KSamplerSelect`、`UniBlockSwap`、`VAEDecodeAudio`、`KepStringLiteral`、`MiniMaxH3PromptEnhancer`、`VAEDecode`、`GetImageSize`、`SeedVR2`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`ModelAttentionBackend`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`RTXVideoSuperResolution`、`SamplerCustomAdvanced`、`Int`、`BasicScheduler`、`ExtendIntermediateSigmas`、`VHS_VideoCombine`、`RandomNoise`、`LoraLoaderModelOnly`、`MiniMaxH3ImageToVideo`、`UNETLoader`、`LoadImage`、`ResizeImageMaskNode`、`ResolutionSelector`

**缺卡**（3）：`Label (rgthree)`、`Label (rgthree)`、`easy clearCacheAll`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
