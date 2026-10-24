---
key: 图片生成/图生图/林茜数字人_Qwen 2.1 Turbo换脸工作流_2112478289444036610.json
name: 林茜数字人_Qwen 2.1 Turbo换脸工作流_2112478289444036610
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/林茜数字人_Qwen 2.1 Turbo换脸工作流_2112478289444036610.json
hash: 525aee55cccfa4da
coverage: 0.730769
learned_at: 2026-10-23 13:09:47
nodes: [MarkdownNote, MarkdownNote, EmptyLatentImage, ComfySwitchNode, QwenImage21Cache, CLIPLoader, ComfySwitchNode, BatchImagesNode, TextGenerate, ManualSigmas, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, CFGGuider, PrimitiveStringMultiline, PreviewAny, TextEncodeQwenImage21, LoadImage, VAEDecode, ImageScaleToTotalPixels, VAELoader, CLIPLoader, UNETLoader, LoraLoaderModelOnly, SaveImage, Image Comparer (rgthree)]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/林茜数字人_Qwen 2.1 Turbo换脸工作流_2112478289444036610.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/林茜数字人_Qwen 2.1 Turbo换脸工作流_2112478289444036610.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `MarkdownNote`
- `MarkdownNote`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `CLIPLoader`
- `ComfySwitchNode`
- `BatchImagesNode`
- `TextGenerate`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `TextEncodeQwenImage21`
- `LoadImage`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `VAELoader`
- `CLIPLoader`
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `SaveImage`
- `Image Comparer (rgthree)`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **73%**（19/26）

**有卡**：`EmptyLatentImage`、`QwenImage21Cache`、`CLIPLoader`、`BatchImagesNode`、`TextGenerate`、`ManualSigmas`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`CFGGuider`、`TextEncodeQwenImage21`、`LoadImage`、`VAEDecode`、`ImageScaleToTotalPixels`、`VAELoader`、`UNETLoader`、`LoraLoaderModelOnly`、`SaveImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache
