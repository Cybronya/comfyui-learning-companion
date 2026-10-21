---
key: 图片生成/图生图/qwen2.1移除rgba背景｜图生图透明通道处理利器_2104569513869135873.json
name: qwen2.1移除rgba背景｜图生图透明通道处理利器_2104569513869135873
type: Text To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/qwen2.1移除rgba背景｜图生图透明通道处理利器_2104569513869135873.json
hash: 9e878f3740459193
coverage: 0.88785
learned_at: 2026-10-21 00:46:13
nodes: [CLIPLoader, VAELoader, QwenImage21Cache, KSampler, easy seed, UNETLoader, VAEDecode, ComfySwitchNode, StringFunction|pysssss, PreviewAny, BatchImagesNode, StringConstantMultiline, CLIPLoader, PreviewAny, TextGenerate, EmptyLatentImage, StringReplace, TextEncodeQwenImage21, ResolutionSelector, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LoadImage, FluxKontextImageScale, LoadImage, LayerUtility: ImageScaleByAspectRatio V2, CLIPLoader, VAELoader, QwenImage21Cache, KSampler, easy seed, UNETLoader, VAEDecode, ComfySwitchNode, StringFunction|pysssss, PreviewAny, BatchImagesNode, StringConstantMultiline, CLIPLoader, PreviewAny, TextGenerate, EmptyLatentImage, StringReplace, LoadImage, TextEncodeQwenImage21, ResolutionSelector, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadImage, LoadImage, Image Comparer (rgthree), SaveImage, FluxKontextImageScale, LoadImage, StringConstantMultiline, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, Image Comparer (rgthree), SaveImage, StringConstantMultiline, 孤海注释, 孤海注释, UNETLoader, CLIPLoader, CLIPTextEncode, VAELoader, EmptyLatentImage, KSampler, VAEDecode, solarL_SaveImagesToZip, JjkText, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, LoraLoaderModelOnly, CLIPTextEncode, Note]
patterns: [text_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"batch_size": 1, "cfg": 4.5, "denoise": 1, "height": 80, "sampler_name": "er_sde", "scheduler": "beta", "seed": 598626327129635, "steps": 4, "width": 80}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/qwen2.1移除rgba背景｜图生图透明通道处理利器_2104569513869135873.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/qwen2.1移除rgba背景｜图生图透明通道处理利器_2104569513869135873.json`

## 结构

**生成流程**：Model → Condition → Latent → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
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
- `孤海注释`
- `孤海注释`
- `UNETLoader` ★核心
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `EmptyLatentImage` ★核心
- `KSampler` ★核心
- `VAEDecode` ★核心
- `solarL_SaveImagesToZip`
- `JjkText`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `Note`

**识别到的模式**：text_to_image

## 关键参数

- `seed` = `598626327129635`
- `steps` = `4`
- `cfg` = `4.5`
- `sampler_name` = `er_sde`
- `scheduler` = `beta`
- `denoise` = `1`
- `width` = `80`
- `height` = `80`
- `batch_size` = `1`

## 知识

覆盖率 **89%**（95/107）

**有卡**：`CLIPLoader`、`VAELoader`、`QwenImage21Cache`、`KSampler`、`easy seed`、`UNETLoader`、`VAEDecode`、`StringFunction|pysssss`、`BatchImagesNode`、`StringConstantMultiline`、`TextGenerate`、`EmptyLatentImage`、`StringReplace`、`TextEncodeQwenImage21`、`ResolutionSelector`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`FluxKontextImageScale`、`SaveImage`、`CLIPTextEncode`、`solarL_SaveImagesToZip`、`LoraLoaderModelOnly`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
