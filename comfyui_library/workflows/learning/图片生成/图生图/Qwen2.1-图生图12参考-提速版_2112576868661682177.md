---
key: 图片生成/图生图/Qwen2.1-图生图12参考-提速版_2112576868661682177.json
name: Qwen2.1-图生图12参考-提速版_2112576868661682177
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen2.1-图生图12参考-提速版_2112576868661682177.json
hash: bc04e482a3fc69b0
coverage: 1
learned_at: 2026-10-23 11:19:04
nodes: [UNETLoader, CLIPLoader, VAELoader, LoraLoaderModelOnly, QwenImage21Cache, EmptyLatentImage, KSampler, VAEDecode, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, LoadImage, LoadImage]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 720, "sampler_name": "euler", "scheduler": "simple", "seed": 240728840750075, "steps": 8, "width": 1280}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen2.1-图生图12参考-提速版_2112576868661682177.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen2.1-图生图12参考-提速版_2112576868661682177.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（21 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `QwenImage21Cache`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `1280`
- `height` = `720`
- `batch_size` = `1`
- `seed` = `240728840750075`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（21/21）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`LoraLoaderModelOnly`、`QwenImage21Cache`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImage`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
