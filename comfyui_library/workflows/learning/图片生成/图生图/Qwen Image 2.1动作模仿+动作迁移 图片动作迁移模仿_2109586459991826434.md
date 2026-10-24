---
key: 图片生成/图生图/Qwen Image 2.1动作模仿+动作迁移 图片动作迁移模仿_2109586459991826434.json
name: Qwen Image 2.1动作模仿+动作迁移 图片动作迁移模仿_2109586459991826434
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1动作模仿+动作迁移 图片动作迁移模仿_2109586459991826434.json
hash: f216a777f3d32ce7
coverage: 0.888889
learned_at: 2026-10-23 11:12:50
nodes: [CLIPLoader, VAELoader, VAEDecode, TextEncodeQwenImage21, JjkText, ImageResizeKJv2, DWPreprocessor, PrimitiveInt, EmptyLatentImage, KSampler, LoraLoaderModelOnly, UNETLoader, LoadImage, SaveImage, ImageStitch, ImageStitch, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 858087407575364, "steps": 30, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1动作模仿+动作迁移 图片动作迁移模仿_2109586459991826434.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1动作模仿+动作迁移 图片动作迁移模仿_2109586459991826434.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `TextEncodeQwenImage21`
- `JjkText`
- `ImageResizeKJv2`
- `DWPreprocessor`
- `PrimitiveInt`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoadImage`
- `SaveImage`
- `ImageStitch`
- `ImageStitch`
- `SaveImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `858087407575364`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **89%**（16/18）

**有卡**：`CLIPLoader`、`VAELoader`、`VAEDecode`、`TextEncodeQwenImage21`、`ImageResizeKJv2`、`DWPreprocessor`、`EmptyLatentImage`、`KSampler`、`LoraLoaderModelOnly`、`UNETLoader`、`LoadImage`、`SaveImage`、`ImageStitch`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage
