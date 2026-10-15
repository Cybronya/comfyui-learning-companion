---
key: 图片生成/文生图/Qwen Image 2.1 V2文生图，文本到图像生成升级版本工作流_2103243206614937601.json
name: Qwen Image 2.1 V2文生图，文本到图像生成升级版本工作流_2103243206614937601
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 V2文生图，文本到图像生成升级版本工作流_2103243206614937601.json
hash: 81ac07490903f0b6
coverage: 0.844444
learned_at: 2026-10-10 20:58:51
nodes: [UNETLoader, TextEncodeQwenImage21, VAELoader, EmptyLatentImage, PreviewAny, StringConcatenate, TextGenerate, VAEDecode, KSampler, SaveImage, SaveImageAdvanced, CLIPLoader, PrimitiveStringMultiline, ResolutionSelector, RegexExtract, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1 V2文生图，文本到图像生成升级版本工作流_2103243206614937601.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1 V2文生图，文本到图像生成升级版本工作流_2103243206614937601.json`

## 结构

**节点**（45 个）：
- `UNETLoader`
- `TextEncodeQwenImage21`
- `VAELoader`
- `EmptyLatentImage`
- `PreviewAny`
- `StringConcatenate`
- `TextGenerate`
- `VAEDecode`
- `KSampler`
- `SaveImage`
- `SaveImageAdvanced`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `RegexExtract`
- `PrimitiveStringMultiline`
- `孤海注释`
- `孤海注释`
- `UNETLoader`
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
- `KSampler`
- `EmptyLatentImage`
- `JjkText`
- `CLIPTextEncode`
- `CLIPTextEncode`
- `solarL_SaveImagesToZip`
- `VAEDecode`
- `CLIPLoader`
- `VAELoader`
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

覆盖率 **84%**（38/45）

**有卡**：`UNETLoader`、`TextEncodeQwenImage21`、`VAELoader`、`EmptyLatentImage`、`PreviewAny`、`StringConcatenate`、`TextGenerate`、`VAEDecode`、`KSampler`、`SaveImage`、`SaveImageAdvanced`、`CLIPLoader`、`PrimitiveStringMultiline`、`ResolutionSelector`、`RegexExtract`、`孤海注释`、`LoraLoaderModelOnly`、`JjkText`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
