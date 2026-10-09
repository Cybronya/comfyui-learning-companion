---
key: 图片生成/文生图/Flux1.1pro-精炼人像lora_1910491843820253185.json
name: Flux1.1pro-精炼人像lora_1910491843820253185.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Flux1.1pro-精炼人像lora_1910491843820253185.json
hash: c93039c8353d5c0f
coverage: 1
learned_at: 2026-10-07 19:12:42
nodes: [FluxGuidance, CLIPTextEncode, DualCLIPLoader, VAELoader, VAEDecode, KSampler, TeaCache, LoraLoaderModelOnly, CLIPTextEncode, EmptyLatentImage, SaveImage, UNETLoader, LoraLoaderModelOnly]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 450213742954707, "steps": 8, "width": 768}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Flux1.1pro-精炼人像lora_1910491843820253185.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1910491843820253185.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（13 个）：
- `FluxGuidance`
- `CLIPTextEncode` ★核心
- `DualCLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `TeaCache`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `450213742954707`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `768`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（13/13）

**有卡**：`FluxGuidance`、`CLIPTextEncode`、`DualCLIPLoader`、`VAELoader`、`VAEDecode`、`KSampler`、`TeaCache`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`SaveImage`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、EmptyLatentImage、FluxGuidance

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
