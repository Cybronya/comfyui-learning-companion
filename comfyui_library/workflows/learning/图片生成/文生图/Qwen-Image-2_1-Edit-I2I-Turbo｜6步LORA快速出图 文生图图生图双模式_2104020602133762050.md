---
key: 图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo｜6步LORA快速出图 文生图图生图双模式_2104020602133762050.json
name: Qwen-Image-2_1-Edit-I2I-Turbo｜6步LORA快速出图 文生图图生图双模式_2104020602133762050
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2_1-Edit-I2I-Turbo｜6步LORA快速出图 文生图图生图双模式_2104020602133762050.json
hash: 2adb6b16a0e43cae
coverage: 0.870968
learned_at: 2026-10-07 02:25:52
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

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `ResolutionSelector`
- `QwenImage21Cache`
- `UnetLoaderGGUF` ★核心
- `Any Switch (rgthree)`
- `VAELoader`
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `ImageScaleBy`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `Fast Groups Bypasser (rgthree)`
- `UNETLoader` ★核心
- `LoadImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `SaveImage`
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
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
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **87%**（54/62）

**有卡**：`ResolutionSelector`、`QwenImage21Cache`、`UnetLoaderGGUF`、`VAELoader`、`LoraLoaderModelOnly`、`CLIPLoader`、`ImageScaleBy`、`KSampler`、`VAEDecode`、`EmptyLatentImage`、`UNETLoader`、`LoadImage`、`TextEncodeQwenImage21`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
