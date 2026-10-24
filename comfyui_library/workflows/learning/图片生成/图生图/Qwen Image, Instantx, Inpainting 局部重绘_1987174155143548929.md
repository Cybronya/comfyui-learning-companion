---
key: 图片生成/图生图/Qwen Image, Instantx, Inpainting 局部重绘_1987174155143548929.json
name: Qwen Image, Instantx, Inpainting 局部重绘_1987174155143548929
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image, Instantx, Inpainting 局部重绘_1987174155143548929.json
hash: 6b43fa51ae9a0e5d
coverage: 0.913043
learned_at: 2026-10-23 11:13:29
nodes: [VAELoader, ModelSamplingAuraFlow, CLIPTextEncode, CLIPLoader, PreviewImage, SetLatentNoiseMask, VAEEncode, SaveImage, KSampler, ImageConcanate, SaveImage, CLIPTextEncode, VAEDecode, GrowMask, UNETLoader, LoraLoaderModelOnly, ControlNetInpaintingAliMamaApply, ControlNetLoader, LoadImage, MaskPreview, ImageCompositeMasked, Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 888888, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen Image, Instantx, Inpainting 局部重绘_1987174155143548929.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image, Instantx, Inpainting 局部重绘_1987174155143548929.json`

## 结构

**生成流程**：Model → Encode → Condition → Control → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `PreviewImage`
- `SetLatentNoiseMask`
- `VAEEncode` ★核心
- `SaveImage`
- `KSampler` ★核心
- `ImageConcanate`
- `SaveImage`
- `CLIPTextEncode` ★核心
- `VAEDecode` ★核心
- `GrowMask`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `ControlNetInpaintingAliMamaApply`
- `ControlNetLoader`
- `LoadImage`
- `MaskPreview`
- `ImageCompositeMasked`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `888888`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **91%**（21/23）

**有卡**：`VAELoader`、`ModelSamplingAuraFlow`、`CLIPTextEncode`、`CLIPLoader`、`SetLatentNoiseMask`、`VAEEncode`、`SaveImage`、`KSampler`、`ImageConcanate`、`VAEDecode`、`GrowMask`、`UNETLoader`、`LoraLoaderModelOnly`、`ControlNetInpaintingAliMamaApply`、`ControlNetLoader`、`LoadImage`、`MaskPreview`、`ImageCompositeMasked`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
