---
key: 图片生成/文生图/Wan2.2 Magic Wan Image文生图_1970727639172476929.json
name: Wan2.2 Magic Wan Image文生图_1970727639172476929
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Wan2.2 Magic Wan Image文生图_1970727639172476929.json
hash: 95541b6573737770
coverage: 0.916667
learned_at: 2026-10-10 20:59:13
nodes: [ModelSamplingSD3, EmptyLatentImage, CLIPLoader, KSampler, VAEDecode, CLIPTextEncode, CLIPTextEncode, VAELoader, UNETLoader, SaveImage, PrimitiveStringMultiline, FluxResolutionNode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 3, "denoise": 1, "height": 1376, "sampler_name": "deis", "scheduler": "simple", "seed": 217555667952032, "steps": 30, "width": 768}
---

# 图片生成/文生图/Wan2.2 Magic Wan Image文生图_1970727639172476929.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Wan2.2 Magic Wan Image文生图_1970727639172476929.json`

## 结构

**节点**（12 个）：
- `ModelSamplingSD3`
- `EmptyLatentImage`
- `CLIPLoader`
- `KSampler`
- `VAEDecode`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `VAELoader`
- `UNETLoader`
- `SaveImage`
- `PrimitiveStringMultiline`
- `FluxResolutionNode`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `3`
- `denoise` = `1`
- `height` = `1376`
- `sampler_name` = `deis`
- `scheduler` = `simple`
- `seed` = `217555667952032`
- `steps` = `30`
- `width` = `768`

## 知识

覆盖率 **92%**（11/12）

**有卡**：`ModelSamplingSD3`、`EmptyLatentImage`、`CLIPLoader`、`KSampler`、`VAEDecode`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`SaveImage`、`PrimitiveStringMultiline`
