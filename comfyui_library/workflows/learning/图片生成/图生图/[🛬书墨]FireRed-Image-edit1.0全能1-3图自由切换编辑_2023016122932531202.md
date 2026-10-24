---
key: 图片生成/图生图/[🛬书墨]FireRed-Image-edit1.0全能1-3图自由切换编辑_2023016122932531202.json
name: [🛬书墨]FireRed-Image-edit1.0全能1-3图自由切换编辑_2023016122932531202
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/[🛬书墨]FireRed-Image-edit1.0全能1-3图自由切换编辑_2023016122932531202.json
hash: 810ff20200f5d8f4
coverage: 0.703704
learned_at: 2026-10-23 11:33:31
nodes: [LoadImage, FluxKontextImageScale, FluxKontextImageScale, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, easy int, Image Comparer (rgthree), Any Switch (rgthree), PreviewImage, FluxKontextImageScale, Any Switch (rgthree), LoadImage, CR SDXL Aspect Ratio, Fast Groups Muter (rgthree), TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, LoadImage, Fast Groups Muter (rgthree), VAEDecode, SaveImage, LoraLoaderModelOnly, UNETLoader, CLIPLoader, VAELoader, PrimitiveStringMultiline, MarkdownNote]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "FlowMatchEulerDiscreteScheduler", "seed": 341574584026307, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/[🛬书墨]FireRed-Image-edit1.0全能1-3图自由切换编辑_2023016122932531202.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/[🛬书墨]FireRed-Image-edit1.0全能1-3图自由切换编辑_2023016122932531202.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（27 个）：
- `LoadImage`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `Image Comparer (rgthree)`
- `Any Switch (rgthree)`
- `PreviewImage`
- `FluxKontextImageScale`
- `Any Switch (rgthree)`
- `LoadImage`
- `CR SDXL Aspect Ratio`
- `Fast Groups Muter (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `LoadImage`
- `Fast Groups Muter (rgthree)`
- `VAEDecode` ★核心
- `SaveImage`
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `PrimitiveStringMultiline`
- `MarkdownNote`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `341574584026307`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `FlowMatchEulerDiscreteScheduler`
- `denoise` = `1`

## 知识

覆盖率 **70%**（19/27）

**有卡**：`LoadImage`、`FluxKontextImageScale`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`CR SDXL Aspect Ratio`、`TextEncodeQwenImageEditPlus`、`KSampler`、`VAEDecode`、`SaveImage`、`LoraLoaderModelOnly`、`UNETLoader`、`CLIPLoader`、`VAELoader`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、TextEncodeQwenImageEditPlus

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
