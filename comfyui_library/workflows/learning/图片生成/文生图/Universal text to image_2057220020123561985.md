---
key: 图片生成/文生图/Universal text to image_2057220020123561985.json
name: Universal text to image_2057220020123561985
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Universal text to image_2057220020123561985.json
hash: 254a46f638801081
coverage: 0.923077
learned_at: 2026-10-19 22:45:42
nodes: [CLIPLoader, UNETLoader, VAELoader, LoraLoaderModelOnly, EmptyLatentImage, ModelSamplingAuraFlow, TextEncodeQwenImageEditPlus, JjkText, CLIPTextEncode, CFGNorm, KSampler, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 2, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 558204870042534, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Universal text to image_2057220020123561985.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Universal text to image_2057220020123561985.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `ModelSamplingAuraFlow`
- `TextEncodeQwenImageEditPlus`
- `JjkText`
- `CLIPTextEncode` ★核心
- `CFGNorm`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `558204870042534`
- `steps` = `4`
- `cfg` = `2`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（12/13）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`ModelSamplingAuraFlow`、`TextEncodeQwenImageEditPlus`、`CLIPTextEncode`、`CFGNorm`、`KSampler`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
