---
key: 图片生成/文生图/多个lor测试工作流(SD1.5-XL) (1)_2024321140805607426.json
name: 多个lor测试工作流(SD1.5-XL) (1)_2024321140805607426
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/多个lor测试工作流(SD1.5-XL) (1)_2024321140805607426.json
hash: becaa43bd30c335d
coverage: 0.870968
learned_at: 2026-10-19 22:30:29
nodes: [easy anythingIndexSwitch, Lora Loader, CLIPSetLastLayer, Lora Loader, Lora Loader, SomethingToString, VAEDecode, easy forLoopEnd, easy forLoopStart, PreviewImage, ImageListToImageBatch, SaveImage, CR Image Grid Panel, Note, easy rangeFloat, Note, easy showAnything, easy anythingIndexSwitch, easy batchAnything, CR Text Concatenate, AddLabel, ImageListToImageBatch, CR Image Grid Panel, SaveImage, CLIPTextEncode, CheckpointLoaderSimple, Lora Loader, Lora Loader, KSampler, EmptyLatentImage, CLIPTextEncode]
patterns: [text_to_image]
missing: []
parameters: {"batch_size": 1, "cfg": 7, "checkpoint": "WAI_realistic_2.5D_NSFW-illustrious-SDXL_v16_v2.safetensors", "denoise": 1, "height": 1536, "sampler_name": "euler_ancestral", "scheduler": "simple", "seed": 858640296934707, "steps": 28, "width": 1024}
---

# 图片生成/文生图/多个lor测试工作流(SD1.5-XL) (1)_2024321140805607426.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/多个lor测试工作流(SD1.5-XL) (1)_2024321140805607426.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `easy anythingIndexSwitch`
- `Lora Loader`
- `CLIPSetLastLayer`
- `Lora Loader`
- `Lora Loader`
- `SomethingToString`
- `VAEDecode` ★核心
- `easy forLoopEnd`
- `easy forLoopStart`
- `PreviewImage`
- `ImageListToImageBatch`
- `SaveImage`
- `CR Image Grid Panel`
- `Note`
- `easy rangeFloat`
- `Note`
- `easy showAnything`
- `easy anythingIndexSwitch`
- `easy batchAnything`
- `CR Text Concatenate`
- `AddLabel`
- `ImageListToImageBatch`
- `CR Image Grid Panel`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `CheckpointLoaderSimple` ★核心
- `Lora Loader`
- `Lora Loader`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `checkpoint` = `WAI_realistic_2.5D_NSFW-illustrious-SDXL_v16_v2.safetensors`
- `seed` = `858640296934707`
- `steps` = `28`
- `cfg` = `7`
- `sampler_name` = `euler_ancestral`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（27/31）

**有卡**：`easy anythingIndexSwitch`、`Lora Loader`、`CLIPSetLastLayer`、`SomethingToString`、`VAEDecode`、`easy forLoopEnd`、`easy forLoopStart`、`ImageListToImageBatch`、`SaveImage`、`CR Image Grid Panel`、`easy rangeFloat`、`easy batchAnything`、`CR Text Concatenate`、`AddLabel`、`CLIPTextEncode`、`CheckpointLoaderSimple`、`KSampler`、`EmptyLatentImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、CLIPTextEncode、EmptyLatentImage、Lora Loader、Lora Loader、CLIPSetLastLayer
