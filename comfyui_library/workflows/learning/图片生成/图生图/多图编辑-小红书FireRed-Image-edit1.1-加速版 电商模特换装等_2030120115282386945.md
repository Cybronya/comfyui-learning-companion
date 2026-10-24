---
key: 图片生成/图生图/多图编辑-小红书FireRed-Image-edit1.1-加速版 电商模特换装等_2030120115282386945.json
name: 多图编辑-小红书FireRed-Image-edit1.1-加速版 电商模特换装等_2030120115282386945
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多图编辑-小红书FireRed-Image-edit1.1-加速版 电商模特换装等_2030120115282386945.json
hash: 847aa67451c4525b
coverage: 0.77551
learned_at: 2026-10-23 12:45:12
nodes: [ModelSamplingAuraFlow, ImageConcatMulti, ImageConcatMulti, UNETLoader, CLIPLoader, VAELoader, CFGNorm, FluxKontextImageScale, FluxKontextImageScale, LoadImage, LoadImage, Reroute, AddLabel, VAEDecode, Reroute, Reroute, Reroute, Reroute, Reroute, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, CR Prompt Text, LoadImage, easy int, MarkdownNote, MarkdownNote, LoadImage, MarkdownNote, KSampler, LoraLoaderModelOnly, CLIPLoader, VAELoader, EmptySD3LatentImage, UNETLoader, CR Text Concatenate, LoraLoaderModelOnly, CLIPTextEncode, CLIPTextEncode, ModelSamplingAuraFlow, KSampler, CR Text, CR Text, VAEDecode, PreviewImage, SaveImage, Image Comparer (rgthree), KOOK_SaveJPGImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "res_multistep", "scheduler": "simple", "seed": 112918600386067, "steps": 25}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/多图编辑-小红书FireRed-Image-edit1.1-加速版 电商模特换装等_2030120115282386945.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多图编辑-小红书FireRed-Image-edit1.1-加速版 电商模特换装等_2030120115282386945.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（49 个）：
- `ModelSamplingAuraFlow`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `CFGNorm`
- `FluxKontextImageScale`
- `FluxKontextImageScale`
- `LoadImage`
- `LoadImage`
- `Reroute`
- `AddLabel`
- `VAEDecode` ★核心
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Prompt Text`
- `LoadImage`
- `easy int`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `CLIPLoader`
- `VAELoader`
- `EmptySD3LatentImage`
- `UNETLoader` ★核心
- `CR Text Concatenate`
- `LoraLoaderModelOnly` ★核心
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `ModelSamplingAuraFlow`
- `KSampler` ★核心
- `CR Text`
- `CR Text`
- `VAEDecode` ★核心
- `PreviewImage`
- `SaveImage`
- `Image Comparer (rgthree)`
- `KOOK_SaveJPGImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `112918600386067`
- `steps` = `25`
- `cfg` = `4`
- `sampler_name` = `res_multistep`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（38/49）

**有卡**：`ModelSamplingAuraFlow`、`ImageConcatMulti`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGNorm`、`FluxKontextImageScale`、`LoadImage`、`AddLabel`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Prompt Text`、`easy int`、`KSampler`、`LoraLoaderModelOnly`、`EmptySD3LatentImage`、`CR Text Concatenate`、`CLIPTextEncode`、`CR Text`、`SaveImage`、`KOOK_SaveJPGImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、CLIPLoader、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
