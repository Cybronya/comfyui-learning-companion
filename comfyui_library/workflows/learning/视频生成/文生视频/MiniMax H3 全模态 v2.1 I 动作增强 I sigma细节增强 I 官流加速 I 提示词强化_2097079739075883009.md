---
key: 视频生成/文生视频/MiniMax H3 全模态 v2.1 I 动作增强 I sigma细节增强 I 官流加速 I 提示词强化_2097079739075883009.json
name: MiniMax H3 全模态 v2.1 I 动作增强 I sigma细节增强 I 官流加速 I 提示词强化_2097079739075883009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 全模态 v2.1 I 动作增强 I sigma细节增强 I 官流加速 I 提示词强化_2097079739075883009.json
hash: 84af062062f5998c
coverage: 0.404959
learned_at: 2026-10-11 21:41:41
nodes: [Note, CLIPLoader, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, LoadImage, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, SetNode, SetNode, BasicGuider, KSamplerSelect, VAEDecodeAudio, SetNode, VAELoader, VAEDecode, GetImageSize, ComfyMathExpression, SeedVR2, SeedVR2ExtraArgs, SeedVR2BlockSwap, UNETLoader, easy clearCacheAll, SetNode, SetNode, RTXVideoSuperResolution, GetNode, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), SamplerCustomAdvanced, GetNode, GetNode, GetNode, MarkdownNote, Int, GetNode, GetNode, SetNode, SetNode, VHS_VideoCombine, RandomNoise, MiniMaxH3ReferenceToVideo, GetNode, Note, llama_cpp_parameters, Note, LoadImage, LoadImage, LoadImage, MiniMaxChunkFeedForward, llama_cpp_instruct_adv, easy showAnything, KepStringLiteral, SetNode, LoadAudioUI, LoadAudioUI, LoadAudioUI, SetNode, MiniMaxLowVRAMAttention, BasicScheduler, String Literal, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, String Literal, LoraLoaderModelOnly, String Literal, SetNode, SetNode, Label (rgthree), Label (rgthree), LoraLoaderBypassModelOnly, LoraLoaderModelOnly, ExtendIntermediateSigmas, Fast Groups Bypasser (rgthree), llama_cpp_model_loader, LoadImage, PrimitiveStringMultiline, MarkdownNote, String Literal, PrimitiveFloat, ResolutionSelector]
patterns: []
missing: [Label (rgthree), Label (rgthree), String Literal, String Literal, String Literal, String Literal, easy clearCacheAll]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/MiniMax H3 全模态 v2.1 I 动作增强 I sigma细节增强 I 官流加速 I 提示词强化_2097079739075883009.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 全模态 v2.1 I 动作增强 I sigma细节增强 I 官流加速 I 提示词强化_2097079739075883009.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（121 个）：
- `Note`
- `CLIPLoader`
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
- `GetNode`
- `GetNode`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `LoadImage`
- `SetNode`
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
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `VAEDecodeAudio` ★核心
- `SetNode`
- `VAELoader`
- `VAEDecode` ★核心
- `GetImageSize`
- `ComfyMathExpression`
- `SeedVR2`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `UNETLoader` ★核心
- `easy clearCacheAll`
- `SetNode`
- `SetNode`
- `RTXVideoSuperResolution`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `MarkdownNote`
- `Int`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `RandomNoise`
- `MiniMaxH3ReferenceToVideo`
- `GetNode`
- `Note`
- `llama_cpp_parameters`
- `Note`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxChunkFeedForward`
- `llama_cpp_instruct_adv`
- `easy showAnything`
- `KepStringLiteral`
- `SetNode`
- `LoadAudioUI`
- `LoadAudioUI`
- `LoadAudioUI`
- `SetNode`
- `MiniMaxLowVRAMAttention`
- `BasicScheduler`
- `String Literal`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `String Literal`
- `LoraLoaderModelOnly` ★核心
- `String Literal`
- `SetNode`
- `SetNode`
- `Label (rgthree)`
- `Label (rgthree)`
- `LoraLoaderBypassModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ExtendIntermediateSigmas`
- `Fast Groups Bypasser (rgthree)`
- `llama_cpp_model_loader`
- `LoadImage`
- `PrimitiveStringMultiline`
- `MarkdownNote`
- `String Literal`
- `PrimitiveFloat`
- `ResolutionSelector`

## 知识

覆盖率 **40%**（49/121）

**有卡**：`CLIPLoader`、`VAELoader`、`VHS_LoadVideo`、`LoadImage`、`ComfyMathExpression`、`BasicGuider`、`KSamplerSelect`、`VAEDecodeAudio`、`VAEDecode`、`GetImageSize`、`SeedVR2`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`UNETLoader`、`RTXVideoSuperResolution`、`SamplerCustomAdvanced`、`Int`、`VHS_VideoCombine`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`llama_cpp_parameters`、`MiniMaxChunkFeedForward`、`llama_cpp_instruct_adv`、`KepStringLiteral`、`LoadAudioUI`、`MiniMaxLowVRAMAttention`、`BasicScheduler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`LoraLoaderModelOnly`、`LoraLoaderBypassModelOnly`、`ExtendIntermediateSigmas`、`llama_cpp_model_loader`、`ResolutionSelector`

**缺卡**（7）：`Label (rgthree)`、`Label (rgthree)`、`String Literal`、`String Literal`、`String Literal`、`String Literal`、`easy clearCacheAll`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
