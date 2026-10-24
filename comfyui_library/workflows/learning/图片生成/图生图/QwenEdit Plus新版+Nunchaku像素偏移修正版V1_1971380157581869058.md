---
key: 图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V1_1971380157581869058.json
name: QwenEdit Plus新版+Nunchaku像素偏移修正版V1_1971380157581869058
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V1_1971380157581869058.json
hash: 7b43e73f6a32a0a3
coverage: 0.863636
learned_at: 2026-10-23 11:20:06
nodes: [ModelSamplingAuraFlow, SaveImage, VAELoader, CLIPLoader, ImageScaleToTotalPixels, TextEncodeQwenImageEdit, EmptySD3LatentImage, Note, LoraLoaderModelOnly, CFGNorm, NunchakuQwenImageDiTLoader, ImageStitch, KSampler, DF_Get_image_size, VAEEncode, TextEncodeQwenImageEditPlus_lrzjason, CR Prompt Text, VAEDecode, LoadImage, Image Comparer (rgthree), PreviewImage, SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 113887565438823, "steps": 20}
---

# 图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V1_1971380157581869058.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V1_1971380157581869058.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（22 个）：
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAELoader`
- `CLIPLoader`
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImageEdit`
- `EmptySD3LatentImage`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `NunchakuQwenImageDiTLoader`
- `ImageStitch`
- `KSampler` ★核心
- `DF_Get_image_size`
- `VAEEncode` ★核心
- `TextEncodeQwenImageEditPlus_lrzjason`
- `CR Prompt Text`
- `VAEDecode` ★核心
- `LoadImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `113887565438823`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（19/22）

**有卡**：`ModelSamplingAuraFlow`、`SaveImage`、`VAELoader`、`CLIPLoader`、`ImageScaleToTotalPixels`、`TextEncodeQwenImageEdit`、`EmptySD3LatentImage`、`LoraLoaderModelOnly`、`CFGNorm`、`NunchakuQwenImageDiTLoader`、`ImageStitch`、`KSampler`、`DF_Get_image_size`、`VAEEncode`、`TextEncodeQwenImageEditPlus_lrzjason`、`CR Prompt Text`、`VAEDecode`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEdit
