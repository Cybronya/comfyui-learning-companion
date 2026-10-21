---
key: 图片生成/文生图/qwen-image（0.1）_2038784092753367042.json
name: qwen-image（0.1）_2038784092753367042
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image（0.1）_2038784092753367042.json
hash: 50fea477d06403ce
coverage: 1
learned_at: 2026-10-21 02:57:32
nodes: [KSampler, CLIPTextEncode, VAEDecode, EmptyLatentImage, CLIPLoader, CLIPTextEncode, SaveImage, VAELoader, UNETLoader]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "denoise": 1, "height": 1920, "sampler_name": "euler", "scheduler": "simple", "seed": 808281691596370, "steps": 20, "width": 1080}
---

# 图片生成/文生图/qwen-image（0.1）_2038784092753367042.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image（0.1）_2038784092753367042.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（9 个）：
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `SaveImage`
- `VAELoader`
- `UNETLoader` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `808281691596370`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1080`
- `height` = `1920`
- `batch_size` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`KSampler`、`CLIPTextEncode`、`VAEDecode`、`EmptyLatentImage`、`CLIPLoader`、`SaveImage`、`VAELoader`、`UNETLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage
