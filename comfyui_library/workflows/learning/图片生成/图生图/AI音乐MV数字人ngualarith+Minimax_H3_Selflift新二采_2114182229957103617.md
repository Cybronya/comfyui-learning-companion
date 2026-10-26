---
key: 图片生成/图生图/AI音乐MV数字人ngualarith+Minimax_H3_Selflift新二采_2114182229957103617.json
name: AI音乐MV数字人ngualarith+Minimax_H3_Selflift新二采_2114182229957103617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/AI音乐MV数字人ngualarith+Minimax_H3_Selflift新二采_2114182229957103617.json
hash: 9c3e9c590b7f5994
coverage: 0.909091
learned_at: 2026-10-26 22:01:20
nodes: [ModelAttentionBackend, MiniMaxLowVRAMAttention, LTXVSeparateAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, BasicScheduler, SolidMask, KSamplerSelect, LTXVConcatAVLatent, UNETLoader, CLIPLoader, VAELoader, VAELoader, ConditioningZeroOut, MiniMaxChunkFeedForward, Reroute, LoraLoaderModelOnly, LoadImage, ResolutionSelector, MiniMaxH3ReferenceToVideo, SoundFlow_GetLength, ComfyNumberConvert, ComfyMathExpression, PreviewAny, SelfLiftAvatarH3Sampler, LoadAudio, TrimAudioDuration, VAEDecode, Text Multiline, LTXVSeparateAVLatent, VHS_VideoCombine, LoadImage, PreviewImage]
patterns: []
missing: []
---

# 图片生成/图生图/AI音乐MV数字人ngualarith+Minimax_H3_Selflift新二采_2114182229957103617.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/AI音乐MV数字人ngualarith+Minimax_H3_Selflift新二采_2114182229957103617.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

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
- `PreviewImage`

## 知识

覆盖率 **91%**（30/33）

**有卡**：`ModelAttentionBackend`、`MiniMaxLowVRAMAttention`、`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`BasicScheduler`、`SolidMask`、`KSamplerSelect`、`LTXVConcatAVLatent`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`MiniMaxChunkFeedForward`、`LoraLoaderModelOnly`、`LoadImage`、`ResolutionSelector`、`MiniMaxH3ReferenceToVideo`、`SoundFlow_GetLength`、`ComfyNumberConvert`、`ComfyMathExpression`、`SelfLiftAvatarH3Sampler`、`LoadAudio`、`TrimAudioDuration`、`VAEDecode`、`Text Multiline`、`VHS_VideoCombine`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
