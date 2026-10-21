---
key: 图片生成/文生图/SD1.5_xl文生图_2083827064628666369.json
name: SD1.5_xl文生图_2083827064628666369
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SD1.5_xl文生图_2083827064628666369.json
hash: 6417ed146fc48753
coverage: 0.777778
learned_at: 2026-10-20 00:39:34
nodes: [VAEDecode, CLIPTextEncode, Note, CLIPTextEncode, Note, EmptyLatentImage, SaveImage, KSampler, CheckpointLoaderSimple]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "XL真人写实摄影_V1.safetensors", "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 238340264054122, "steps": 29, "width": 1024}
---

# 图片生成/文生图/SD1.5_xl文生图_2083827064628666369.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SD1.5_xl文生图_2083827064628666369.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（9 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `Note`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `238340264054122`
- `steps` = `29`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`
- `checkpoint` = `XL真人写实摄影_V1.safetensors`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`EmptyLatentImage`、`SaveImage`、`KSampler`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora
