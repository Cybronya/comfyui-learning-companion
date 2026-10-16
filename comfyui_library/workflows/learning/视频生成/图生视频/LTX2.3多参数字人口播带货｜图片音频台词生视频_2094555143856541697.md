---
key: 视频生成/图生视频/LTX2.3多参数字人口播带货｜图片音频台词生视频_2094555143856541697.json
name: LTX2.3多参数字人口播带货｜图片音频台词生视频_2094555143856541697
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX2.3多参数字人口播带货｜图片音频台词生视频_2094555143856541697.json
hash: e3afc178104c8bf2
coverage: 0.808081
learned_at: 2026-10-17 00:02:14
nodes: [KSamplerSelect, CFGGuider, BasicScheduler, GetNode, GetNode, SimpleMath+, easy showAnything, GetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, RandomNoise, LTX2SamplingPreviewOverride, LTX2_NAG, CLIPTextEncode, LTXVConditioning, PathchSageAttentionKJ, LTXVConcatAVLatent, LTXVSeparateAVLatent, LTXVConcatAVLatent, LatentUpscaleModelLoader, SamplerCustomAdvanced, GetNode, LTXVImgToVideoInplace, LTXVCropGuides, LTXVLatentUpsampler, KSampler, LTXVSeparateAVLatent, GetNode, VAEDecodeTiled, easy cleanGpuUsed, ImageSharpen, SetNode, SetNode, CheckpointLoaderSimple, LTXAVTextEncoderLoader, LTXVAudioVAELoader, SetNode, LTXVImgToVideoInplace, GetNode, INTConstant, INTConstant, INTConstant, SimpleMath+, GetImageSize, INTConstant, Reroute, Reroute, SimpleMath+, CM_FloatToInt, AudioDuration_wan, SolidMask, LTXVAudioVAEEncode, SetLatentNoiseMask, LTXVPreprocess, EmptyLTXVLatentVideo, PrimitiveBoolean, INTConstant, CLIPTextEncode, IndexTTS2Run, PrimitiveStringMultiline, VHS_VideoCombine, AudioPad, SetNode, PreviewAudio, ResizeImageMaskNode, ResizeImagesByLongerEdge, LoadAudio, LoadImage, Int, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX2.3多参数字人口播带货｜图片音频台词生视频_2094555143856541697.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX2.3多参数字人口播带货｜图片音频台词生视频_2094555143856541697.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（99 个）：
- `KSamplerSelect` ★核心
- `CFGGuider`
- `BasicScheduler`
- `GetNode`
- `GetNode`
- `SimpleMath+`
- `easy showAnything`
- `GetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `RandomNoise`
- `LTX2SamplingPreviewOverride`
- `LTX2_NAG`
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `PathchSageAttentionKJ`
- `LTXVConcatAVLatent`
- `LTXVSeparateAVLatent`
- `LTXVConcatAVLatent`
- `LatentUpscaleModelLoader`
- `SamplerCustomAdvanced` ★核心
- `GetNode`
- `LTXVImgToVideoInplace`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `GetNode`
- `VAEDecodeTiled` ★核心
- `easy cleanGpuUsed`
- `ImageSharpen`
- `SetNode`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `SetNode`
- `LTXVImgToVideoInplace`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `SimpleMath+`
- `GetImageSize`
- `INTConstant`
- `Reroute`
- `Reroute`
- `SimpleMath+`
- `CM_FloatToInt`
- `AudioDuration_wan`
- `SolidMask`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `PrimitiveBoolean`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `IndexTTS2Run`
- `PrimitiveStringMultiline`
- `VHS_VideoCombine`
- `AudioPad`
- `SetNode`
- `PreviewAudio`
- `ResizeImageMaskNode`
- `ResizeImagesByLongerEdge`
- `LoadAudio`
- `LoadImage`
- `Int`
- `PrimitiveStringMultiline`
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
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `JjkText`
- `EmptyLatentImage` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **81%**（80/99）

**有卡**：`KSamplerSelect`、`CFGGuider`、`BasicScheduler`、`SimpleMath+`、`LoraLoaderModelOnly`、`RandomNoise`、`LTX2SamplingPreviewOverride`、`LTX2_NAG`、`CLIPTextEncode`、`LTXVConditioning`、`PathchSageAttentionKJ`、`LTXVConcatAVLatent`、`LTXVSeparateAVLatent`、`LatentUpscaleModelLoader`、`SamplerCustomAdvanced`、`LTXVImgToVideoInplace`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`KSampler`、`VAEDecodeTiled`、`easy cleanGpuUsed`、`ImageSharpen`、`CheckpointLoaderSimple`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`INTConstant`、`GetImageSize`、`CM_FloatToInt`、`AudioDuration_wan`、`SolidMask`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`PrimitiveBoolean`、`IndexTTS2Run`、`VHS_VideoCombine`、`AudioPad`、`PreviewAudio`、`ResizeImageMaskNode`、`ResizeImagesByLongerEdge`、`LoadAudio`、`LoadImage`、`Int`、`UNETLoader`、`CLIPLoader`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
