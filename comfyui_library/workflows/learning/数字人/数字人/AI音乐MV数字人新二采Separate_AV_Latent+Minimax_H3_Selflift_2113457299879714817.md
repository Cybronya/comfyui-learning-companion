---
key: 数字人/数字人/AI音乐MV数字人新二采Separate_AV_Latent+Minimax_H3_Selflift_2113457299879714817.json
name: AI音乐MV数字人新二采Separate_AV_Latent+Minimax_H3_Selflift_2113457299879714817
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/AI音乐MV数字人新二采Separate_AV_Latent+Minimax_H3_Selflift_2113457299879714817.json
hash: a8e0e9453836e38a
coverage: 0.869565
learned_at: 2026-10-26 22:10:10
nodes: [MiniMaxChunkFeedForward, CLIPLoader, VAELoader, VAELoader, Reroute, SoundFlow_GetLength, ComfyMathExpression, ComfyNumberConvert, LTXVSeparateAVLatent, SolidMask, SetLatentNoiseMask, LTXVConcatAVLatent, LoadImage, TrimAudioDuration, LoadAudio, PrimitiveFloat, PrimitiveFloat, ResolutionSelector, LoadImage, Textbox, VHS_VideoCombine, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, MiniMaxH3ReferenceToVideo, ModelAttentionBackend, LTXVAudioVAEEncode, UNETLoader, LoraLoaderModelOnly, SelfLiftAvatarH3Sampler, MiniMaxLowVRAMAttention, Note, LoraLoaderModelOnly, LoraLoaderModelOnly, KSamplerSelect, LTXVSeparateAVLatent, ConditioningZeroOut, BasicScheduler, PreviewAny, VAEDecode, LoadImage, PreviewImage]
patterns: []
missing: []
---

# 数字人/数字人/AI音乐MV数字人新二采Separate_AV_Latent+Minimax_H3_Selflift_2113457299879714817.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/AI音乐MV数字人新二采Separate_AV_Latent+Minimax_H3_Selflift_2113457299879714817.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Output → Other

**节点**（46 个）：
- `MiniMaxChunkFeedForward`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `Reroute`
- `SoundFlow_GetLength`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `LTXVSeparateAVLatent`
- `SolidMask`
- `SetLatentNoiseMask`
- `LTXVConcatAVLatent`
- `LoadImage`
- `TrimAudioDuration`
- `LoadAudio`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `ResolutionSelector`
- `LoadImage`
- `Textbox`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `MiniMaxH3ReferenceToVideo`
- `ModelAttentionBackend`
- `LTXVAudioVAEEncode` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SelfLiftAvatarH3Sampler` ★核心
- `MiniMaxLowVRAMAttention`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSamplerSelect` ★核心
- `LTXVSeparateAVLatent`
- `ConditioningZeroOut`
- `BasicScheduler`
- `PreviewAny`
- `VAEDecode` ★核心
- `LoadImage`
- `PreviewImage`

## 知识

覆盖率 **87%**（40/46）

**有卡**：`MiniMaxChunkFeedForward`、`CLIPLoader`、`VAELoader`、`SoundFlow_GetLength`、`ComfyMathExpression`、`ComfyNumberConvert`、`LTXVSeparateAVLatent`、`SolidMask`、`SetLatentNoiseMask`、`LTXVConcatAVLatent`、`LoadImage`、`TrimAudioDuration`、`LoadAudio`、`ResolutionSelector`、`Textbox`、`VHS_VideoCombine`、`MiniMaxH3ReferenceToVideo`、`ModelAttentionBackend`、`LTXVAudioVAEEncode`、`UNETLoader`、`LoraLoaderModelOnly`、`SelfLiftAvatarH3Sampler`、`MiniMaxLowVRAMAttention`、`KSamplerSelect`、`ConditioningZeroOut`、`BasicScheduler`、`VAEDecode`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、ConditioningZeroOut、ResolutionSelector、LoadImage、UNETLoader
