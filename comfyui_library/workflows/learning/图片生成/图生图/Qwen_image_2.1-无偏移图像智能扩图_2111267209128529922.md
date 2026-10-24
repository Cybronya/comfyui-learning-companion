---
key: 图片生成/图生图/Qwen_image_2.1-无偏移图像智能扩图_2111267209128529922.json
name: Qwen_image_2.1-无偏移图像智能扩图_2111267209128529922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1-无偏移图像智能扩图_2111267209128529922.json
hash: 40a577fe89b8e649
coverage: 0.8
learned_at: 2026-10-23 11:21:27
nodes: [QwenImage21Cache, Seed (rgthree), UNETLoader, Image Comparer (rgthree), VAEDecode, KSampler, CLIPLoader, PreviewImage, TextEncodeQwenImage21, DrawMaskOnImage, LoadImage, ImageScaleToTotalPixels, ImageScaleToTotalPixels, VAELoader, PreviewImage, ImagePadForOutpaint, LoraLoaderModelOnly, SaveImage, EmptyImage, PreviewImage]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 355732091438417, "steps": 30}
---

# 图片生成/图生图/Qwen_image_2.1-无偏移图像智能扩图_2111267209128529922.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1-无偏移图像智能扩图_2111267209128529922.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `QwenImage21Cache`
- `Seed (rgthree)`
- `UNETLoader` ★核心
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `CLIPLoader`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `DrawMaskOnImage`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `VAELoader`
- `PreviewImage`
- `ImagePadForOutpaint`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `EmptyImage`
- `PreviewImage`

## 关键参数

- `seed` = `355732091438417`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（16/20）

**有卡**：`QwenImage21Cache`、`Seed (rgthree)`、`UNETLoader`、`VAEDecode`、`KSampler`、`CLIPLoader`、`TextEncodeQwenImage21`、`DrawMaskOnImage`、`LoadImage`、`ImageScaleToTotalPixels`、`VAELoader`、`ImagePadForOutpaint`、`LoraLoaderModelOnly`、`SaveImage`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
