---
key: 图片生成/图生图/SD1.5图生图+DW+自动翻译负面提示词-真人转动漫_1927174469725618177.json
name: SD1.5图生图+DW+自动翻译负面提示词-真人转动漫_1927174469725618177
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/SD1.5图生图+DW+自动翻译负面提示词-真人转动漫_1927174469725618177.json
hash: 4ef7dea5cd9933b6
coverage: 0.894737
learned_at: 2026-10-23 11:23:36
nodes: [SaveImage, ImageConcanate, VAEDecode, PreviewImage, LoraLoaderModelOnly, LayerUtility: ImageScaleByAspectRatio V2, ControlNetLoader, VAELoader, KSampler, PreviewImage, EmptyLatentImage, ClipInterrogator, CR Apply ControlNet, CLIPTextEncode, CLIPTextEncode, LoadImage, CheckpointLoaderSimple, DeepTranslatorTextNode, AIO_Preprocessor]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "awpainting_v14.safetensors", "denoise": 1, "height": 1536, "sampler_name": "dpmpp_2m", "scheduler": "karras", "seed": 905127368398077, "steps": 30, "width": 1024}
---

# 图片生成/图生图/SD1.5图生图+DW+自动翻译负面提示词-真人转动漫_1927174469725618177.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/SD1.5图生图+DW+自动翻译负面提示词-真人转动漫_1927174469725618177.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `SaveImage`
- `ImageConcanate`
- `VAEDecode` ★核心
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ControlNetLoader`
- `VAELoader`
- `KSampler` ★核心
- `PreviewImage`
- `EmptyLatentImage` ★核心
- `ClipInterrogator`
- `CR Apply ControlNet`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CheckpointLoaderSimple` ★核心
- `DeepTranslatorTextNode`
- `AIO_Preprocessor`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `905127368398077`
- `steps` = `30`
- `cfg` = `7`
- `sampler_name` = `dpmpp_2m`
- `scheduler` = `karras`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `checkpoint` = `awpainting_v14.safetensors`

## 知识

覆盖率 **89%**（17/19）

**有卡**：`SaveImage`、`ImageConcanate`、`VAEDecode`、`LoraLoaderModelOnly`、`LayerUtility: ImageScaleByAspectRatio V2`、`ControlNetLoader`、`VAELoader`、`KSampler`、`EmptyLatentImage`、`ClipInterrogator`、`CR Apply ControlNet`、`CLIPTextEncode`、`LoadImage`、`CheckpointLoaderSimple`、`DeepTranslatorTextNode`、`AIO_Preprocessor`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、LoadImage
