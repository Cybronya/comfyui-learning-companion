---
key: 图片生成/文生图/文生图（SD1.5;SDXL）_2064679284408672257.json
name: 文生图（SD1.5;SDXL）_2064679284408672257
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图（SD1.5;SDXL）_2064679284408672257.json
hash: e3b2773ff7ea091f
coverage: 0.7
learned_at: 2026-10-19 23:23:15
nodes: [CLIPTextEncode, Note, CLIPTextEncode, Note, CheckpointLoaderSimple, EmptyLatentImage, KSampler, SaveImage, VAEDecode, PreviewImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "XL真人写实摄影_V1.safetensors", "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 1034942935868292, "steps": 29, "width": 1024}
---

# 图片生成/文生图/文生图（SD1.5;SDXL）_2064679284408672257.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图（SD1.5;SDXL）_2064679284408672257.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（10 个）：
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `Note`
- `CheckpointLoaderSimple` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SaveImage`
- `VAEDecode` ★核心
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `XL真人写实摄影_V1.safetensors`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1034942935868292`
- `steps` = `29`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **70%**（7/10）

**有卡**：`CLIPTextEncode`、`CheckpointLoaderSimple`、`EmptyLatentImage`、`KSampler`、`SaveImage`、`VAEDecode`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora
