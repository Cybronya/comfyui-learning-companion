---
key: 图片生成/图生图/Qwen_image_2.1_多合一图像编辑_加速工作流_2108746804220219393.json
name: Qwen_image_2.1_多合一图像编辑_加速工作流_2108746804220219393
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1_多合一图像编辑_加速工作流_2108746804220219393.json
hash: 563302f53747c425
coverage: 0.678571
learned_at: 2026-10-23 11:21:29
nodes: [EmptyLatentImage, TextGenerate, MarkdownNote, MarkdownNote, MarkdownNote, Fast Bypasser (rgthree), MarkdownNote, Seed (rgthree), Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, PathchSageAttentionKJ, QwenImage21Cache, ImageScaleToTotalPixels, PreviewAny, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, Note, MarkdownNote, VAEDecode, Fast Bypasser (rgthree), EasyCache, TextEncodeQwenImage21, Any Switch (rgthree), VAELoader, CLIPLoader, PrimitiveStringMultiline, PrimitiveStringMultiline, ResolutionSelector, ImageConcatMulti, ImageScaleToTotalPixels, LoadImage, ImageConcatMulti, ImageScaleToTotalPixels, LoadImage, ImageConcatMulti, LoadImage, ImageConcatMulti, LoadImage, ImageConcanate, LoadImage, ImageScaleToTotalPixels, ComfySwitchNode, ImageScaleToTotalPixels, SaveImageAdvanced, Any Switch (rgthree), Any Switch (rgthree), Fast Groups Muter (rgthree), ComfySwitchNode, MarkdownNote, UNETLoader, CLIPLoader, ImageConcanate, SaveImage, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 983904027334291, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen_image_2.1_多合一图像编辑_加速工作流_2108746804220219393.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen_image_2.1_多合一图像编辑_加速工作流_2108746804220219393.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（56 个）：
- `EmptyLatentImage` ★核心
- `TextGenerate`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Fast Bypasser (rgthree)`
- `MarkdownNote`
- `Seed (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Image Comparer (rgthree)`
- `KSampler` ★核心
- `PathchSageAttentionKJ`
- `QwenImage21Cache`
- `ImageScaleToTotalPixels`
- `PreviewAny`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `Note`
- `MarkdownNote`
- `VAEDecode` ★核心
- `Fast Bypasser (rgthree)`
- `EasyCache`
- `TextEncodeQwenImage21`
- `Any Switch (rgthree)`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageConcatMulti`
- `LoadImage`
- `ImageConcatMulti`
- `LoadImage`
- `ImageConcanate`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `ComfySwitchNode`
- `ImageScaleToTotalPixels`
- `SaveImageAdvanced`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Fast Groups Muter (rgthree)`
- `ComfySwitchNode`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `ImageConcanate`
- `SaveImage`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `983904027334291`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **68%**（38/56）

**有卡**：`EmptyLatentImage`、`TextGenerate`、`Fast Bypasser (rgthree)`、`Seed (rgthree)`、`KSampler`、`PathchSageAttentionKJ`、`QwenImage21Cache`、`ImageScaleToTotalPixels`、`VAEDecode`、`EasyCache`、`TextEncodeQwenImage21`、`VAELoader`、`CLIPLoader`、`ResolutionSelector`、`ImageConcatMulti`、`LoadImage`、`ImageConcanate`、`SaveImageAdvanced`、`UNETLoader`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
