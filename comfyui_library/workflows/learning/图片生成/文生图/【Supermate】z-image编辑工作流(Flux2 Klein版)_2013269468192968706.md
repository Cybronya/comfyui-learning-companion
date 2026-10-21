---
key: 图片生成/文生图/【Supermate】z-image编辑工作流(Flux2 Klein版)_2013269468192968706.json
name: 【Supermate】z-image编辑工作流(Flux2 Klein版)_2013269468192968706
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【Supermate】z-image编辑工作流(Flux2 Klein版)_2013269468192968706.json
hash: be97eefa4f0455d2
coverage: 0.925373
learned_at: 2026-10-19 22:15:48
nodes: [KSamplerSelect, RandomNoise, CFGGuider, Flux2Scheduler, ImageScaleToTotalPixels, SamplerCustomAdvanced, ConditioningZeroOut, DrawMaskOnImage, VAEDecode, ImageConcanate, PreviewImage, ColorMatch, GetImageSize, VAEEncode, CLIPTextEncode, easy seed, EmptyFlux2LatentImage, ReferenceLatent, ReferenceLatent, SaveImage, PreviewImage, ImagePadForOutpaint, ImageScaleToTotalPixels, ConditioningZeroOut, CLIPTextEncode, EmptyLatentImage, KSamplerSelect, RandomNoise, CFGGuider, Flux2Scheduler, ImageScaleToTotalPixels, ConditioningZeroOut, VAEDecode, ImageConcanate, PreviewImage, ColorMatch, GetImageSize, VAEEncode, easy seed, EmptyFlux2LatentImage, ReferenceLatent, ReferenceLatent, SaveImage, PreviewImage, VAEDecode, ImageScaleToTotalPixels, KSampler, SaveImage, DrawMaskOnImage, Label (rgthree), Label (rgthree), Label (rgthree), SamplerCustomAdvanced, VAELoader, UNETLoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, UNETLoader, CLIPLoader, VAELoader, Fast Groups Bypasser (rgthree), LoadImage, CLIPTextEncode]
patterns: [text_to_image, image_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 4324235352, "steps": 30, "width": 720}
---

# 图片生成/文生图/【Supermate】z-image编辑工作流(Flux2 Klein版)_2013269468192968706.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【Supermate】z-image编辑工作流(Flux2 Klein版)_2013269468192968706.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（67 个）：
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
- `SamplerCustomAdvanced` ★核心
- `ConditioningZeroOut`
- `DrawMaskOnImage`
- `VAEDecode` ★核心
- `ImageConcanate`
- `PreviewImage`
- `ColorMatch`
- `GetImageSize`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `easy seed`
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `ReferenceLatent`
- `SaveImage`
- `PreviewImage`
- `ImagePadForOutpaint`
- `ImageScaleToTotalPixels`
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSamplerSelect` ★核心
- `RandomNoise`
- `CFGGuider`
- `Flux2Scheduler`
- `ImageScaleToTotalPixels`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `ImageConcanate`
- `PreviewImage`
- `ColorMatch`
- `GetImageSize`
- `VAEEncode` ★核心
- `easy seed`
- `EmptyFlux2LatentImage`
- `ReferenceLatent`
- `ReferenceLatent`
- `SaveImage`
- `PreviewImage`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `SaveImage`
- `DrawMaskOnImage`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `SamplerCustomAdvanced` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `4324235352`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **93%**（62/67）

**有卡**：`KSamplerSelect`、`RandomNoise`、`CFGGuider`、`Flux2Scheduler`、`ImageScaleToTotalPixels`、`SamplerCustomAdvanced`、`ConditioningZeroOut`、`DrawMaskOnImage`、`VAEDecode`、`ImageConcanate`、`ColorMatch`、`GetImageSize`、`VAEEncode`、`CLIPTextEncode`、`easy seed`、`EmptyFlux2LatentImage`、`ReferenceLatent`、`SaveImage`、`ImagePadForOutpaint`、`EmptyLatentImage`、`KSampler`、`Label (rgthree)`、`VAELoader`、`UNETLoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut
