---
key: 图片生成/图生图/Qwen-Image-Edit-Rapid-AIO_2091382579567087618.json
name: Qwen-Image-Edit-Rapid-AIO_2091382579567087618
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit-Rapid-AIO_2091382579567087618.json
hash: 0ad2084dcda41452
coverage: 1
learned_at: 2026-10-23 11:16:59
nodes: [TextEncodeQwenImageEditPlus, VAEEncode, LoadImage, LoadImage, TextEncodeQwenImageEditPlus, ImageScaleToTotalPixels, KSampler, LoadImage, CheckpointLoaderSimple, VAEDecode, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 8, "checkpoint": "Qwen-Rapid-AIO-NSFW-v17.safetensors", "denoise": 1, "sampler_name": "euler_ancestral", "scheduler": "beta", "seed": 661204298260176, "steps": 20}
---

# 图片生成/图生图/Qwen-Image-Edit-Rapid-AIO_2091382579567087618.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-Edit-Rapid-AIO_2091382579567087618.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（11 个）：
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImageEditPlus`
- `ImageScaleToTotalPixels`
- `KSampler` ★核心
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `VAEDecode` ★核心
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `661204298260176`
- `steps` = `20`
- `cfg` = `8`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-NSFW-v17.safetensors`

## 知识

覆盖率 **100%**（11/11）

**有卡**：`TextEncodeQwenImageEditPlus`、`VAEEncode`、`LoadImage`、`ImageScaleToTotalPixels`、`KSampler`、`CheckpointLoaderSimple`、`VAEDecode`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、LoadImage、TextEncodeQwenImageEditPlus、VAEEncode、SaveImage、ImageScaleToTotalPixels
