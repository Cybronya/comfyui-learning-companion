---
key: 图片生成/文生图/巨型建筑 _ 巨型怪物（Krea2 + Flux.2 Klein 三采样）_2075937547938779137.json
name: 巨型建筑 _ 巨型怪物（Krea2 + Flux.2 Klein 三采样）_2075937547938779137
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/巨型建筑 _ 巨型怪物（Krea2 + Flux.2 Klein 三采样）_2075937547938779137.json
hash: 35e4fec6471a85ae
coverage: 0.450549
learned_at: 2026-10-20 00:21:14
nodes: [Reroute, VAEEncodeTiled, VAEDecodeTiled, easy showAnything, ComfyNumberConvert, easy showAnything, ComfyNumberConvert, EmptyLatentImage, Reroute, Reroute, ResolutionSelector, Reroute, easy int, Reroute, VAELoader, CLIPTextEncode, CLIPTextEncode, Reroute, UNETLoader, CLIPLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageScaleToTotalPixels, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPTextEncode, ConditioningZeroOut, Reroute, UNETLoader, GetImageSize, KSamplerAdvanced, VAEEncodeTiled, Reroute, Reroute, Reroute, EmptyFlux2LatentImage, ImageScaleToTotalPixels, VAEDecodeTiled, CLIPTextEncode, Reroute, ColorMatchV2, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Seed (rgthree), SaveImage, SaveImage, Image Comparer (rgthree), KSamplerAdvanced, CLIPLoader, VAELoader, MuyeTextEditOutput, MuyeTextEditOutput, CR Prompt Text, SaveImage, Reroute, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecodeTiled, KSampler, ReferenceLatent, ReferenceLatent, Reroute, Image Comparer (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 875707475343622, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 图片生成/文生图/巨型建筑 _ 巨型怪物（Krea2 + Flux.2 Klein 三采样）_2075937547938779137.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/巨型建筑 _ 巨型怪物（Krea2 + Flux.2 Klein 三采样）_2075937547938779137.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（91 个）：
- `Reroute`
- `VAEEncodeTiled` ★核心
- `VAEDecodeTiled` ★核心
- `easy showAnything`
- `ComfyNumberConvert`
- `easy showAnything`
- `ComfyNumberConvert`
- `EmptyLatentImage` ★核心
- `Reroute`
- `Reroute`
- `ResolutionSelector`
- `Reroute`
- `easy int`
- `Reroute`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `UNETLoader` ★核心
- `CLIPLoader`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ImageScaleToTotalPixels`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `Reroute`
- `UNETLoader` ★核心
- `GetImageSize`
- `KSamplerAdvanced` ★核心
- `VAEEncodeTiled` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `EmptyFlux2LatentImage`
- `ImageScaleToTotalPixels`
- `VAEDecodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `Reroute`
- `ColorMatchV2`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Seed (rgthree)`
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `KSamplerAdvanced` ★核心
- `CLIPLoader`
- `VAELoader`
- `MuyeTextEditOutput`
- `MuyeTextEditOutput`
- `CR Prompt Text`
- `SaveImage`
- `Reroute`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecodeTiled` ★核心
- `KSampler` ★核心
- `ReferenceLatent`
- `ReferenceLatent`
- `Reroute`
- `Image Comparer (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `875707475343622`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **45%**（41/91）

**有卡**：`VAEEncodeTiled`、`VAEDecodeTiled`、`ComfyNumberConvert`、`EmptyLatentImage`、`ResolutionSelector`、`easy int`、`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`ImageScaleToTotalPixels`、`ConditioningZeroOut`、`GetImageSize`、`KSamplerAdvanced`、`EmptyFlux2LatentImage`、`ColorMatchV2`、`Seed (rgthree)`、`SaveImage`、`MuyeTextEditOutput`、`CR Prompt Text`、`LoraLoaderModelOnly`、`KSampler`、`ReferenceLatent`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
