---
key: 图片生成/文生图/Qwen_Image_2.1全能图像（二合一）+ 提示增强工作流_2102656831150710786.json
name: Qwen_Image_2.1全能图像（二合一）+ 提示增强工作流_2102656831150710786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_Image_2.1全能图像（二合一）+ 提示增强工作流_2102656831150710786.json
hash: a6989a66b6ce490f
coverage: 0.736842
learned_at: 2026-10-07 02:29:38
nodes: [MarkdownNote, MarkdownNote, TextEncodeQwenImage21, QwenImage21Cache, PreviewAny, SaveImageAdvanced, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Label (rgthree), TextGenerate, PrimitiveStringMultiline, EmptyLatentImage, UNETLoader, CLIPLoader, PrimitiveStringMultiline, ComfySwitchNode, SeedNode, CLIPLoader, PrimitiveBoolean, StringConcatenate, Textbox, VAEDecode, ResolutionSelector, ComfySwitchNode, Note, Note, PrimitiveBoolean, VAELoader, KSampler]
patterns: []
missing: [Label (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 739404592123668, "steps": 35, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/Qwen_Image_2.1全能图像（二合一）+ 提示增强工作流_2102656831150710786.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen_Image_2.1全能图像（二合一）+ 提示增强工作流_2102656831150710786.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（38 个）：
- `MarkdownNote`
- `MarkdownNote`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `PreviewAny`
- `SaveImageAdvanced`
- `SaveImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Label (rgthree)`
- `TextGenerate`
- `PrimitiveStringMultiline`
- `EmptyLatentImage` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `SeedNode`
- `CLIPLoader`
- `PrimitiveBoolean`
- `StringConcatenate`
- `Textbox`
- `VAEDecode` ★核心
- `ResolutionSelector`
- `ComfySwitchNode`
- `Note`
- `Note`
- `PrimitiveBoolean`
- `VAELoader`
- `KSampler` ★核心

## 关键参数

- `width` = `1024`
- `height` = `1536`
- `batch_size` = `1`
- `seed` = `739404592123668`
- `steps` = `35`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **74%**（28/38）

**有卡**：`TextEncodeQwenImage21`、`QwenImage21Cache`、`SaveImageAdvanced`、`SaveImage`、`LoadImage`、`TextGenerate`、`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`SeedNode`、`PrimitiveBoolean`、`StringConcatenate`、`Textbox`、`VAEDecode`、`ResolutionSelector`、`VAELoader`、`KSampler`

**缺卡**（1）：`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
