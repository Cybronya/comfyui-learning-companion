---
key: 图片生成/图生图/QwenImage2.1 I2I官方提示词助手｜图生图有帮手｜描述写不好也能改图_2102637170602364929.json
name: QwenImage2.1 I2I官方提示词助手｜图生图有帮手｜描述写不好也能改图_2102637170602364929
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenImage2.1 I2I官方提示词助手｜图生图有帮手｜描述写不好也能改图_2102637170602364929.json
hash: 69d0a4a8e04634cd
coverage: 0.695238
learned_at: 2026-10-10 20:48:10
nodes: [ResolutionSelector, SaveImageAdvanced, ImageScaleToTotalPixels, ImageScaleToTotalPixels, TextGenerate, JsonExtractString, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, KSampler, ComfySwitchNode, QwenImage21Cache, Fast Groups Bypasser (rgthree), LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, SetNode, SetNode, SetNode, SetNode, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, SetNode, LoadImage, LoadImage, SetNode, ImageScaleToTotalPixels, ImageScaleToTotalPixels, SetNode, SetNode, LoadImage, ImageScaleToTotalPixels, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, CLIPLoader, Fast Groups Bypasser (rgthree), PrimitiveStringMultiline, TextConcatenator, PrimitiveStringMultiline, easy showAnything, easy showAnything, LoadImage, LoadImage, SaveImage, VAEDecode, ImageBatchMulti, GetNode, Any Switch (rgthree), TextEncodeQwenImage21, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QwenImage2.1 I2I官方提示词助手｜图生图有帮手｜描述写不好也能改图_2102637170602364929.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenImage2.1 I2I官方提示词助手｜图生图有帮手｜描述写不好也能改图_2102637170602364929.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（105 个）：
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
- `Any Switch (rgthree)`
- `TextEncodeQwenImage21`
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

覆盖率 **70%**（73/105）

**有卡**：`ResolutionSelector`、`SaveImageAdvanced`、`ImageScaleToTotalPixels`、`TextGenerate`、`JsonExtractString`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`LoadImage`、`TextConcatenator`、`SaveImage`、`VAEDecode`、`ImageBatchMulti`、`TextEncodeQwenImage21`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
