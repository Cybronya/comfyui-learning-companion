---
key: 图片生成/图生图/Qwen image 2.1透明背景抠图_2101914691361660930.json
name: Qwen image 2.1透明背景抠图_2101914691361660930.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1透明背景抠图_2101914691361660930.json
hash: 656b153735dc048d
coverage: 0.708333
learned_at: 2026-10-09 22:27:07
nodes: [TextEncodeQwenImage21, KSampler, UNETLoader, CLIPLoader, VAELoader, CLIPLoader, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, VAEDecode, ImageConcatMulti, SaveImageAdvanced, ImageConcatMulti, SaveImageAdvanced, SaveImage, easy cleanGpuUsed, TextCombinerTwo, easy showAnything, ResolutionSelector, JjkText, JjkText, LoadImage, MarkdownNote, Label (rgthree)]
patterns: []
missing: [Label (rgthree), easy cleanGpuUsed]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
discoveries: [次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识]
---

# 图片生成/图生图/Qwen image 2.1透明背景抠图_2101914691361660930.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2101914691361660930.json`

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

覆盖率 **71%**（17/24）

**有卡**：`TextEncodeQwenImage21`、`KSampler`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`VAEDecode`、`ImageConcatMulti`、`SaveImageAdvanced`、`SaveImage`、`TextCombinerTwo`、`ResolutionSelector`、`LoadImage`

**缺卡**（2）：`Label (rgthree)`、`easy cleanGpuUsed`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `Label (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
