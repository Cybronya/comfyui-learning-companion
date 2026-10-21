---
key: 图片生成/文生图/文生图：Qwen-image-Edite-Remix-AIO-v2.0_2045815282651893761.json
name: 文生图：Qwen-image-Edite-Remix-AIO-v2.0_2045815282651893761
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图：Qwen-image-Edite-Remix-AIO-v2.0_2045815282651893761.json
hash: 03757a40302fd882
coverage: 0.916667
learned_at: 2026-10-21 03:01:11
nodes: [CLIPTextEncode, EmptyLatentImage, SaveImage, VAEDecode, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SeedVR2LoadDiTModel, CheckpointLoaderSimple, SaveImage, Image Comparer (rgthree), KSampler, CLIPTextEncode]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "checkpoint": "Qwen-Image-Edit-Remix-AIO.safetensors", "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 883116753131435, "steps": 4, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/文生图：Qwen-image-Edite-Remix-AIO-v2.0_2045815282651893761.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图：Qwen-image-Edite-Remix-AIO-v2.0_2045815282651893761.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（12 个）：
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SeedVR2LoadDiTModel`
- `CheckpointLoaderSimple` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `checkpoint` = `Qwen-Image-Edit-Remix-AIO.safetensors`
- `seed` = `883116753131435`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`CLIPTextEncode`、`EmptyLatentImage`、`SaveImage`、`VAEDecode`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`CheckpointLoaderSimple`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SeedVR2LoadDiTModel、SeedVR2LoadVAEModel、SeedVR2VideoUpscaler

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
