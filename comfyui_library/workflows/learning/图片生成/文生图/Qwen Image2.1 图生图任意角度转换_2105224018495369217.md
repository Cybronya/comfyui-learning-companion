---
key: 图片生成/文生图/Qwen Image2.1 图生图任意角度转换_2105224018495369217.json
name: Qwen Image2.1 图生图任意角度转换_2105224018495369217
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/Qwen Image2.1 图生图任意角度转换_2105224018495369217.json
hash: 1e5850c552c66189
coverage: 0.823529
learned_at: 2026-10-10 20:58:55
nodes: [MarkdownNote, LoadBackgroundRemovalModel, RemoveBackground, InvertMask, TripoSplatPreprocessImage, PreviewImage, UNETLoader, CLIPVisionLoader, VAELoader, VAELoader, TripoSplatConditioning, KSampler, VAEDecodeTripoSplat, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, TextEncodeQwenImage21, QwenImage21Cache, KSampler, VAEDecode, MarkdownNote, ComfySwitchNode, SaveImage, CreateCameraInfo, LoraLoaderModelOnly, RenderSplat, GetImageSize, ImageScaleToMaxDimension, MarkdownNote, LoadImage, SaveImage, ImageConcanate, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 3, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 20260930, "steps": 24}
---

# 图片生成/文生图/Qwen Image2.1 图生图任意角度转换_2105224018495369217.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/Qwen Image2.1 图生图任意角度转换_2105224018495369217.json`

## 结构

**节点**（34 个）：
- `MarkdownNote`
- `LoadBackgroundRemovalModel`
- `RemoveBackground`
- `InvertMask`
- `TripoSplatPreprocessImage`
- `PreviewImage`
- `UNETLoader`
- `CLIPVisionLoader`
- `VAELoader`
- `VAELoader`
- `TripoSplatConditioning`
- `KSampler`
- `VAEDecodeTripoSplat`
- `MarkdownNote`
- `UNETLoader`
- `CLIPLoader`
- `VAELoader`
- `TextEncodeQwenImage21`
- `QwenImage21Cache`
- `KSampler`
- `VAEDecode`
- `MarkdownNote`
- `ComfySwitchNode`
- `SaveImage`
- `CreateCameraInfo`
- `LoraLoaderModelOnly`
- `RenderSplat`
- `GetImageSize`
- `ImageScaleToMaxDimension`
- `MarkdownNote`
- `LoadImage`
- `SaveImage`
- `ImageConcanate`
- `SaveImage`

## 关键参数

- `cfg` = `3`
- `denoise` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `seed` = `20260930`
- `steps` = `24`

## 知识

覆盖率 **82%**（28/34）

**有卡**：`MarkdownNote`、`LoadBackgroundRemovalModel`、`RemoveBackground`、`InvertMask`、`TripoSplatPreprocessImage`、`PreviewImage`、`UNETLoader`、`CLIPVisionLoader`、`VAELoader`、`TripoSplatConditioning`、`KSampler`、`VAEDecodeTripoSplat`、`CLIPLoader`、`TextEncodeQwenImage21`、`QwenImage21Cache`、`VAEDecode`、`ComfySwitchNode`、`SaveImage`、`CreateCameraInfo`、`LoraLoaderModelOnly`、`RenderSplat`、`GetImageSize`
