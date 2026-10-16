---
key: 视频生成/图生视频/MiniMax+H3-9.2_2095010503541215234.json
name: MiniMax+H3-9.2_2095010503541215234
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax+H3-9.2_2095010503541215234.json
hash: 078884e9c6c60989
coverage: 0.97619
learned_at: 2026-10-17 00:02:27
nodes: [BasicGuider, VAEDecode, VAELoader, VAELoader, SamplerCustomAdvanced, KSamplerSelect, VAEDecodeAudio, CreateVideo, MiniMaxH3MemoryEfficientSageAttentionPatch, SplitSigmasDenoise, DisableNoise, BasicGuider, SamplerCustomAdvanced, SaveVideo, ComfyMathExpression, RandomNoise, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, BasicScheduler, ExtendIntermediateSigmas, LoraLoaderModelOnly, UNETLoader, CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadAudio, LoadAudio, LoadAudio, easy cleanGpuUsed, LoadImage, LoadImage, LoadImage, LoadImage, PrimitiveFloat, ResolutionSelector, MiniMaxH3ReferenceToVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/MiniMax+H3-9.2_2095010503541215234.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax+H3-9.2_2095010503541215234.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Output → Other

**节点**（42 个）：
- `BasicGuider`
- `VAEDecode` ★核心
- `VAELoader`
- `VAELoader`
- `SamplerCustomAdvanced` ★核心
- `KSamplerSelect` ★核心
- `VAEDecodeAudio` ★核心
- `CreateVideo`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SplitSigmasDenoise`
- `DisableNoise`
- `BasicGuider`
- `SamplerCustomAdvanced` ★核心
- `SaveVideo`
- `ComfyMathExpression`
- `RandomNoise`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `BasicScheduler`
- `ExtendIntermediateSigmas`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `easy cleanGpuUsed`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `PrimitiveFloat`
- `ResolutionSelector`
- `MiniMaxH3ReferenceToVideo`

## 知识

覆盖率 **98%**（41/42）

**有卡**：`BasicGuider`、`VAEDecode`、`VAELoader`、`SamplerCustomAdvanced`、`KSamplerSelect`、`VAEDecodeAudio`、`CreateVideo`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`SplitSigmasDenoise`、`DisableNoise`、`SaveVideo`、`ComfyMathExpression`、`RandomNoise`、`LoraLoaderModelOnly`、`BasicScheduler`、`ExtendIntermediateSigmas`、`UNETLoader`、`CLIPLoader`、`LoadImage`、`LoadAudio`、`easy cleanGpuUsed`、`ResolutionSelector`、`MiniMaxH3ReferenceToVideo`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect
