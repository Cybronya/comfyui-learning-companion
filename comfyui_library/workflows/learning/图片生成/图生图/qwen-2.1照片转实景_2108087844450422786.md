---
key: 图片生成/图生图/qwen-2.1照片转实景_2108087844450422786.json
name: qwen-2.1照片转实景_2108087844450422786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-2.1照片转实景_2108087844450422786.json
hash: da44a783e7fb4e25
coverage: 0.9375
learned_at: 2026-10-21 00:46:05
nodes: [XinbaoImageStandardizer, TextEncodeQwenImage21, KSampler, EmptyLatentImage, GetImageSize, SaveImage, VAEDecode, ImageConcatMulti, CR Text, Image Comparer (rgthree), SaveImage, UNETLoader, LoraLoaderModelOnly, CLIPLoader, VAELoader, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 2048, "sampler_name": "euler", "scheduler": "simple", "seed": 347361276400062, "steps": 25, "width": 1088}
---

# 图片生成/图生图/qwen-2.1照片转实景_2108087844450422786.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-2.1照片转实景_2108087844450422786.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（16 个）：
- `XinbaoImageStandardizer`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `GetImageSize`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `CR Text`
- `Image Comparer (rgthree)`
- `SaveImage`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `LoadImage`

## 关键参数

- `seed` = `347361276400062`
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

**有卡**：`XinbaoImageStandardizer`、`TextEncodeQwenImage21`、`KSampler`、`EmptyLatentImage`、`GetImageSize`、`SaveImage`、`VAEDecode`、`ImageConcatMulti`、`CR Text`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`VAELoader`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage
