---
key: 图片生成/图生图/FireRed-Image-edit1.1单图_双图_三图编辑_2030064414078017537.json
name: FireRed-Image-edit1.1单图_双图_三图编辑_2030064414078017537
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1单图_双图_三图编辑_2030064414078017537.json
hash: 1192ad660350a448
coverage: 0.964286
learned_at: 2026-10-23 10:55:51
nodes: [CLIPLoader, CFGNorm, LoraLoaderModelOnly, SaveImage, KSampler, VAEDecode, ModelSamplingAuraFlow, VAELoader, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, FluxKontextImageScale, UNETLoader, FluxKontextImageScale, FluxKontextImageScale, CLIPLoader, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, UNETLoader, EmptyLatentImage, LoadImage, LoadImage, CLIPLoader, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, UNETLoader, VAELoader, VAEEncode, LoadImage, CR Prompt Text, VAEDecode, FluxKontextImageScale, SaveImage, Image Comparer (rgthree), LoadImage, CR Prompt Text, KSampler, KSampler, FluxKontextImageScale, VAELoader, VAEEncode, CR Prompt Text, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, ModelSamplingAuraFlow, CFGNorm, SaveImage, VAEDecode, FluxKontextImageScale, Image Comparer (rgthree), LoraLoaderModelOnly, CFGNorm, EmptyLatentImage, LoadImage, LoraLoaderModelOnly]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 876542100097928, "steps": 8, "width": 1920}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/FireRed-Image-edit1.1单图_双图_三图编辑_2030064414078017537.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/FireRed-Image-edit1.1单图_双图_三图编辑_2030064414078017537.json`

## 结构

**生成流程**：Model → Encode → Latent → Sampling → Decode → Output → Other

**节点**（56 个）：
- `CLIPLoader`
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `VAELoader`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `FluxKontextImageScale`
- `UNETLoader` ★核心
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `CLIPLoader`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoadImage`
- `CLIPLoader`
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `UNETLoader` ★核心
- `VAELoader`
- `VAEEncode` ★核心
- `LoadImage`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `SaveImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `CR Prompt Text`
- `KSampler` ★核心
- `KSampler` ★核心
- `FluxKontextImageScale`
- `VAELoader`
- `VAEEncode` ★核心
- `CR Prompt Text`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `SaveImage`
- `VAEDecode` ★核心
- `FluxKontextImageScale`
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `876542100097928`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **96%**（54/56）

**有卡**：`CLIPLoader`、`CFGNorm`、`LoraLoaderModelOnly`、`SaveImage`、`KSampler`、`VAEDecode`、`ModelSamplingAuraFlow`、`VAELoader`、`TextEncodeQwenImageEditPlus`、`FluxKontextImageScale`、`UNETLoader`、`EmptyLatentImage`、`LoadImage`、`VAEEncode`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 3 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
