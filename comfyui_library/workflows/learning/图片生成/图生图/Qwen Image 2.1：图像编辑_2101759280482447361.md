---
key: 图片生成/图生图/Qwen Image 2.1：图像编辑_2101759280482447361.json
name: Qwen Image 2.1：图像编辑_2101759280482447361
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1：图像编辑_2101759280482447361.json
hash: c1f4c07517c18ee4
coverage: 0.5
learned_at: 2026-10-06 21:41:48
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, CLIPLoader, PrimitiveStringMultiline, PreviewAny, BatchImagesNode, SaveImage, ImageCompare, SaveImageAdvanced, ComfySwitchNode, TextGenerate, JjkText, LoadImage, LoadImage]
patterns: []
missing: [BatchImagesNode, ImageCompare, TextGenerate, PreviewAny, SaveImageAdvanced]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 555537776240235, "steps": 25, "width": 1024}
discoveries: [次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识, 次要节点 `ImageCompare` 知识库中没有该节点类型的任何知识, 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识, 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明, 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen Image 2.1：图像编辑_2101759280482447361.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1：图像编辑_2101759280482447361.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（24 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `BatchImagesNode`
- `SaveImage`
- `ImageCompare`
- `SaveImageAdvanced`
- `ComfySwitchNode`
- `TextGenerate`
- `JjkText`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `555537776240235`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **50%**（12/24）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`SaveImage`、`LoadImage`

**缺卡**（5）：`BatchImagesNode`、`ImageCompare`、`TextGenerate`、`PreviewAny`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache

## 学习发现

- 次要节点 `BatchImagesNode` 知识库中没有该节点类型的任何知识
- 次要节点 `ImageCompare` 知识库中没有该节点类型的任何知识
- 次要节点 `TextGenerate` 知识库中没有该节点类型的任何知识
- 次要节点 `PreviewAny` 仅有 SaveImage 的通用知识，没有该节点自己的说明
- 次要节点 `SaveImageAdvanced` 仅有 SaveImage 的通用知识，没有该节点自己的说明
