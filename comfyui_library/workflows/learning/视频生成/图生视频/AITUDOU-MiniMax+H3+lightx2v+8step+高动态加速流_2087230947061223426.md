---
key: 视频生成/图生视频/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2087230947061223426.json
name: AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2087230947061223426
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2087230947061223426.json
hash: f57a55f378fff0a7
coverage: 0.472727
learned_at: 2026-10-16 21:27:26
nodes: [BasicGuider, RandomNoise, CLIPLoader, SetNode, VAELoader, SetNode, VAELoader, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, SamplerCustomAdvanced, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, SigmasGraph, Label (rgthree), KSamplerSelect, MarkdownNote, GetNode, GetNode, GetNode, GetNode, ResolutionSelector, BasicScheduler, GetNode, SetNode, SetNode, MiniMaxH3MemoryEfficientSageAttentionPatch, SetNode, SetNode, GetNode, ComfyMathExpression, SetNode, SetNode, SetNode, GetNode, GetNode, Label (rgthree), UNETLoader, SetNode, MiniMaxH3ReferenceToVideo, LoraLoaderModelOnly, VHS_VideoCombine, LoadImage, Text, Float, LoraLoaderModelOnly, Label (rgthree), LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2087230947061223426.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/AITUDOU-MiniMax+H3+lightx2v+8step+高动态加速流_2087230947061223426.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（55 个）：
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
- `Label (rgthree)`
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
- `Label (rgthree)`
- `UNETLoader` ★核心
- `SetNode`
- `MiniMaxH3ReferenceToVideo`
- `LoraLoaderModelOnly` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `Text`
- `Float`
- `LoraLoaderModelOnly` ★核心
- `Label (rgthree)`
- `LoadImage`

## 知识

覆盖率 **47%**（26/55）

**有卡**：`BasicGuider`、`RandomNoise`、`CLIPLoader`、`VAELoader`、`SamplerCustomAdvanced`、`VAEDecodeAudio`、`VAEDecode`、`SigmasGraph`、`Label (rgthree)`、`KSamplerSelect`、`ResolutionSelector`、`BasicScheduler`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ComfyMathExpression`、`UNETLoader`、`MiniMaxH3ReferenceToVideo`、`LoraLoaderModelOnly`、`VHS_VideoCombine`、`LoadImage`、`Text`、`Float`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
