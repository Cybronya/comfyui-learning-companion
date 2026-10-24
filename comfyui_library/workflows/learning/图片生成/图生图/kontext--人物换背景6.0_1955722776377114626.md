---
key: 图片生成/图生图/kontext--人物换背景6.0_1955722776377114626.json
name: kontext--人物换背景6.0_1955722776377114626
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/kontext--人物换背景6.0_1955722776377114626.json
hash: ee34b2d693872fe7
coverage: 0.866667
learned_at: 2026-10-23 11:39:00
nodes: [CLIPTextEncode, EmptySD3LatentImage, FluxGuidance, ReferenceLatent, LayerUtility: ImageReelComposit, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, GetImageSize+, KSampler, Reroute, CLIPTextEncode, CR Text, CR Text, VAEEncode, PreviewImage, easy promptConcat, FluxKontextImageScale, ImageStitch, FluxKontextImageScale, easy imageRemBg, PreviewImage, KSampler, VAEDecode, VAEDecode, CLIPTextEncode, FluxGuidance, ConditioningZeroOut, ReferenceLatent, VAEEncode, ImageResize+, LayerUtility: ImageReel, PreviewImage, PreviewImage, LoraLoaderModelOnly, UnetLoaderGGUF, VAELoader, DualCLIPLoader, Anything Everywhere3, easy seed, LoadImage, SaveImage, FloatSlider, LoadImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 774685737890535, "steps": 20}
---

# 图片生成/图生图/kontext--人物换背景6.0_1955722776377114626.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/kontext--人物换背景6.0_1955722776377114626.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `CLIPTextEncode` ★核心
- `EmptySD3LatentImage`
- `FluxGuidance`
- `ReferenceLatent`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSize+`
- `KSampler` ★核心
- `Reroute`
- `CLIPTextEncode` ★核心
- `CR Text`
- `CR Text`
- `VAEEncode` ★核心
- `PreviewImage`
- `easy promptConcat`
- `FluxKontextImageScale`
- `ImageStitch`
- `FluxKontextImageScale`
- `easy imageRemBg`
- `PreviewImage`
- `KSampler` ★核心
- `VAEDecode` ★核心
- `VAEDecode` ★核心
- `CLIPTextEncode` ★核心
- `FluxGuidance`
- `ConditioningZeroOut`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `ImageResize+`
- `LayerUtility: ImageReel`
- `PreviewImage`
- `PreviewImage`
- `LoraLoaderModelOnly` ★核心
- `UnetLoaderGGUF` ★核心
- `VAELoader`
- `DualCLIPLoader`
- `Anything Everywhere3`
- `easy seed`
- `LoadImage`
- `SaveImage`
- `FloatSlider`
- `LoadImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `774685737890535`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **87%**（39/45）

**有卡**：`CLIPTextEncode`、`EmptySD3LatentImage`、`FluxGuidance`、`ReferenceLatent`、`LayerUtility: ImageReelComposit`、`LayerUtility: PurgeVRAM`、`LayerUtility: ImageScaleByAspectRatio V2`、`GetImageSize+`、`KSampler`、`CR Text`、`VAEEncode`、`easy promptConcat`、`FluxKontextImageScale`、`ImageStitch`、`easy imageRemBg`、`VAEDecode`、`ConditioningZeroOut`、`ImageResize+`、`LayerUtility: ImageReel`、`LoraLoaderModelOnly`、`UnetLoaderGGUF`、`VAELoader`、`DualCLIPLoader`、`easy seed`、`LoadImage`、`SaveImage`、`FloatSlider`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、ConditioningZeroOut、LoadImage、LayerUtility: ImageScaleByAspectRatio V2
