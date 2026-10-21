---
key: 图片生成/文生图/【Supermate】Real-Qwen-Image2512-V2-Klein workflow_2022216516262957057.json
name: 【Supermate】Real-Qwen-Image2512-V2-Klein workflow_2022216516262957057
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/【Supermate】Real-Qwen-Image2512-V2-Klein workflow_2022216516262957057.json
hash: 37edc3a573e9cd09
coverage: 0.896552
learned_at: 2026-10-19 22:30:17
nodes: [ImageResize+, KSampler, ConditioningZeroOut, SaveImage, VAEDecode, VAEDecode, easy cleanGpuUsed, ModelSamplingAuraFlow, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, KSampler, Seed (rgthree), CLIPTextEncode, VAELoader, CLIPLoader, PreviewImage, easy cleanGpuUsed, VAEEncode, ReferenceLatent, CLIPTextEncode, CLIPTextEncode, Image Comparer (rgthree), EmptyLatentImage, Label (rgthree), Fast Groups Muter (rgthree)]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1.5, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 121125480055509, "steps": 4, "width": 960}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/【Supermate】Real-Qwen-Image2512-V2-Klein workflow_2022216516262957057.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/【Supermate】Real-Qwen-Image2512-V2-Klein workflow_2022216516262957057.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（29 个）：
- `ImageResize+`
- `KSampler` ★核心
- `ConditioningZeroOut`
- `SaveImage`
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ModelSamplingAuraFlow`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `Seed (rgthree)`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `PreviewImage`
- `easy cleanGpuUsed`
- `VAEEncode` ★核心
- `ReferenceLatent`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `EmptyLatentImage` ★核心
- `Label (rgthree)`
- `Fast Groups Muter (rgthree)`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `121125480055509`
- `steps` = `4`
- `cfg` = `1.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `960`
- `height` = `1280`
- `batch_size` = `1`

## 知识

覆盖率 **90%**（26/29）

**有卡**：`ImageResize+`、`KSampler`、`ConditioningZeroOut`、`SaveImage`、`VAEDecode`、`easy cleanGpuUsed`、`ModelSamplingAuraFlow`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`Seed (rgthree)`、`CLIPTextEncode`、`VAEEncode`、`ReferenceLatent`、`EmptyLatentImage`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
