---
key: 图片生成/图生图/Qwen image 2.1 多图编辑_2101841037932191746.json
name: Qwen image 2.1 多图编辑_2101841037932191746
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 多图编辑_2101841037932191746.json
hash: 8fe86f5bab98c778
coverage: 0.848485
learned_at: 2026-10-21 00:42:55
nodes: [CLIPLoader, VAELoader, BatchImagesNode, Fast Groups Bypasser (rgthree), LoadImage, ImageConcanate, VAEDecode, Image Comparer (rgthree), SaveImage, SaveImage, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, ResolutionSelector, EmptyLatentImage, ComfySwitchNode, KSampler, QwenImage21Cache, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, TextEncodeQwenImage21, EmptyLatentImage, TextGenerateLTX2Prompt, CLIPLoader, RH_Translator, easy showAnything, PreviewAny, Latent Switch (JPS), ImageConcanate]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 999, "steps": 50, "width": 1024}
---

# 图片生成/图生图/Qwen image 2.1 多图编辑_2101841037932191746.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen image 2.1 多图编辑_2101841037932191746.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（33 个）：
- `CLIPLoader`
- `VAELoader`
- `BatchImagesNode`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `ImageConcanate`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
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
- `TextEncodeQwenImage21`
- `EmptyLatentImage` ★核心
- `TextGenerateLTX2Prompt`
- `CLIPLoader`
- `RH_Translator`
- `easy showAnything`
- `PreviewAny`
- `Latent Switch (JPS)`
- `ImageConcanate`

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

覆盖率 **85%**（28/33）

**有卡**：`CLIPLoader`、`VAELoader`、`BatchImagesNode`、`LoadImage`、`ImageConcanate`、`VAEDecode`、`SaveImage`、`LayerUtility: ImageScaleByAspectRatio V2`、`UNETLoader`、`ResolutionSelector`、`EmptyLatentImage`、`KSampler`、`QwenImage21Cache`、`TextEncodeQwenImage21`、`TextGenerateLTX2Prompt`、`RH_Translator`、`Latent Switch (JPS)`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、EmptyLatentImage、ResolutionSelector、LoadImage
