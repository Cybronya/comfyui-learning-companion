---
key: SDMAI写实1.5大模型 realistic model V3.0 (早期1.5大模型体验工作流）_1954187211258392578.json
name: SDMAI写实1.5大模型 realistic model V3.0 (早期1.5大模型体验工作流）_1954187211258392578
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/SDMAI写实1.5大模型 realistic model V3.0 (早期1.5大模型体验工作流）_1954187211258392578.json
hash: 03bb79f4034da2a8
coverage: 1
learned_at: 2026-10-10 20:59:10
nodes: [CheckpointLoaderSimple, ImageScaleBy, VAEEncode, EmptyLatentImage, VAEDecode, VAEDecode, CLIPTextEncode, KSampler, SaveImage, KSampler, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 8, "checkpoint": "SDMAI写实realistic model_v3.0.safetensors", "denoise": 0.6000000000000001, "height": 768, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 1004806193718047, "steps": 20, "width": 512}
---

# SDMAI写实1.5大模型 realistic model V3.0 (早期1.5大模型体验工作流）_1954187211258392578.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/SDMAI写实1.5大模型 realistic model V3.0 (早期1.5大模型体验工作流）_1954187211258392578.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output

**节点**（11 个）：
- `CheckpointLoaderSimple` ★核心
- `ImageScaleBy`
- `VAEEncode` ★核心
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `KSampler` ★核心
- `SaveImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `SDMAI写实realistic model_v3.0.safetensors`
- `width` = `512`
- `height` = `768`
- `batch_size` = `1`
- `seed` = `1004806193718047`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `0.6000000000000001`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`CheckpointLoaderSimple`、`ImageScaleBy`、`VAEEncode`、`EmptyLatentImage`、`VAEDecode`、`CLIPTextEncode`、`KSampler`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、VAEEncode、SaveImage、ImageScaleBy
