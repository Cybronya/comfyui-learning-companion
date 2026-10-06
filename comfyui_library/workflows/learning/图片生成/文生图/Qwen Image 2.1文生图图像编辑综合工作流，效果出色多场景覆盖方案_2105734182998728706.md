---
key: 图片生成/文生图/Qwen Image 2.1文生图图像编辑综合工作流，效果出色多场景覆盖方案_2105734182998728706.json
name: Qwen Image 2.1文生图图像编辑综合工作流，效果出色多场景覆盖方案_2105734182998728706
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图图像编辑综合工作流，效果出色多场景覆盖方案_2105734182998728706.json
hash: d802be711d7f458b
coverage: 0.811321
learned_at: 2026-10-07 02:20:34
nodes: [LoadImage, VAELoader, LoadImage, LoadImage, Anything Everywhere, Text Multiline, CLIPLoader, UNETLoader, QwenImage21Cache, GetNode, ResolutionSelector, VAEDecode, SetNode, LoadImage, LoadImage, Text Multiline, SaveImage, KSampler, AnySwitch, TextEncodeQwenImage21, EmptyLatentImage, ImageScaleToTotalPixels, VAEEncode, Image Comparer (rgthree), 孤海注释, 孤海注释, UNETLoader, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, EmptyLatentImage, JjkText, CLIPTextEncode, CLIPTextEncode, solarL_SaveImagesToZip, VAEDecode, CLIPLoader, VAELoader, Note]
patterns: [text_to_image, image_to_image]
missing: [Text Multiline, Text Multiline]
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, [medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/文生图/Qwen Image 2.1文生图图像编辑综合工作流，效果出色多场景覆盖方案_2105734182998728706.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image 2.1文生图图像编辑综合工作流，效果出色多场景覆盖方案_2105734182998728706.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `LoadImage`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `Anything Everywhere`
- `Text Multiline`
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `GetNode`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `SetNode`
- `LoadImage`
- `LoadImage`
- `Text Multiline`
- `SaveImage`
- `KSampler` ★核心
- `AnySwitch`
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
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
- `EmptyLatentImage` ★核心
- `JjkText`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `solarL_SaveImagesToZip`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `Note`

**识别到的模式**：text_to_image、image_to_image

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

覆盖率 **81%**（43/53）

**有卡**：`LoadImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`KSampler`、`AnySwitch`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ImageScaleToTotalPixels`、`VAEEncode`、`LoraLoaderModelOnly`、`CLIPTextEncode`、`solarL_SaveImagesToZip`

**缺卡**（2）：`Text Multiline`、`Text Multiline`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、EmptyLatentImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
