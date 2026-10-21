---
key: 图片生成/文生图/Krea2-turbo-White_Marble-AlO_V1_BF 16模型文生图_2093507555816468481.json
name: Krea2-turbo-White_Marble-AlO_V1_BF 16模型文生图_2093507555816468481
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Krea2-turbo-White_Marble-AlO_V1_BF 16模型文生图_2093507555816468481.json
hash: 95454c3e7fb358a9
coverage: 1
learned_at: 2026-10-20 01:18:55
nodes: [CLIPTextEncode, EmptyLatentImage, CheckpointLoaderSimple, VAEDecode, SaveImage, KSampler, CLIPTextEncode, CheckpointLoaderSimple]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": null, "denoise": 1, "height": 640, "sampler_name": "euler", "scheduler": "simple", "seed": 194174390856079, "steps": 20, "width": 480}
---

# 图片生成/文生图/Krea2-turbo-White_Marble-AlO_V1_BF 16模型文生图_2093507555816468481.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Krea2-turbo-White_Marble-AlO_V1_BF 16模型文生图_2093507555816468481.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output

**节点**（8 个）：
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `480`
- `height` = `640`
- `batch_size` = `1`
- `checkpoint` = `None`
- `seed` = `194174390856079`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **100%**（8/8）

**有卡**：`CLIPTextEncode`、`EmptyLatentImage`、`CheckpointLoaderSimple`、`VAEDecode`、`SaveImage`、`KSampler`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、SaveImage、sd15-t2i-basic、sd15-t2i-lora
