---
key: 视频生成/文生视频/AIGC特异点-Minimax-H3多参考双采放大生成视频（Singularity）_2096091492187205633.json
name: AIGC特异点-Minimax-H3多参考双采放大生成视频（Singularity）_2096091492187205633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AIGC特异点-Minimax-H3多参考双采放大生成视频（Singularity）_2096091492187205633.json
hash: 628d3f1c5bdd7e60
coverage: 0.533333
learned_at: 2026-10-15 22:43:59
nodes: [LoadImage, LoadImage, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_LoadVideo, SetNode, SetNode, SetNode, VHS_LoadVideo, SetNode, LoadImage, LoadImage, SetNode, SetNode, SetNode, VAEDecodeAudio, VAEDecode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, MiniMaxH3ReferenceToVideo, SetNode, LTXVSeparateAVLatent, Note, SetNode, SetNode, SetNode, LoadImage, LoadImage, CLIPLoader, LoadImage, LoadImage, LoadImage, 忽略多组孤海, 忽略多组孤海, MarkdownNote, LoadAudio, LoadAudio, LoadAudio, VHS_LoadVideo, 忽略多组孤海, 忽略多组孤海, Text, SamplerCustomAdvanced, VAELoader, GetNode, RandomNoise, PrimitiveFloat, easy float, ComfyMathExpression, SetNode, MinimaxH3LatentUpscaler3D, SamplerCustomAdvanced, LTXVConcatAVLatent, VAELoader, VAEDecodeAudio, VAEDecode, Lora Loader Stack (rgthree), UNETLoader, ModelAttentionBackend, MiniMaxH3MemoryEfficientSageAttentionPatch, SolAttnMiniMax, GetNode, BasicGuider, KSamplerSelect, SplitSigmas, ResolutionSelector, MarkdownNote, VHS_VideoCombine, VHS_VideoCombine, BasicScheduler]
patterns: []
missing: []
---

# 视频生成/文生视频/AIGC特异点-Minimax-H3多参考双采放大生成视频（Singularity）_2096091492187205633.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AIGC特异点-Minimax-H3多参考双采放大生成视频（Singularity）_2096091492187205633.json`

## 结构

**生成流程**：Model → Latent → Sampling → Decode → Process → Other

**节点**（90 个）：
- `LoadImage`
- `LoadImage`
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
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `SetNode`
- `SetNode`
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
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `MiniMaxH3ReferenceToVideo`
- `SetNode`
- `LTXVSeparateAVLatent`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `忽略多组孤海`
- `忽略多组孤海`
- `MarkdownNote`
- `LoadAudio`
- `LoadAudio`
- `LoadAudio`
- `VHS_LoadVideo`
- `忽略多组孤海`
- `忽略多组孤海`
- `Text`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `GetNode`
- `RandomNoise`
- `PrimitiveFloat`
- `easy float`
- `ComfyMathExpression`
- `SetNode`
- `MinimaxH3LatentUpscaler3D`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `VAELoader`
- `VAEDecodeAudio` ★核心
- `VAEDecode` ★核心
- `Lora Loader Stack (rgthree)`
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `SolAttnMiniMax`
- `GetNode`
- `BasicGuider`
- `KSamplerSelect` ★核心
- `SplitSigmas`
- `ResolutionSelector`
- `MarkdownNote`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `BasicScheduler`

## 知识

覆盖率 **53%**（48/90）

**有卡**：`LoadImage`、`VHS_LoadVideo`、`VAEDecodeAudio`、`VAEDecode`、`MiniMaxH3ReferenceToVideo`、`LTXVSeparateAVLatent`、`CLIPLoader`、`忽略多组孤海`、`LoadAudio`、`Text`、`SamplerCustomAdvanced`、`VAELoader`、`RandomNoise`、`easy float`、`ComfyMathExpression`、`MinimaxH3LatentUpscaler3D`、`LTXVConcatAVLatent`、`Lora Loader Stack (rgthree)`、`UNETLoader`、`ModelAttentionBackend`、`MiniMaxH3MemoryEfficientSageAttentionPatch`、`SolAttnMiniMax`、`BasicGuider`、`KSamplerSelect`、`SplitSigmas`、`ResolutionSelector`、`VHS_VideoCombine`、`BasicScheduler`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、ResolutionSelector、LoadImage、UNETLoader、KSamplerSelect、SamplerCustomAdvanced
