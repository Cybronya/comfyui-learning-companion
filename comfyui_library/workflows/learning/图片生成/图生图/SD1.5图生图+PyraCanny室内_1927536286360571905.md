---
key: 图片生成/图生图/SD1.5图生图+PyraCanny室内_1927536286360571905.json
name: SD1.5图生图+PyraCanny室内_1927536286360571905
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5图生图+PyraCanny室内_1927536286360571905.json
hash: 21f48d0ee31922e3
coverage: 0.882353
learned_at: 2026-10-23 11:23:37
nodes: [SaveImage, ImageConcanate, VAEDecode, PreviewImage, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, KSampler, PreviewImage, ClipInterrogator, CR Apply ControlNet, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ControlNetLoader, CheckpointLoaderSimple, LoadImage, AIO_Preprocessor]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "SD1.5-灵动水彩_v1.0.safetensors", "denoise": 1, "height": 1536, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 120131342708899, "steps": 30, "width": 1024}
---

# 图片生成/图生图/SD1.5图生图+PyraCanny室内_1927536286360571905.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5图生图+PyraCanny室内_1927536286360571905.json`

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
- `ControlNetLoader`
- `CheckpointLoaderSimple` ★核心
- `LoadImage`
- `AIO_Preprocessor`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `120131342708899`
- `steps` = `30`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `checkpoint` = `SD1.5-灵动水彩_v1.0.safetensors`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`SaveImage`、`ImageConcanate`、`VAEDecode`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`KSampler`、`ClipInterrogator`、`CR Apply ControlNet`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyLatentImage`、`ControlNetLoader`、`CheckpointLoaderSimple`、`LoadImage`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
