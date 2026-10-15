---
key: 视频生成/文生视频/MiniMax H3 全功能全模态 I 最新官流加速 v1.0 I 极致优化 I 提示词强化_2087318804178231297.json
name: MiniMax H3 全功能全模态 I 最新官流加速 v1.0 I 极致优化 I 提示词强化_2087318804178231297
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax H3 全功能全模态 I 最新官流加速 v1.0 I 极致优化 I 提示词强化_2087318804178231297.json
hash: 9a4004f9e3059a05
coverage: 0.863636
learned_at: 2026-10-15 22:45:35
nodes: [KepStringLiteral, Note, MarkdownNote, VHS_LoadVideo, VAELoader, VAELoader, ComfyMathExpression, PrimitiveFloat, RandomNoise, UniBlockSwap, UNETLoader, CLIPLoader, MiniMaxH3GenerationTailLoader, VAEDecodeAudio, VAEDecode, SamplerCustomAdvanced, LoadImage, LoadImage, LoadImage, VHS_LoadAudioUpload, VHS_LoadAudioUpload, VHS_LoadAudioUpload, VHS_LoadVideo, VHS_LoadVideo, Fast Groups Bypasser (rgthree), BasicGuider, MiniMaxH3PromptEnhancer, MiniMaxH3MemoryEfficientSageAttentionPatch, BasicScheduler, ResolutionSelector, PrimitiveStringMultiline, RTXVideoSuperResolution, SeedVR2ExtraArgs, SeedVR2BlockSwap, Note, Label (rgthree), MiniMaxH3ReferenceToVideo, LoadImage, LoadImage, VHS_VideoCombine, SeedVR2, LoraLoaderModelOnly, KSamplerSelect, Label (rgthree)]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax H3 全功能全模态 I 最新官流加速 v1.0 I 极致优化 I 提示词强化_2087318804178231297.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax H3 全功能全模态 I 最新官流加速 v1.0 I 极致优化 I 提示词强化_2087318804178231297.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（44 个）：
- `KepStringLiteral`
- `Note`
- `MarkdownNote`
- `VHS_LoadVideo`
- `VAELoader`
- `VAELoader`
- `ComfyMathExpression`
- `PrimitiveFloat`
- `RandomNoise`
- `UniBlockSwap`
- `UNETLoader` ★核心
- `CLIPLoader`
- `MiniMaxH3GenerationTailLoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_LoadAudioUpload`
- `VHS_LoadAudioUpload`
- `VHS_LoadAudioUpload`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `BasicGuider`
- `MiniMaxH3PromptEnhancer`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `BasicScheduler`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
- `RTXVideoSuperResolution`
- `SeedVR2ExtraArgs`
- `SeedVR2BlockSwap`
- `Note`
- `Label (rgthree)`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `SeedVR2`
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `Label (rgthree)`

## 知识

覆盖率 **86%**（38/44）

**有卡**：`KepStringLiteral`、`VHS_LoadVideo`、`VAELoader`、`ComfyMathExpression`、`RandomNoise`、`UniBlockSwap`、`UNETLoader`、`CLIPLoader`、`MiniMaxH3GenerationTailLoader`、`VAEDecodeAudio`、`VAEDecode`、`SamplerCustomAdvanced`、`LoadImage`、`VHS_LoadAudioUpload`、`BasicGuider`、`MiniMaxH3PromptEnhancer`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`BasicScheduler`、`ResolutionSelector`、`RTXVideoSuperResolution`、`SeedVR2ExtraArgs`、`SeedVR2BlockSwap`、`Label (rgthree)`、`MiniMaxH3ReferenceToVideo`、`VHS_VideoCombine`、`SeedVR2`、`LoraLoaderModelOnly`、`KSamplerSelect`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
