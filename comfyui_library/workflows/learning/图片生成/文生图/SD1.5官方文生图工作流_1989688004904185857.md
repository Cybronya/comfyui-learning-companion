---
key: 图片生成/文生图/SD1.5官方文生图工作流_1989688004904185857.json
name: SD1.5官方文生图工作流_1989688004904185857
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SD1.5官方文生图工作流_1989688004904185857.json
hash: 2292e502142766cb
coverage: 1
learned_at: 2026-10-10 20:59:10
nodes: [CLIPTextEncode, KSampler, VAEDecode, SaveImage, EmptyLatentImage, CLIPTextEncode, CheckpointLoaderSimple]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "v1-5-pruned-emaonly.ckpt", "denoise": 1, "height": 512, "sampler_name": "euler", "scheduler": "normal", "seed": 565855587383452, "steps": 20, "width": 512}
---

# 图片生成/文生图/SD1.5官方文生图工作流_1989688004904185857.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SD1.5官方文生图工作流_1989688004904185857.json`

## 结构

**节点**（7 个）：
- `CLIPTextEncode`
- `KSampler`
- `VAEDecode`
- `SaveImage`
- `EmptyLatentImage`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `8`
- `checkpoint` = `v1-5-pruned-emaonly.ckpt`
- `denoise` = `1`
- `height` = `512`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `seed` = `565855587383452`
- `steps` = `20`
- `width` = `512`

## 知识

覆盖率 **100%**（7/7）

**有卡**：`CLIPTextEncode`、`KSampler`、`VAEDecode`、`SaveImage`、`EmptyLatentImage`、`CheckpointLoaderSimple`
