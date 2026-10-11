---
key: 视频生成/文生视频/MiniMax H3 全模态 v2.0 I 混合模型 I 极速二采放大 I 官流加速 I 提示词强化_2089987121053528066.json
name: MiniMax H3 全模态 v2.0 I 混合模型 I 极速二采放大 I 官流加速 I 提示词强化_2089987121053528066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 全模态 v2.0 I 混合模型 I 极速二采放大 I 官流加速 I 提示词强化_2089987121053528066.json
hash: a2025e0397354066
coverage: 0.402985
learned_at: 2026-10-11 21:19:44
nodes: [MiniMaxH3GenerationTailLoader, Label (rgthree), Note, CLIPLoader, VAELoader, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, UNETLoader, KSamplerSelect, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, LTXVSeparateAVLatent, VHS_LoadAudioUpload, VHS_LoadAudioUpload, VHS_LoadAudioUpload, Int, Int, LoadImage, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, SetNode, SetNode, RTXVideoSuperResolution, SplitSigmas, GetNode, GetNode, BasicGuider, KSamplerSelect, UniBlockSwap, VAEDecodeAudio, SetNode, SetNode, SetNode, SamplerCustomAdvanced, BasicGuider, LTXVConcatAVLatent, SetNode, easy clearCacheAll, SetNode, GetNode, GetNode, LoadImage, LoadImage, ResolutionSelector, BasicScheduler, Note, KepStringLiteral, MiniMaxH3PromptEnhancer, SetNode, easy clearCacheAll, MarkdownNote, VHS_VideoCombine, LoadImage, PrimitiveStringMultiline, GetNode, GetNode, GetNode, GetNode, MiniMaxH3ReferenceToVideo, MathExpression|pysssss, SetNode, SamplerCustomAdvanced, PrimitiveFloat, MiniMaxH3MemoryEfficientSageAttentionPatch, MarkdownNote, LoraLoaderModelOnly, ModelAttentionBackend, SetNode, RandomNoise, VAEDecode, GetImageSize, SeedVR2, SeedVR2BlockSwap, SeedVR2ExtraArgs, ComfyMathExpression, UnloadAllModels, easy clearCacheAll, Fast Groups Bypasser (rgthree), Float, MarkdownNote, SetNode, SetNode, Label (rgthree), MinimaxH3LatentUpscaler3D, GetNode]
patterns: []
missing: [Label (rgthree), Label (rgthree), MathExpression|pysssss, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/MiniMax H3 全模态 v2.0 I 混合模型 I 极速二采放大 I 官流加速 I 提示词强化_2089987121053528066.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 全模态 v2.0 I 混合模型 I 极速二采放大 I 官流加速 I 提示词强化_2089987121053528066.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（134 个）：
- `MiniMaxH3GenerationTailLoader`
- `Label (rgthree)`
- `Note`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `LTXVSeparateAVLatent`
- `VHS_LoadAudioUpload`
- `VHS_LoadAudioUpload`
- `VHS_LoadAudioUpload`
- `Int`
- `Int`
- `LoadImage`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `RTXVideoSuperResolution`
- `SplitSigmas`
- `GetNode`
- `GetNode`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `UniBlockSwap`
- `VAEDecodeAudio` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `BasicGuider`
- `LTXVConcatAVLatent`
- `SetNode`
- `easy clearCacheAll`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `BasicScheduler`
- `Note`
- `KepStringLiteral`
- `MiniMaxH3PromptEnhancer`
- `SetNode`
- `easy clearCacheAll`
- `MarkdownNote`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveStringMultiline`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `MathExpression|pysssss`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `PrimitiveFloat`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `SetNode`
- `RandomNoise`
- `VAEDecode` ★核心
- `GetImageSize`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `ComfyMathExpression`
- `UnloadAllModels`
- `easy clearCacheAll`
- `Fast Groups Bypasser (rgthree)`
- `Float`
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `MinimaxH3LatentUpscaler3D`
- `GetNode`

## 知识

覆盖率 **40%**（54/134）

**有卡**：`MiniMaxH3GenerationTailLoader`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`KSamplerSelect`、`VHS_LoadVideo`、`LTXVSeparateAVLatent`、`VHS_LoadAudioUpload`、`Int`、`LoadImage`、`ComfyMathExpression`、`RTXVideoSuperResolution`、`SplitSigmas`、`BasicGuider`、`UniBlockSwap`、`VAEDecodeAudio`、`SamplerCustomAdvanced`、`LTXVConcatAVLatent`、`ResolutionSelector`、`BasicScheduler`、`KepStringLiteral`、`MiniMaxH3PromptEnhancer`、`VHS_VideoCombine`、`MiniMaxH3ReferenceToVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`ModelAttentionBackend`、`RandomNoise`、`VAEDecode`、`GetImageSize`、`SeedVR2`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`UnloadAllModels`、`Float`、`MinimaxH3LatentUpscaler3D`

**缺卡**（6）：`Label (rgthree)`、`Label (rgthree)`、`MathExpression|pysssss`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
