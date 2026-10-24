---
key: 图片生成/图生图/Qwen-Image-ControlNet-Inpainting支持_1966168675248148482.json
name: Qwen-Image-ControlNet-Inpainting支持_1966168675248148482
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-ControlNet-Inpainting支持_1966168675248148482.json
hash: 2c47ec818a0864e0
coverage: 0.947368
learned_at: 2026-10-23 11:16:34
nodes: [VAELoader, UNETLoader, LoraLoaderModelOnly, CLIPTextEncode, ModelSamplingAuraFlow, ImageScaleToTotalPixels, VAEEncode, SaveImage, SaveImage, Image Comparer (rgthree), CLIPTextEncode, LoadImage, CLIPLoader, ImageAndMaskPreview, ControlNetLoader, ControlNetInpaintingAliMamaApply, KSampler, VAEDecode, ImageConcanate]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 266908390130552, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen-Image-ControlNet-Inpainting支持_1966168675248148482.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-ControlNet-Inpainting支持_1966168675248148482.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（19 个）：
- `VAELoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `SaveImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `CLIPTextEncode` ★核心
- `LoadImage`
- `CLIPLoader`
- `ImageAndMaskPreview`
- `ControlNetLoader`
- `ControlNetInpaintingAliMamaApply`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `ImageConcanate`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `266908390130552`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（18/19）

**有卡**：`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`ModelSamplingAuraFlow`、`ImageScaleToTotalPixels`、`VAEEncode`、`SaveImage`、`LoadImage`、`CLIPLoader`、`ImageAndMaskPreview`、`ControlNetLoader`、`ControlNetInpaintingAliMamaApply`、`KSampler`、`VAEDecode`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
