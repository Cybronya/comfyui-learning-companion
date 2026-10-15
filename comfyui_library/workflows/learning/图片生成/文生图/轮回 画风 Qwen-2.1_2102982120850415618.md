---
key: 图片生成/文生图/轮回 画风 Qwen-2.1_2102982120850415618.json
name: 轮回 画风 Qwen-2.1_2102982120850415618
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/轮回 画风 Qwen-2.1_2102982120850415618.json
hash: 7c8da6432ee58587
coverage: 0.727273
learned_at: 2026-10-10 20:59:58
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, Label (rgthree), LoadImage, QwenImage21Cache, VAEDecode, EmptyLatentImage, LoadImage, JjkText, OpenposePreprocessor, PreviewImage, TextEncodeQwenImage21, LoraLoaderBypassModelOnly, CLIPLoader, CLIPTextEncode, UNETLoader, ResolutionSelector, VAELoader, SaveImage, KSampler, CLIPTextEncode]
patterns: [text_to_image]
missing: [Label (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 798072321765255, "steps": 25, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/轮回 画风 Qwen-2.1_2102982120850415618.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/轮回 画风 Qwen-2.1_2102982120850415618.json`

## 结构

**节点**（22 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Label (rgthree)`
- `LoadImage`
- `QwenImage21Cache`
- `VAEDecode`
- `EmptyLatentImage`
- `LoadImage`
- `JjkText`
- `OpenposePreprocessor`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `LoraLoaderBypassModelOnly`
- `CLIPLoader`
- `CLIPTextEncode`
- `UNETLoader`
- `ResolutionSelector`
- `VAELoader`
- `SaveImage`
- `KSampler`
- `CLIPTextEncode`

**识别到的模式**：text_to_image

## 关键参数

- `batch_size` = `1`
- `cfg` = `1`
- `denoise` = `1`
- `height` = `1024`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `798072321765255`
- `steps` = `25`
- `width` = `1024`

## 知识

覆盖率 **73%**（16/22）

**有卡**：`MarkdownNote`、`Label (rgthree)`、`LoadImage`、`QwenImage21Cache`、`VAEDecode`、`EmptyLatentImage`、`JjkText`、`OpenposePreprocessor`、`PreviewImage`、`TextEncodeQwenImage21`、`LoraLoaderBypassModelOnly`、`CLIPLoader`、`CLIPTextEncode`

**缺卡**（1）：`Label (rgthree)`

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
