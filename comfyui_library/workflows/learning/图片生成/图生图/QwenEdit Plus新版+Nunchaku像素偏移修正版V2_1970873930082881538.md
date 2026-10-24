---
key: 图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V2_1970873930082881538.json
name: QwenEdit Plus新版+Nunchaku像素偏移修正版V2_1970873930082881538
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V2_1970873930082881538.json
hash: 89215980b7006ecb
coverage: 0.857143
learned_at: 2026-10-23 11:20:06
nodes: [ModelSamplingAuraFlow, SaveImage, VAELoader, CLIPLoader, LoadImage, ImageScaleToTotalPixels, TextEncodeQwenImageEdit, EmptySD3LatentImage, VAEDecode, PreviewImage, Image Comparer (rgthree), Note, LoraLoaderModelOnly, CFGNorm, NunchakuQwenImageDiTLoader, ImageStitch, KSampler, DF_Get_image_size, VAEEncode, CR Prompt Text, TextEncodeQwenImageEditPlus_lrzjason]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1022602540247473, "steps": 20}
---

# 图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V2_1970873930082881538.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/QwenEdit Plus新版+Nunchaku像素偏移修正版V2_1970873930082881538.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（21 个）：
- `ModelSamplingAuraFlow`
- `SaveImage`
- `VAELoader`
- `CLIPLoader`
- `LoadImage`
- `ImageScaleToTotalPixels`
- `TextEncodeQwenImageEdit`
- `EmptySD3LatentImage`
- `VAEDecode` ★核心
- `PreviewImage`
- `Image Comparer (rgthree)`
- `Note`
- `LoraLoaderModelOnly` ★核心
- `CFGNorm`
- `NunchakuQwenImageDiTLoader`
- `ImageStitch`
- `KSampler` ★核心
- `DF_Get_image_size`
- `VAEEncode` ★核心
- `CR Prompt Text`
- `TextEncodeQwenImageEditPlus_lrzjason`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1022602540247473`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **86%**（18/21）

**有卡**：`ModelSamplingAuraFlow`、`SaveImage`、`VAELoader`、`CLIPLoader`、`LoadImage`、`ImageScaleToTotalPixels`、`TextEncodeQwenImageEdit`、`EmptySD3LatentImage`、`VAEDecode`、`LoraLoaderModelOnly`、`CFGNorm`、`NunchakuQwenImageDiTLoader`、`ImageStitch`、`KSampler`、`DF_Get_image_size`、`VAEEncode`、`CR Prompt Text`、`TextEncodeQwenImageEditPlus_lrzjason`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPLoader、LoadImage、CFGNorm、TextEncodeQwenImageEdit
