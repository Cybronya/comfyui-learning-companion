---
key: 视频生成/文生视频/MiniMax+H3+refV1.2Lora-多参考工作流（全接口开放内部开发版）_2096531122523033602.json
name: MiniMax+H3+refV1.2Lora-多参考工作流（全接口开放内部开发版）_2096531122523033602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/MiniMax+H3+refV1.2Lora-多参考工作流（全接口开放内部开发版）_2096531122523033602.json
hash: b27c59ab0791f77c
coverage: 0.782609
learned_at: 2026-10-11 21:41:46
nodes: [MarkdownNote, KSamplerSelect, BasicGuider, ComfyMathExpression, SetNode, GetNode, VAEDecodeAudio, SetNode, MarkdownNote, PathchSageAttentionKJ, MiniMaxH3SigmaShift, RandomNoise, MarkdownNote, CLIPLoader, VAELoader, VAELoader, SamplerCustomAdvanced, UNETLoader, VHS_LoadVideo, SetNode, VAEDecode, BasicScheduler, VHS_LoadVideo, ResolutionSelector, PrimitiveFloat, MiniMaxH3ReferenceToVideo, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, VHS_LoadVideo, VHS_LoadVideo, VHS_LoadVideo, LoadAudio, LoadAudio, LoadAudio, VHS_LoadVideo, VHS_VideoCombine, LoadImage, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, PrimitiveStringMultiline, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/文生视频/MiniMax+H3+refV1.2Lora-多参考工作流（全接口开放内部开发版）_2096531122523033602.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/MiniMax+H3+refV1.2Lora-多参考工作流（全接口开放内部开发版）_2096531122523033602.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（46 个）：
- `MarkdownNote`
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
- `BasicScheduler`
- `VHS_LoadVideo`
- `ResolutionSelector`
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
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `PrimitiveFloat`
- `PrimitiveStringMultiline`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`KSamplerSelect`、`BasicGuider`、`ComfyMathExpression`、`VAEDecodeAudio`、`PathchSageAttentionKJ`、`MiniMaxH3SigmaShift`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`UNETLoader`、`VHS_LoadVideo`、`VAEDecode`、`BasicScheduler`、`ResolutionSelector`、`MiniMaxH3ReferenceToVideo`、`LoadImage`、`LoadAudio`、`VHS_VideoCombine`、`LoraLoaderModelOnly`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
