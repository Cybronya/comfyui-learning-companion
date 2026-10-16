---
key: 视频生成/图生视频/MiniMax+H3-8.24_2091826993972203521.json
name: MiniMax+H3-8.24_2091826993972203521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax+H3-8.24_2091826993972203521.json
hash: dfa0abd2dd4ee425
coverage: 0.426667
learned_at: 2026-10-16 22:30:38
nodes: [BasicGuider, RandomNoise, CLIPLoader, SetNode, VAELoader, SetNode, VAELoader, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, SigmasGraph, KSamplerSelect, MarkdownNote, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, ComfyMathExpression, SetNode, SetNode, GetNode, UNETLoader, VHS_VideoCombine, SetNode, SetNode, SetNode, GetNode, Float, BasicScheduler, MiniMaxH3MemoryEfficientSageAttentionPatch, LoraLoaderModelOnly, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, MiniMaxH3ReferenceToVideo, LoadAudio, LoadAudio, LoadAudio, ResolutionSelector, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Text, LoadImage, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax+H3-8.24_2091826993972203521.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax+H3-8.24_2091826993972203521.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（75 个）：
- `BasicGuider`
- `RandomNoise`
- `CLIPLoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `SigmasGraph`
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `GetNode`
- `UNETLoader` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `Float`
- `BasicScheduler`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
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
- `MiniMaxH3ReferenceToVideo`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Text`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **43%**（32/75）

**有卡**：`BasicGuider`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`VAEDecode`、`SigmasGraph`、`KSamplerSelect`、`ComfyMathExpression`、`UNETLoader`、`VHS_VideoCombine`、`Float`、`BasicScheduler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`LoraLoaderModelOnly`、`MiniMaxH3ReferenceToVideo`、`LoadAudio`、`ResolutionSelector`、`LoadImage`、`Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
