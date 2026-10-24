---
key: 图片生成/图生图/SD1.5图生图+Canny真人转动漫_1927539264094113794.json
name: SD1.5图生图+Canny真人转动漫_1927539264094113794
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5图生图+Canny真人转动漫_1927539264094113794.json
hash: a10fd994e69540cf
coverage: 0.882353
learned_at: 2026-10-23 11:23:35
nodes: [SaveImage, ImageConcanate, VAEDecode, PreviewImage, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ClipInterrogator, CR Apply ControlNet, CLIPTextEncode, ConditioningZeroOut, EmptyLatentImage, ControlNetLoader, LoadImage, AIO_Preprocessor, CheckpointLoaderSimple, KSampler]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "漫画 Outline Color勾线彩画凤_1.0.safetensors", "denoise": 1, "height": 1536, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 625510290306179, "steps": 25, "width": 1024}
---

# 图片生成/图生图/SD1.5图生图+Canny真人转动漫_1927539264094113794.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5图生图+Canny真人转动漫_1927539264094113794.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（17 个）：
- `SaveImage`
- `ImageConcanate`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ClipInterrogator`
- `CR Apply ControlNet`
- `CLIPTextEncode` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `ControlNetLoader`
- `LoadImage`
- `AIO_Preprocessor`
- `CheckpointLoaderSimple` ★核心
- `KSampler` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `checkpoint` = `漫画 Outline Color勾线彩画凤_1.0.safetensors`
- `seed` = `625510290306179`
- `steps` = `25`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`SaveImage`、`ImageConcanate`、`VAEDecode`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`ClipInterrogator`、`CR Apply ControlNet`、`CLIPTextEncode`、`ConditioningZeroOut`、`EmptyLatentImage`、`ControlNetLoader`、`LoadImage`、`AIO_Preprocessor`、`CheckpointLoaderSimple`、`KSampler`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LoadImage
