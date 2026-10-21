---
key: 图片生成/图生图/Qwen_Image_2.1_PE模特换装超清放大版，图生图高清画质提升工作流_2105518053244096514.json
name: Qwen_Image_2.1_PE模特换装超清放大版，图生图高清画质提升工作流_2105518053244096514
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1_PE模特换装超清放大版，图生图高清画质提升工作流_2105518053244096514.json
hash: b684d6de007400a0
coverage: 0.872727
learned_at: 2026-10-21 00:43:56
nodes: [CLIPLoader, LoadImage, LoadImage, LoadImage, LoadImage, QwenPERewriteT8, QwenImage21Cache, UNETLoader, ComfySwitchNode, TextEncodeQwenImage21, VAELoader, LoadImage, LoadImage, MuyeTextEditOutput, ImageScaleToTotalPixels, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, PreviewImage, SeedVR2LoadDiTModel, VAEDecode, EmptyLatentImage, Any Switch (rgthree), SaveImage, KSampler, Image Comparer (rgthree), Int, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, EmptyImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen_Image_2.1_PE模特换装超清放大版，图生图高清画质提升工作流_2105518053244096514.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1_PE模特换装超清放大版，图生图高清画质提升工作流_2105518053244096514.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（55 个）：
- `CLIPLoader`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `QwenPERewriteT8`
- `QwenImage21Cache`
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `MuyeTextEditOutput`
- `ImageScaleToTotalPixels`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `Any Switch (rgthree)`
- `SaveImage`
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `Int`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`
- `EmptyImage`
- `PreviewImage`

**识别到的模式**：text_to_image

## 关键参数

- `width` = `80`
- `height` = `80`
- `batch_size` = `1`
- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`

## 知识

覆盖率 **87%**（48/55）

**有卡**：`CLIPLoader`、`LoadImage`、`QwenPERewriteT8`、`QwenImage21Cache`、`UNETLoader`、`TextEncodeQwenImage21`、`VAELoader`、`MuyeTextEditOutput`、`ImageScaleToTotalPixels`、`SeedVR2LoadVAEModel`、`SeedVR2VideoUpscaler`、`SeedVR2LoadDiTModel`、`VAEDecode`、`EmptyLatentImage`、`SaveImage`、`KSampler`、`Int`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`EmptyImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
