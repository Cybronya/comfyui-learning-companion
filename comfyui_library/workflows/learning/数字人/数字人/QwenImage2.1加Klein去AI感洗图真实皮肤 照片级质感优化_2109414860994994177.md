---
key: 数字人/数字人/QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109414860994994177.json
name: QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109414860994994177
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109414860994994177.json
hash: 7867ec9ea4343a1e
coverage: 0.867647
learned_at: 2026-10-19 00:41:05
nodes: [RandomNoise, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, VAELoader, ReferenceLatent, ReferenceLatent, KSamplerSelect, CFGGuider, VAEDecode, ConditioningZeroOut, VAEEncode, VAEDecode, SamplerCustomAdvanced, EmptyLatentImage, UNETLoader, CLIPTextEncode, KSampler, CLIPTextEncode, ColorMatch, ImageScaleToTotalPixels, GetImageSize, EmptyFlux2LatentImage, Flux2Scheduler, LoraLoaderModelOnly, ImageSharpen, SaveImage, ImageSharpen, CLIPTextEncode, ResolutionSelector, QwenImagePromptOptimizer, PreviewAny, PreviewImage, PreviewImage, Image Comparer (rgthree), Image Comparer (rgthree), QwenImagePromptStyler, LoadImage, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 数字人/数字人/QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109414860994994177.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/QwenImage2.1加Klein去AI感洗图真实皮肤 照片级质感优化_2109414860994994177.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（68 个）：
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

覆盖率 **87%**（59/68）

**有卡**：`RandomNoise`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ReferenceLatent`、`KSamplerSelect`、`CFGGuider`、`VAEDecode`、`ConditioningZeroOut`、`VAEEncode`、`SamplerCustomAdvanced`、`EmptyLatentImage`、`CLIPTextEncode`、`KSampler`、`ColorMatch`、`ImageScaleToTotalPixels`、`GetImageSize`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`LoraLoaderModelOnly`、`ImageSharpen`、`SaveImage`、`ResolutionSelector`、`QwenImagePromptOptimizer`、`QwenImagePromptStyler`、`LoadImage`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
