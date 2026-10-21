---
key: 图片生成/文生图/MiniMax H3-多参考生视频（8.31最佳）_2094270099418079233.json
name: MiniMax H3-多参考生视频（8.31最佳）_2094270099418079233
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/MiniMax H3-多参考生视频（8.31最佳）_2094270099418079233.json
hash: 389c02c89db7148f
coverage: 0.413793
learned_at: 2026-10-20 01:19:23
nodes: [SetNode, LoadImage, LoadImage, VAELoader, VAELoader, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_LoadVideo, SetNode, SetNode, SetNode, VHS_LoadVideo, VHS_LoadVideo, SetNode, SetNode, LoadImage, LoadImage, LoadImage, SetNode, SetNode, SetNode, GetNode, SetNode, LoraLoaderModelOnly, CLIPLoader, Reroute, Reroute, GetNode, GetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, MiniMaxH3ReferenceToVideo, SetNode, SamplerCustomAdvanced, SetNode, BasicGuider, SetNode, SetNode, SetNode, VAEDecode, VAEDecodeAudio, GetNode, MarkdownNote, SamplerCustomAdvanced, GetNode, GetNode, GetNode, LTXVSeparateAVLatent, LoadAudio, SetNode, LoadAudio, SetNode, LoadAudio, SetNode, Note, KSamplerSelect, UNETLoader, SetNode, GetNode, SetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, VHS_VideoCombine, SplitSigmas, VHS_VideoCombine, SetNode, LoadImage, LoadImage, LTXVConcatAVLatent, MinimaxH3LatentUpscaler3D, GetNode, SetNode, ComfyMathExpression, GetNode, GetNode, easy float, BasicScheduler, PrimitiveFloat, RandomNoise, LoadImage, ResolutionSelector, Text, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, 忽略多组孤海, Note]
patterns: []
missing: []
---

# 图片生成/文生图/MiniMax H3-多参考生视频（8.31最佳）_2094270099418079233.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/MiniMax H3-多参考生视频（8.31最佳）_2094270099418079233.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（116 个）：
- `SetNode`
- `LoadImage`
- `LoadImage`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `Reroute`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `SetNode`
- `BasicGuider`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAEDecode` ★核心
- `VAEDecodeAudio` ★核心
- `GetNode`
- `MarkdownNote`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `LTXVSeparateAVLatent`
- `LoadAudio`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `LoadAudio`
- `SetNode`
- `Note`
- `KSamplerSelect` ★核心
- `UNETLoader` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `VHS_VideoCombine`
- `SplitSigmas`
- `VHS_VideoCombine`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LTXVConcatAVLatent`
- `MinimaxH3LatentUpscaler3D`
- `GetNode`
- `SetNode`
- `ComfyMathExpression`
- `GetNode`
- `GetNode`
- `easy float`
- `BasicScheduler`
- `PrimitiveFloat`
- `RandomNoise`
- `LoadImage`
- `ResolutionSelector`
- `Text`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `忽略多组孤海`
- `Note`

## 知识

覆盖率 **41%**（48/116）

**有卡**：`LoadImage`、`VAELoader`、`VHS_LoadVideo`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAEDecodeAudio`、`VAEDecode`、`MiniMaxH3ReferenceToVideo`、`SamplerCustomAdvanced`、`BasicGuider`、`LTXVSeparateAVLatent`、`LoadAudio`、`KSamplerSelect`、`UNETLoader`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`VHS_VideoCombine`、`SplitSigmas`、`LTXVConcatAVLatent`、`MinimaxH3LatentUpscaler3D`、`ComfyMathExpression`、`easy float`、`BasicScheduler`、`RandomNoise`、`ResolutionSelector`、`Text`、`忽略多组孤海`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
