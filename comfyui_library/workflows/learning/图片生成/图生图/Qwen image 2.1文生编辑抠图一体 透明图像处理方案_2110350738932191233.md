---
key: 图片生成/图生图/Qwen image 2.1文生编辑抠图一体 透明图像处理方案_2110350738932191233.json
name: Qwen image 2.1文生编辑抠图一体 透明图像处理方案_2110350738932191233
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1文生编辑抠图一体 透明图像处理方案_2110350738932191233.json
hash: f66db028faeecead
coverage: 0.862069
learned_at: 2026-10-23 11:14:10
nodes: [TextEncodeQwenImage21, ComfySwitchNode, LoadImage, LoadImage, Image Comparer (rgthree), SaveImage, VOSR2ModelLoader, Change Channel Count, VOSR2Upscale, SaveImage, LoadImage, QwenImage21Cache, VAEDecode, QwenPERewriteT8, easy showAnything, EmptyLatentImage, Fast Groups Bypasser (rgthree), PrimitiveBoolean, PrimitiveBoolean, SaveImageAdvanced, LoadImage, ResolutionSelector, CR Text, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, KSampler, LoraLoaderModelOnly, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, CLIPTextEncode, CLIPTextEncode, CLIPLoader, JjkText, VAEDecode, EmptyLatentImage, VAELoader, solarL_SaveImagesToZip, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen image 2.1文生编辑抠图一体 透明图像处理方案_2110350738932191233.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1文生编辑抠图一体 透明图像处理方案_2110350738932191233.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（58 个）：
- `TextEncodeQwenImage21`
- `ComfySwitchNode`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `VOSR2ModelLoader`
- `Change Channel Count`
- `VOSR2Upscale`
- `SaveImage`
- `LoadImage`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `QwenPERewriteT8`
- `easy showAnything`
- `EmptyLatentImage` ★核心
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `SaveImageAdvanced`
- `LoadImage`
- `ResolutionSelector`
- `CR Text`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `孤海注释`
- `孤海注释`
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
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `CLIPLoader`
- `JjkText`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `VAELoader`
- `solarL_SaveImagesToZip`
- `Note`

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

覆盖率 **86%**（50/58）

**有卡**：`TextEncodeQwenImage21`、`LoadImage`、`SaveImage`、`VOSR2ModelLoader`、`Change Channel Count`、`VOSR2Upscale`、`QwenImage21Cache`、`VAEDecode`、`QwenPERewriteT8`、`EmptyLatentImage`、`PrimitiveBoolean`、`SaveImageAdvanced`、`ResolutionSelector`、`CR Text`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`LoraLoaderModelOnly`、`KSampler`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 2 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
