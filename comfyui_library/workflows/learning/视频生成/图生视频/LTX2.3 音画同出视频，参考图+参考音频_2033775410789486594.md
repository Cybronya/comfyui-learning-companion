---
key: 视频生成/图生视频/LTX2.3 音画同出视频，参考图+参考音频_2033775410789486594.json
name: LTX2.3 音画同出视频，参考图+参考音频_2033775410789486594.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2033775410789486594.json
hash: 15c72a1a8e5dc233
coverage: 0.954545
learned_at: 2026-10-15 22:35:41
nodes: [LoraLoaderModelOnly, PathchSageAttentionKJ, AudioPad, ResizeImagesByLongerEdge, LTXVPreprocess, IndexTTS2Run, LoraLoaderModelOnly, AudioDuration_wan, CM_FloatToInt, LoadImage, LoadAudio, PrimitiveStringMultiline, GetImageSize, SimpleMath+, SimpleMath+, EmptyLTXVLatentVideo, SolidMask, LTXVImgToVideoInplace, CheckpointLoaderSimple, LTX2SamplingPreviewOverride, KSampler, LTXVSeparateAVLatent, VAEDecodeTiled, LayerUtility: PurgeVRAM V2, LatentUpscaleModelLoader, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, LTXVConcatAVLatent, KSampler, VHS_VideoCombine, LTXVAudioVAEEncode, SetLatentNoiseMask, SimpleMath+, easy showAnything, SaveAudio, ResizeImageMaskNode, LTXAVTextEncoderLoader, LTXVAudioVAELoader, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, LTXVConcatAVLatent]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"cfg": 1, "checkpoint": "ltx-2.3-22b-dev.safetensors", "denoise": 0.4, "sampler_name": "euler", "scheduler": "simple", "seed": 15892740037726, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 视频生成/图生视频/LTX2.3 音画同出视频，参考图+参考音频_2033775410789486594.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2033775410789486594.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（44 个）：
- `LoraLoaderModelOnly` ★核心
- `PathchSageAttentionKJ`
- `AudioPad`
- `ResizeImagesByLongerEdge`
- `LTXVPreprocess`
- `IndexTTS2Run`
- `LoraLoaderModelOnly` ★核心
- `AudioDuration_wan`
- `CM_FloatToInt`
- `LoadImage`
- `LoadAudio`
- `PrimitiveStringMultiline`
- `GetImageSize`
- `SimpleMath+`
- `SimpleMath+`
- `EmptyLTXVLatentVideo`
- `SolidMask`
- `LTXVImgToVideoInplace`
- `CheckpointLoaderSimple` ★核心
- `LTX2SamplingPreviewOverride`
- `KSampler` ★核心
- `LTXVSeparateAVLatent`
- `VAEDecodeTiled` ★核心
- `LayerUtility: PurgeVRAM V2`
- `LatentUpscaleModelLoader`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `LTXVConcatAVLatent`
- `KSampler` ★核心
- `VHS_VideoCombine`
- `LTXVAudioVAEEncode` ★核心
- `SetLatentNoiseMask`
- `SimpleMath+`
- `easy showAnything`
- `SaveAudio`
- `ResizeImageMaskNode`
- `LTXAVTextEncoderLoader`
- `LTXVAudioVAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `LTXVConcatAVLatent`

## 关键参数

- `checkpoint` = `ltx-2.3-22b-dev.safetensors`
- `seed` = `15892740037726`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.4`

## 知识

覆盖率 **95%**（42/44）

**有卡**：`LoraLoaderModelOnly`、`PathchSageAttentionKJ`、`AudioPad`、`ResizeImagesByLongerEdge`、`LTXVPreprocess`、`IndexTTS2Run`、`AudioDuration_wan`、`CM_FloatToInt`、`LoadImage`、`LoadAudio`、`GetImageSize`、`SimpleMath+`、`EmptyLTXVLatentVideo`、`SolidMask`、`LTXVImgToVideoInplace`、`CheckpointLoaderSimple`、`LTX2SamplingPreviewOverride`、`KSampler`、`LTXVSeparateAVLatent`、`VAEDecodeTiled`、`LayerUtility: PurgeVRAM V2`、`LatentUpscaleModelLoader`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVConcatAVLatent`、`VHS_VideoCombine`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SaveAudio`、`ResizeImageMaskNode`、`LTXAVTextEncoderLoader`、`LTXVAudioVAELoader`、`CLIPTextEncode`、`LTXVConditioning`

**用到的条目**：KSampler、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LTXVLatentUpsampler、LTXVConcatAVLatent、LTXVSeparateAVLatent

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
