---
key: 图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V2_1971610645382819842.json
name: QwenEdit Plus新版+Nunchaku像素偏移修正版V2_1971610645382819842
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V2_1971610645382819842.json
hash: b0b5891f938c7e3e
coverage: 0.857143
learned_at: 2026-10-23 11:20:06
nodes: [ModelSamplingAuraFlow, SaveImage, VAELoader, CLIPLoader, TextEncodeQwenImageEdit, EmptySD3LatentImage, VAEDecode, Image Comparer (rgthree), Note, LoraLoaderModelOnly, CFGNorm, DF_Get_image_size, VAEEncode, LoadImage, CR Prompt Text, NunchakuQwenImageDiTLoader, KSampler, ImageScaleToTotalPixels, PreviewImage, ImageStitch, TextEncodeQwenImageEditPlus_lrzjason]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 175170549121376, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V2_1971610645382819842.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V2_1971610645382819842.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAELoader`
- `CLIPLoader`
- `TextEncodeQwenImageEdit`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `DF_Get_image_size`
- `VAEEncode` ★核心
- `LoadImage`
- `CR Prompt Text`
- `NunchakuQwenImageDiTLoader`
- `KSampler` ★核心
- `ImageScaleToTotalPixels`
- `PreviewImage`
- `ImageStitch`
- `TextEncodeQwenImageEditPlus_lrzjason`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `175170549121376`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`ModelSamplingAuraFlow`、`SaveImage`、`VAELoader`、`CLIPLoader`、`TextEncodeQwenImageEdit`、`EmptySD3LatentImage`、`VAEDecode`、`LoraLoaderModelOnly`、`CFGNorm`、`DF_Get_image_size`、`VAEEncode`、`LoadImage`、`CR Prompt Text`、`NunchakuQwenImageDiTLoader`、`KSampler`、`ImageScaleToTotalPixels`、`ImageStitch`、`TextEncodeQwenImageEditPlus_lrzjason`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEdit

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
