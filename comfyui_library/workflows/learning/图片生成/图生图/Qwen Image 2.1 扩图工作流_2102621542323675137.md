---
key: 图片生成/图生图/Qwen Image 2.1 扩图工作流_2102621542323675137.json
name: Qwen Image 2.1 扩图工作流_2102621542323675137
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 扩图工作流_2102621542323675137.json
hash: 5162971f5f35c729
coverage: 0.666667
learned_at: 2026-10-10 20:48:05
nodes: [KSampler, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, QwenImage21Cache, ResizeImageMaskNode, EmptyLatentImage, ImagePadForOutpaint, DrawMaskOnImage, GetImageSize, VAEDecode, CLIPLoader, VAELoader, UNETLoader, TextEncodeQwenImage21, ResolutionSelector, SaveImageAdvanced, PreviewImage, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 112233, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 扩图工作流_2102621542323675137.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 扩图工作流_2102621542323675137.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `KSampler` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `QwenImage21Cache`
- `ResizeImageMaskNode`
- `EmptyLatentImage` ★核心
- `ImagePadForOutpaint`
- `DrawMaskOnImage`
- `GetImageSize`
- `VAEDecode` ★核心
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `SaveImageAdvanced`
- `PreviewImage`
- `SaveImage`
- `LoadImage`

## 关键参数

- `seed` = `112233`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **67%**（16/24）

**有卡**：`KSampler`、`QwenImage21Cache`、`ResizeImageMaskNode`、`EmptyLatentImage`、`ImagePadForOutpaint`、`DrawMaskOnImage`、`GetImageSize`、`VAEDecode`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`TextEncodeQwenImage21`、`ResolutionSelector`、`SaveImageAdvanced`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
