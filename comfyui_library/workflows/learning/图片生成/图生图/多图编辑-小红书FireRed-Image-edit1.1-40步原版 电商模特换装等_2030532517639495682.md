---
key: 图片生成/图生图/多图编辑-小红书FireRed-Image-edit1.1-40步原版 电商模特换装等_2030532517639495682.json
name: 多图编辑-小红书FireRed-Image-edit1.1-40步原版 电商模特换装等_2030532517639495682
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/多图编辑-小红书FireRed-Image-edit1.1-40步原版 电商模特换装等_2030532517639495682.json
hash: 229687883e27a463
coverage: 0.714286
learned_at: 2026-10-23 12:45:10
nodes: [ModelSamplingAuraFlow, ImageConcatMulti, ImageConcatMulti, UNETLoader, CLIPLoader, VAELoader, CFGNorm, FluxKontextImageScale, FluxKontextImageScale, LoadImage, KOOK_SaveJPGImage, Reroute, AddLabel, SaveImage, VAEDecode, Reroute, Image Comparer (rgthree), Reroute, Reroute, Reroute, Reroute, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, easy int, MarkdownNote, MarkdownNote, LoadImage, MarkdownNote, LoraLoaderModelOnly, KSampler, LoadImage, LoadImage, CR Prompt Text]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 4, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 718116875229192, "steps": 40}
---

# 图片生成/图生图/多图编辑-小红书FireRed-Image-edit1.1-40步原版 电商模特换装等_2030532517639495682.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/多图编辑-小红书FireRed-Image-edit1.1-40步原版 电商模特换装等_2030532517639495682.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（35 个）：
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
- `KOOK_SaveJPGImage`
- `Reroute`
- `AddLabel`
- `SaveImage`
- `VAEDecode` ★核心
- `Reroute`
- `Image Comparer (rgthree)`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `MarkdownNote`
- `MarkdownNote`
- `LoadImage`
- `MarkdownNote`
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `718116875229192`
- `steps` = `40`
- `cfg` = `4`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（25/35）

**有卡**：`ModelSamplingAuraFlow`、`ImageConcatMulti`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`CFGNorm`、`FluxKontextImageScale`、`LoadImage`、`KOOK_SaveJPGImage`、`AddLabel`、`SaveImage`、`VAEDecode`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`LoraLoaderModelOnly`、`KSampler`、`CR Prompt Text`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
