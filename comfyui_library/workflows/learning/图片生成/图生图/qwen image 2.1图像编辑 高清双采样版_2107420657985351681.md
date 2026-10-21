---
key: 图片生成/图生图/qwen image 2.1图像编辑 高清双采样版_2107420657985351681.json
name: qwen image 2.1图像编辑 高清双采样版_2107420657985351681
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen image 2.1图像编辑 高清双采样版_2107420657985351681.json
hash: 6a631e2d7f5ba9d7
coverage: 0.830508
learned_at: 2026-10-21 00:46:01
nodes: [CLIPLoader, UNETLoader, KSampler, VAEDecode, VAELoader, EmptyLatentImage, ComfySwitchNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, easy showAnything, QwenPERewriteT8, LoadImage, LoadImage, ResolutionSelector, LoadImage, TextEncodeQwenImage21, QwenImage21BlockCacheT8, QwenImage21SageAttentionT8, QwenImage21SpectrumT8, UNETLoader, CLIPLoader, VAELoader, KSamplerSelect, LCSSharpnessCalibrate, LCSLoadData, VAEEncode, ConditioningZeroOut, ReferenceLatent, ReferenceLatent, LCSColorAnchor, LCSSharpnessIntervene, CFGGuider, Flux2Scheduler, EmptyFlux2LatentImage, SamplerCustomAdvanced, VAEDecode, ColorMatch, SetNode, LoraLoaderModelOnly, LoraLoaderModelOnly, easy cleanGpuUsed, SetNode, GetNode, CLIPTextEncode, CR Prompt Text, Image Comparer (rgthree), RandomNoise, ImageScaleToTotalPixels, GetImageSize, 孤海注释, 孤海注释, 孤海注释, 孤海注释, SaveImage, SaveImage]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 19960422, "steps": 40, "width": 1024}
---

# 图片生成/图生图/qwen image 2.1图像编辑 高清双采样版_2107420657985351681.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen image 2.1图像编辑 高清双采样版_2107420657985351681.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（59 个）：
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
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `孤海注释`
- `SaveImage`
- `SaveImage`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `seed` = `19960422`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（49/59）

**有卡**：`CLIPLoader`、`UNETLoader`、`KSampler`、`VAEDecode`、`VAELoader`、`EmptyLatentImage`、`LoadImage`、`QwenPERewriteT8`、`ResolutionSelector`、`TextEncodeQwenImage21`、`QwenImage21BlockCacheT8`、`QwenImage21SageAttentionT8`、`QwenImage21SpectrumT8`、`KSamplerSelect`、`LCSSharpnessCalibrate`、`LCSLoadData`、`VAEEncode`、`ConditioningZeroOut`、`ReferenceLatent`、`LCSColorAnchor`、`LCSSharpnessIntervene`、`CFGGuider`、`Flux2Scheduler`、`EmptyFlux2LatentImage`、`SamplerCustomAdvanced`、`ColorMatch`、`LoraLoaderModelOnly`、`easy cleanGpuUsed`、`CLIPTextEncode`、`CR Prompt Text`、`RandomNoise`、`ImageScaleToTotalPixels`、`GetImageSize`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader
