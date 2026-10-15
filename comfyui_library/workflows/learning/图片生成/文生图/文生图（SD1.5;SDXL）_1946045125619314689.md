---
key: 图片生成/文生图/文生图（SD1.5;SDXL）_1946045125619314689.json
name: 文生图（SD1.5;SDXL）_1946045125619314689
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图（SD1.5;SDXL）_1946045125619314689.json
hash: 666eb0a73bee39fd
coverage: 0.777778
learned_at: 2026-10-10 20:59:49
nodes: [VAEDecode, CLIPTextEncode, Note, CLIPTextEncode, Note, CheckpointLoaderSimple, EmptyLatentImage, SaveImage, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "XL真人写实摄影_V1.safetensors", "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 334203732458272, "steps": 29, "width": 1024}
---

# 图片生成/文生图/文生图（SD1.5;SDXL）_1946045125619314689.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/文生图（SD1.5;SDXL）_1946045125619314689.json`

## 结构

**节点**（9 个）：
- `VAEDecode`
- `CLIPTextEncode`
- `Note`
- `CLIPTextEncode`
- `Note`
- `CheckpointLoaderSimple`
- `EmptyLatentImage`
- `SaveImage`
- `KSampler`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `8`
- `checkpoint` = `XL真人写实摄影_V1.safetensors`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `seed` = `334203732458272`
- `steps` = `29`
- `width` = `1024`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`Note`、`CheckpointLoaderSimple`、`EmptyLatentImage`
