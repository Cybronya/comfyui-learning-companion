---
key: 图片生成/图生图/换装-Qwen Image 2.1-图像编辑_2101859929576534017.json
name: 换装-Qwen Image 2.1-图像编辑_2101859929576534017
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/换装-Qwen Image 2.1-图像编辑_2101859929576534017.json
hash: 3ccda362e977419a
coverage: 0.833333
learned_at: 2026-10-21 00:53:49
nodes: [MarkdownNote, MarkdownNote, CLIPLoader, UNETLoader, VAELoader, ComfySwitchNode, LoadImage, VAEDecode, LoadImage, ImageCompare, SaveImageAdvanced, QwenImage21Cache, TextEncodeQwenImage21, KSampler, SaveImage, EmptyLatentImage, ResolutionSelector, PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 25, "width": 1024}
---

# 图片生成/图生图/换装-Qwen Image 2.1-图像编辑_2101859929576534017.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/换装-Qwen Image 2.1-图像编辑_2101859929576534017.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（18 个）：
- `MarkdownNote`
- `MarkdownNote`
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `ComfySwitchNode`
- `LoadImage`
- `VAEDecode` ★核心
- `LoadImage`
- `ImageCompare`
- `SaveImageAdvanced`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `KSampler` ★核心
- `SaveImage`
- `EmptyLatentImage` ★核心
- `ResolutionSelector`
- `PrimitiveBoolean`

## 关键参数

- `seed` = `42`
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

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`LoadImage`、`VAEDecode`、`ImageCompare`、`SaveImageAdvanced`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`KSampler`、`SaveImage`、`EmptyLatentImage`、`ResolutionSelector`、`PrimitiveBoolean`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
