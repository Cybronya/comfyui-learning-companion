---
key: 图片生成/图生图/lor测试工作流(SD1.5-XL)_2024319167456878594.json
name: lor测试工作流(SD1.5-XL)_2024319167456878594
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/lor测试工作流(SD1.5-XL)_2024319167456878594.json
hash: 81519775550896ac
coverage: 0.875
learned_at: 2026-10-23 11:40:55
nodes: [VAEDecode, ImageListToBatch+, CR Image Grid Panel, easy showAnything, CLIPTextEncode, AddLabel, Note, FloatRange //Inspire, CLIPSetLastLayer, SomethingToString, LoraLoaderModelOnly, EmptyLatentImage, KSampler, SaveImage, CheckpointLoaderSimple, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "WAI_realistic_2.5D_NSFW-illustrious-SDXL_v16_v2.safetensors", "denoise": 1, "height": 1536, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 858640296934706, "steps": 28, "width": 1024}
---

# 图片生成/图生图/lor测试工作流(SD1.5-XL)_2024319167456878594.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/lor测试工作流(SD1.5-XL)_2024319167456878594.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `VAEDecode` ★核心
- `ImageListToBatch+`
- `CR Image Grid Panel`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `AddLabel`
- `Note`
- `FloatRange //Inspire`
- `CLIPSetLastLayer`
- `SomethingToString`
- `LoraLoaderModelOnly` ★核心
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `SaveImage`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `858640296934706`
- `steps` = `28`
- `cfg` = `7`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`
- `checkpoint` = `WAI_realistic_2.5D_NSFW-illustrious-SDXL_v16_v2.safetensors`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`VAEDecode`、`ImageListToBatch+`、`CR Image Grid Panel`、`CLIPTextEncode`、`AddLabel`、`FloatRange //Inspire`、`CLIPSetLastLayer`、`SomethingToString`、`LoraLoaderModelOnly`、`EmptyLatentImage`、`KSampler`、`SaveImage`、`CheckpointLoaderSimple`

**用到的条目**：KSampler、VAEDecode、LoraLoaderModelOnly、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、CLIPSetLastLayer、SaveImage
