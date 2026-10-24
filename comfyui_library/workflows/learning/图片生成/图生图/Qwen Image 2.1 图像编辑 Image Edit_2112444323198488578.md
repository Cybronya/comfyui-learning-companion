---
key: 图片生成/图生图/Qwen Image 2.1 图像编辑 Image Edit_2112444323198488578.json
name: Qwen Image 2.1 图像编辑 Image Edit_2112444323198488578
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 图像编辑 Image Edit_2112444323198488578.json
hash: 533a22b3e4cb4769
coverage: 0.761905
learned_at: 2026-10-23 11:12:42
nodes: [MarkdownNote, VAELoader, EmptyLatentImage, MarkdownNote, ComfySwitchNode, TextEncodeQwenImage21, VAEDecode, SaveImageAdvanced, BatchImagesNode, QwenImage21Cache, KSampler, TextGenerateLTX2Prompt, UNETLoader, LoadImage, GetImageSize, ResolutionSelector, CLIPLoader, CLIPLoader, PrimitiveStringMultiline, easy showAnything, SaveImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1098662658191703, "steps": 25, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 图像编辑 Image Edit_2112444323198488578.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 图像编辑 Image Edit_2112444323198488578.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `MarkdownNote`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `MarkdownNote`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `VAEDecode` ★核心
- `SaveImageAdvanced`
- `BatchImagesNode`
- `QwenImage21Cache`
- `KSampler` ★核心
- `TextGenerateLTX2Prompt`
- `UNETLoader` ★核心
- `LoadImage`
- `GetImageSize`
- `ResolutionSelector`
- `CLIPLoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `easy showAnything`
- `SaveImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1098662658191703`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（16/21）

**有卡**：`VAELoader`、`EmptyLatentImage`、`TextEncodeQwenImage21`、`VAEDecode`、`SaveImageAdvanced`、`BatchImagesNode`、`QwenImage21Cache`、`KSampler`、`TextGenerateLTX2Prompt`、`UNETLoader`、`LoadImage`、`GetImageSize`、`ResolutionSelector`、`CLIPLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
