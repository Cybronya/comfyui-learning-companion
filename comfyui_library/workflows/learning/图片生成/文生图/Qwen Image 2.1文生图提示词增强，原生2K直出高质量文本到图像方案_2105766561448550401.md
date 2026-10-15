---
key: 图片生成/文生图/Qwen Image 2.1文生图提示词增强，原生2K直出高质量文本到图像方案_2105766561448550401.json
name: Qwen Image 2.1文生图提示词增强，原生2K直出高质量文本到图像方案_2105766561448550401
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图提示词增强，原生2K直出高质量文本到图像方案_2105766561448550401.json
hash: e29d15970bf0de74
coverage: 0.840909
learned_at: 2026-10-10 20:58:54
nodes: [PreviewAny, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, CLIPLoader, KSampler, VAEDecode, SaveImageAdvanced, SaveImage, TextGenerate, ResolutionSelector, PrimitiveStringMultiline, PrimitiveStringMultiline, 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图提示词增强，原生2K直出高质量文本到图像方案_2105766561448550401.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图提示词增强，原生2K直出高质量文本到图像方案_2105766561448550401.json`

## 结构

**节点**（44 个）：
- `PreviewAny`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage`
- `CLIPLoader`
- `KSampler`
- `VAEDecode`
- `SaveImageAdvanced`
- `SaveImage`
- `TextGenerate`
- `ResolutionSelector`
- `PrimitiveStringMultiline`
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

覆盖率 **84%**（37/44）

**有卡**：`PreviewAny`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`KSampler`、`VAEDecode`、`SaveImageAdvanced`、`SaveImage`、`TextGenerate`、`ResolutionSelector`、`PrimitiveStringMultiline`、`孤海注释`、`LoraLoaderModelOnly`、`JjkText`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
