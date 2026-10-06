---
key: 图片生成/文生图/Qwen Image2.1 图生图任意角度转换_2105224018495369217.json
name: Qwen Image2.1 图生图任意角度转换_2105224018495369217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1 图生图任意角度转换_2105224018495369217.json
hash: 1e5850c552c66189
coverage: 0.823529
learned_at: 2026-10-06 22:57:43
nodes: [MarkdownNote, LoadBackgroundRemovalModel, RemoveBackground, InvertMask, TripoSplatPreprocessImage, PreviewImage, UNETLoader, CLIPVisionLoader, VAELoader, VAELoader, TripoSplatConditioning, KSampler, VAEDecodeTripoSplat, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, MarkdownNote, ComfySwitchNode, SaveImage, CreateCameraInfo, LoraLoaderModelOnly, RenderSplat, GetImageSize, ImageScaleToMaxDimension, MarkdownNote, LoadImage, SaveImage, ImageConcanate, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 20260930, "steps": 24}
---

# 图片生成/文生图/Qwen Image2.1 图生图任意角度转换_2105224018495369217.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1 图生图任意角度转换_2105224018495369217.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（34 个）：
- `MarkdownNote`
- `LoadBackgroundRemovalModel`
- `RemoveBackground`
- `InvertMask`
- `TripoSplatPreprocessImage`
- `PreviewImage`
- `UNETLoader` ★核心
- `CLIPVisionLoader`
- `VAELoader`
- `VAELoader`
- `TripoSplatConditioning`
- `KSampler` ★核心
- `VAEDecodeTripoSplat` ★核心
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `MarkdownNote`
- `ComfySwitchNode`
- `SaveImage`
- `CreateCameraInfo`
- `LoraLoaderModelOnly` ★核心
- `RenderSplat`
- `GetImageSize`
- `ImageScaleToMaxDimension`
- `MarkdownNote`
- `LoadImage`
- `SaveImage`
- `ImageConcanate`
- `SaveImage`

## 关键参数

- `seed` = `20260930`
- `steps` = `24`
- `cfg` = `3`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`LoadBackgroundRemovalModel`、`RemoveBackground`、`InvertMask`、`TripoSplatPreprocessImage`、`UNETLoader`、`CLIPVisionLoader`、`VAELoader`、`TripoSplatConditioning`、`KSampler`、`VAEDecodeTripoSplat`、`CLIPLoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`VAEDecode`、`SaveImage`、`CreateCameraInfo`、`LoraLoaderModelOnly`、`RenderSplat`、`GetImageSize`、`ImageScaleToMaxDimension`、`LoadImage`、`ImageConcanate`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、QwenImage21Cache
