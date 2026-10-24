---
key: 图片生成/图生图/[🛫书墨]小红书FireRed-Image-edit1.1_一至三图任意切换_2029240103347949569.json
name: [🛫书墨]小红书FireRed-Image-edit1.1_一至三图任意切换_2029240103347949569
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/[🛫书墨]小红书FireRed-Image-edit1.1_一至三图任意切换_2029240103347949569.json
hash: 408a3662768ec7af
coverage: 0.777778
learned_at: 2026-10-23 11:33:29
nodes: [MarkdownNote, LoadImage, FluxKontextImageScale, FluxKontextImageScale, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, easy int, Image Comparer (rgthree), Any Switch (rgthree), PreviewImage, FluxKontextImageScale, Any Switch (rgthree), CR SDXL Aspect Ratio, TextEncodeQwenImageEditPlus, TextEncodeQwenImageEditPlus, KSampler, LoraLoaderModelOnly, LoadImage, VAEDecode, SaveImage, UNETLoader, CLIPLoader, VAELoader, Fast Groups Muter (rgthree), Fast Groups Muter (rgthree), ModelSamplingAuraFlow, CFGNorm, LoadImage, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageMaskScaleAsV2, LayerUtility: ImageMaskScaleAsV2, Image Batch, CR Image Grid Panel, AddLabel, PrimitiveStringMultiline, KOOK_SaveJPGImage]
patterns: [image_to_image]
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 669770838291426, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 图片生成/图生图/[🛫书墨]小红书FireRed-Image-edit1.1_一至三图任意切换_2029240103347949569.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/[🛫书墨]小红书FireRed-Image-edit1.1_一至三图任意切换_2029240103347949569.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（36 个）：
- `MarkdownNote`
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
- `CR SDXL Aspect Ratio`
- `TextEncodeQwenImageEditPlus`
- `TextEncodeQwenImageEditPlus`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `VAEDecode` ★核心
- `SaveImage`
- `UNETLoader` ★核心
- `CLIPLoader`
- `VAELoader`
- `Fast Groups Muter (rgthree)`
- `Fast Groups Muter (rgthree)`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `LoadImage`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageMaskScaleAsV2`
- `LayerUtility: ImageMaskScaleAsV2`
- `Image Batch`
- `CR Image Grid Panel`
- `AddLabel`
- `PrimitiveStringMultiline`
- `KOOK_SaveJPGImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `669770838291426`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **78%**（28/36）

**有卡**：`LoadImage`、`FluxKontextImageScale`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy int`、`CR SDXL Aspect Ratio`、`TextEncodeQwenImageEditPlus`、`KSampler`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`、`UNETLoader`、`CLIPLoader`、`VAELoader`、`ModelSamplingAuraFlow`、`CFGNorm`、`LayerUtility: ImageMaskScaleAsV2`、`Image Batch`、`CR Image Grid Panel`、`AddLabel`、`KOOK_SaveJPGImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
