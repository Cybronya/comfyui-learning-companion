---
key: 图片生成/文生图/Qwen2.1文生图（写实风格）_2104831851583066113.json
name: Qwen2.1文生图（写实风格）_2104831851583066113
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图（写实风格）_2104831851583066113.json
hash: bc5d038e789d137f
coverage: 0.857143
learned_at: 2026-10-10 20:59:07
nodes: [CLIPTextEncode, UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, EmptyLatentImage, KSampler, VAEDecode, PreviewImage, SaveImage, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 1095958535907224, "steps": 8, "width": 1024}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen2.1文生图（写实风格）_2104831851583066113.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen2.1文生图（写实风格）_2104831851583066113.json`

## 结构

**节点**（14 个）：
- `CLIPTextEncode`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `PreviewImage`
- `SaveImage`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1920`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `1095958535907224`
- `steps` = `8`
- `width` = `1024`

## 知识

覆盖率 **86%**（12/14）

**有卡**：`CLIPTextEncode`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`PreviewImage`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
