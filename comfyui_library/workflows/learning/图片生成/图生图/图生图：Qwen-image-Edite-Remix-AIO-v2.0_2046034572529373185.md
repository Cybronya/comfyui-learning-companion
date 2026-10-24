---
key: 图片生成/图生图/图生图：Qwen-image-Edite-Remix-AIO-v2.0_2046034572529373185.json
name: 图生图：Qwen-image-Edite-Remix-AIO-v2.0_2046034572529373185
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图生图：Qwen-image-Edite-Remix-AIO-v2.0_2046034572529373185.json
hash: 4390677c461785f4
coverage: 0.909091
learned_at: 2026-10-23 12:44:05
nodes: [VAEDecode, SaveImage, Image Comparer (rgthree), VAEEncode, CheckpointLoaderSimple, LoadImage, CLIPTextEncode, LoraLoader, CLIPTextEncode, LatentUpscaleBy, KSampler]
patterns: [image_to_image, lora]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Image-Edit-Remix-AIO-v2.0.safetensors", "denoise": 0.5000000000000001, "lora_name": "动漫转真人Qwen-Edit-2511-Anime2real_V4.safetensors", "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 871264772502626, "steps": 4, "strength_clip": 0.8000000000000002, "strength_model": 1.0000000000000002}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/图生图：Qwen-image-Edite-Remix-AIO-v2.0_2046034572529373185.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图生图：Qwen-image-Edite-Remix-AIO-v2.0_2046034572529373185.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `VAEDecode` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `CLIPTextEncode` ★核心
- `LoraLoader` ★核心
- `CLIPTextEncode` ★核心
- `LatentUpscaleBy`
- `KSampler` ★核心

**识别到的模式**：image_to_image、lora

## 关键参数

- `checkpoint` = `Qwen-Image-Edit-Remix-AIO-v2.0.safetensors`
- `lora_name` = `动漫转真人Qwen-Edit-2511-Anime2real_V4.safetensors`
- `strength_model` = `1.0000000000000002`
- `strength_clip` = `0.8000000000000002`
- `seed` = `871264772502626`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `0.5000000000000001`

## 知识

覆盖率 **91%**（10/11）

**有卡**：`VAEDecode`、`SaveImage`、`VAEEncode`、`CheckpointLoaderSimple`、`LoadImage`、`CLIPTextEncode`、`LoraLoader`、`LatentUpscaleBy`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、LoadImage、LatentUpscaleBy、VAEEncode、LoraLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
