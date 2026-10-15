---
key: 图片生成/文生图/Qwen image 2.1 图片编辑工作流（官方高质量版）_2103413517125771266.json
name: Qwen image 2.1 图片编辑工作流（官方高质量版）_2103413517125771266
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 图片编辑工作流（官方高质量版）_2103413517125771266.json
hash: 74379826a28fc074
coverage: 0.833333
learned_at: 2026-10-10 21:27:50
nodes: [ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, PrimitiveBoolean, 孤海注释, JoinStrings, EmptyLatentImage, ComfySwitchNode, TextGenerate, easy positive, BatchImagesNode, SaveImage, QwenImage21Cache, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, ShowText|pysssss, 忽略多组孤海, VAEDecode, KSampler, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, ResolutionSelector, LoadImage, LoadImage, easy positive, MarkdownNote]
patterns: []
missing: [easy positive, easy positive, 忽略多组孤海]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 633386983712418, "steps": 25, "width": 1024}
discoveries: [次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `easy positive` 知识库中没有该节点类型的任何知识, 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen image 2.1 图片编辑工作流（官方高质量版）_2103413517125771266.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen image 2.1 图片编辑工作流（官方高质量版）_2103413517125771266.json`

## 结构

**节点**（42 个）：
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `PrimitiveBoolean`
- `孤海注释`
- `JoinStrings`
- `EmptyLatentImage`
- `ComfySwitchNode`
- `TextGenerate`
- `easy positive`
- `BatchImagesNode`
- `SaveImage`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `ShowText|pysssss`
- `忽略多组孤海`
- `VAEDecode`
- `KSampler`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `ResolutionSelector`
- `LoadImage`
- `LoadImage`
- `easy positive`
- `MarkdownNote`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `633386983712418`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **83%**（35/42）

**有卡**：`ImageScaleToTotalPixels`、`PrimitiveBoolean`、`孤海注释`、`JoinStrings`、`EmptyLatentImage`、`ComfySwitchNode`、`TextGenerate`、`easy positive`、`BatchImagesNode`、`SaveImage`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ShowText|pysssss`、`忽略多组孤海`、`VAEDecode`、`KSampler`、`LoadImage`

**缺卡**（3）：`easy positive`、`easy positive`、`忽略多组孤海`

## 学习发现

- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `easy positive` 知识库中没有该节点类型的任何知识
- 次要节点 `忽略多组孤海` 知识库中没有该节点类型的任何知识
