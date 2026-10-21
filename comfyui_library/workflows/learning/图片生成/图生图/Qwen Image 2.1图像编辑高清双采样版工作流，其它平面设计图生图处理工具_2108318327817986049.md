---
key: 图片生成/图生图/Qwen Image 2.1图像编辑高清双采样版工作流，其它平面设计图生图处理工具_2108318327817986049.json
name: Qwen Image 2.1图像编辑高清双采样版工作流，其它平面设计图生图处理工具_2108318327817986049
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图像编辑高清双采样版工作流，其它平面设计图生图处理工具_2108318327817986049.json
hash: 9c706fa49206ec23
coverage: 0.880952
learned_at: 2026-10-21 00:42:30
nodes: [CLIPLoader, UNETLoader, KSampler, VAEDecode, VAELoader, EmptyLatentImage, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy showAnything, QwenPERewriteT8, LoadImage, LoadImage, ResolutionSelector, LoadImage, TextEncodeQwenImage21, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, UNETLoader, CLIPLoader, VAELoader, KSamplerSelect, LCSSharpnessCalibrate, LCSLoadData, VAEEncode, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, LCSColorAnchor, LCSSharpnessIntervene, CFGGuider, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, ColorMatch, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, easy cleanGpuUsed, SetNode, GetNode, CLIPTextEncode, CR Prompt Text, Image Comparer (rgthree), RandomNoise, ImageScaleToTotalPixels, GetImageSize, SaveImage, SaveImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image 2.1图像编辑高清双采样版工作流，其它平面设计图生图处理工具_2108318327817986049.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图像编辑高清双采样版工作流，其它平面设计图生图处理工具_2108318327817986049.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（84 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy showAnything`
- `QwenPERewriteT8`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `TextEncodeQwenImage21`
- `QwenImage21BlockCacheT8`
- `QwenImage21SageAttentionT8`
- `QwenImage21SpectrumT8`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSamplerSelect` ★核心
- `LCSSharpnessCalibrate`
- `LCSLoadData`
- `VAEEncode` ★核心
- `ConditioningZeroOut`
- `ReferenceLatent`
- `ReferenceLatent`
- `LCSColorAnchor`
- `LCSSharpnessIntervene`
- `CFGGuider`
- `Flux2Scheduler`
- `EmptyFlux2LatentImage`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ColorMatch`
- `SetNode`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CR Prompt Text`
- `Image Comparer (rgthree)`
- `RandomNoise`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `SaveImage`
- `SaveImage`
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

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **88%**（74/84）

**有卡**：`CLIPLoader`、`UNETLoader`、`KSampler`、`VAEDecode`、`VAELoader`、`EmptyLatentImage`、`LoadImage`、`QwenPERewriteT8`、`ResolutionSelector`、`TextEncodeQwenImage21`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`QwenImage21SpectrumT8`、`KSamplerSelect`、`LCSSharpnessCalibrate`、`LCSLoadData`、`VAEEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`LCSColorAnchor`、`LCSSharpnessIntervene`、`CFGGuider`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`ColorMatch`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`CLIPTextEncode`、`CR Prompt Text`、`RandomNoise`、`ImageScaleToTotalPixels`、`GetImageSize`、`SaveImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
