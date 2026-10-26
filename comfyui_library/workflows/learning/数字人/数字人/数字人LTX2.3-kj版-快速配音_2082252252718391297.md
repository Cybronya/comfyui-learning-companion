---
key: 数字人/数字人/数字人LTX2.3-kj版-快速配音_2082252252718391297.json
name: 数字人LTX2.3-kj版-快速配音_2082252252718391297
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/数字人LTX2.3-kj版-快速配音_2082252252718391297.json
hash: a9c6f7b25248de72
coverage: 0.980952
learned_at: 2026-10-26 02:02:38
nodes: [CFGGuider, LTXVConcatAVLatent, KSamplerSelect, easy getNode, easy getNode, easy getNode, LTXVSeparateAVLatent, SamplerCustomAdvanced, RandomNoise, easy getNode, AudioSeparation, easy setNode, easy getNode, easy setNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy getNode, easy setNode, easy getNode, easy getNode, easy setNode, easy setNode, easy setNode, easy getNode, ManualSigmas, VAEDecodeTiled, easy setNode, easy setNode, LTXVImgToVideoInplace, easy setNode, LTXVAudioVAEEncode, easy setNode, SetLatentNoiseMask, SolidMask, easy float, RandomNoise, SamplerCustomAdvanced, LTXVScheduler, LTXVConcatAVLatent, VAEDecodeTiled, VHS_VideoCombine, easy getNode, easy getNode, easy getNode, LTXVLatentUpsampler, LTXVImgToVideoInplace, easy getNode, LTXVSeparateAVLatent, easy setNode, LTXVPreprocess, EmptyLTXVLatentVideo, easy getNode, easy getNode, easy setNode, easy getNode, easy setNode, easy showAnything, MathExpression|pysssss, MathExpression|pysssss, MathExpression|pysssss, easy getNode, easy getNode, CLIPTextEncode, easy getNode, easy setNode, ImageResizeKJv2, easy setNode, easy getNode, easy setNode, AudioCrop, 1hew_AudioDuration, LoadImage, TTResolutionSelector, CLIPTextEncode, VHS_VideoCombine, DiffusionModelLoaderKJ, VAELoaderKJ, VAELoaderKJ, DualCLIPLoader, LatentUpscaleModelLoader, KSamplerSelect, CFGGuider, easy getNode, easy setNode, LTXVConditioning, LTX2_NAG, LTXVChunkFeedForward, easy setNode, easy getNode, VAEDecode, VAELoader, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, EmptyLatentImage, UNETLoader, solarL_SaveImagesToZip, LoadAudio]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/数字人LTX2.3-kj版-快速配音_2082252252718391297.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/数字人LTX2.3-kj版-快速配音_2082252252718391297.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（105 个）：
- `CFGGuider`
- `LTXVConcatAVLatent`
- `KSamplerSelect` ★核心
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `LTXVSeparateAVLatent`
- `SamplerCustomAdvanced` ★核心
- `RandomNoise`
- `easy getNode`
- `AudioSeparation`
- `easy setNode`
- `easy getNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy setNode`
- `easy setNode`
- `easy getNode`
- `ManualSigmas`
- `VAEDecodeTiled` ★核心
- `easy setNode`
- `easy setNode`
- `LTXVImgToVideoInplace`
- `easy setNode`
- `LTXVAudioVAEEncode` ★核心
- `easy setNode`
- `SetLatentNoiseMask`
- `SolidMask`
- `easy float`
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `LTXVScheduler`
- `LTXVConcatAVLatent`
- `VAEDecodeTiled` ★核心
- `VHS_VideoCombine`
- `easy getNode`
- `easy getNode`
- `easy getNode`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `easy getNode`
- `LTXVSeparateAVLatent`
- `easy setNode`
- `LTXVPreprocess`
- `EmptyLTXVLatentVideo`
- `easy getNode`
- `easy getNode`
- `easy setNode`
- `easy getNode`
- `easy setNode`
- `easy showAnything`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy getNode`
- `easy getNode`
- `CLIPTextEncode` ★核心
- `easy getNode`
- `easy setNode`
- `ImageResizeKJv2`
- `easy setNode`
- `easy getNode`
- `easy setNode`
- `AudioCrop`
- `1hew_AudioDuration`
- `LoadImage`
- `TTResolutionSelector`
- `CLIPTextEncode` ★核心
- `VHS_VideoCombine`
- `DiffusionModelLoaderKJ`
- `VAELoaderKJ`
- `VAELoaderKJ`
- `DualCLIPLoader`
- `LatentUpscaleModelLoader`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `easy getNode`
- `easy setNode`
- `LTXVConditioning`
- `LTX2_NAG`
- `LTXVChunkFeedForward`
- `easy setNode`
- `easy getNode`
- `VAEDecode` ★核心
- `VAELoader`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `solarL_SaveImagesToZip`
- `LoadAudio`

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

覆盖率 **98%**（103/105）

**有卡**：`CFGGuider`、`LTXVConcatAVLatent`、`KSamplerSelect`、`easy getNode`、`LTXVSeparateAVLatent`、`SamplerCustomAdvanced`、`RandomNoise`、`AudioSeparation`、`easy setNode`、`ManualSigmas`、`VAEDecodeTiled`、`LTXVImgToVideoInplace`、`LTXVAudioVAEEncode`、`SetLatentNoiseMask`、`SolidMask`、`easy float`、`LTXVScheduler`、`VHS_VideoCombine`、`LTXVLatentUpsampler`、`LTXVPreprocess`、`EmptyLTXVLatentVideo`、`MathExpression|pysssss`、`CLIPTextEncode`、`ImageResizeKJv2`、`AudioCrop`、`1hew_AudioDuration`、`LoadImage`、`TTResolutionSelector`、`DiffusionModelLoaderKJ`、`VAELoaderKJ`、`DualCLIPLoader`、`LatentUpscaleModelLoader`、`LTXVConditioning`、`LTX2_NAG`、`LTXVChunkFeedForward`、`VAEDecode`、`VAELoader`、`KSampler`、`CLIPLoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`UNETLoader`、`solarL_SaveImagesToZip`、`LoadAudio`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
