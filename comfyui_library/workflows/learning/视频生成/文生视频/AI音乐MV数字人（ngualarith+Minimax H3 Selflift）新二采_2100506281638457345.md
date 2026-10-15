---
key: 视频生成/文生视频/AI音乐MV数字人（ngualarith+Minimax H3 Selflift）新二采_2100506281638457345.json
name: AI音乐MV数字人（ngualarith+Minimax H3 Selflift）新二采_2100506281638457345
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/AI音乐MV数字人（ngualarith+Minimax H3 Selflift）新二采_2100506281638457345.json
hash: 3da493703028ce80
coverage: 0.935484
learned_at: 2026-10-15 22:44:00
nodes: [ModelAttentionBackend, MiniMaxLowVRAMAttention, LTXVSeparateAVLatent, SetLatentNoiseMask, LTXVAudioVAEEncode, MiniMaxH3ReferenceToVideo, BasicScheduler, SolidMask, KSamplerSelect, MiniMaxChunkFeedForward, LTXVConcatAVLatent, UNETLoader, CLIPLoader, VAELoader, VAELoader, ConditioningZeroOut, LoraLoaderModelOnly, PreviewAny, Reroute, LoadImage, SelfLiftAvatarH3Sampler, ResolutionSelector, Text Multiline, TrimAudioDuration, ComfyNumberConvert, SoundFlow_GetLength, ComfyMathExpression, VHS_VideoCombine, LTXVSeparateAVLatent, VAEDecode, LoadAudio]
patterns: []
missing: []
---

# 视频生成/文生视频/AI音乐MV数字人（ngualarith+Minimax H3 Selflift）新二采_2100506281638457345.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/AI音乐MV数字人（ngualarith+Minimax H3 Selflift）新二采_2100506281638457345.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Other

**节点**（31 个）：
- `ModelAttentionBackend`
- `MiniMaxLowVRAMAttention`
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `LTXVAudioVAEEncode` ★核心
- `MiniMaxH3ReferenceToVideo`
- `BasicScheduler`
- `SolidMask`
- `KSamplerSelect` ★核心
- `MiniMaxChunkFeedForward`
- `LTXVConcatAVLatent`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `PreviewAny`
- `Reroute`
- `LoadImage`
- `SelfLiftAvatarH3Sampler` ★核心
- `ResolutionSelector`
- `Text Multiline`
- `TrimAudioDuration`
- `ComfyNumberConvert`
- `SoundFlow_GetLength`
- `ComfyMathExpression`
- `VHS_VideoCombine`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `LoadAudio`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`ModelAttentionBackend`、`MiniMaxLowVRAMAttention`、`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`LTXVAudioVAEEncode`、`MiniMaxH3ReferenceToVideo`、`BasicScheduler`、`SolidMask`、`KSamplerSelect`、`MiniMaxChunkFeedForward`、`LTXVConcatAVLatent`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`LoadImage`、`SelfLiftAvatarH3Sampler`、`ResolutionSelector`、`Text Multiline`、`TrimAudioDuration`、`ComfyNumberConvert`、`SoundFlow_GetLength`、`ComfyMathExpression`、`VHS_VideoCombine`、`VAEDecode`、`LoadAudio`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
