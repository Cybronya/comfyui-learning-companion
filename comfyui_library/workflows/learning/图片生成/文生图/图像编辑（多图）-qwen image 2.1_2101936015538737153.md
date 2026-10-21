---
key: 图片生成/文生图/图像编辑（多图）-qwen image 2.1_2101936015538737153.json
name: 图像编辑（多图）-qwen image 2.1_2101936015538737153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/图像编辑（多图）-qwen image 2.1_2101936015538737153.json
hash: 0a12b04673fe32cd
coverage: 0.882353
learned_at: 2026-10-20 01:52:25
nodes: [VAELoader, CLIPLoader, QwenImage21Cache, ComfySwitchNode, VAEDecode, UNETLoader, KSampler, MarkdownNote, ResolutionSelector, EmptyLatentImage, SaveImage, SaveImageAdvanced, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 192944452481611, "steps": 25, "width": 1024}
---

# 图片生成/文生图/图像编辑（多图）-qwen image 2.1_2101936015538737153.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/图像编辑（多图）-qwen image 2.1_2101936015538737153.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `VAELoader`
- `CLIPLoader`
- `QwenImage21Cache`
- `ComfySwitchNode`
- `VAEDecode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `MarkdownNote`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `SaveImage`
- `SaveImageAdvanced`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `TextEncodeQwenImage21`

## 关键参数

- `seed` = `192944452481611`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（15/17）

**有卡**：`VAELoader`、`CLIPLoader`、`QwenImage21Cache`、`VAEDecode`、`UNETLoader`、`KSampler`、`ResolutionSelector`、`EmptyLatentImage`、`SaveImage`、`SaveImageAdvanced`、`LoadImage`、`TextEncodeQwenImage21`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
