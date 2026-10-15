---
key: 图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo｜6步LORA快速出图 文生图图生图双模式_2104020602133762050.json
name: Qwen-Image-2_1-Edit-I2I-Turbo｜6步LORA快速出图 文生图图生图双模式_2104020602133762050
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo｜6步LORA快速出图 文生图图生图双模式_2104020602133762050.json
hash: 2adb6b16a0e43cae
coverage: 0.870968
learned_at: 2026-10-10 20:59:00
nodes: [ResolutionSelector, QwenImage21Cache, UnetLoaderGGUF, Any Switch (rgthree), VAELoader, LoraLoaderModelOnly, CLIPLoader, ImageScaleBy, KSampler, VAEDecode, Image Comparer (rgthree), EmptyLatentImage, ComfySwitchNode, Fast Groups Bypasser (rgthree), UNETLoader, LoadImage, TextEncodeQwenImage21, LoadImage, SaveImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo｜6步LORA快速出图 文生图图生图双模式_2104020602133762050.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo｜6步LORA快速出图 文生图图生图双模式_2104020602133762050.json`

## 结构

**节点**（62 个）：
- `ResolutionSelector`
- `QwenImage21Cache`
- `UnetLoaderGGUF`
- `Any Switch (rgthree)`
- `VAELoader`
- `LoraLoaderModelOnly`
- `CLIPLoader`
- `ImageScaleBy`
- `KSampler`
- `VAEDecode`
- `Image Comparer (rgthree)`
- `EmptyLatentImage`
- `ComfySwitchNode`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader`
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
- `CLIPLoader`
- `CLIPTextEncode`
- `VAELoader`
- `EmptyLatentImage`
- `KSampler`
- `VAEDecode`
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `LoraLoaderModelOnly`
- `CLIPTextEncode`
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `4.5`
- `denoise` = `1`
- `height` = `80`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `seed` = `598626327129635`
- `steps` = `4`
- `width` = `80`

## 知识

覆盖率 **87%**（54/62）

**有卡**：`ResolutionSelector`、`QwenImage21Cache`、`UnetLoaderGGUF`、`Any Switch (rgthree)`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`ImageScaleBy`、`KSampler`、`VAEDecode`、`Image Comparer (rgthree)`、`EmptyLatentImage`、`ComfySwitchNode`、`Fast Groups Bypasser (rgthree)`、`UNETLoader`、`LoadImage`、`TextEncodeQwenImage21`、`SaveImage`、`孤海注释`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`JjkText`

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
