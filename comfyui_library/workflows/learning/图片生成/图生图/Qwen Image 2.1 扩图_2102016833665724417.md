---
key: 图片生成/图生图/Qwen Image 2.1 扩图_2102016833665724417.json
name: Qwen Image 2.1 扩图_2102016833665724417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 扩图_2102016833665724417.json
hash: ce2fdd0f469f0080
coverage: 0.666667
learned_at: 2026-10-21 00:42:14
nodes: [ResolutionSelector, KSampler, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, QwenImage21Cache, TextEncodeQwenImage21, ResizeImageMaskNode, EmptyLatentImage, DrawMaskOnImage, PreviewImage, GetImageSize, SaveImageAdvanced, VAEDecode, SaveImage, CLIPLoader, VAELoader, UNETLoader, LoadImage, ImagePadForOutpaint]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 112233, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 扩图_2102016833665724417.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 扩图_2102016833665724417.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（24 个）：
- `ResolutionSelector`
- `KSampler` ★核心
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `ResizeImageMaskNode`
- `EmptyLatentImage` ★核心
- `DrawMaskOnImage`
- `PreviewImage`
- `GetImageSize`
- `SaveImageAdvanced`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `UNETLoader` ★核心
- `LoadImage`
- `ImagePadForOutpaint`

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

**有卡**：`ResolutionSelector`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`ResizeImageMaskNode`、`EmptyLatentImage`、`DrawMaskOnImage`、`GetImageSize`、`SaveImageAdvanced`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`VAELoader`、`UNETLoader`、`LoadImage`、`ImagePadForOutpaint`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
