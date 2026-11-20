---
key: 平台全量/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2099072668573196290.json
name: AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2099072668573196290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2099072668573196290.json
hash: 2d315aa7626b29cf
coverage: 0.430108
learned_at: 2026-11-14 00:15:13
nodes: [SetNode, VAELoader, SetNode, VAELoader, SetNode, SetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, KSamplerSelect, MarkdownNote, SetNode, ComfyMathExpression, SetNode, CLIPLoader, Label (rgthree), SetNode, SetNode, LoadImage, LoadImage, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, LoraLoaderModelOnly, SetNode, SamplerCustomAdvanced, RandomNoise, BasicGuider, GetNode, SetNode, GetNode, SetNode, SplitSigmas, MiniMaxH3MemoryEfficientSageAttentionPatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Label (rgthree), SetNode, AudioSeparation, AudioSeparation, SetNode, AudioSeparation, LoadAudio, SetNode, GetNode, BasicScheduler, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, Label (rgthree), LoadImage, LoadImage, SetNode, UNETLoader, Fast Groups Bypasser (rgthree), SetNode, LoadImage, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage, Float, ResolutionSelector, LoadAudio, GetNode, Text, LoadAudio, GetNode, MiniMaxH3ReferenceToVideo, GetNode, GetNode, GetNode]
patterns: []
missing: []
---

# 平台全量/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2099072668573196290.json

> 来源文件 `comfyui_library/workflows/平台全量/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2099072668573196290.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Other

**节点**（93 个）：
- `SetNode`
- `VAELoader`
- `SetNode`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `KSamplerSelect` ★核心
- `MarkdownNote`
- `SetNode`
- `ComfyMathExpression`
- `SetNode`
- `CLIPLoader`
- `Label (rgthree)`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
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
- `SetNode`
- `SetNode`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `BasicGuider`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SplitSigmas`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
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
- `Label (rgthree)`
- `SetNode`
- `AudioSeparation`
- `AudioSeparation`
- `SetNode`
- `AudioSeparation`
- `LoadAudio`
- `SetNode`
- `GetNode`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `Label (rgthree)`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `LoadImage`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Float`
- `ResolutionSelector`
- `LoadAudio`
- `GetNode`
- `Text`
- `LoadAudio`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `GetNode`
- `GetNode`
- `GetNode`

## 知识

覆盖率 **43%**（40/93）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`ComfyMathExpression`、`CLIPLoader`、`Label (rgthree)`、`LoadImage`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`RandomNoise`、`BasicGuider`、`SplitSigmas`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`AudioSeparation`、`LoadAudio`、`BasicScheduler`、`UNETLoader`、`VHS_VideoCombine`、`Float`、`ResolutionSelector`、`Text`、`MiniMaxH3ReferenceToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
