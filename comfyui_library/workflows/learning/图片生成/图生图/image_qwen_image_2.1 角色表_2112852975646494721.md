---
key: 图片生成/图生图/image_qwen_image_2.1 角色表_2112852975646494721.json
name: image_qwen_image_2.1 角色表_2112852975646494721
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/image_qwen_image_2.1 角色表_2112852975646494721.json
hash: 0e71c169b1a28fcb
coverage: 1
learned_at: 2026-10-26 22:04:05
nodes: [UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, QwenImage21Cache, TextEncodeQwenImage21, easy promptLine, LoadImage, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 633907050706283, "steps": 25, "width": 1024}
---

# 图片生成/图生图/image_qwen_image_2.1 角色表_2112852975646494721.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/image_qwen_image_2.1 角色表_2112852975646494721.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（11 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `easy promptLine`
- `LoadImage`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `633907050706283`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`easy promptLine`、`LoadImage`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
