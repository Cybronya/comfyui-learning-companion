---
key: 视频生成/文生视频/MiniMax H3 全模态 v2.1 I 动作增强 I sigma细节增强 I 官流加速 I 提示词强化_2097079739075883009.json
name: MiniMax H3 全模态 v2.1 I 动作增强 I sigma细节增强 I 官流加速 I 提示词强化_2097079739075883009
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 全模态 v2.1 I 动作增强 I sigma细节增强 I 官流加速 I 提示词强化_2097079739075883009.json
hash: 84af062062f5998c
coverage: 0.46281
learned_at: 2026-10-15 22:45:35
nodes: [Note, CLIPLoader, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, LoadImage, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, SetNode, SetNode, BasicGuider, KSamplerSelect, VAEDecodeAudio, SetNode, VAELoader, VAEDecode, GetImageSize, ComfyMathExpression, SeedVR2, SeedVR2ExtraArgs, SeedVR2BlockSwap, UNETLoader, easy clearCacheAll, SetNode, SetNode, RTXVideoSuperResolution, GetNode, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), SamplerCustomAdvanced, GetNode, GetNode, GetNode, MarkdownNote, Int, GetNode, GetNode, SetNode, SetNode, VHS_VideoCombine, RandomNoise, MiniMaxH3ReferenceToVideo, GetNode, Note, llama_cpp_parameters, Note, LoadImage, LoadImage, LoadImage, MiniMaxChunkFeedForward, llama_cpp_instruct_adv, easy showAnything, KepStringLiteral, SetNode, LoadAudioUI, LoadAudioUI, LoadAudioUI, SetNode, MiniMaxLowVRAMAttention, BasicScheduler, String Literal, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, String Literal, LoraLoaderModelOnly, String Literal, SetNode, SetNode, Label (rgthree), Label (rgthree), LoraLoaderBypassModelOnly, LoraLoaderModelOnly, ExtendIntermediateSigmas, Fast Groups Bypasser (rgthree), llama_cpp_model_loader, LoadImage, PrimitiveStringMultiline, MarkdownNote, String Literal, PrimitiveFloat, ResolutionSelector]
patterns: []
missing: []
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

覆盖率 **46%**（56/121）

**有卡**：`CLIPLoader`、`VAELoader`、`VHS_LoadVideo`、`LoadImage`、`ComfyMathExpression`、`BasicGuider`、`KSamplerSelect`、`VAEDecodeAudio`、`VAEDecode`、`GetImageSize`、`SeedVR2`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`UNETLoader`、`easy clearCacheAll`、`RTXVideoSuperResolution`、`SamplerCustomAdvanced`、`Int`、`VHS_VideoCombine`、`RandomNoise`、`MiniMaxH3ReferenceToVideo`、`llama_cpp_parameters`、`MiniMaxChunkFeedForward`、`llama_cpp_instruct_adv`、`KepStringLiteral`、`LoadAudioUI`、`MiniMaxLowVRAMAttention`、`BasicScheduler`、`String Literal`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`LoraLoaderModelOnly`、`Label (rgthree)`、`LoraLoaderBypassModelOnly`、`ExtendIntermediateSigmas`、`llama_cpp_model_loader`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
