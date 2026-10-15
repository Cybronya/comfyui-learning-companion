---
key: 视频生成/文生视频/MiniMax H3 全模态 v2.0 I 混合模型 I sigma细节增强 I 官流加速 I 提示词强化_2091435408507891714.json
name: MiniMax H3 全模态 v2.0 I 混合模型 I sigma细节增强 I 官流加速 I 提示词强化_2091435408507891714
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 全模态 v2.0 I 混合模型 I sigma细节增强 I 官流加速 I 提示词强化_2091435408507891714.json
hash: dbc68ae9ef4c2757
coverage: 0.440367
learned_at: 2026-10-15 22:45:35
nodes: [MiniMaxH3GenerationTailLoader, Label (rgthree), Note, CLIPLoader, VAELoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadAudioUpload, VHS_LoadAudioUpload, LoadImage, SetNode, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, SetNode, SetNode, SetNode, BasicGuider, KSamplerSelect, UniBlockSwap, VAEDecodeAudio, SetNode, VAELoader, Note, KepStringLiteral, MiniMaxH3PromptEnhancer, SetNode, MarkdownNote, VAEDecode, GetImageSize, ComfyMathExpression, SeedVR2, SeedVR2ExtraArgs, SeedVR2BlockSwap, UNETLoader, easy clearCacheAll, ModelAttentionBackend, SetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, SetNode, RTXVideoSuperResolution, GetNode, GetNode, GetNode, GetNode, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, SamplerCustomAdvanced, GetNode, GetNode, GetNode, MarkdownNote, Int, GetNode, BasicScheduler, GetNode, SetNode, SetNode, SetNode, ExtendIntermediateSigmas, VHS_VideoCombine, RandomNoise, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, LoadImage, LoadImage, LoadImage, VHS_LoadAudioUpload, LoadImage, Label (rgthree), ResolutionSelector, PrimitiveFloat]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 全模态 v2.0 I 混合模型 I sigma细节增强 I 官流加速 I 提示词强化_2091435408507891714.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 全模态 v2.0 I 混合模型 I sigma细节增强 I 官流加速 I 提示词强化_2091435408507891714.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（109 个）：
- `MiniMaxH3GenerationTailLoader`
- `Label (rgthree)`
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
- `VHS_LoadAudioUpload`
- `VHS_LoadAudioUpload`
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
- `UNETLoader` ★核心
- `easy clearCacheAll`
- `ModelAttentionBackend`
- `SetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SetNode`
- `SetNode`
- `RTXVideoSuperResolution`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
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
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_LoadAudioUpload`
- `LoadImage`
- `Label (rgthree)`
- `ResolutionSelector`
- `PrimitiveFloat`

## 知识

覆盖率 **44%**（48/109）

**有卡**：`MiniMaxH3GenerationTailLoader`、`Label (rgthree)`、`CLIPLoader`、`VAELoader`、`VHS_LoadVideo`、`VHS_LoadAudioUpload`、`LoadImage`、`ComfyMathExpression`、`BasicGuider`、`KSamplerSelect`、`UniBlockSwap`、`VAEDecodeAudio`、`KepStringLiteral`、`MiniMaxH3PromptEnhancer`、`VAEDecode`、`GetImageSize`、`SeedVR2`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`UNETLoader`、`easy clearCacheAll`、`ModelAttentionBackend`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`RTXVideoSuperResolution`、`SamplerCustomAdvanced`、`Int`、`BasicScheduler`、`ExtendIntermediateSigmas`、`VHS_VideoCombine`、`RandomNoise`、`LoraLoaderModelOnly`、`MiniMaxH3ReferenceToVideo`、`ResolutionSelector`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
