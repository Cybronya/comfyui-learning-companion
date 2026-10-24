---
key: 图片生成/图生图/qwen-2.1 照片转实景摄影 Photo-to-Real-Scene Conversion_2108715825342541826.json
name: qwen-2.1 照片转实景摄影 Photo-to-Real-Scene Conversion_2108715825342541826
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-2.1 照片转实景摄影 Photo-to-Real-Scene Conversion_2108715825342541826.json
hash: f025d6bd1216093e
coverage: 0.9375
learned_at: 2026-10-23 11:42:12
nodes: [XinbaoImageStandardizer, TextEncodeQwenImage21, KSampler, EmptyLatentImage, GetImageSize, VAEDecode, ImageConcatMulti, Image Comparer (rgthree), UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, LoadImage, SaveImage, CR Text, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 896992095249944, "steps": 25, "width": 1088}
---

# 图片生成/图生图/qwen-2.1 照片转实景摄影 Photo-to-Real-Scene Conversion_2108715825342541826.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-2.1 照片转实景摄影 Photo-to-Real-Scene Conversion_2108715825342541826.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `XinbaoImageStandardizer`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `Image Comparer (rgthree)`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`
- `SaveImage`
- `CR Text`
- `SaveImage`

## 关键参数

- `seed` = `896992095249944`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1088`
- `height` = `2048`
- `batch_size` = `1`

## 知识

覆盖率 **94%**（15/16）

**有卡**：`XinbaoImageStandardizer`、`TextEncodeQwenImage21`、`KSampler`、`EmptyLatentImage`、`GetImageSize`、`VAEDecode`、`ImageConcatMulti`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`LoadImage`、`SaveImage`、`CR Text`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage
