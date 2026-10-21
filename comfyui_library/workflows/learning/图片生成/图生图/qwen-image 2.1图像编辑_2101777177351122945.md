---
key: 图片生成/图生图/qwen-image 2.1图像编辑_2101777177351122945.json
name: qwen-image 2.1图像编辑_2101777177351122945
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image 2.1图像编辑_2101777177351122945.json
hash: a71c95bb10cb8e10
coverage: 0.823529
learned_at: 2026-10-21 00:46:05
nodes: [ResolutionSelector, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, MarkdownNote, MarkdownNote, ComfySwitchNode, QwenImage21Cache, KSampler, VAEDecode, SaveImageAdvanced, SaveImage, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 502502339428834, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen-image 2.1图像编辑_2101777177351122945.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image 2.1图像编辑_2101777177351122945.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（17 个）：
- `ResolutionSelector`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `MarkdownNote`
- `ComfySwitchNode`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `SaveImage`
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `502502339428834`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（14/17）

**有卡**：`ResolutionSelector`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`QwenImage21Cache`、`KSampler`、`VAEDecode`、`SaveImageAdvanced`、`SaveImage`、`TextEncodeQwenImage21`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
