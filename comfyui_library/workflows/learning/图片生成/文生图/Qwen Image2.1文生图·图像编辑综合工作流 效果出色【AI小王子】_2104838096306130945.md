---
key: 图片生成/文生图/Qwen Image2.1文生图·图像编辑综合工作流 效果出色【AI小王子】_2104838096306130945.json
name: Qwen Image2.1文生图·图像编辑综合工作流 效果出色【AI小王子】_2104838096306130945
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图·图像编辑综合工作流 效果出色【AI小王子】_2104838096306130945.json
hash: 6235188d2f1af307
coverage: 0.6
learned_at: 2026-10-06 22:57:52
nodes: [LoadImage, VAELoader, LoadImage, LoadImage, Anything Everywhere, Text Multiline, CLIPLoader, UNETLoader, QwenImage21Cache, MarkdownNote, GetNode, ResolutionSelector, VAEDecode, SetNode, 忽略多组孤海, 孤海注释, LoadImage, LoadImage, Text Multiline, SaveImage, KSampler, AnySwitch, TextEncodeQwenImage21, EmptyLatentImage, ImageScaleToTotalPixels, VAEEncode, Image Comparer (rgthree), 孤海注释, 孤海注释, 忽略多组孤海]
patterns: [image_to_image]
missing: [Text Multiline, Text Multiline, 忽略多组孤海, 忽略多组孤海]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 245967651573861, "steps": 30, "width": 1024}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen Image2.1文生图·图像编辑综合工作流 效果出色【AI小王子】_2104838096306130945.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1文生图·图像编辑综合工作流 效果出色【AI小王子】_2104838096306130945.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `LoadImage`
- `VAELoader`
- `LoadImage`
- `LoadImage`
- `Anything Everywhere`
- `Text Multiline`
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `MarkdownNote`
- `GetNode`
- `ResolutionSelector`
- `VAEDecode` ★核心
- `SetNode`
- `忽略多组孤海`
- `孤海注释`
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
- `忽略多组孤海`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `245967651573861`
- `steps` = `30`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **60%**（18/30）

**有卡**：`LoadImage`、`VAELoader`、`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`ResolutionSelector`、`VAEDecode`、`SaveImage`、`KSampler`、`AnySwitch`、`TextEncodeQwenImage21`、`EmptyLatentImage`、`ImageScaleToTotalPixels`、`VAEEncode`

**缺卡**（4）：`Text Multiline`、`Text Multiline`、`忽略多组孤海`、`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
