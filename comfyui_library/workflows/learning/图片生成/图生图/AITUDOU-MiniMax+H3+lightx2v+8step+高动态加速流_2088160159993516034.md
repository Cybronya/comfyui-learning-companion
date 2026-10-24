---
key: 图片生成/图生图/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2088160159993516034.json
name: AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2088160159993516034
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2088160159993516034.json
hash: cbf5a4e0dded3722
coverage: 0.442308
learned_at: 2026-10-23 10:50:24
nodes: [BasicGuider, RandomNoise, CLIPLoader, SetNode, VAELoader, SetNode, VAELoader, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, SigmasGraph, KSamplerSelect, MarkdownNote, GetNode, GetNode, GetNode, GetNode, ResolutionSelector, BasicScheduler, GetNode, SetNode, SetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, SetNode, GetNode, ComfyMathExpression, SetNode, SetNode, SetNode, GetNode, GetNode, UNETLoader, SetNode, MiniMaxH3ReferenceToVideo, LoraLoaderModelOnly, LoadImage, Float, LoraLoaderModelOnly, Text, LoadImage, VHS_VideoCombine]
patterns: []
missing: []
---

# 图片生成/图生图/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2088160159993516034.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2088160159993516034.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（52 个）：
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
- `ResolutionSelector`
- `BasicScheduler`
- `GetNode`
- `SetNode`
- `SetNode`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SetNode`
- `SetNode`
- `GetNode`
- `ComfyMathExpression`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `UNETLoader` ★核心
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `Float`
- `LoraLoaderModelOnly` ★核心
- `Text`
- `LoadImage`
- `VHS_VideoCombine`

## 知识

覆盖率 **44%**（23/52）

**有卡**：`BasicGuider`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`VAEDecode`、`SigmasGraph`、`KSamplerSelect`、`ResolutionSelector`、`BasicScheduler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ComfyMathExpression`、`UNETLoader`、`MiniMaxH3ReferenceToVideo`、`LoraLoaderModelOnly`、`LoadImage`、`Float`、`Text`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
