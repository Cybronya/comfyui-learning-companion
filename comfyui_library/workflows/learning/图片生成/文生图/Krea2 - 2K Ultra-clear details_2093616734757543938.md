---
key: 图片生成/文生图/Krea2 - 2K Ultra-clear details_2093616734757543938.json
name: Krea2 - 2K Ultra-clear details_2093616734757543938
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2 - 2K Ultra-clear details_2093616734757543938.json
hash: 97a209762e63f7e5
coverage: 1
learned_at: 2026-10-20 01:18:52
nodes: [CLIPLoader, CLIPTextEncode, VAELoader, SeedVR2LoadVAEModel, VAEDecode, EmptyLatentImage, SaveImage, SeedVR2VideoUpscaler, LoraLoaderModelOnly, CLIPTextEncode, SeedVR2LoadDiTModel, KSampler, UNETLoader]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 960, "sampler_name": "euler", "scheduler": "simple", "seed": 83717559377987, "steps": 9, "width": 544}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Krea2 - 2K Ultra-clear details_2093616734757543938.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2 - 2K Ultra-clear details_2093616734757543938.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（13 个）：
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `SeedVR2LoadVAEModel`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `SeedVR2VideoUpscaler`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `SeedVR2LoadDiTModel`
- `KSampler` ★核心
- `UNETLoader` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `544`
- `height` = `960`
- `batch_size` = `1`
- `seed` = `83717559377987`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`SeedVR2LoadVAEModel`、`VAEDecode`、`EmptyLatentImage`、`SaveImage`、`SeedVR2VideoUpscaler`、`LoraLoaderModelOnly`、`SeedVR2LoadDiTModel`、`KSampler`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
