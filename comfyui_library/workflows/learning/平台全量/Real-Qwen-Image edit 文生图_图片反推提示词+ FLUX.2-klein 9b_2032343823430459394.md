---
key: 平台全量/Real-Qwen-Image edit 文生图_图片反推提示词+ FLUX.2-klein 9b_2032343823430459394.json
name: Real-Qwen-Image edit 文生图_图片反推提示词+ FLUX.2-klein 9b_2032343823430459394
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Real-Qwen-Image edit 文生图_图片反推提示词+ FLUX.2-klein 9b_2032343823430459394.json
hash: 7e494cf1ef8ced37
coverage: 0.935484
learned_at: 2026-11-14 00:54:34
nodes: [ConditioningZeroOut, VAEDecode, ModelSamplingAuraFlow, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, CLIPTextEncode, VAELoader, CLIPLoader, VAEEncode, ReferenceLatent, CLIPTextEncode, LoadImage, EmptyLatentImage, Seed (rgthree), CLIPTextEncode, KSampler, VAEDecode, PreviewImage, easy cleanGpuUsed, KSampler, easy cleanGpuUsed, ImageResize+, Image Comparer (rgthree), SaveImage, RH_Captioner, CR Text, easy textSwitch]
patterns: [text_to_image, image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler_ancestral", "scheduler": "sgm_uniform", "seed": 548249873467021, "steps": 4, "width": 960}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Real-Qwen-Image edit 文生图_图片反推提示词+ FLUX.2-klein 9b_2032343823430459394.json

> 来源文件 `comfyui_library/workflows/平台全量/Real-Qwen-Image edit 文生图_图片反推提示词+ FLUX.2-klein 9b_2032343823430459394.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `PreviewImage`
- `easy cleanGpuUsed`
- `KSampler` ★核心
- `easy cleanGpuUsed`
- `ImageResize+`
- `Image Comparer (rgthree)`
- `SaveImage`
- `RH_Captioner`
- `CR Text`
- `easy textSwitch`

**识别到的模式**：text_to_image、image_to_image

## 关键参数

- `width` = `960`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `548249873467021`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `sgm_uniform`
- `denoise` = `1`

## 知识

覆盖率 **94%**（29/31）

**有卡**：`ConditioningZeroOut`、`VAEDecode`、`ModelSamplingAuraFlow`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`CLIPTextEncode`、`VAEEncode`、`ReferenceLatent`、`LoadImage`、`EmptyLatentImage`、`Seed (rgthree)`、`KSampler`、`easy cleanGpuUsed`、`ImageResize+`、`SaveImage`、`RH_Captioner`、`CR Text`、`easy textSwitch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
