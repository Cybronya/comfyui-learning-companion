---
key: 视频生成/图生视频/LTX-2.5-I2V图生视频｜双采样加速视频生成工作流_2096312957528530946.json
name: LTX-2.5-I2V图生视频｜双采样加速视频生成工作流_2096312957528530946
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/LTX-2.5-I2V图生视频｜双采样加速视频生成工作流_2096312957528530946.json
hash: 3221ebb47b069771
coverage: 0.891892
learned_at: 2026-10-17 01:09:24
nodes: [KSamplerSelect, LTXVConcatAVLatent, SamplerCustomAdvanced, CFGGuider, RandomNoise, ImageScaleBy, LoadImage, ManualSigmas, easy showAnything, easy showAnything, ImageResizeKJv2, LTXVPreprocess, ResolutionSelector, LatentUpscaleModelLoader, CLIPLoader, VAELoader, VAELoader, UNETLoader, ModelAttentionBackend, CLIPTextEncode, CLIPTextEncode, LTXVConditioning, EmptyImage, PrimitiveFloat, PrimitiveInt, LTXVEmptyLatentAudio, GetImageSize, EmptyLTXVLatentVideo, LTXVImgToVideoInplace, LTXVSeparateAVLatent, LTXVCropGuides, LTXVLatentUpsampler, LTXVImgToVideoInplace, RandomNoise, CFGGuider, KSamplerSelect, LTXVConcatAVLatent, ManualSigmas, SamplerCustomAdvanced, LTXVSeparateAVLatent, LTXVAudioVAEDecode, VAEDecodeTiled, ComfyMathExpression, CR Prompt Text, VHS_VideoCombine, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPLoader, CLIPTextEncode, JjkText, EmptyLatentImage, solarL_SaveImagesToZip, VAEDecode, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/LTX-2.5-I2V图生视频｜双采样加速视频生成工作流_2096312957528530946.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/LTX-2.5-I2V图生视频｜双采样加速视频生成工作流_2096312957528530946.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（74 个）：
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `RandomNoise`
- `ImageScaleBy`
- `LoadImage`
- `ManualSigmas`
- `easy showAnything`
- `easy showAnything`
- `ImageResizeKJv2`
- `LTXVPreprocess`
- `ResolutionSelector`
- `LatentUpscaleModelLoader`
- `CLIPLoader`
- `VAELoader`
- `VAELoader`
- `UNETLoader` ★核心
- `ModelAttentionBackend`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVConditioning`
- `EmptyImage`
- `PrimitiveFloat`
- `PrimitiveInt`
- `LTXVEmptyLatentAudio` ★核心
- `GetImageSize`
- `EmptyLTXVLatentVideo`
- `LTXVImgToVideoInplace`
- `LTXVSeparateAVLatent`
- `LTXVCropGuides`
- `LTXVLatentUpsampler` ★核心
- `LTXVImgToVideoInplace`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `LTXVConcatAVLatent`
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `LTXVSeparateAVLatent`
- `LTXVAudioVAEDecode` ★核心
- `VAEDecodeTiled` ★核心
- `ComfyMathExpression`
- `CR Prompt Text`
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

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **89%**（66/74）

**有卡**：`KSamplerSelect`、`LTXVConcatAVLatent`、`SamplerCustomAdvanced`、`CFGGuider`、`RandomNoise`、`ImageScaleBy`、`LoadImage`、`ManualSigmas`、`ImageResizeKJv2`、`LTXVPreprocess`、`ResolutionSelector`、`LatentUpscaleModelLoader`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`ModelAttentionBackend`、`CLIPTextEncode`、`LTXVConditioning`、`EmptyImage`、`LTXVEmptyLatentAudio`、`GetImageSize`、`EmptyLTXVLatentVideo`、`LTXVImgToVideoInplace`、`LTXVSeparateAVLatent`、`LTXVCropGuides`、`LTXVLatentUpsampler`、`LTXVAudioVAEDecode`、`VAEDecodeTiled`、`ComfyMathExpression`、`CR Prompt Text`、`VHS_VideoCombine`、`LoraLoaderModelOnly`、`KSampler`、`EmptyLatentImage`、`solarL_SaveImagesToZip`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
