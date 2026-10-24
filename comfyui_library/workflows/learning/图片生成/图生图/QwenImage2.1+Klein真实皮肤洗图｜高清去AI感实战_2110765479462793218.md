---
key: 图片生成/图生图/QwenImage2.1+Klein真实皮肤洗图｜高清去AI感实战_2110765479462793218.json
name: QwenImage2.1+Klein真实皮肤洗图｜高清去AI感实战_2110765479462793218
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenImage2.1+Klein真实皮肤洗图｜高清去AI感实战_2110765479462793218.json
hash: 6a18358711294561
coverage: 0.890244
learned_at: 2026-10-23 11:20:43
nodes: [RandomNoise, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, VAELoader, ReferenceLatent, ReferenceLatent, KSamplerSelect, CFGGuider, VAEDecode, ConditioningZeroOut, VAEEncode, VAEDecode, SamplerCustomAdvanced, EmptyLatentImage, UNETLoader, CLIPTextEncode, KSampler, CLIPTextEncode, ColorMatch, ImageScaleToTotalPixels, GetImageSize, EmptyFlux2LatentImage, Flux2Scheduler, LoraLoaderModelOnly, ImageSharpen, SaveImage, ImageSharpen, CLIPTextEncode, ResolutionSelector, QwenImagePromptOptimizer, PreviewAny, PreviewImage, PreviewImage, Image Comparer (rgthree), Image Comparer (rgthree), QwenImagePromptStyler, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QwenImage2.1+Klein真实皮肤洗图｜高清去AI感实战_2110765479462793218.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenImage2.1+Klein真实皮肤洗图｜高清去AI感实战_2110765479462793218.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（82 个）：
- `RandomNoise`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `VAELoader`
- `ReferenceLatent`
- `ReferenceLatent`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `VAEDecode` ★核心
- `ConditioningZeroOut`
- `VAEEncode` ★核心
- `VAEDecode` ★核心
- `SamplerCustomAdvanced` ★核心
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `ColorMatch`
- `ImageScaleToTotalPixels`
- `GetImageSize`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `LoraLoaderModelOnly` ★核心
- `ImageSharpen`
- `SaveImage`
- `ImageSharpen`
- `CLIPTextEncode` ★核心
- `ResolutionSelector`
- `QwenImagePromptOptimizer`
- `PreviewAny`
- `PreviewImage`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `QwenImagePromptStyler`
- `LoadImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **89%**（73/82）

**有卡**：`RandomNoise`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ReferenceLatent`、`KSamplerSelect`、`CFGGuider`、`VAEDecode`、`ConditioningZeroOut`、`VAEEncode`、`SamplerCustomAdvanced`、`EmptyLatentImage`、`CLIPTextEncode`、`KSampler`、`ColorMatch`、`ImageScaleToTotalPixels`、`GetImageSize`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`LoraLoaderModelOnly`、`ImageSharpen`、`SaveImage`、`ResolutionSelector`、`QwenImagePromptOptimizer`、`QwenImagePromptStyler`、`LoadImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
