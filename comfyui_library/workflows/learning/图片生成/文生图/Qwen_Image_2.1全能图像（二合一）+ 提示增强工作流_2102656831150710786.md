---
key: 图片生成/文生图/Qwen_Image_2.1全能图像（二合一）+ 提示增强工作流_2102656831150710786.json
name: Qwen_Image_2.1全能图像（二合一）+ 提示增强工作流_2102656831150710786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen_Image_2.1全能图像（二合一）+ 提示增强工作流_2102656831150710786.json
hash: a6989a66b6ce490f
coverage: 0.763158
learned_at: 2026-10-15 22:27:26
nodes: [MarkdownNote, MarkdownNote, TextEncodeQwenImage21, QwenImage21Cache, PreviewAny, SaveImageAdvanced, SaveImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Label (rgthree), TextGenerate, PrimitiveStringMultiline, EmptyLatentImage, UNETLoader, CLIPLoader, PrimitiveStringMultiline, ComfySwitchNode, SeedNode, CLIPLoader, PrimitiveBoolean, StringConcatenate, Textbox, VAEDecode, ResolutionSelector, ComfySwitchNode, Note, Note, PrimitiveBoolean, VAELoader, KSampler]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1536, "sampler_name": "euler", "scheduler": "simple", "seed": 739404592123668, "steps": 35, "width": 1024}
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

覆盖率 **76%**（29/38）

**有卡**：`TextEncodeQwenImage21`、`QwenImage21Cache`、`SaveImageAdvanced`、`SaveImage`、`LoadImage`、`Label (rgthree)`、`TextGenerate`、`EmptyLatentImage`、`UNETLoader`、`CLIPLoader`、`SeedNode`、`PrimitiveBoolean`、`StringConcatenate`、`Textbox`、`VAEDecode`、`ResolutionSelector`、`VAELoader`、`KSampler`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
