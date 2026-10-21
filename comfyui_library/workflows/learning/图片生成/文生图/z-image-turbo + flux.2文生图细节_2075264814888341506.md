---
key: 图片生成/文生图/z-image-turbo + flux.2文生图细节_2075264814888341506.json
name: z-image-turbo + flux.2文生图细节_2075264814888341506
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/z-image-turbo + flux.2文生图细节_2075264814888341506.json
hash: 036dfbe281e07233
coverage: 1
learned_at: 2026-10-20 00:20:49
nodes: [CLIPTextEncode, LatentUpscaleBy, EmptyLatentImage, KSampler, KSampler, VAELoader, CLIPLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, UNETLoader, VAEDecode, SaveImage, CLIPTextEncode, EmptyLatentImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1280, "sampler_name": "euler", "scheduler": "simple", "seed": 1023995704261792, "steps": 9, "width": 720}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/z-image-turbo + flux.2文生图细节_2075264814888341506.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/z-image-turbo + flux.2文生图细节_2075264814888341506.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output

**节点**（14 个）：
- `CLIPTextEncode` ★核心
- `LatentUpscaleBy`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `KSampler` ★核心
- `VAELoader`
- `CLIPLoader`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `720`
- `height` = `1280`
- `batch_size` = `1`
- `seed` = `1023995704261792`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（14/14）

**有卡**：`CLIPTextEncode`、`LatentUpscaleBy`、`EmptyLatentImage`、`KSampler`、`VAELoader`、`CLIPLoader`、`LoraLoaderModelOnly`、`UNETLoader`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
