---
key: 图片生成/图生图/Qwen+image+2.1图片编辑｜图生图局部修改轻松改细节_2104555432860807170.json
name: Qwen+image+2.1图片编辑｜图生图局部修改轻松改细节_2104555432860807170
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen+image+2.1图片编辑｜图生图局部修改轻松改细节_2104555432860807170.json
hash: 4214799bfaf67c16
coverage: 0.84
learned_at: 2026-10-21 00:43:04
nodes: [UNETLoader, VAELoader, QwenImage21Cache, TextEncodeQwenImage21, LoadImage, LoadImage, PrimitiveStringMultiline, StringConcatenate, BatchImagesNode, ImageScaleToTotalPixels, SaveImage, SaveImageAdvanced, KSampler, VAEDecode, RegexExtract, CLIPLoader, TextGenerate, ComfySwitchNode, PreviewAny, Image Comparer (rgthree), PrimitiveStringMultiline, Fast Groups Bypasser (rgthree), PrimitiveBoolean, ComfySwitchNode, EmptyLatentImage, LoadImage, ResolutionSelector, PrimitiveBoolean, PrimitiveInt, LoadImage, LoadImage, LoadImage, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/Qwen+image+2.1图片编辑｜图生图局部修改轻松改细节_2104555432860807170.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen+image+2.1图片编辑｜图生图局部修改轻松改细节_2104555432860807170.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（75 个）：
- `UNETLoader` ★核心
- `VAELoader`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `PrimitiveStringMultiline`
- `StringConcatenate`
- `BatchImagesNode`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `SaveImageAdvanced`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `RegexExtract`
- `CLIPLoader`
- `TextGenerate`
- `ComfySwitchNode`
- `PreviewAny`
- `Image Comparer (rgthree)`
- `PrimitiveStringMultiline`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `ComfySwitchNode`
- `EmptyLatentImage` ★核心
- `LoadImage`
- `ResolutionSelector`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `LoadImage`
- `LoadImage`
- `LoadImage`
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

覆盖率 **84%**（63/75）

**有卡**：`UNETLoader`、`VAELoader`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`LoadImage`、`StringConcatenate`、`BatchImagesNode`、`ImageScaleToTotalPixels`、`SaveImage`、`SaveImageAdvanced`、`KSampler`、`VAEDecode`、`RegexExtract`、`CLIPLoader`、`TextGenerate`、`PrimitiveBoolean`、`EmptyLatentImage`、`ResolutionSelector`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
