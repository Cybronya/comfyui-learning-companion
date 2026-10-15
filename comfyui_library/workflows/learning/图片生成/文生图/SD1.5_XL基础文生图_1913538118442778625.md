---
key: 图片生成/文生图/SD1.5_XL基础文生图_1913538118442778625.json
name: SD1.5_XL基础文生图_1913538118442778625
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SD1.5_XL基础文生图_1913538118442778625.json
hash: 0fb31dcba6d4697a
coverage: 1
learned_at: 2026-10-10 20:59:10
nodes: [VAEDecode, SaveImage, CLIPTextEncode, KSampler, EmptyLatentImage, CLIPTextEncode, CheckpointLoaderSimple]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "全网首发｜SHMILY油画风_v2.1(不仅是人物）.safetensors", "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "normal", "seed": 589141046621615, "steps": 25, "width": 512}
---

# 图片生成/文生图/SD1.5_XL基础文生图_1913538118442778625.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SD1.5_XL基础文生图_1913538118442778625.json`

## 结构

**节点**（7 个）：
- `VAEDecode`
- `SaveImage`
- `CLIPTextEncode`
- `KSampler`
- `EmptyLatentImage`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `8`
- `checkpoint` = `全网首发｜SHMILY油画风_v2.1(不仅是人物）.safetensors`
- `denoise` = `1`
- `height` = `512`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `seed` = `589141046621615`
- `steps` = `25`
- `width` = `512`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`VAEDecode`、`SaveImage`、`CLIPTextEncode`、`KSampler`、`EmptyLatentImage`、`CheckpointLoaderSimple`
