---
key: 图片生成/图生图/Qwen-Image-2.1-遮罩局部重绘-V1_2109819371383250946.json
name: Qwen-Image-2.1-遮罩局部重绘-V1_2109819371383250946
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1-遮罩局部重绘-V1_2109819371383250946.json
hash: 93cacda3c3c48edd
coverage: 0.766667
learned_at: 2026-10-23 11:16:27
nodes: [CLIPLoader, VAELoader, KSampler, QwenImage21Cache, Seed (rgthree), VAEEncode, SetLatentNoiseMask, TextEncodeQwenImage21, Label (rgthree), UNETLoader, ComfySwitchNode, PreviewImage, DrawMaskOnImage, ComfySwitchNode, Int, Int, SimpleMath+, Image Comparer (rgthree), VAEDecode, PrimitiveStringMultiline, LoadImage, PreviewImage, InpaintStitchImproved, SimpleMath+, InpaintCropImproved, LoadImage, easy isNone, ImageScaleToTotalPixels, Image Comparer (rgthree), SaveImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 734594250377860, "steps": 25}
---

# 图片生成/图生图/Qwen-Image-2.1-遮罩局部重绘-V1_2109819371383250946.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Qwen-Image-2.1-遮罩局部重绘-V1_2109819371383250946.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（30 个）：
- `CLIPLoader`
- `VAELoader`
- `KSampler` ★核心
- `QwenImage21Cache`
- `Seed (rgthree)`
- `VAEEncode` ★核心
- `SetLatentNoiseMask`
- `TextEncodeQwenImage21`
- `Label (rgthree)`
- `UNETLoader` ★核心
- `ComfySwitchNode`
- `PreviewImage`
- `DrawMaskOnImage`
- `ComfySwitchNode`
- `Int`
- `Int`
- `SimpleMath+`
- `Image Comparer (rgthree)`
- `VAEDecode` ★核心
- `PrimitiveStringMultiline`
- `LoadImage`
- `PreviewImage`
- `InpaintStitchImproved`
- `SimpleMath+`
- `InpaintCropImproved`
- `LoadImage`
- `easy isNone`
- `ImageScaleToTotalPixels`
- `Image Comparer (rgthree)`
- `SaveImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `734594250377860`
- `steps` = `25`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **77%**（23/30）

**有卡**：`CLIPLoader`、`VAELoader`、`KSampler`、`QwenImage21Cache`、`Seed (rgthree)`、`VAEEncode`、`SetLatentNoiseMask`、`TextEncodeQwenImage21`、`Label (rgthree)`、`UNETLoader`、`DrawMaskOnImage`、`Int`、`SimpleMath+`、`VAEDecode`、`LoadImage`、`InpaintStitchImproved`、`InpaintCropImproved`、`easy isNone`、`ImageScaleToTotalPixels`、`SaveImage`

**用到的条目**：KSampler、VAEDecode、TextEncodeQwenImage21、VAELoader、CLIPLoader、LoadImage、QwenImage21Cache、UNETLoader
