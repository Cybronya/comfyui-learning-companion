---
key: 图片生成/图生图/Qwen Image 2.1 多图编辑_2104447345671888898.json
name: Qwen Image 2.1 多图编辑_2104447345671888898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 多图编辑_2104447345671888898.json
hash: b884e1091866d20f
coverage: 0.756757
learned_at: 2026-10-21 00:42:13
nodes: [CLIPLoader, BatchImagesNode, Fast Groups Bypasser (rgthree), LoadImage, ImageConcanate, VAEDecode, SaveImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, KSampler, QwenImage21Cache, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, EmptyLatentImage, TextGenerateLTX2Prompt, CLIPLoader, RH_Translator, easy showAnything, Latent Switch (JPS), ImageConcanate, TextEncodeQwenImage21, VAELoader, PreviewAny, MarkdownNote, MarkdownNote, MarkdownNote, MarkdownNote, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 多图编辑_2104447345671888898.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 多图编辑_2104447345671888898.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（37 个）：
- `CLIPLoader`
- `BatchImagesNode`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `ImageConcanate`
- `VAEDecode` ★核心
- `SaveImage`
- `SaveImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `ResolutionSelector`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `KSampler` ★核心
- `QwenImage21Cache`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `EmptyLatentImage` ★核心
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `RH_Translator`
- `easy showAnything`
- `Latent Switch (JPS)`
- `ImageConcanate`
- `TextEncodeQwenImage21`
- `VAELoader`
- `PreviewAny`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `Image Comparer (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `999`
- `steps` = `50`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **76%**（28/37）

**有卡**：`CLIPLoader`、`BatchImagesNode`、`LoadImage`、`ImageConcanate`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`TextGenerateLTX2Prompt`、`RH_Translator`、`Latent Switch (JPS)`、`TextEncodeQwenImage21`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
