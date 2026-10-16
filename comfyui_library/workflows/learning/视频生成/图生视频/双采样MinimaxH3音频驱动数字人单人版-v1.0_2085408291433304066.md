---
key: 视频生成/图生视频/双采样MinimaxH3音频驱动数字人单人版-v1.0_2085408291433304066.json
name: 双采样MinimaxH3音频驱动数字人单人版-v1.0_2085408291433304066
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/双采样MinimaxH3音频驱动数字人单人版-v1.0_2085408291433304066.json
hash: ec287e8eb6f1e570
coverage: 0.630137
learned_at: 2026-10-16 20:50:53
nodes: [KSamplerSelect, CLIPLoader, Note, BasicGuider, VAEEncode, VAEEncodeAudio, SamplerCustomAdvanced, easy clearCacheAll, SetNode, SetNode, SetNode, VAELoader, VAELoader, SetNode, SetNode, GetNode, GetNode, GetNode, RandomNoise, ExtendIntermediateSigmas, SamplerCustomAdvanced, VHS_VideoCombine, VAEDecode, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, VAEDecode, INTConstant, UNETLoader, UNETLoader, MiniMaxH3MemoryEfficientSageAttentionPatch, ModelAttentionBackend, LoraLoaderBypassModelOnly, MiniMaxH3ReferenceToVideo, VRGDG_MiniMaxH3AudioDrive, H3SigmaRefiner, ExtendIntermediateSigmas, SetNode, Reroute, Reroute, H3SigmaRefiner, UNETLoader, LoraLoaderBypassModelOnly, BasicGuider, KSamplerSelect, BasicScheduler, PT_H3ConcatAVLatent, GetNode, ImageResizeKJv2, GetNode, GetNode, PrimitiveFloat, ComfyMathExpression, SoundFlow_GetLength, SetNode, INTConstant, BasicScheduler, GetNode, ResolutionSelector, Reroute, Reroute, MarkdownNote, ResolutionSelector, LoadAudio, AudioCrop, PreviewAudio, MarkdownNote, PrimitiveStringMultiline, LoadImage, VHS_VideoCombine, 孤海注释, 孤海注释, 孤海注释, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/双采样MinimaxH3音频驱动数字人单人版-v1.0_2085408291433304066.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/双采样MinimaxH3音频驱动数字人单人版-v1.0_2085408291433304066.json`

## 结构

**生成流程**：Model → Encode → Latent → Sampling → Decode → Process → Other

**节点**（73 个）：
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `Note`
- `BasicGuider`
- `VAEEncode` ★核心
- `VAEEncodeAudio` ★核心
- `SamplerCustomAdvanced` ★核心
- `easy clearCacheAll`
- `SetNode`
- `SetNode`
- `SetNode`
- `VAELoader`
- `VAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `ExtendIntermediateSigmas`
- `SamplerCustomAdvanced` ★核心
- `VHS_VideoCombine`
- `VAEDecode` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `VAEDecode` ★核心
- `INTConstant`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `ModelAttentionBackend`
- `LoraLoaderBypassModelOnly` ★核心
- `MiniMaxH3ReferenceToVideo`
- `VRGDG_MiniMaxH3AudioDrive`
- `H3SigmaRefiner`
- `ExtendIntermediateSigmas`
- `SetNode`
- `Reroute`
- `Reroute`
- `H3SigmaRefiner`
- `UNETLoader` ★核心
- `LoraLoaderBypassModelOnly` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `PT_H3ConcatAVLatent`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `PrimitiveFloat`
- `ComfyMathExpression`
- `SoundFlow_GetLength`
- `SetNode`
- `INTConstant`
- `BasicScheduler`
- `GetNode`
- `ResolutionSelector`
- `Reroute`
- `Reroute`
- `MarkdownNote`
- `ResolutionSelector`
- `LoadAudio`
- `AudioCrop`
- `PreviewAudio`
- `MarkdownNote`
- `PrimitiveStringMultiline`
- `LoadImage`
- `VHS_VideoCombine`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `Note`

## 知识

覆盖率 **63%**（46/73）

**有卡**：`KSamplerSelect`、`CLIPLoader`、`BasicGuider`、`VAEEncode`、`VAEEncodeAudio`、`SamplerCustomAdvanced`、`easy clearCacheAll`、`VAELoader`、`RandomNoise`、`ExtendIntermediateSigmas`、`VHS_VideoCombine`、`VAEDecode`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`ModelAttentionBackend`、`INTConstant`、`UNETLoader`、`LoraLoaderBypassModelOnly`、`MiniMaxH3ReferenceToVideo`、`VRGDG_MiniMaxH3AudioDrive`、`H3SigmaRefiner`、`BasicScheduler`、`PT_H3ConcatAVLatent`、`ImageResizeKJv2`、`ComfyMathExpression`、`SoundFlow_GetLength`、`ResolutionSelector`、`LoadAudio`、`AudioCrop`、`PreviewAudio`、`LoadImage`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
