---
key: 图片生成/图生图/Qwen image 2.1透明背景抠图_2101914691361660930.json
name: Qwen image 2.1透明背景抠图_2101914691361660930
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1透明背景抠图_2101914691361660930.json
hash: 656b153735dc048d
coverage: 0.791667
learned_at: 2026-10-15 22:25:20
nodes: [TextEncodeQwenImage21, KSampler, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, VAEDecode, ImageConcatMulti, SaveImageAdvanced, ImageConcatMulti, SaveImageAdvanced, SaveImage, easy cleanGpuUsed, TextCombinerTwo, easy showAnything, ResolutionSelector, JjkText, JjkText, LoadImage, MarkdownNote, Label (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1透明背景抠图_2101914691361660930.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1透明背景抠图_2101914691361660930.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CLIPLoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `VAEDecode` ★核心
- `ImageConcatMulti`
- `SaveImageAdvanced`
- `ImageConcatMulti`
- `SaveImageAdvanced`
- `SaveImage`
- `easy cleanGpuUsed`
- `TextCombinerTwo`
- `easy showAnything`
- `ResolutionSelector`
- `JjkText`
- `JjkText`
- `LoadImage`
- `MarkdownNote`
- `Label (rgthree)`

## 关键参数

- `seed` = `999`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **79%**（19/24）

**有卡**：`TextEncodeQwenImage21`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`VAEDecode`、`ImageConcatMulti`、`SaveImageAdvanced`、`SaveImage`、`easy cleanGpuUsed`、`TextCombinerTwo`、`ResolutionSelector`、`LoadImage`、`Label (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
