---
key: 平台全量/qwen-image2.1图像编辑_2115372324064157697.json
name: qwen-image2.1图像编辑_2115372324064157697
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/qwen-image2.1图像编辑_2115372324064157697.json
hash: 51aaed96244f52a7
coverage: 0.782609
learned_at: 2026-11-14 01:16:25
nodes: [UNETLoader, CLIPLoader, VAELoader, VAEDecode, KSampler, ComfySwitchNode, QwenImage21Cache, TextEncodeQwenImage21, CLIPLoader, PrimitiveStringMultiline, PreviewAny, ComfySwitchNode, BatchImagesNode, TextGenerate, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, Image Comparer (rgthree), TextInputNode, SaveImage, ResolutionSelector, EmptyLatentImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 1027502758043795, "steps": 25, "width": 1024}
---

# 平台全量/qwen-image2.1图像编辑_2115372324064157697.json

> 来源文件 `comfyui_library/workflows/平台全量/qwen-image2.1图像编辑_2115372324064157697.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（23 个）：
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `VAEDecode` ★核心
- `KSampler` ★核心
- `ComfySwitchNode`
- `QwenImage21Cache`
- `TextEncodeQwenImage21`
- `CLIPLoader`
- `PrimitiveStringMultiline`
- `PreviewAny`
- `ComfySwitchNode`
- `BatchImagesNode`
- `TextGenerate`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `TextInputNode`
- `SaveImage`
- `ResolutionSelector`
- `EmptyLatentImage` ★核心

## 关键参数

- `seed` = `1027502758043795`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **78%**（18/23）

**有卡**：`UNETLoader`、`CLIPLoader`、`VAELoader`、`VAEDecode`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`BatchImagesNode`、`TextGenerate`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`TextInputNode`、`SaveImage`、`ResolutionSelector`、`EmptyLatentImage`

**用到的条目**：KSampler、TextEncodeQwenImage21、VAEDecode、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
