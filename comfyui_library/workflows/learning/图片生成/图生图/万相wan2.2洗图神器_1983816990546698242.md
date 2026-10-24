---
key: 图片生成/图生图/万相wan2.2洗图神器_1983816990546698242.json
name: 万相wan2.2洗图神器_1983816990546698242
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/万相wan2.2洗图神器_1983816990546698242.json
hash: 87a1f7ab0ffa0e27
coverage: 0.913043
learned_at: 2026-10-23 12:01:16
nodes: [LoraLoaderModelOnly, Image Comparer (rgthree), CR Text Concatenate, ImageScaleToTotalPixels, CLIPLoader, easy showAnything, CLIPTextEncode, VAELoader, CLIPTextEncode, Florence2Run, Florence2ModelLoader, LoraLoaderModelOnly, SaveImage, UNETLoader, ModelSamplingSD3, KSampler, VAEEncode, UpscaleModelLoader, SaveImage, VAEDecode, ImageUpscaleWithModel, MuyeTextEditOutput, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 0.20000000000000004, "sampler_name": "euler", "scheduler": "beta", "seed": 661271709140896, "steps": 7}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/万相wan2.2洗图神器_1983816990546698242.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/万相wan2.2洗图神器_1983816990546698242.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `LoraLoaderModelOnly` ★核心
- `Image Comparer (rgthree)`
- `CR Text Concatenate`
- `ImageScaleToTotalPixels`
- `CLIPLoader`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPTextEncode` ★核心
- `Florence2Run`
- `Florence2ModelLoader`
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `ModelSamplingSD3`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `UpscaleModelLoader`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageUpscaleWithModel`
- `MuyeTextEditOutput`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `661271709140896`
- `steps` = `7`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `beta`
- `denoise` = `0.20000000000000004`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`LoraLoaderModelOnly`、`CR Text Concatenate`、`ImageScaleToTotalPixels`、`CLIPLoader`、`CLIPTextEncode`、`VAELoader`、`Florence2Run`、`Florence2ModelLoader`、`SaveImage`、`UNETLoader`、`ModelSamplingSD3`、`KSampler`、`VAEEncode`、`UpscaleModelLoader`、`VAEDecode`、`ImageUpscaleWithModel`、`MuyeTextEditOutput`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
