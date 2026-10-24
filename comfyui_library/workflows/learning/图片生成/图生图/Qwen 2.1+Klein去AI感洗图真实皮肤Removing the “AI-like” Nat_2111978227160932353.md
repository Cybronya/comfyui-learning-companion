---
key: 图片生成/图生图/Qwen 2.1+Klein去AI感洗图真实皮肤Removing the “AI-like” Nat_2111978227160932353.json
name: Qwen 2.1+Klein去AI感洗图真实皮肤Removing the “AI-like” Nat_2111978227160932353
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen 2.1+Klein去AI感洗图真实皮肤Removing the “AI-like” Nat_2111978227160932353.json
hash: cc30077302ad833e
coverage: 0.868421
learned_at: 2026-10-23 11:11:34
nodes: [RandomNoise, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, VAELoader, ReferenceLatent, ReferenceLatent, KSamplerSelect, CFGGuider, VAEDecode, ConditioningZeroOut, VAEEncode, SamplerCustomAdvanced, EmptyLatentImage, UNETLoader, CLIPTextEncode, KSampler, CLIPTextEncode, ColorMatch, ImageScaleToTotalPixels, GetImageSize, EmptyFlux2LatentImage, Flux2Scheduler, LoraLoaderModelOnly, CLIPTextEncode, ResolutionSelector, PreviewImage, PreviewImage, LoadImage, PreviewAny, VAEDecode, Image Comparer (rgthree), ImageSharpen, ImageSharpen, Image Comparer (rgthree), SaveImage, QwenImagePromptOptimizer]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 2, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 300169977184620, "steps": 30, "width": 2048}
---

# 图片生成/图生图/Qwen 2.1+Klein去AI感洗图真实皮肤Removing the “AI-like” Nat_2111978227160932353.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen 2.1+Klein去AI感洗图真实皮肤Removing the “AI-like” Nat_2111978227160932353.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（38 个）：
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
- `CLIPTextEncode` ★核心
- `ResolutionSelector`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `PreviewAny`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `ImageSharpen`
- `ImageSharpen`
- `Image Comparer (rgthree)`
- `SaveImage`
- `QwenImagePromptOptimizer`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `2048`
- `height` = `2048`
- `batch_size` = `1`
- `seed` = `300169977184620`
- `steps` = `30`
- `cfg` = `2`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（33/38）

**有卡**：`RandomNoise`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ReferenceLatent`、`KSamplerSelect`、`CFGGuider`、`VAEDecode`、`ConditioningZeroOut`、`VAEEncode`、`SamplerCustomAdvanced`、`EmptyLatentImage`、`CLIPTextEncode`、`KSampler`、`ColorMatch`、`ImageScaleToTotalPixels`、`GetImageSize`、`EmptyFlux2LatentImage`、`Flux2Scheduler`、`LoraLoaderModelOnly`、`ResolutionSelector`、`LoadImage`、`ImageSharpen`、`SaveImage`、`QwenImagePromptOptimizer`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
