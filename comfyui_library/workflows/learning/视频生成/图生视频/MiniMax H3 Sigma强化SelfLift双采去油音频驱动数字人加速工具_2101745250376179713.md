---
key: 视频生成/图生视频/MiniMax H3 Sigma强化SelfLift双采去油音频驱动数字人加速工具_2101745250376179713.json
name: MiniMax H3 Sigma强化SelfLift双采去油音频驱动数字人加速工具_2101745250376179713
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Sigma强化SelfLift双采去油音频驱动数字人加速工具_2101745250376179713.json
hash: 6b8f5faa876338a4
coverage: 0.603448
learned_at: 2026-10-17 02:14:16
nodes: [MiniMaxChunkFeedForward, LTXVConcatAVLatent, LTXVSeparateAVLatent, ConditioningZeroOut, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelAttentionBackend, SetNode, GetNode, SetNode, CLIPLoader, SetNode, GetNode, VAELoader, GetNode, SetNode, MiniMaxLowVRAMAttention, GetNode, UNETLoader, VAELoader, SetLatentNoiseMask, SetNode, SetNode, ModelPreviewOverrideKJ, GetNode, GetNode, easy showAnything, SolidMask, ComfyMathExpression, ComfyNumberConvert, GetNode, GetNode, SoundFlow_GetLength, GetNode, LTXVSeparateAVLatent, VAEDecode, ComfyMathExpression, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SetNode, SetNode, LoadImage, GetNode, SetNode, LoadImage, LoadImage, SetNode, KSamplerSelect, BasicScheduler, H3SigmaRefiner, LoadImage, GetNode, GetNode, GetNode, GetNode, GetNode, Text Concatenate, GetNode, SetNode, GetNode, GetNode, LTXVAudioVAEEncode, GetNode, SetNode, GetNode, SelfLiftAvatarH3Sampler, SetNode, JjkText, SetNode, GetNode, easy cleanGpuUsed, MiniMaxH3ReferenceToVideo, GetImageRangeFromBatch, LayerUtility: PurgeVRAM V2, LoadAudio, ResolutionSelector, GetNode, easy seed, VHS_VideoCombine, JjkText, JjkText, AudioCrop, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/MiniMax H3 Sigma强化SelfLift双采去油音频驱动数字人加速工具_2101745250376179713.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/MiniMax H3 Sigma强化SelfLift双采去油音频驱动数字人加速工具_2101745250376179713.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（116 个）：
- `MiniMaxChunkFeedForward`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `ConditioningZeroOut`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelAttentionBackend`
- `SetNode`
- `GetNode`
- `SetNode`
- `CLIPLoader`
- `SetNode`
- `GetNode`
- `VAELoader`
- `GetNode`
- `SetNode`
- `MiniMaxLowVRAMAttention`
- `GetNode`
- `UNETLoader` ★核心
- `VAELoader`
- `SetLatentNoiseMask`
- `SetNode`
- `SetNode`
- `ModelPreviewOverrideKJ`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `SolidMask`
- `ComfyMathExpression`
- `ComfyNumberConvert`
- `GetNode`
- `GetNode`
- `SoundFlow_GetLength`
- `GetNode`
- `LTXVSeparateAVLatent`
- `VAEDecode` ★核心
- `ComfyMathExpression`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `GetNode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `H3SigmaRefiner`
- `LoadImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Text Concatenate`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `LTXVAudioVAEEncode` ★核心
- `GetNode`
- `SetNode`
- `GetNode`
- `SelfLiftAvatarH3Sampler` ★核心
- `SetNode`
- `JjkText`
- `SetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `MiniMaxH3ReferenceToVideo`
- `GetImageRangeFromBatch`
- `LayerUtility: PurgeVRAM V2`
- `LoadAudio`
- `ResolutionSelector`
- `GetNode`
- `easy seed`
- `VHS_VideoCombine`
- `JjkText`
- `JjkText`
- `AudioCrop`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **60%**（70/116）

**有卡**：`MiniMaxChunkFeedForward`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`ConditioningZeroOut`、`LoraLoaderModelOnly`、`ModelAttentionBackend`、`CLIPLoader`、`VAELoader`、`MiniMaxLowVRAMAttention`、`UNETLoader`、`SetLatentNoiseMask`、`ModelPreviewOverrideKJ`、`SolidMask`、`ComfyMathExpression`、`ComfyNumberConvert`、`SoundFlow_GetLength`、`VAEDecode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`KSamplerSelect`、`BasicScheduler`、`H3SigmaRefiner`、`Text Concatenate`、`LTXVAudioVAEEncode`、`SelfLiftAvatarH3Sampler`、`easy cleanGpuUsed`、`MiniMaxH3ReferenceToVideo`、`GetImageRangeFromBatch`、`LayerUtility: PurgeVRAM V2`、`LoadAudio`、`ResolutionSelector`、`easy seed`、`VHS_VideoCombine`、`AudioCrop`、`KSampler`、`EmptyLatentImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
