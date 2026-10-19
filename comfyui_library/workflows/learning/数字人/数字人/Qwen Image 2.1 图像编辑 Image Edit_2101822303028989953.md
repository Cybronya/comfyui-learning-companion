---
key: 数字人/数字人/Qwen Image 2.1 图像编辑 Image Edit_2101822303028989953.json
name: Qwen Image 2.1 图像编辑 Image Edit_2101822303028989953
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Qwen Image 2.1 图像编辑 Image Edit_2101822303028989953.json
hash: 5aaf97c7616b0b37
coverage: 0.75
learned_at: 2026-10-19 00:19:12
nodes: [MarkdownNote, CLIPLoader, VAELoader, EmptyLatentImage, ResolutionSelector, MarkdownNote, ComfySwitchNode, TextEncodeQwenImage21, LoadImage, VAEDecode, Image Comparer (rgthree), SaveImageAdvanced, BatchImagesNode, UNETLoader, LoadImage, CLIPLoader, LoadImage, SaveImage, easy showAnything, LoadImage, QwenImage21Cache, KSampler, PrimitiveStringMultiline, TextGenerateLTX2Prompt]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 300862765067678, "steps": 25, "width": 1024}
---

# 数字人/数字人/Qwen Image 2.1 图像编辑 Image Edit_2101822303028989953.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Qwen Image 2.1 图像编辑 Image Edit_2101822303028989953.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `MarkdownNote`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `LoadImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `SaveImageAdvanced`
- `BatchImagesNode`
- `UNETLoader` ★核心
- `LoadImage`
- `CLIPLoader`
- `LoadImage`
- `SaveImage`
- `easy showAnything`
- `LoadImage`
- `QwenImage21Cache`
- `KSampler` ★核心
- `PrimitiveStringMultiline`
- `TextGenerateLTX2Prompt`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `300862765067678`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **75%**（18/24）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`ResolutionSelector`、`TextEncodeQwenImage21`、`LoadImage`、`VAEDecode`、`SaveImageAdvanced`、`BatchImagesNode`、`UNETLoader`、`SaveImage`、`QwenImage21Cache`、`KSampler`、`TextGenerateLTX2Prompt`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
