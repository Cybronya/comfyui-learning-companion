---
key: 图片生成/文生图/Z-image-distall-patch（文生图）写实性lora_2004006107569897473.json
name: Z-image-distall-patch（文生图）写实性lora_2004006107569897473
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Z-image-distall-patch（文生图）写实性lora_2004006107569897473.json
hash: 93db15bc1dfd871c
coverage: 1
learned_at: 2026-10-19 21:47:08
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, LoraLoaderModelOnly, LoraLoaderModelOnly, VAEDecode, easy promptLine, CLIPTextEncode, ConditioningZeroOut, KSampler, ImageConcatMulti, LoraLoaderModelOnly, KSampler, VAEDecode, SaveImage, SaveImage, SaveImage, CR Prompt Text]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1560, "sampler_name": "euler", "scheduler": "simple", "seed": 875069027257983, "steps": 10, "width": 1080}
---

# 图片生成/文生图/Z-image-distall-patch（文生图）写实性lora_2004006107569897473.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Z-image-distall-patch（文生图）写实性lora_2004006107569897473.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `easy promptLine`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `KSampler` ★核心
- `ImageConcatMulti`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `SaveImage`
- `CR Prompt Text`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1560`
- `batch_size` = `1`
- `seed` = `875069027257983`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（19/19）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`LoraLoaderModelOnly`、`VAEDecode`、`easy promptLine`、`CLIPTextEncode`、`ConditioningZeroOut`、`KSampler`、`ImageConcatMulti`、`SaveImage`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage
