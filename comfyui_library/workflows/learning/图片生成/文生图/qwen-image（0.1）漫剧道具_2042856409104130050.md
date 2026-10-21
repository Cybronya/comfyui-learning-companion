---
key: 图片生成/文生图/qwen-image（0.1）漫剧道具_2042856409104130050.json
name: qwen-image（0.1）漫剧道具_2042856409104130050
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image（0.1）漫剧道具_2042856409104130050.json
hash: 966adff0c4851207
coverage: 1
learned_at: 2026-10-21 02:57:33
nodes: [VAEDecode, EmptyLatentImage, CLIPLoader, SaveImage, VAELoader, UNETLoader, CLIPTextEncode, CLIPTextEncode, KSampler]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 732182395088784, "steps": 9, "width": 1080}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/qwen-image（0.1）漫剧道具_2042856409104130050.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image（0.1）漫剧道具_2042856409104130050.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（9 个）：
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `SaveImage`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`
- `seed` = `732182395088784`
- `steps` = `9`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`VAEDecode`、`EmptyLatentImage`、`CLIPLoader`、`SaveImage`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`KSampler`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
