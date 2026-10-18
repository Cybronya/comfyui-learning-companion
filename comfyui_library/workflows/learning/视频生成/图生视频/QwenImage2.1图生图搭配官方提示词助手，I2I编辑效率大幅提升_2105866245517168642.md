---
key: 视频生成/图生视频/QwenImage2.1图生图搭配官方提示词助手，I2I编辑效率大幅提升_2105866245517168642.json
name: QwenImage2.1图生图搭配官方提示词助手，I2I编辑效率大幅提升_2105866245517168642
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/QwenImage2.1图生图搭配官方提示词助手，I2I编辑效率大幅提升_2105866245517168642.json
hash: bb2c6c1f64d32e03
coverage: 0.612245
learned_at: 2026-10-17 22:18:50
nodes: [ResolutionSelector, SaveImageAdvanced, ImageScaleToTotalPixels, ImageScaleToTotalPixels, TextGenerate, JsonExtractString, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, Fast Groups Bypasser (rgthree), LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, SetNode, SetNode, SetNode, SetNode, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, SetNode, LoadImage, LoadImage, SetNode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SetNode, SetNode, LoadImage, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPLoader, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, TextConcatenator, PrimitiveStringMultiline, easy showAnything, easy showAnything, LoadImage, LoadImage, SaveImage, VAEDecode, ImageBatchMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Any Switch (rgthree), TextEncodeQwenImage21, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note, LoadImage, PreviewImage]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 视频生成/图生视频/QwenImage2.1图生图搭配官方提示词助手，I2I编辑效率大幅提升_2105866245517168642.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/QwenImage2.1图生图搭配官方提示词助手，I2I编辑效率大幅提升_2105866245517168642.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（98 个）：
- `ResolutionSelector`
- `SaveImageAdvanced`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `TextGenerate`
- `JsonExtractString`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `SetNode`
- `SetNode`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPLoader`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveStringMultiline`
- `TextConcatenator`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `VAEDecode` ★核心
- `ImageBatchMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Any Switch (rgthree)`
- `TextEncodeQwenImage21`
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
- `LoadImage`
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

覆盖率 **61%**（60/98）

**有卡**：`ResolutionSelector`、`SaveImageAdvanced`、`ImageScaleToTotalPixels`、`TextGenerate`、`JsonExtractString`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`LoadImage`、`TextConcatenator`、`SaveImage`、`VAEDecode`、`ImageBatchMulti`、`TextEncodeQwenImage21`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
