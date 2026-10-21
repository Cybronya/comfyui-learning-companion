---
key: 图片生成/图生图/qwen2.1移除rgba_2103878728098082818.json
name: qwen2.1移除rgba_2103878728098082818
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1移除rgba_2103878728098082818.json
hash: 69bd57d8354d7a31
coverage: 0.875
learned_at: 2026-10-21 00:46:12
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, KSampler, easy seed, UNETLoader, VAEDecode, ComfySwitchNode, StringFunction|pysssss, PreviewAny, BatchImagesNode, StringConstantMultiline, CLIPLoader, PreviewAny, TextGenerate, EmptyLatentImage, StringReplace, TextEncodeQwenImage21, ResolutionSelector, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LoadImage, FluxKontextImageScale, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, VAELoader, QwenImage21Cache, KSampler, easy seed, UNETLoader, VAEDecode, ComfySwitchNode, StringFunction|pysssss, PreviewAny, BatchImagesNode, StringConstantMultiline, CLIPLoader, PreviewAny, TextGenerate, EmptyLatentImage, StringReplace, LoadImage, TextEncodeQwenImage21, ResolutionSelector, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LoadImage, Image Comparer (rgthree), SaveImage, FluxKontextImageScale, LoadImage, StringConstantMultiline, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Image Comparer (rgthree), SaveImage, StringConstantMultiline]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 1, "denoise": 1, "height": 1024, "sampler_name": "euler", "scheduler": "simple", "seed": 372980352069668, "steps": 40, "width": 1024}
---

# 图片生成/图生图/qwen2.1移除rgba_2103878728098082818.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1移除rgba_2103878728098082818.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（64 个）：
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `easy seed`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `StringFunction|pysssss`
- `PreviewAny`
- `BatchImagesNode`
- `StringConstantMultiline`
- `CLIPLoader`
- `PreviewAny`
- `TextGenerate`
- `EmptyLatentImage` ★核心
- `StringReplace`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `FluxKontextImageScale`
- `LoadImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CLIPLoader`
- `VAELoader`
- `QwenImage21Cache`
- `KSampler` ★核心
- `easy seed`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `ComfySwitchNode`
- `StringFunction|pysssss`
- `PreviewAny`
- `BatchImagesNode`
- `StringConstantMultiline`
- `CLIPLoader`
- `PreviewAny`
- `TextGenerate`
- `EmptyLatentImage` ★核心
- `StringReplace`
- `LoadImage`
- `TextEncodeQwenImage21`
- `ResolutionSelector`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `FluxKontextImageScale`
- `LoadImage`
- `StringConstantMultiline`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `Image Comparer (rgthree)`
- `SaveImage`
- `StringConstantMultiline`

## 关键参数

- `seed` = `372980352069668`
- `steps` = `40`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`
- `width` = `1024`
- `height` = `1024`
- `batch_size` = `1`

## 知识

覆盖率 **88%**（56/64）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`KSampler`、`easy seed`、`UNETLoader`、`VAEDecode`、`StringFunction|pysssss`、`BatchImagesNode`、`StringConstantMultiline`、`TextGenerate`、`EmptyLatentImage`、`StringReplace`、`TextEncodeQwenImage21`、`ResolutionSelector`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`FluxKontextImageScale`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、UNETLoader、CLIPLoader、EmptyLatentImage、ResolutionSelector
