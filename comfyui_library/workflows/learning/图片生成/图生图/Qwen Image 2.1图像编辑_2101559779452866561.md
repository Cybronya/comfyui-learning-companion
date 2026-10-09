---
key: 图片生成/图生图/Qwen Image 2.1图像编辑_2101559779452866561.json
name: Qwen Image 2.1图像编辑_2101559779452866561.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1图像编辑_2101559779452866561.json
hash: 9c782d1bb7af8ddf
coverage: 0.727273
learned_at: 2026-10-09 22:19:27
nodes: [CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, QwenImage21Cache, ModelAttentionBackend, UNETLoader, ImageCompare, KSampler, TextEncodeQwenImage21, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SaveImageAdvanced, MarkdownNote, Note, LoadImage, ResizeImageMaskNode, GetImageSize, Reroute, Reroute, Reroute, Reroute, ComfySwitchNode, MarkdownNote, SaveImage, PrimitiveStringMultiline, ResolutionSelector, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 42, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1图像编辑_2101559779452866561.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/2101559779452866561.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
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
- `MarkdownNote`
- `Note`
- `LoadImage`
- `ResizeImageMaskNode`
- `GetImageSize`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `ComfySwitchNode`
- `MarkdownNote`
- `SaveImage`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `LoadImage`

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

覆盖率 **73%**（24/33）

**有卡**：`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`ModelAttentionBackend`、`UNETLoader`、`ImageCompare`、`KSampler`、`TextEncodeQwenImage21`、`LoadImage`、`SaveImageAdvanced`、`ResizeImageMaskNode`、`GetImageSize`、`SaveImage`、`ResolutionSelector`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
