---
key: Qwen-Image-Edit-Rapid-AIO-图像编辑_1977650991560577025.json
name: Qwen-Image-Edit-Rapid-AIO-图像编辑_1977650991560577025
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-Edit-Rapid-AIO-图像编辑_1977650991560577025.json
hash: 9586963085ff1350
coverage: 0.9
learned_at: 2026-10-10 20:59:00
nodes: [ImageScaleToTotalPixels, VAEEncode, KSampler, PreviewImage, TextEncodeQwenImageEditPlus, CheckpointLoaderSimple, TextEncodeQwenImageEditPlus, VAEDecode, SaveImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "checkpoint": "Qwen-Rapid-AIO-v3.safetensors", "denoise": 1, "sampler_name": "sa_solver", "scheduler": "beta", "seed": 65454653, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# Qwen-Image-Edit-Rapid-AIO-图像编辑_1977650991560577025.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-Edit-Rapid-AIO-图像编辑_1977650991560577025.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（10 个）：
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `KSampler` ★核心
- `PreviewImage`
- `TextEncodeQwenImageEditPlus`
- `CheckpointLoaderSimple` ★核心
- `TextEncodeQwenImageEditPlus`
- `VAEDecode` ★核心
- `SaveImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `65454653`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `sa_solver`
- `scheduler` = `beta`
- `denoise` = `1`
- `checkpoint` = `Qwen-Rapid-AIO-v3.safetensors`

## 知识

覆盖率 **90%**（9/10）

**有卡**：`ImageScaleToTotalPixels`、`VAEEncode`、`KSampler`、`TextEncodeQwenImageEditPlus`、`CheckpointLoaderSimple`、`VAEDecode`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、CheckpointLoaderSimple、LoadImage、TextEncodeQwenImageEditPlus、VAEEncode、SaveImage、ImageScaleToTotalPixels

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
