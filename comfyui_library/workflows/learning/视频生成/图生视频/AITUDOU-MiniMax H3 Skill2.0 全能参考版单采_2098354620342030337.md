---
key: 视频生成/图生视频/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2098354620342030337.json
name: AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2098354620342030337
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2098354620342030337.json
hash: 36250b4fcdeab5f6
coverage: 0.430108
learned_at: 2026-10-17 01:44:20
nodes: [SetNode, VAELoader, SetNode, VAELoader, SetNode, SetNode, GetNode, GetNode, GetNode, VAEDecodeAudio, VAEDecode, KSamplerSelect, MarkdownNote, SetNode, ComfyMathExpression, SetNode, CLIPLoader, Label (rgthree), SetNode, SetNode, LoadImage, LoadImage, SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, LoraLoaderModelOnly, SetNode, SamplerCustomAdvanced, RandomNoise, BasicGuider, GetNode, SetNode, GetNode, SetNode, SplitSigmas, MiniMaxH3MemoryEfficientSageAttentionPatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Label (rgthree), SetNode, MiniMaxH3ReferenceToVideo, AudioSeparation, AudioSeparation, SetNode, AudioSeparation, LoadAudio, SetNode, GetNode, GetNode, BasicScheduler, LoraLoaderModelOnly, LoraLoaderModelOnly, SetNode, Label (rgthree), GetNode, GetNode, LoadImage, LoadImage, SetNode, UNETLoader, Fast Groups Bypasser (rgthree), SetNode, GetNode, GetNode, LoadImage, LoadImage, LoadImage, LoadAudio, LoadImage, LoadImage, VHS_VideoCombine, ResolutionSelector, LoadAudio, Float, Text]
patterns: []
missing: []
---

# 视频生成/图生视频/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2098354620342030337.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/AITUDOU-MiniMax H3 Skill2.0 全能参考版单采_2098354620342030337.json`

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
- `MiniMaxH3ReferenceToVideo`
- `AudioSeparation`
- `AudioSeparation`
- `SetNode`
- `AudioSeparation`
- `LoadAudio`
- `SetNode`
- `GetNode`
- `GetNode`
- `BasicScheduler`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `SetNode`
- `Label (rgthree)`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `UNETLoader` ★核心
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `ResolutionSelector`
- `LoadAudio`
- `Float`
- `Text`

## 知识

覆盖率 **43%**（40/93）

**有卡**：`VAELoader`、`VAEDecodeAudio`、`VAEDecode`、`KSamplerSelect`、`ComfyMathExpression`、`CLIPLoader`、`Label (rgthree)`、`LoadImage`、`LoraLoaderModelOnly`、`SamplerCustomAdvanced`、`RandomNoise`、`BasicGuider`、`SplitSigmas`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`MiniMaxH3ReferenceToVideo`、`AudioSeparation`、`LoadAudio`、`BasicScheduler`、`UNETLoader`、`VHS_VideoCombine`、`ResolutionSelector`、`Float`、`Text`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
