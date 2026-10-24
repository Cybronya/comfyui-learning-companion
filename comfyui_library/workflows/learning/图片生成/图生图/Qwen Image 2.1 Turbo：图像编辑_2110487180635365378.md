---
key: 图片生成/图生图/Qwen Image 2.1 Turbo：图像编辑_2110487180635365378.json
name: Qwen Image 2.1 Turbo：图像编辑_2110487180635365378
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 Turbo：图像编辑_2110487180635365378.json
hash: 7b95c20e47901fdc
coverage: 0.703704
learned_at: 2026-10-23 11:12:38
nodes: [MarkdownNote, MarkdownNote, MarkdownNote, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, VAEDecode, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, CLIPLoader, PrimitiveStringMultiline, PreviewAny, BatchImagesNode, ManualSigmas, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, CFGGuider, ImageCompare, SaveImage, SaveImageAdvanced, ComfySwitchNode, TextGenerate, JjkText, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 图片生成/图生图/Qwen Image 2.1 Turbo：图像编辑_2110487180635365378.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen Image 2.1 Turbo：图像编辑_2110487180635365378.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `MarkdownNote`
- `MarkdownNote`
- `MarkdownNote`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `BatchImagesNode`
- `ManualSigmas`
- `KSamplerSelect` ★核心
- `RandomNoise`
- `SamplerCustomAdvanced` ★核心
- `CFGGuider`
- `ImageCompare`
- `SaveImage`
- `SaveImageAdvanced`
- `ComfySwitchNode`
- `TextGenerate`
- `JjkText`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **70%**（19/27）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`VAEDecode`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`BatchImagesNode`、`ManualSigmas`、`KSamplerSelect`、`RandomNoise`、`SamplerCustomAdvanced`、`CFGGuider`、`ImageCompare`、`SaveImage`、`SaveImageAdvanced`、`TextGenerate`、`LoadImage`

**用到的条目**：VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、LoadImage、QwenImage21Cache、UNETLoader
