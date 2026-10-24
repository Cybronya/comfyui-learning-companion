---
key: 图片生成/图生图/SD1.5图生图+dense pose真人转动漫_1927166776063459329.json
name: SD1.5图生图+dense pose真人转动漫_1927166776063459329
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5图生图+dense pose真人转动漫_1927166776063459329.json
hash: b1580562af375a74
coverage: 0.888889
learned_at: 2026-10-23 11:23:40
nodes: [ConditioningZeroOut, CLIPTextEncode, EmptyLatentImage, SaveImage, ImageConcanate, VAEDecode, PreviewImage, ClipInterrogator, CR Apply ControlNet, PreviewImage, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, ControlNetLoader, VAELoader, KSampler, CheckpointLoaderSimple, AIO_Preprocessor, LoadImage]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "DreamWorld_MIX_梦之境动漫风格大模型_v1.0.safetensors", "denoise": 1, "height": 1536, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 130232415805892, "steps": 30, "width": 1024}
---

# 图片生成/图生图/SD1.5图生图+dense pose真人转动漫_1927166776063459329.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5图生图+dense pose真人转动漫_1927166776063459329.json`

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
- `KSampler` ★核心
- `CheckpointLoaderSimple` ★核心
- `AIO_Preprocessor`
- `LoadImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `130232415805892`
- `steps` = `30`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `DreamWorld_MIX_梦之境动漫风格大模型_v1.0.safetensors`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`ConditioningZeroOut`、`CLIPTextEncode`、`EmptyLatentImage`、`SaveImage`、`ImageConcanate`、`VAEDecode`、`ClipInterrogator`、`CR Apply ControlNet`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`ControlNetLoader`、`VAELoader`、`KSampler`、`CheckpointLoaderSimple`、`AIO_Preprocessor`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
