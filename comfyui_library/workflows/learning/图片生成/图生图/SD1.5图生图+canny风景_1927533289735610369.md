---
key: 图片生成/图生图/SD1.5图生图+canny风景_1927533289735610369.json
name: SD1.5图生图+canny风景_1927533289735610369
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5图生图+canny风景_1927533289735610369.json
hash: eda8c68bcc89d1c9
coverage: 0.882353
learned_at: 2026-10-23 11:23:40
nodes: [SaveImage, ImageConcanate, VAEDecode, PreviewImage, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, KSampler, PreviewImage, ClipInterrogator, CR Apply ControlNet, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, AIO_Preprocessor, ControlNetLoader, LoadImage, CheckpointLoaderSimple]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "漫画 Outline Color勾线彩画凤_1.0.safetensors", "denoise": 1, "height": 1536, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 481847222202563, "steps": 30, "width": 1024}
---

# 图片生成/图生图/SD1.5图生图+canny风景_1927533289735610369.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5图生图+canny风景_1927533289735610369.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `SaveImage`
- `ImageConcanate`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `KSampler` ★核心
- `PreviewImage`
- `ClipInterrogator`
- `CR Apply ControlNet`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `AIO_Preprocessor`
- `ControlNetLoader`
- `LoadImage`
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `481847222202563`
- `steps` = `30`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `checkpoint` = `漫画 Outline Color勾线彩画凤_1.0.safetensors`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`SaveImage`、`ImageConcanate`、`VAEDecode`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`ClipInterrogator`、`CR Apply ControlNet`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyLatentImage`、`AIO_Preprocessor`、`ControlNetLoader`、`LoadImage`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
