---
key: 图片生成/文生图/API - SD3.5文生图_2091140151840952322.json
name: API - SD3.5文生图_2091140151840952322
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/API - SD3.5文生图_2091140151840952322.json
hash: 5ddb65757c93e23f
coverage: 0.9
learned_at: 2026-10-20 00:58:38
nodes: [CLIPTextEncode, VAEDecode, CLIPTextEncode, EmptyLatentImage, SaveImage, KSampler, PrimitiveStringMultiline, CheckpointLoaderSimple, Int, Int]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "illustrijEVO_lvl2.safetensors", "denoise": 1, "height": 512, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 653967173585317, "steps": 20, "width": 16}
---

# 图片生成/文生图/API - SD3.5文生图_2091140151840952322.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/API - SD3.5文生图_2091140151840952322.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（10 个）：
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `CheckpointLoaderSimple` ★核心
- `Int`
- `Int`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `16`
- `height` = `512`
- `batch_size` = `1`
- `seed` = `653967173585317`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `illustrijEVO_lvl2.safetensors`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`CLIPTextEncode`、`VAEDecode`、`EmptyLatentImage`、`SaveImage`、`KSampler`、`CheckpointLoaderSimple`、`Int`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、Int、sd15-t2i-basic
