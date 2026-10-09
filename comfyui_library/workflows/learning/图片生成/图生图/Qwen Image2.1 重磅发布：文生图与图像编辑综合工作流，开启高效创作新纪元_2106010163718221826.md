---
key: 图片生成/图生图/Qwen Image2.1 重磅发布：文生图与图像编辑综合工作流，开启高效创作新纪元_2106010163718221826.json
name: Qwen Image2.1 重磅发布：文生图与图像编辑综合工作流，开启高效创作新纪元_2106010163718221826.json
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image2.1 重磅发布：文生图与图像编辑综合工作流，开启高效创作新纪元_2106010163718221826.json
hash: 2341a71068b86e32
coverage: 0.6
learned_at: 2026-10-09 22:09:17
nodes: [VAELoader, Anything Everywhere, Text Multiline, CLIPLoader, UNETLoader, QwenImage21Cache, MarkdownNote, GetNode, VAEDecode, SetNode, 忽略多组孤海, 孤海注释, KSampler, AnySwitch, EmptyLatentImage, ImageScaleToTotalPixels, VAEEncode, 孤海注释, 孤海注释, 忽略多组孤海, TextEncodeQwenImage21, LoadImage, LoadImage, SaveImage, LoadImage, ResolutionSelector, Image Comparer (rgthree), LoadImage, Text Multiline, LoadImage]
patterns: [image_to_image]
missing: [Text Multiline, Text Multiline, 忽略多组孤海, 忽略多组孤海]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1059976043427543, "steps": 30, "width": 1024}
discoveries: [次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Qwen Image2.1 重磅发布：文生图与图像编辑综合工作流，开启高效创作新纪元_2106010163718221826.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2106010163718221826.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `VAELoader`
- `Anything Everywhere`
- `Text Multiline`
- `CLIPLoader`
- `UNETLoader` ★核心
- `QwenImage21Cache`
- `MarkdownNote`
- `GetNode`
- `VAEDecode` ★核心
- `SetNode`
- `忽略多组孤海`
- `孤海注释`
- `KSampler` ★核心
- `AnySwitch`
- `EmptyLatentImage` ★核心
- `ImageScaleToTotalPixels`
- `VAEEncode` ★核心
- `孤海注释`
- `孤海注释`
- `忽略多组孤海`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `LoadImage`
- `ResolutionSelector`
- `Image Comparer (rgthree)`
- `LoadImage`
- `Text Multiline`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1059976043427543`
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

**有卡**：`VAELoader`、`CLIPLoader`、`UNETLoader`、`QwenImage21Cache`、`VAEDecode`、`KSampler`、`AnySwitch`、`EmptyLatentImage`、`ImageScaleToTotalPixels`、`VAEEncode`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImage`、`ResolutionSelector`

**缺卡**（4）：`Text Multiline`、`Text Multiline`、`忽略多组孤海`、`忽略多组孤海`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Multiline` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
