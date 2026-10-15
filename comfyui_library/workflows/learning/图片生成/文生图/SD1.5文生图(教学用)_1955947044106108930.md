---
key: 图片生成/文生图/SD1.5文生图(教学用)_1955947044106108930.json
name: SD1.5文生图(教学用)_1955947044106108930
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SD1.5文生图(教学用)_1955947044106108930.json
hash: 52fe8eec849e9291
coverage: 0.875
learned_at: 2026-10-10 20:59:10
nodes: [CLIPTextEncode, CLIPTextEncode, EmptyLatentImage, easy positive, CheckpointLoaderSimple, KSampler, VAEDecode, SaveImage]
patterns: [text_to_image]
missing: [easy positive]
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "epicrealism_pureEvolutionV5-inpainting.safetensors", "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 173655344067579, "steps": 25, "width": 1024}
discoveries: [次要节点 `easy positive` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/SD1.5文生图(教学用)_1955947044106108930.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SD1.5文生图(教学用)_1955947044106108930.json`

## 结构

**节点**（8 个）：
- `CLIPTextEncode`
- `CLIPTextEncode`
- `EmptyLatentImage`
- `easy positive`
- `CheckpointLoaderSimple`
- `KSampler`
- `VAEDecode`
- `SaveImage`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `7`
- `checkpoint` = `epicrealism_pureEvolutionV5-inpainting.safetensors`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `seed` = `173655344067579`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **88%**（7/8）

**有卡**：`CLIPTextEncode`、`EmptyLatentImage`、`easy positive`、`CheckpointLoaderSimple`、`KSampler`、`VAEDecode`

**缺卡**（1）：`easy positive`

## 学习发现

- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
