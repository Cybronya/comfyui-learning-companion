---
key: 图片生成/文生图/文生图（SD1.5;SDXL）_1946045125619314689.json
name: 文生图（SD1.5;SDXL）_1946045125619314689.json
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/文生图（SD1.5;SDXL）_1946045125619314689.json
hash: 666eb0a73bee39fd
coverage: 0.777778
learned_at: 2026-10-07 22:52:43
nodes: [VAEDecode, CLIPTextEncode, Note, CLIPTextEncode, Note, CheckpointLoaderSimple, EmptyLatentImage, SaveImage, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "XL真人写实摄影_V1.safetensors", "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "normal", "seed": 334203732458272, "steps": 29, "width": 1024}
---

# 图片生成/文生图/文生图（SD1.5;SDXL）_1946045125619314689.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/1946045125619314689.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（9 个）：
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `Note`
- `CLIPTextEncode` ★核心
- `Note`
- `CheckpointLoaderSimple` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `XL真人写实摄影_V1.safetensors`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `334203732458272`
- `steps` = `29`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **78%**（7/9）

**有卡**：`VAEDecode`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`EmptyLatentImage`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora
