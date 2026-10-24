---
key: 图片生成/图生图/SD1.5图生图+open pose真人转动漫_1927161870132662273.json
name: SD1.5图生图+open pose真人转动漫_1927161870132662273
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5图生图+open pose真人转动漫_1927161870132662273.json
hash: 75bae0f2ee9a752b
coverage: 0.888889
learned_at: 2026-10-23 11:23:41
nodes: [ConditioningZeroOut, CLIPTextEncode, EmptyLatentImage, SaveImage, ImageConcanate, VAEDecode, PreviewImage, ClipInterrogator, CR Apply ControlNet, PreviewImage, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, ControlNetLoader, VAELoader, LoadImage, AIO_Preprocessor, KSampler, CheckpointLoaderSimple]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "ComicTrainee丨动漫插画模型_v2.0.safetensors", "denoise": 1, "height": 1536, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 157113972219196, "steps": 30, "width": 1024}
---

# 图片生成/图生图/SD1.5图生图+open pose真人转动漫_1927161870132662273.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5图生图+open pose真人转动漫_1927161870132662273.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `EmptyLatentImage` ★核心
- `SaveImage`
- `ImageConcanate`
- `VAEDecode` ★核心
- `PreviewImage`
- `ClipInterrogator`
- `CR Apply ControlNet`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ControlNetLoader`
- `VAELoader`
- `LoadImage`
- `AIO_Preprocessor`
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `157113972219196`
- `steps` = `30`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `ComicTrainee丨动漫插画模型_v2.0.safetensors`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`EmptyLatentImage`、`SaveImage`、`ImageConcanate`、`VAEDecode`、`ClipInterrogator`、`CR Apply ControlNet`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`ControlNetLoader`、`VAELoader`、`LoadImage`、`AIO_Preprocessor`、`KSampler`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
