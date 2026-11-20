---
key: 平台全量/多图编辑 去水印+换装换脸高清修复 QwenEdit最新图像编辑换装全能图片2.0_2039222441611894786.json
name: 多图编辑 去水印+换装换脸高清修复 QwenEdit最新图像编辑换装全能图片2.0_2039222441611894786
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/多图编辑 去水印+换装换脸高清修复 QwenEdit最新图像编辑换装全能图片2.0_2039222441611894786.json
hash: 92eca359b1cdc14c
coverage: 0.954545
learned_at: 2026-11-14 01:57:38
nodes: [CLIPLoader, UNETLoader, VAELoader, ModelSamplingAuraFlow, CFGNorm, LoraLoaderModelOnly, VAEDecode, FluxKontextMultiReferenceLatentMethod, FluxKontextMultiReferenceLatentMethod, VAEEncode, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, ImageConcanate, CR Text, ImageScaleToTotalPixels, SaveImage, SaveImage, ImageConcanate, Fast Groups Bypasser (rgthree), LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 961052179702201, "steps": 4}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/多图编辑 去水印+换装换脸高清修复 QwenEdit最新图像编辑换装全能图片2.0_2039222441611894786.json

> 来源文件 `comfyui_library/workflows/平台全量/多图编辑 去水印+换装换脸高清修复 QwenEdit最新图像编辑换装全能图片2.0_2039222441611894786.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `CLIPLoader`
- `UNETLoader` ★核心
- `VAELoader`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `LoraLoaderModelOnly` ★核心
- `VAEDecode` ★核心
- `FluxKontextMultiReferenceLatentMethod`
- `FluxKontextMultiReferenceLatentMethod`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `ImageConcanate`
- `CR Text`
- `ImageScaleToTotalPixels`
- `SaveImage`
- `SaveImage`
- `ImageConcanate`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `961052179702201`
- `steps` = `4`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **95%**（21/22）

**有卡**：`CLIPLoader`、`UNETLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`LoraLoaderModelOnly`、`VAEDecode`、`FluxKontextMultiReferenceLatentMethod`、`VAEEncode`、`TextEncodeQwenImageEditPlus`、`KSampler`、`ImageConcanate`、`CR Text`、`ImageScaleToTotalPixels`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
