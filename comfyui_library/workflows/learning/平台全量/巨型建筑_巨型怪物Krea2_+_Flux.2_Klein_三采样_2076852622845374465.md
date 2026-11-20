---
key: 平台全量/巨型建筑_巨型怪物Krea2_+_Flux.2_Klein_三采样_2076852622845374465.json
name: 巨型建筑_巨型怪物Krea2_+_Flux.2_Klein_三采样_2076852622845374465
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/巨型建筑_巨型怪物Krea2_+_Flux.2_Klein_三采样_2076852622845374465.json
hash: 68135c11e124c986
coverage: 0.450549
learned_at: 2026-11-14 02:03:02
nodes: [Reroute, VAEEncodeTiled, VAEDecodeTiled, easy showAnything, ComfyNumberConvert, easy showAnything, ComfyNumberConvert, EmptyLatentImage, Reroute, Reroute, ResolutionSelector, Reroute, easy int, Reroute, VAELoader, CLIPTextEncode, CLIPTextEncode, Reroute, UNETLoader, CLIPLoader, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, ImageScaleToTotalPixels, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, CLIPTextEncode, ConditioningZeroOut, Reroute, UNETLoader, GetImageSize, KSamplerAdvanced, VAEEncodeTiled, Reroute, Reroute, Reroute, EmptyFlux2LatentImage, ImageScaleToTotalPixels, VAEDecodeTiled, CLIPTextEncode, Reroute, ColorMatchV2, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Reroute, Seed (rgthree), SaveImage, SaveImage, Image Comparer (rgthree), KSamplerAdvanced, CLIPLoader, VAELoader, MuyeTextEditOutput, CR Prompt Text, SaveImage, Reroute, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecodeTiled, KSampler, ReferenceLatent, ReferenceLatent, Reroute, Image Comparer (rgthree), MuyeTextEditOutput]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler_ancestral", "scheduler": "normal", "seed": 782962412752945, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换]
---

# 平台全量/巨型建筑_巨型怪物Krea2_+_Flux.2_Klein_三采样_2076852622845374465.json

> 来源文件 `comfyui_library/workflows/平台全量/巨型建筑_巨型怪物Krea2_+_Flux.2_Klein_三采样_2076852622845374465.json`

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
- `MuyeTextEditOutput`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `782962412752945`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **45%**（41/91）

**有卡**：`VAEEncodeTiled`、`VAEDecodeTiled`、`ComfyNumberConvert`、`EmptyLatentImage`、`ResolutionSelector`、`easy int`、`VAELoader`、`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`ImageScaleToTotalPixels`、`ConditioningZeroOut`、`GetImageSize`、`KSamplerAdvanced`、`EmptyFlux2LatentImage`、`ColorMatchV2`、`Seed (rgthree)`、`SaveImage`、`MuyeTextEditOutput`、`CR Prompt Text`、`LoraLoaderModelOnly`、`KSampler`、`ReferenceLatent`

**用到的条目**：KSampler、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [high] 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换
