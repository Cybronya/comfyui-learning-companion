---
key: 视频生成/文生视频/MiniMax+H3+新ref V1.0 Lora 阿里8步版本-多参考工作流_2096537181975310338.json
name: MiniMax+H3+新ref V1.0 Lora 阿里8步版本-多参考工作流_2096537181975310338
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax+H3+新ref V1.0 Lora 阿里8步版本-多参考工作流_2096537181975310338.json
hash: 7b244b62a63b37d8
coverage: 0.782609
learned_at: 2026-10-15 22:46:15
nodes: [KSamplerSelect, BasicGuider, ComfyMathExpression, SetNode, GetNode, VAEDecodeAudio, SetNode, MarkdownNote, PathchSageAttentionKJ, MiniMaxH3SigmaShift, RandomNoise, MarkdownNote, CLIPLoader, VAELoader, VAELoader, SamplerCustomAdvanced, UNETLoader, VHS_LoadVideo, SetNode, VAEDecode, VHS_LoadVideo, PrimitiveFloat, MiniMaxH3ReferenceToVideo, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, LoadAudio, LoadAudio, LoadAudio, VHS_LoadVideo, VHS_VideoCombine, LoadImage, PrimitiveFloat, PrimitiveStringMultiline, LoadImage, LoadImage, LoadImage, BasicScheduler, MarkdownNote, ResolutionSelector, LoraLoaderModelOnly]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax+H3+新ref V1.0 Lora 阿里8步版本-多参考工作流_2096537181975310338.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax+H3+新ref V1.0 Lora 阿里8步版本-多参考工作流_2096537181975310338.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（46 个）：
- `KSamplerSelect` ★核心
- `BasicGuider`
- `ComfyMathExpression`
- `SetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `SetNode`
- `MarkdownNote`
- `PathchSageAttentionKJ`
- `MiniMaxH3SigmaShift`
- `RandomNoise`
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `UNETLoader` ★核心
- `VHS_LoadVideo`
- `SetNode`
- `VAEDecode` ★核心
- `VHS_LoadVideo`
- `PrimitiveFloat`
- `MiniMaxH3ReferenceToVideo`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `VHS_LoadVideo`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `LoadImage`
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `BasicScheduler`
- `MarkdownNote`
- `ResolutionSelector`
- `LoraLoaderModelOnly` ★核心

## 知识

覆盖率 **78%**（36/46）

**有卡**：`KSamplerSelect`、`BasicGuider`、`ComfyMathExpression`、`VAEDecodeAudio`、`PathchSageAttentionKJ`、`MiniMaxH3SigmaShift`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`UNETLoader`、`VHS_LoadVideo`、`VAEDecode`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`LoadAudio`、`VHS_VideoCombine`、`BasicScheduler`、`ResolutionSelector`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
