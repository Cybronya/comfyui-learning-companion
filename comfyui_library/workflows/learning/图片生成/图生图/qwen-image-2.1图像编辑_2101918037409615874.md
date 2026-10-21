---
key: 图片生成/图生图/qwen-image-2.1图像编辑_2101918037409615874.json
name: qwen-image-2.1图像编辑_2101918037409615874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen-image-2.1图像编辑_2101918037409615874.json
hash: 7dc50a35344329d0
coverage: 0.833333
learned_at: 2026-10-21 00:46:06
nodes: [MarkdownNote, CLIPLoader, VAELoader, KSampler, ComfySwitchNode, QwenImage21Cache, LoadImage, TextEncodeQwenImage21, ResolutionSelector, EmptyLatentImage, Note, LoadImage, UNETLoader, VAEDecode, SaveImage, SaveImageAdvanced, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 846295274196631, "steps": 25, "width": 1024}
---

# 图片生成/图生图/qwen-image-2.1图像编辑_2101918037409615874.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen-image-2.1图像编辑_2101918037409615874.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Output → Other

**节点**（18 个）：
- `MarkdownNote`
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `LoadImage`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `Note`
- `LoadImage`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImageAdvanced`
- `LoadImage`
- `LoadImage`

## 关键参数

- `seed` = `846295274196631`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **83%**（15/18）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`QwenImage21Cache`、`LoadImage`、`TextEncodeQwenImage21`、`ResolutionSelector`、`EmptyLatentImage`、`UNETLoader`、`VAEDecode`、`SaveImage`、`SaveImageAdvanced`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
