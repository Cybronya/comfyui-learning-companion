---
key: 平台全量/Qwen image 2.1 Turbo 多合一图像编辑工作流 V1_2111129116396318722.json
name: Qwen image 2.1 Turbo 多合一图像编辑工作流 V1_2111129116396318722
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen image 2.1 Turbo 多合一图像编辑工作流 V1_2111129116396318722.json
hash: 931ecd996096dc41
coverage: 0.685185
learned_at: 2026-11-14 00:50:39
nodes: [EmptyLatentImage, ImageConcatMulti, ImageConcatMulti, ImageConcatMulti, MarkdownNote, MarkdownNote, Any Switch (rgthree), Any Switch (rgthree), Fast Groups Bypasser (rgthree), ImageConcanate, PrimitiveStringMultiline, ComfySwitchNode, TextEncodeQwenImage21, RandomNoise, CFGGuider, MarkdownNote, KSamplerSelect, CLIPLoader, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageConcatMulti, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, ImageScaleToTotalPixels, LoadImage, MarkdownNote, SaveImage, SaveImage, VAELoader, ComfySwitchNode, SamplerCustomAdvanced, Reroute, MarkdownNote, QwenImage21Cache, Note, Seed (rgthree), ResolutionSelector, Fast Groups Muter (rgthree), ImageScaleToTotalPixels, ImageScaleToTotalPixels, Image Comparer (rgthree), PathchSageAttentionKJ, PrimitiveStringMultiline, VAEDecode, ImageConcanate, MarkdownNote, UNETLoader, ManualSigmas]
patterns: []
missing: []
parameters: {"batch_size": 1, "height": 1024, "width": 1024}
---

# 平台全量/Qwen image 2.1 Turbo 多合一图像编辑工作流 V1_2111129116396318722.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen image 2.1 Turbo 多合一图像编辑工作流 V1_2111129116396318722.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（54 个）：
- `EmptyLatentImage` ★核心
- `ImageConcatMulti`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `MarkdownNote`
- `MarkdownNote`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `ImageConcanate`
- `PrimitiveStringMultiline`
- `ComfySwitchNode`
- `TextEncodeQwenImage21`
- `RandomNoise`
- `CFGGuider`
- `MarkdownNote`
- `KSamplerSelect` ★核心
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageConcatMulti`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `MarkdownNote`
- `SaveImage`
- `SaveImage`
- `VAELoader`
- `ComfySwitchNode`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `MarkdownNote`
- `QwenImage21Cache`
- `Note`
- `Seed (rgthree)`
- `ResolutionSelector`
- `Fast Groups Muter (rgthree)`
- `ImageScaleToTotalPixels`
- `ImageScaleToTotalPixels`
- `Image Comparer (rgthree)`
- `PathchSageAttentionKJ`
- `PrimitiveStringMultiline`
- `VAEDecode` ★核心
- `ImageConcanate`
- `MarkdownNote`
- `UNETLoader` ★核心
- `ManualSigmas`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **69%**（37/54）

**有卡**：`EmptyLatentImage`、`ImageConcatMulti`、`ImageConcanate`、`TextEncodeQwenImage21`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`CLIPLoader`、`ImageScaleToTotalPixels`、`LoadImage`、`SaveImage`、`VAELoader`、`SamplerCustomAdvanced`、`QwenImage21Cache`、`Seed (rgthree)`、`ResolutionSelector`、`PathchSageAttentionKJ`、`VAEDecode`、`UNETLoader`、`ManualSigmas`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage、QwenImage21Cache
