---
key: 平台全量/qwen-image2.1完美去水印_2118744819949465602.json
name: qwen-image2.1完美去水印_2118744819949465602
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen-image2.1完美去水印_2118744819949465602.json
hash: 28efa9e8e1199bfd
coverage: 0.85
learned_at: 2026-11-14 01:16:26
nodes: [MarkdownNote, LoadImage, TextEncodeQwenImage21, UNETLoader, CLIPLoader, VAELoader, ImageScaleToTotalPixels, GrowMask, FeatherMask, MaskToImage, PreviewImage, RandomNoise, CFGGuider, KSamplerSelect, ManualSigmas, SamplerCustomAdvanced, VAEDecode, ImageCompositeMasked, SaveImage, Image Comparer (rgthree)]
patterns: []
missing: []
---

# 平台全量/qwen-image2.1完美去水印_2118744819949465602.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen-image2.1完美去水印_2118744819949465602.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（20 个）：
- `MarkdownNote`
- `LoadImage`
- `TextEncodeQwenImage21`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `ImageScaleToTotalPixels`
- `GrowMask`
- `FeatherMask`
- `MaskToImage`
- `PreviewImage`
- `RandomNoise`
- `CFGGuider`
- `KSamplerSelect` ★核心
- `ManualSigmas`
- `SamplerCustomAdvanced` ★核心
- `VAEDecode` ★核心
- `ImageCompositeMasked`
- `SaveImage`
- `Image Comparer (rgthree)`

## 知识

覆盖率 **85%**（17/20）

**有卡**：`LoadImage`、`TextEncodeQwenImage21`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ImageScaleToTotalPixels`、`GrowMask`、`FeatherMask`、`MaskToImage`、`RandomNoise`、`CFGGuider`、`KSamplerSelect`、`ManualSigmas`、`SamplerCustomAdvanced`、`VAEDecode`、`ImageCompositeMasked`、`SaveImage`

**用到的条目**：TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、LoadImage、UNETLoader、CFGGuider、KSamplerSelect
