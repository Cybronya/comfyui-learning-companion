---
key: 图片生成/图生图/Qwen image 2.1 多合一图像编辑 加速工作流 V1.5_2104920188973051905.json
name: Qwen image 2.1 多合一图像编辑 加速工作流 V1.5_2104920188973051905
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 多合一图像编辑 加速工作流 V1.5_2104920188973051905.json
hash: a7b44623c07c3d4e
coverage: 0.612903
learned_at: 2026-10-21 00:42:55
nodes: [MarkdownNote, EmptyLatentImage, Seed (rgthree), Image Comparer (rgthree), ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, MarkdownNote, ImageConcanate, Any Switch (rgthree), VAELoader, CLIPLoader, PrimitiveStringMultiline, ImageConcatMulti, ImageScaleToTotalPixels, LoadImage, ImageConcatMulti, ImageScaleToTotalPixels, LoadImage, ImageConcatMulti, LoadImage, ImageConcatMulti, LoadImage, ImageConcanate, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, UNETLoader, Note, MarkdownNote, MarkdownNote, SaveImageAdvanced, Any Switch (rgthree), Any Switch (rgthree), ComfySwitchNode, Fast Bypasser (rgthree), CLIPLoader, Fast Groups Muter (rgthree), Fast Groups Bypasser (rgthree), PreviewAny, TextEncodeQwenImage21, TextGenerate, KSampler, PrimitiveInt, ComfySwitchNode, PrimitiveInt, MarkdownNote, MarkdownNote, MarkdownNote, LoraLoaderModelOnly, ComfySwitchNode, Reroute, VAEDecode, SaveImage, PrimitiveBoolean, PrimitiveStringMultiline, ResolutionSelector, ComfySwitchNode, PathchSageAttentionKJ, QwenImage21Cache]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1038303222157694, "steps": 40, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1 多合一图像编辑 加速工作流 V1.5_2104920188973051905.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 多合一图像编辑 加速工作流 V1.5_2104920188973051905.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（62 个）：
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `Seed (rgthree)`
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `MarkdownNote`
- `ImageConcanate`
- `Any Switch (rgthree)`
- `VAELoader`
- `CLIPLoader`
- `PrimitiveStringMultiline`
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
- `LoadImage`
- `ImageScaleToTotalPixels`
- `UNETLoader` ★核心
- `Note`
- `MarkdownNote`
- `MarkdownNote`
- `SaveImageAdvanced`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `ComfySwitchNode`
- `Fast Bypasser (rgthree)`
- `CLIPLoader`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `TextGenerate`
- `KSampler` ★核心
- `PrimitiveInt`
- `ComfySwitchNode`
- `PrimitiveInt`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `ComfySwitchNode`
- `Reroute`
- `VAEDecode` ★核心
- `SaveImage`
- `PrimitiveBoolean`
- `PrimitiveStringMultiline`
- `ResolutionSelector`
- `ComfySwitchNode`
- `PathchSageAttentionKJ`
- `QwenImage21Cache`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `1038303222157694`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **61%**（38/62）

**有卡**：`EmptyLatentImage`、`Seed (rgthree)`、`ImageScaleToTotalPixels`、`ImageConcanate`、`VAELoader`、`CLIPLoader`、`ImageConcatMulti`、`LoadImage`、`UNETLoader`、`SaveImageAdvanced`、`Fast Bypasser (rgthree)`、`TextEncodeQwenImage21`、`TextGenerate`、`KSampler`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`PrimitiveBoolean`、`ResolutionSelector`、`PathchSageAttentionKJ`、`QwenImage21Cache`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、ResolutionSelector
