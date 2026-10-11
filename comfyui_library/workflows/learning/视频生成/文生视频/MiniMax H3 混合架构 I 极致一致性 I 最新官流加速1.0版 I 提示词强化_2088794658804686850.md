---
key: 视频生成/文生视频/MiniMax H3 混合架构 I 极致一致性 I 最新官流加速1.0版 I 提示词强化_2088794658804686850.json
name: MiniMax H3 混合架构 I 极致一致性 I 最新官流加速1.0版 I 提示词强化_2088794658804686850
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 混合架构 I 极致一致性 I 最新官流加速1.0版 I 提示词强化_2088794658804686850.json
hash: bbeb6d1d38b56164
coverage: 0.818182
learned_at: 2026-10-11 21:19:44
nodes: [KepStringLiteral, Note, ComfyMathExpression, MiniMaxH3GenerationTailLoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, LoadImage, LoadImage, VHS_LoadAudioUpload, BasicGuider, MiniMaxH3PromptEnhancer, SeedVR2ExtraArgs, SeedVR2BlockSwap, SeedVR2, KSamplerSelect, RTXVideoSuperResolution, BasicScheduler, RandomNoise, MiniMaxChunkFeedForward, MiniMaxLowVRAMAttention, CLIPLoader, VAELoader, VAELoader, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, Fast Groups Bypasser (rgthree), LoraLoaderModelOnly, Note, LoadImage, LoadImage, MarkdownNote, Label (rgthree), UNETLoader, MiniMaxH3HybridLoader, LoadImage, PrimitiveStringMultiline, PrimitiveFloat, ResolutionSelector, VHS_LoadAudioUpload, VHS_LoadAudioUpload, MiniMaxH3ReferenceToVideo, VHS_VideoCombine, Label (rgthree)]
patterns: []
missing: [Label (rgthree), Label (rgthree)]
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 视频生成/文生视频/MiniMax H3 混合架构 I 极致一致性 I 最新官流加速1.0版 I 提示词强化_2088794658804686850.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 混合架构 I 极致一致性 I 最新官流加速1.0版 I 提示词强化_2088794658804686850.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（44 个）：
- `KepStringLiteral`
- `Note`
- `ComfyMathExpression`
- `MiniMaxH3GenerationTailLoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `VHS_LoadAudioUpload`
- `BasicGuider`
- `MiniMaxH3PromptEnhancer`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `SeedVR2`
- `KSamplerSelect` ★核心
- `RTXVideoSuperResolution`
- `BasicScheduler`
- `RandomNoise`
- `MiniMaxChunkFeedForward`
- `MiniMaxLowVRAMAttention`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `Fast Groups Bypasser (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `LoadImage`
- `LoadImage`
- `MarkdownNote`
- `Label (rgthree)`
- `UNETLoader` ★核心
- `MiniMaxH3HybridLoader`
- `LoadImage`
- `PrimitiveStringMultiline`
- `PrimitiveFloat`
- `ResolutionSelector`
- `VHS_LoadAudioUpload`
- `VHS_LoadAudioUpload`
- `MiniMaxH3ReferenceToVideo`
- `VHS_VideoCombine`
- `Label (rgthree)`

## 知识

覆盖率 **82%**（36/44）

**有卡**：`KepStringLiteral`、`ComfyMathExpression`、`MiniMaxH3GenerationTailLoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`LoadImage`、`VHS_LoadAudioUpload`、`BasicGuider`、`MiniMaxH3PromptEnhancer`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`SeedVR2`、`KSamplerSelect`、`RTXVideoSuperResolution`、`BasicScheduler`、`RandomNoise`、`MiniMaxChunkFeedForward`、`MiniMaxLowVRAMAttention`、`CLIPLoader`、`VAELoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`LoraLoaderModelOnly`、`UNETLoader`、`MiniMaxH3HybridLoader`、`ResolutionSelector`、`MiniMaxH3ReferenceToVideo`、`VHS_VideoCombine`

**缺卡**（2）：`Label (rgthree)`、`Label (rgthree)`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
