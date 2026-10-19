---
key: 数字人/数字人/口播数字人｜LTX2.3 音频驱动 嘴型精准 高清输出_2089343112496898050.json
name: 口播数字人｜LTX2.3 音频驱动 嘴型精准 高清输出_2089343112496898050
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/口播数字人｜LTX2.3 音频驱动 嘴型精准 高清输出_2089343112496898050.json
hash: edceff340f44894d
coverage: 0.823529
learned_at: 2026-10-18 19:07:50
nodes: [SetNode, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVConcatAVLatent, SetNode, GetNode, GetNode, KSampler, GetNode, GetNode, GetNode, Reroute, Reroute, SolidMask, SimpleMath+, SimpleMath+, SimpleMath+, SetNode, PreviewAudio, LTXVImgToVideoInplace, INTConstant, INTConstant, EmptyLTXVLatentVideo, BasicScheduler, RandomNoise, INTConstant, KSamplerSelect, LTXVAudioVAELoader, PathchSageAttentionKJ, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, CheckpointLoaderSimple, RH_GetAudioDuration, LTXVAudioVAEEncode, ResizeImagesByLongerEdge, LTXVPreprocess, GetImageSize, CM_FloatToInt, LTX2_NAG, LTX2SamplingPreviewOverride, LTXVCropGuides, LTXVConditioning, CFGGuider, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVSeparateAVLatent, SetLatentNoiseMask, VAEDecodeTiled, easy showAnything, LoadImage, LoadAudio, CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, VHS_VideoCombine, 孤海注释, 孤海注释, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, KSampler, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, VAELoader, CLIPLoader, EmptyLatentImage, JjkText, CLIPTextEncode, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "ltx-2.3-22b-distilled-1.1-42.9G.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/口播数字人｜LTX2.3 音频驱动 嘴型精准 高清输出_2089343112496898050.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/口播数字人｜LTX2.3 音频驱动 嘴型精准 高清输出_2089343112496898050.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（85 个）：
- `SetNode`
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `LTXVConcatAVLatent`
- `SetNode`
- `GetNode`
- `GetNode`
- `KSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `SolidMask`
- `SimpleMath+`
- `SimpleMath+`
- `SimpleMath+`
- `SetNode`
- `PreviewAudio`
- `LTXVImgToVideoInplace`
- `INTConstant`
- `INTConstant`
- `EmptyLTXVLatentVideo`
- `BasicScheduler`
- `RandomNoise`
- `INTConstant`
- `KSamplerSelect` ★核心
- `LTXVAudioVAELoader`
- `PathchSageAttentionKJ`
- `LatentUpscaleModelLoader`
- `LTXAVTextEncoderLoader`
- `CheckpointLoaderSimple` ★核心
- `RH_GetAudioDuration`
- `LTXVAudioVAEEncode` ★核心
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `GetImageSize`
- `CM_FloatToInt`
- `LTX2_NAG`
- `LTX2SamplingPreviewOverride`
- `LTXVCropGuides`
- `LTXVConditioning`
- `CFGGuider`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVSeparateAVLatent`
- `SetLatentNoiseMask`
- `VAEDecodeTiled` ★核心
- `easy showAnything`
- `LoadImage`
- `LoadAudio`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `孤海注释`
- `孤海注释`
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
- `UNETLoader` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `ltx-2.3-22b-distilled-1.1-42.9G.safetensors`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **82%**（70/85）

**有卡**：`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`KSampler`、`SolidMask`、`SimpleMath+`、`PreviewAudio`、`LTXVImgToVideoInplace`、`INTConstant`、`EmptyLTXVLatentVideo`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`LTXVAudioVAELoader`、`PathchSageAttentionKJ`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`RH_GetAudioDuration`、`LTXVAudioVAEEncode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`GetImageSize`、`CM_FloatToInt`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXVCropGuides`、`LTXVConditioning`、`CFGGuider`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`VAEDecodeTiled`、`LoadImage`、`LoadAudio`、`CLIPTextEncode`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`UNETLoader`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`、`CLIPLoader`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
