---
key: 数字人/数字人/LTX2.3音频驱动口播数字人嘴型精准高清生成工具_2100997215920676865.json
name: LTX2.3音频驱动口播数字人嘴型精准高清生成工具_2100997215920676865
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/LTX2.3音频驱动口播数字人嘴型精准高清生成工具_2100997215920676865.json
hash: dad1fc20827e139a
coverage: 0.825581
learned_at: 2026-10-19 00:19:10
nodes: [SetNode, LTXVConcatAVLatent, SamplerCustomAdvanced, LTXVConcatAVLatent, SetNode, GetNode, GetNode, KSampler, GetNode, GetNode, GetNode, Reroute, Reroute, SolidMask, SimpleMath+, SimpleMath+, SimpleMath+, SetNode, PreviewAudio, LTXVImgToVideoInplace, INTConstant, INTConstant, EmptyLTXVLatentVideo, BasicScheduler, RandomNoise, INTConstant, KSamplerSelect, LTXVAudioVAELoader, PathchSageAttentionKJ, LatentUpscaleModelLoader, LTXAVTextEncoderLoader, CheckpointLoaderSimple, RH_GetAudioDuration, LTXVAudioVAEEncode, ResizeImagesByLongerEdge, LTXVPreprocess, GetImageSize, CM_FloatToInt, LTX2_NAG, LTX2SamplingPreviewOverride, LTXVCropGuides, LTXVConditioning, CFGGuider, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVSeparateAVLatent, SetLatentNoiseMask, VAEDecodeTiled, easy showAnything, LoadImage, LoadAudio, CLIPTextEncode, CLIPTextEncode, easy cleanGpuUsed, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "ltx-2.3-22b-distilled-1.1-42.9G.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/LTX2.3音频驱动口播数字人嘴型精准高清生成工具_2100997215920676865.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/LTX2.3音频驱动口播数字人嘴型精准高清生成工具_2100997215920676865.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（86 个）：
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
- `checkpoint` = `ltx-2.3-22b-distilled-1.1-42.9G.safetensors`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（71/86）

**有卡**：`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`KSampler`、`SolidMask`、`SimpleMath+`、`PreviewAudio`、`LTXVImgToVideoInplace`、`INTConstant`、`EmptyLTXVLatentVideo`、`BasicScheduler`、`RandomNoise`、`KSamplerSelect`、`LTXVAudioVAELoader`、`PathchSageAttentionKJ`、`LatentUpscaleModelLoader`、`LTXAVTextEncoderLoader`、`CheckpointLoaderSimple`、`RH_GetAudioDuration`、`LTXVAudioVAEEncode`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`GetImageSize`、`CM_FloatToInt`、`LTX2_NAG`、`LTX2SamplingPreviewOverride`、`LTXVCropGuides`、`LTXVConditioning`、`CFGGuider`、`LTXVLatentUpsampler`、`LTXVSeparateAVLatent`、`SetLatentNoiseMask`、`VAEDecodeTiled`、`LoadImage`、`LoadAudio`、`CLIPTextEncode`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`UNETLoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
