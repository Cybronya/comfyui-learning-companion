---
key: 平台全量/FireRed-Image-edit1.1内衣虚拟试衣(lora版)_2104408381980237826.json
name: FireRed-Image-edit1.1内衣虚拟试衣(lora版)_2104408381980237826
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/FireRed-Image-edit1.1内衣虚拟试衣(lora版)_2104408381980237826.json
hash: b34169a843646d8f
coverage: 0.875
learned_at: 2026-11-14 00:26:44
nodes: [VAEEncode, Any Switch (rgthree), TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, VAELoader, ModelSamplingAuraFlow, CFGNorm, PreviewImage, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ImageStitch, LoadImage, LoadImage, LoadImage, easy int, easy int, easy positive, SaveImage, VAEDecode, LayerUtility: PurgeVRAM, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, UnetLoaderGGUF, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ImageStitch, SaveImage, ImageScale, CLIPLoader]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 928082820217048, "steps": 6}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/FireRed-Image-edit1.1内衣虚拟试衣(lora版)_2104408381980237826.json

> 来源文件 `comfyui_library/workflows/平台全量/FireRed-Image-edit1.1内衣虚拟试衣(lora版)_2104408381980237826.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（32 个）：
- `VAEEncode` ★核心
- `Any Switch (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `PreviewImage`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ImageStitch`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `easy int`
- `easy int`
- `easy positive`
- `SaveImage`
- `VAEDecode` ★核心
- `LayerUtility: PurgeVRAM`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ImageStitch`
- `SaveImage`
- `ImageScale`
- `CLIPLoader`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `928082820217048`
- `steps` = `6`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **88%**（28/32）

**有卡**：`VAEEncode`、`TextEncodeQwenImageEditPlus`、`KSampler`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageStitch`、`LoadImage`、`easy int`、`easy positive`、`SaveImage`、`VAEDecode`、`LayerUtility: PurgeVRAM`、`LoraLoaderModelOnly`、`UNETLoader`、`UnetLoaderGGUF`、`ImageScale`、`CLIPLoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、UNETLoader、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
