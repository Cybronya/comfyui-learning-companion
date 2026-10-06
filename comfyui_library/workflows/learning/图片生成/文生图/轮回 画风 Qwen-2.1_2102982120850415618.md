---
key: 图片生成/文生图/轮回 画风 Qwen-2.1_2102982120850415618.json
name: 轮回 画风 Qwen-2.1_2102982120850415618
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/轮回 画风 Qwen-2.1_2102982120850415618.json
hash: 7c8da6432ee58587
coverage: 0.727273
learned_at: 2026-10-07 02:02:37
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, Label (rgthree), LoadImage, QwenImage21Cache, VAEDecode, EmptyLatentImage, LoadImage, JjkText, OpenposePreprocessor, PreviewImage, TextEncodeQwenImage21, LoraLoaderBypassModelOnly, CLIPLoader, CLIPTextEncode, UNETLoader, ResolutionSelector, VAELoader, SaveImage, KSampler, CLIPTextEncode]
patterns: [text_to_image]
missing: [Label (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 798072321765255, "steps": 25, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识]
---

# 图片生成/文生图/轮回 画风 Qwen-2.1_2102982120850415618.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/轮回 画风 Qwen-2.1_2102982120850415618.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（22 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Label (rgthree)`
- `LoadImage`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `EmptyLatentImage` ★核心
- `LoadImage`
- `JjkText`
- `OpenposePreprocessor`
- `PreviewImage`
- `TextEncodeQwenImage21`
- `LoraLoaderBypassModelOnly` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `ResolutionSelector`
- `VAELoader`
- `SaveImage`
- `KSampler` ★核心
- `CLIPTextEncode` ★核心

**识别到的模式**：text_to_image

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `798072321765255`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **73%**（16/22）

**有卡**：`LoadImage`、`QwenImage21Cache`、`VAEDecode`、`EmptyLatentImage`、`OpenposePreprocessor`、`TextEncodeQwenImage21`、`LoraLoaderBypassModelOnly`、`CLIPLoader`、`CLIPTextEncode`、`UNETLoader`、`ResolutionSelector`、`VAELoader`、`SaveImage`、`KSampler`

**缺卡**（1）：`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPTextEncode、CLIPLoader、EmptyLatentImage、ResolutionSelector

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
