---
key: 图片生成/图生图/qwen2.1图像编辑_2103878738139246594.json
name: qwen2.1图像编辑_2103878738139246594
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1图像编辑_2103878738139246594.json
hash: ecf449940bf7f24d
coverage: 0.875
learned_at: 2026-10-21 00:46:11
nodes: [QwenImage21Cache, easy seed, VAEDecode, BatchImagesNode, StringConstantMultiline, StringReplace, TextEncodeQwenImage21, ResolutionSelector, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LoadImage, Image Comparer (rgthree), FluxKontextImageScale, LayerUtility: ImageScaleByAspectRatio V2, UNETLoader, CLIPLoader, VAELoader, EmptyLatentImage, ComfySwitchNode, LoadImage, SaveImage, CLIPLoader, KSampler, TextGenerate, StringFunction|pysssss, PreviewAny, PreviewAny, StringConstantMultiline, LoadImage]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 372980352069668, "steps": 40, "width": 1024}
---

# 图片生成/图生图/qwen2.1图像编辑_2103878738139246594.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1图像编辑_2103878738139246594.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `QwenImage21Cache`
- `easy seed`
- `VAEDecode` ★核心
- `BatchImagesNode`
- `StringConstantMultiline`
- `StringReplace`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `FluxKontextImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptyLatentImage` ★核心
- `ComfySwitchNode`
- `LoadImage`
- `SaveImage`
- `CLIPLoader`
- `KSampler` ★核心
- `TextGenerate`
- `StringFunction|pysssss`
- `PreviewAny`
- `PreviewAny`
- `StringConstantMultiline`
- `LoadImage`

## 关键参数

- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`
- `seed` = `372980352069668`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`QwenImage21Cache`、`easy seed`、`VAEDecode`、`BatchImagesNode`、`StringConstantMultiline`、`StringReplace`、`TextEncodeQwenImage21`、`ResolutionSelector`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`FluxKontextImageScale`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`EmptyLatentImage`、`SaveImage`、`KSampler`、`TextGenerate`、`StringFunction|pysssss`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、UNETLoader、CLIPLoader、EmptyLatentImage、ResolutionSelector
