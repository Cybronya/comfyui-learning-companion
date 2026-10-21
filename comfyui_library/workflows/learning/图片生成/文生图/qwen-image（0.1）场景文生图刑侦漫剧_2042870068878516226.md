---
key: 图片生成/文生图/qwen-image（0.1）场景文生图刑侦漫剧_2042870068878516226.json
name: qwen-image（0.1）场景文生图刑侦漫剧_2042870068878516226
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/qwen-image（0.1）场景文生图刑侦漫剧_2042870068878516226.json
hash: 95dd3216cfc4ba5f
coverage: 1
learned_at: 2026-10-21 02:57:33
nodes: [VAEDecode, CLIPLoader, VAELoader, UNETLoader, CLIPTextEncode, EmptyLatentImage, KSampler, SaveImage, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1080, "sampler_name": "euler", "scheduler": "simple", "seed": 379313659915764, "steps": 20, "width": 1920}
---

# 图片生成/文生图/qwen-image（0.1）场景文生图刑侦漫剧_2042870068878516226.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/qwen-image（0.1）场景文生图刑侦漫剧_2042870068878516226.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（9 个）：
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SaveImage`
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `379313659915764`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（9/9）

**有卡**：`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`CLIPTextEncode`、`EmptyLatentImage`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、UNETLoader、SaveImage
