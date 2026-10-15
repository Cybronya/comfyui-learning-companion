---
key: 图片生成/文生图/QWen2.1文生图_2102420206202216450.json
name: QWen2.1文生图_2102420206202216450
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/QWen2.1文生图_2102420206202216450.json
hash: 78a25c2979e0d2b1
coverage: 0.615385
learned_at: 2026-10-10 20:58:50
nodes: [KSampler, QwenImage21Cache, MarkdownNote, MarkdownNote, EmptyLatentImage, TextEncodeQwenImage21, TextGenerate, ComfySwitchNode, PreviewAny, CLIPLoader, PrimitiveStringMultiline, CR Prompt Text, UNETLoader, UNETLoader, MarkdownNote, ComfySwitchNode, ComfySwitchNode, PrimitiveBoolean, CLIPLoader, CLIPLoader, VAELoader, ResolutionSelector, PrimitiveBoolean, PrimitiveInt, VAEDecode, SaveImage]
patterns: []
missing: [CR Prompt Text]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 0, "steps": 25, "width": 1024}
discoveries: [次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明]
---

# 图片生成/文生图/QWen2.1文生图_2102420206202216450.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/QWen2.1文生图_2102420206202216450.json`

## 结构

**节点**（26 个）：
- `KSampler`
- `QwenImage21Cache`
- `MarkdownNote`
- `MarkdownNote`
- `EmptyLatentImage`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `ComfySwitchNode`
- `PreviewAny`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `CR Prompt Text`
- `UNETLoader`
- `UNETLoader`
- `MarkdownNote`
- `ComfySwitchNode`
- `ComfySwitchNode`
- `PrimitiveBoolean`
- `CLIPLoader`
- `CLIPLoader`
- `VAELoader`
- `ResolutionSelector`
- `PrimitiveBoolean`
- `PrimitiveInt`
- `VAEDecode`
- `SaveImage`

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

覆盖率 **62%**（16/26）

**有卡**：`KSampler`、`QwenImage21Cache`、`MarkdownNote`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`TextGenerate`、`ComfySwitchNode`、`PreviewAny`、`CLIPLoader`、`PrimitiveStringMultiline`、`CR Prompt Text`、`UNETLoader`

**缺卡**（1）：`CR Prompt Text`

## 学习发现

- 次要节点 `CR Prompt Text` 仅有 CLIPTextEncode 的通用知识，没有该节点自己的说明
