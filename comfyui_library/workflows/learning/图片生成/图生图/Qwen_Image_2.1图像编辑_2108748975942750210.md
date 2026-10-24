---
key: 图片生成/图生图/Qwen_Image_2.1图像编辑_2108748975942750210.json
name: Qwen_Image_2.1图像编辑_2108748975942750210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1图像编辑_2108748975942750210.json
hash: becb27bba0e07028
coverage: 0.774194
learned_at: 2026-10-23 11:21:14
nodes: [CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, QwenImage21Cache, ModelAttentionBackend, UNETLoader, ImageCompare, KSampler, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SaveImageAdvanced, LoadImage, ResizeImageMaskNode, GetImageSize, Reroute, Reroute, Reroute, Reroute, ComfySwitchNode, SaveImage, PrimitiveStringMultiline, ResolutionSelector, LoadImage, MarkdownNote]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen_Image_2.1图像编辑_2108748975942750210.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_Image_2.1图像编辑_2108748975942750210.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（31 个）：
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `QwenImage21Cache`
- `ModelAttentionBackend`
- `UNETLoader` ★核心
- `ImageCompare`
- `KSampler` ★核心
- `TextEncodeQwenImage21`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SaveImageAdvanced`
- `LoadImage`
- `ResizeImageMaskNode`
- `GetImageSize`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ComfySwitchNode`
- `SaveImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `LoadImage`
- `MarkdownNote`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `42`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（24/31）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`ModelAttentionBackend`、`UNETLoader`、`ImageCompare`、`KSampler`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImageAdvanced`、`ResizeImageMaskNode`、`GetImageSize`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
