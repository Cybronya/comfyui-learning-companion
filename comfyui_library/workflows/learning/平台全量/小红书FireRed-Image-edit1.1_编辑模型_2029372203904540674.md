---
key: 平台全量/小红书FireRed-Image-edit1.1_编辑模型_2029372203904540674.json
name: 小红书FireRed-Image-edit1.1_编辑模型_2029372203904540674
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/小红书FireRed-Image-edit1.1_编辑模型_2029372203904540674.json
hash: c3f4d28049135c81
coverage: 0.8
learned_at: 2026-11-14 02:01:23
nodes: [LoadImage, FluxKontextImageScale, FluxKontextImageScale, VAEEncode, Image Comparer (rgthree), Any Switch (rgthree), FluxKontextImageScale, Any Switch (rgthree), TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, LoraLoaderModelOnly, LoadImage, VAEDecode, SaveImage, CLIPLoader, VAELoader, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), ModelSamplingAuraFlow, CFGNorm, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageMaskScaleAsV2, Image Batch, CR Image Grid Panel, KOOK_SaveJPGImage, LoadImage, UNETLoader, CR SDXL Aspect Ratio, LayerUtility: ImageScaleByAspectRatio V2, easy int, PreviewImage, AddLabel, PrimitiveStringMultiline]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 619524120499009, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/小红书FireRed-Image-edit1.1_编辑模型_2029372203904540674.json

> 来源文件 `comfyui_library/workflows/平台全量/小红书FireRed-Image-edit1.1_编辑模型_2029372203904540674.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
- `LoadImage`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `Image Comparer (rgthree)`
- `Any Switch (rgthree)`
- `FluxKontextImageScale`
- `Any Switch (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `CLIPLoader`
- `VAELoader`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageMaskScaleAsV2`
- `Image Batch`
- `CR Image Grid Panel`
- `KOOK_SaveJPGImage`
- `LoadImage`
- `UNETLoader` ★核心
- `CR SDXL Aspect Ratio`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `PreviewImage`
- `AddLabel`
- `PrimitiveStringMultiline`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `619524120499009`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **80%**（28/35）

**有卡**：`LoadImage`、`FluxKontextImageScale`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`KSampler`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`LayerUtility: ImageMaskScaleAsV2`、`Image Batch`、`CR Image Grid Panel`、`KOOK_SaveJPGImage`、`UNETLoader`、`CR SDXL Aspect Ratio`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`AddLabel`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
