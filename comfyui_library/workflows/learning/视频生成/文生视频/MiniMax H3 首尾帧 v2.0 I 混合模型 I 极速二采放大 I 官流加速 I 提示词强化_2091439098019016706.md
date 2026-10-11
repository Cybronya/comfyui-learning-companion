---
key: 视频生成/文生视频/MiniMax H3 首尾帧 v2.0 I 混合模型 I 极速二采放大 I 官流加速 I 提示词强化_2091439098019016706.json
name: MiniMax H3 首尾帧 v2.0 I 混合模型 I 极速二采放大 I 官流加速 I 提示词强化_2091439098019016706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 首尾帧 v2.0 I 混合模型 I 极速二采放大 I 官流加速 I 提示词强化_2091439098019016706.json
hash: 9ac64feb3ecbeac3
coverage: 0.381356
learned_at: 2026-10-11 21:19:44
nodes: [MiniMaxH3GenerationTailLoader, Label (rgthree), CLIPLoader, VAELoader, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, UniBlockSwap, SetNode, SetNode, VAELoader, Note, KepStringLiteral, MiniMaxH3PromptEnhancer, SetNode, MarkdownNote, GetImageSize, ComfyMathExpression, SeedVR2, SeedVR2ExtraArgs, SeedVR2BlockSwap, SplitSigmas, SetNode, ModelAttentionBackend, SetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, MarkdownNote, RTXVideoSuperResolution, MarkdownNote, BasicScheduler, SetNode, SetNode, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, LoraLoaderModelOnly, Int, Int, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ResolutionSelector, GetNode, SetNode, SetNode, ComfyMathExpression, GetNode, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, KSamplerSelect, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, MathExpression|pysssss, GetNode, GetNode, GetNode, LTXVConcatAVLatent, LTXVSeparateAVLatent, GetNode, VAEDecodeAudio, VAEDecode, GetNode, MiniMaxH3ImageToVideo, GetNode, KSamplerSelect, BasicGuider, easy clearCacheAll, SetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, ResizeImageMaskNode, SetNode, GetNode, ResizeImageMaskNode, SetNode, ResizeImageMaskNode, GetNode, SetNode, GetNode, GetNode, ResizeImageMaskNode, SetNode, MinimaxH3LatentUpscaler3D, SetNode, SetNode, easy clearCacheAll, easy clearCacheAll, MathExpression|pysssss, MathExpression|pysssss, MiniMaxH3ImageToVideo, BasicGuider, SamplerCustomAdvanced, RandomNoise, UNETLoader, VHS_VideoCombine, Label (rgthree), LoadImage, PrimitiveFloat, Float]
patterns: []
missing: [Label (rgthree), Label (rgthree), MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/MiniMax H3 首尾帧 v2.0 I 混合模型 I 极速二采放大 I 官流加速 I 提示词强化_2091439098019016706.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 首尾帧 v2.0 I 混合模型 I 极速二采放大 I 官流加速 I 提示词强化_2091439098019016706.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（118 个）：
- `MiniMaxH3GenerationTailLoader`
- `Label (rgthree)`
- `CLIPLoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `UniBlockSwap`
- `SetNode`
- `SetNode`
- `VAELoader`
- `Note`
- `KepStringLiteral`
- `MiniMaxH3PromptEnhancer`
- `SetNode`
- `MarkdownNote`
- `GetImageSize`
- `ComfyMathExpression`
- `SeedVR2`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `SplitSigmas`
- `SetNode`
- `ModelAttentionBackend`
- `SetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SetNode`
- `MarkdownNote`
- `RTXVideoSuperResolution`
- `MarkdownNote`
- `BasicScheduler`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `LoraLoaderModelOnly` ★核心
- `Int`
- `Int`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ResolutionSelector`
- `GetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `GetNode`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `KSamplerSelect` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `MathExpression|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `GetNode`
- `MiniMaxH3ImageToVideo`
- `GetNode`
- `KSamplerSelect` ★核心
- `BasicGuider`
- `easy clearCacheAll`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `SetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `SetNode`
- `ResizeImageMaskNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `ResizeImageMaskNode`
- `SetNode`
- `MinimaxH3LatentUpscaler3D`
- `SetNode`
- `SetNode`
- `easy clearCacheAll`
- `easy clearCacheAll`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MiniMaxH3ImageToVideo`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `Label (rgthree)`
- `LoadImage`
- `PrimitiveFloat`
- `Float`

## 知识

覆盖率 **38%**（45/118）

**有卡**：`MiniMaxH3GenerationTailLoader`、`CLIPLoader`、`VAELoader`、`UniBlockSwap`、`KepStringLiteral`、`MiniMaxH3PromptEnhancer`、`GetImageSize`、`ComfyMathExpression`、`SeedVR2`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`SplitSigmas`、`ModelAttentionBackend`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`RTXVideoSuperResolution`、`BasicScheduler`、`LoraLoaderModelOnly`、`Int`、`ResolutionSelector`、`LoadImage`、`KSamplerSelect`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`VAEDecodeAudio`、`VAEDecode`、`MiniMaxH3ImageToVideo`、`BasicGuider`、`SamplerCustomAdvanced`、`ResizeImageMaskNode`、`MinimaxH3LatentUpscaler3D`、`RandomNoise`、`UNETLoader`、`VHS_VideoCombine`、`Float`

**缺卡**（8）：`Label (rgthree)`、`Label (rgthree)`、`MathExpression|pysssss`、`MathExpression|pysssss`、`MathExpression|pysssss`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `MathExpression|pysssss` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
