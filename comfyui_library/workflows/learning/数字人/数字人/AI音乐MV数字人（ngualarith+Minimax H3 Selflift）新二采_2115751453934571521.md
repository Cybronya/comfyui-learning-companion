---
key: 数字人/数字人/AI音乐MV数字人（ngualarith+Minimax H3 Selflift）新二采_2115751453934571521.json
name: AI音乐MV数字人（ngualarith+Minimax H3 Selflift）新二采_2115751453934571521
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/AI音乐MV数字人（ngualarith+Minimax H3 Selflift）新二采_2115751453934571521.json
hash: 5b0c852f3432df32
coverage: 0.939394
learned_at: 2026-10-30 17:56:29
nodes: [ModelAttentionBackend, MiniMaxLowVRAMAttention, LTXVSeparateAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, BasicScheduler, SolidMask, KSamplerSelect, LTXVConcatAVLatent, UNETLoader, CLIPLoader, VAELoader, VAELoader, ConditioningZeroOut, MiniMaxChunkFeedForward, Reroute, LoraLoaderModelOnly, LoadImage, ResolutionSelector, MiniMaxH3ReferenceToVideo, SoundFlow_GetLength, ComfyNumberConvert, ComfyMathExpression, PreviewAny, SelfLiftAvatarH3Sampler, LoadAudio, TrimAudioDuration, VAEDecode, Text Multiline, LTXVSeparateAVLatent, VHS_VideoCombine, LoadImage, LoadImage]
patterns: []
missing: []
---

# 数字人/数字人/AI音乐MV数字人（ngualarith+Minimax H3 Selflift）新二采_2115751453934571521.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/AI音乐MV数字人（ngualarith+Minimax H3 Selflift）新二采_2115751453934571521.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Other

**节点**（33 个）：
- `ModelAttentionBackend`
- `MiniMaxLowVRAMAttention`
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `BasicScheduler`
- `SolidMask`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `ConditioningZeroOut`
- `MiniMaxChunkFeedForward`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `ResolutionSelector`
- `MiniMaxH3ReferenceToVideo`
- `SoundFlow_GetLength`
- `ComfyNumberConvert`
- `ComfyMathExpression`
- `PreviewAny`
- `SelfLiftAvatarH3Sampler` ★核心
- `LoadAudio`
- `TrimAudioDuration`
- `VAEDecode` ★核心
- `Text Multiline`
- `LTXVSeparateAVLatent`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **94%**（31/33）

**有卡**：`ModelAttentionBackend`、`MiniMaxLowVRAMAttention`、`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`BasicScheduler`、`SolidMask`、`KSamplerSelect`、`LTXVConcatAVLatent`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`MiniMaxChunkFeedForward`、`LoraLoaderModelOnly`、`LoadImage`、`ResolutionSelector`、`MiniMaxH3ReferenceToVideo`、`SoundFlow_GetLength`、`ComfyNumberConvert`、`ComfyMathExpression`、`SelfLiftAvatarH3Sampler`、`LoadAudio`、`TrimAudioDuration`、`VAEDecode`、`Text Multiline`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
