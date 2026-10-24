---
key: 图片生成/图生图/SD1.5图生图+TTPlanet-TileGF增加细节_1927181782981181442.json
name: SD1.5图生图+TTPlanet-TileGF增加细节_1927181782981181442
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5图生图+TTPlanet-TileGF增加细节_1927181782981181442.json
hash: 3ae8435c1880c089
coverage: 0.888889
learned_at: 2026-10-23 11:23:38
nodes: [SaveImage, ImageConcanate, VAEDecode, PreviewImage, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, VAELoader, KSampler, PreviewImage, ClipInterrogator, CR Apply ControlNet, ControlNetLoader, CLIPTextEncode, LoadImage, CheckpointLoaderSimple, ConditioningZeroOut, EmptyLatentImage, AIO_Preprocessor]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "基础算法 V1.5_v 1.5.safetensors", "denoise": 1, "height": 1536, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 394298004604879, "steps": 30, "width": 1024}
---

# 图片生成/图生图/SD1.5图生图+TTPlanet-TileGF增加细节_1927181782981181442.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5图生图+TTPlanet-TileGF增加细节_1927181782981181442.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `SaveImage`
- `ImageConcanate`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAELoader`
- `KSampler` ★核心
- `PreviewImage`
- `ClipInterrogator`
- `CR Apply ControlNet`
- `ControlNetLoader`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `ConditioningZeroOut`
- `EmptyLatentImage` ★核心
- `AIO_Preprocessor`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `394298004604879`
- `steps` = `30`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `checkpoint` = `基础算法 V1.5_v 1.5.safetensors`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`SaveImage`、`ImageConcanate`、`VAEDecode`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAELoader`、`KSampler`、`ClipInterrogator`、`CR Apply ControlNet`、`ControlNetLoader`、`CLIPTextEncode`、`LoadImage`、`CheckpointLoaderSimple`、`ConditioningZeroOut`、`EmptyLatentImage`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage
