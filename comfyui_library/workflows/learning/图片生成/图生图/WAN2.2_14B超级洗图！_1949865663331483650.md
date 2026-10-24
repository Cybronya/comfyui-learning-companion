---
key: 图片生成/图生图/WAN2.2_14B超级洗图！_1949865663331483650.json
name: WAN2.2_14B超级洗图！_1949865663331483650
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/WAN2.2_14B超级洗图！_1949865663331483650.json
hash: 345b48e2df471ca1
coverage: 1
learned_at: 2026-10-23 11:27:30
nodes: [EmptyHunyuanLatentVideo, CLIPLoader, CR Text, UNETLoader, UNETLoader, VAELoader, CLIPTextEncode, VAEEncode, CR Text, KSampler, LoadImage, RH_Captioner, CLIPTextEncode, ModelSamplingSD3, ModelSamplingSD3, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, EsesImageEffectBloom, BetterFilmGrain, SaveImage, ImageSharpen, EsesImageEffectBloom, ImageSharpen, BetterFilmGrain, SaveImage, VAEDecode, VAEDecode, KSampler, KSampler]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 3.5, "denoise": 0.10000000000000002, "sampler_name": "euler", "scheduler": "simple", "seed": 1023591399859136, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/WAN2.2_14B超级洗图！_1949865663331483650.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/WAN2.2_14B超级洗图！_1949865663331483650.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `EmptyHunyuanLatentVideo`
- `CLIPLoader`
- `CR Text`
- `UNETLoader` ★核心
- `UNETLoader` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAEEncode` ★核心
- `CR Text`
- `KSampler` ★核心
- `LoadImage`
- `RH_Captioner`
- `CLIPTextEncode` ★核心
- `ModelSamplingSD3`
- `ModelSamplingSD3`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `EsesImageEffectBloom`
- `BetterFilmGrain`
- `SaveImage`
- `ImageSharpen`
- `EsesImageEffectBloom`
- `ImageSharpen`
- `BetterFilmGrain`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `KSampler` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1023591399859136`
- `steps` = `6`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.10000000000000002`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`EmptyHunyuanLatentVideo`、`CLIPLoader`、`CR Text`、`UNETLoader`、`VAELoader`、`CLIPTextEncode`、`VAEEncode`、`KSampler`、`LoadImage`、`RH_Captioner`、`ModelSamplingSD3`、`LoraLoaderModelOnly`、`EsesImageEffectBloom`、`BetterFilmGrain`、`SaveImage`、`ImageSharpen`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
