---
key: 图片生成/文生图/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json
name: Qwen-Image-2.1 参考生图标准版_2104454950465138689
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json
hash: 71d1cec968cea7b6
coverage: 0.722222
learned_at: 2026-10-10 21:28:31
nodes: [UNETLoader, CLIPLoader, MarkdownNote, VAELoader, EmptyLatentImage, TextGenerate, PrimitiveStringMultiline, PreviewAny, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, SaveImage, LoadImage, CR Text, MarkdownNote, ResolutionSelector, CLIPLoader]
patterns: []
missing: [CR Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen-Image-2.1 参考生图标准版_2104454950465138689.json`

## 结构

**节点**（18 个）：
- `UNETLoader`
- `CLIPLoader`
- `MarkdownNote`
- `VAELoader`
- `EmptyLatentImage`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler`
- `VAEDecode`
- `SaveImage`
- `LoadImage`
- `CR Text`
- `MarkdownNote`
- `ResolutionSelector`
- `CLIPLoader`

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `0`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **72%**（13/18）

**有卡**：`UNETLoader`、`CLIPLoader`、`MarkdownNote`、`VAELoader`、`EmptyLatentImage`、`TextGenerate`、`PrimitiveStringMultiline`、`PreviewAny`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImage`

**缺卡**（1）：`CR Text`

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
