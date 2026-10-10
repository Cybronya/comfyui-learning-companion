---
key: 图片生成/图生图/Qwen image 2.1 多合一图像编辑 加速工作流_2102626139150831618.json
name: Qwen image 2.1 多合一图像编辑 加速工作流_2102626139150831618
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 多合一图像编辑 加速工作流_2102626139150831618.json
hash: d325338ae219f384
coverage: 0.614035
learned_at: 2026-10-10 20:48:08
nodes: [MarkdownNote, EmptyLatentImage, TextGenerate, MarkdownNote, MarkdownNote, MarkdownNote, Fast Bypasser (rgthree), MarkdownNote, Seed (rgthree), Fast Groups Bypasser (rgthree), Image Comparer (rgthree), KSampler, PathchSageAttentionKJ, QwenImage21Cache, ImageScaleToTotalPixels, PreviewAny, ImageScaleToTotalPixels, ImageScaleToTotalPixels, ImageScaleToTotalPixels, Note, MarkdownNote, VAEDecode, Fast Bypasser (rgthree), EasyCache, TextEncodeQwenImage21, Any Switch (rgthree), VAELoader, CLIPLoader, PrimitiveStringMultiline, PrimitiveStringMultiline, ResolutionSelector, ImageConcatMulti, ImageScaleToTotalPixels, LoadImage, ImageConcatMulti, ImageScaleToTotalPixels, LoadImage, ImageConcatMulti, LoadImage, ImageConcatMulti, LoadImage, ImageConcanate, LoadImage, ImageScaleToTotalPixels, LoadImage, ComfySwitchNode, ImageScaleToTotalPixels, SaveImageAdvanced, Any Switch (rgthree), Any Switch (rgthree), Fast Groups Muter (rgthree), ComfySwitchNode, MarkdownNote, UNETLoader, CLIPLoader, ImageConcanate, SaveImage]
patterns: []
missing: [Fast Bypasser (rgthree), Fast Bypasser (rgthree), Seed (rgthree)]
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 916613475229526, "steps": 40, "width": 1024}
discoveries: [次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识, 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 图片生成/图生图/Qwen image 2.1 多合一图像编辑 加速工作流_2102626139150831618.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 多合一图像编辑 加速工作流_2102626139150831618.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（57 个）：
- `MarkdownNote`
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
- `LoadImage`
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

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `916613475229526`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **61%**（35/57）

**有卡**：`EmptyLatentImage`、`TextGenerate`、`KSampler`、`PathchSageAttentionKJ`、`QwenImage21Cache`、`ImageScaleToTotalPixels`、`VAEDecode`、`EasyCache`、`TextEncodeQwenImage21`、`VAELoader`、`CLIPLoader`、`ResolutionSelector`、`ImageConcatMulti`、`LoadImage`、`ImageConcanate`、`SaveImageAdvanced`、`UNETLoader`、`SaveImage`

**缺卡**（3）：`Fast Bypasser (rgthree)`、`Fast Bypasser (rgthree)`、`Seed (rgthree)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage

## 学习发现

- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Fast Bypasser (rgthree)` 知识库中没有该节点类型的任何知识
- 次要节点 `Seed (rgthree)` 仅有 KSampler 的通用知识，没有该节点自己的说明
