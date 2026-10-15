---
key: 图片生成/文生图/Qwen Image2.1综合工作流｜文生图图像编辑换背景 AI小王子出品_2105552519928836097.json
name: Qwen Image2.1综合工作流｜文生图图像编辑换背景 AI小王子出品_2105552519928836097
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1综合工作流｜文生图图像编辑换背景 AI小王子出品_2105552519928836097.json
hash: ff13accfc10eaeaf
coverage: 0.850746
learned_at: 2026-10-10 20:58:56
nodes: [LoadImage, VAELoader, LoadImage, LoadImage, Anything Everywhere, Text Multiline, CLIPLoader, UNETLoader, QwenImage21Cache, GetNode, ResolutionSelector, VAEDecode, SetNode, LoadImage, LoadImage, Text Multiline, SaveImage, KSampler, AnySwitch, TextEncodeQwenImage21, EmptyLatentImage, ImageScaleToTotalPixels, VAEEncode, Image Comparer (rgthree), 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image, image_to_image]
missing: [Text Multiline, Text Multiline]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image2.1综合工作流｜文生图图像编辑换背景 AI小王子出品_2105552519928836097.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1综合工作流｜文生图图像编辑换背景 AI小王子出品_2105552519928836097.json`

## 结构

**节点**（67 个）：
- `LoadImage`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `Anything Everywhere`
- `Text Multiline`
- `CLIPLoader`
- `UNETLoader`
- `QwenImage21Cache`
- `GetNode`
- `ResolutionSelector`
- `VAEDecode`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `SaveImage`
- `KSampler`
- `AnySwitch`
- `TextEncodeQwenImage21`
- `EmptyLatentImage`
- `ImageScaleToTotalPixels`
- `VAEEncode`
- `Image Comparer (rgthree)`
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

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **85%**（57/67）

**有卡**：`LoadImage`、`VAELoader`、`Anything Everywhere`、`Text Multiline`、`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`GetNode`、`ResolutionSelector`、`VAEDecode`、`SetNode`、`SaveImage`、`KSampler`、`AnySwitch`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ImageScaleToTotalPixels`、`VAEEncode`、`Image Comparer (rgthree)`、`孤海注释`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`JjkText`、`LoraLoaderModelOnly`

**缺卡**（2）：`Text Multiline`、`Text Multiline`

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
