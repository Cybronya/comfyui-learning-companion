---
key: 图片生成/图生图/角色换头-单人版-图生图-FireRed-image-edit1.1-换脸_2035907829818724353.json
name: 角色换头-单人版-图生图-FireRed-image-edit1.1-换脸_2035907829818724353
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/角色换头-单人版-图生图-FireRed-image-edit1.1-换脸_2035907829818724353.json
hash: 8cffe2daeee0c740
coverage: 0.961538
learned_at: 2026-10-23 13:27:10
nodes: [CLIPLoader, VAELoader, SaveImage, Image Comparer (rgthree), TextEncodeQwenImageEditPlus, VAEEncode, ModelSamplingAuraFlow, CFGNorm, LoadImage, LoadImage, UNETLoader, TextEncodeQwenImageEditPlus, SeedVR2BlockSwap, VAEDecode, LoraLoaderModelOnly, KSampler, LayerUtility: PurgeVRAM V2, SeedVR2, ClothesSegment, easy int, CR Text, LayerUtility: CropByMask V2, FluxKontextImageScale, ImageScaleToTotalPixels, FluxKontextImageScale, LayerUtility: ImageScaleByAspectRatio V2]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 437163964274405, "steps": 10}
---

# 图片生成/图生图/角色换头-单人版-图生图-FireRed-image-edit1.1-换脸_2035907829818724353.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/角色换头-单人版-图生图-FireRed-image-edit1.1-换脸_2035907829818724353.json`

## 结构

**生成流程**：Model → Encode → Sampling → Decode → Process → Output → Other

**节点**（26 个）：
- `CLIPLoader`
- `VAELoader`
- `SaveImage`
- `Image Comparer (rgthree)`
- `TextEncodeQwenImageEditPlus`
- `VAEEncode` ★核心
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `LoadImage`
- `LoadImage`
- `UNETLoader` ★核心
- `TextEncodeQwenImageEditPlus`
- `SeedVR2BlockSwap`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `LayerUtility: PurgeVRAM V2`
- `SeedVR2`
- `ClothesSegment`
- `easy int`
- `CR Text`
- `LayerUtility: CropByMask V2`
- `FluxKontextImageScale`
- `ImageScaleToTotalPixels`
- `FluxKontextImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `437163964274405`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **96%**（25/26）

**有卡**：`CLIPLoader`、`VAELoader`、`SaveImage`、`TextEncodeQwenImageEditPlus`、`VAEEncode`、`ModelSamplingAuraFlow`、`CFGNorm`、`LoadImage`、`UNETLoader`、`SeedVR2BlockSwap`、`VAEDecode`、`LoraLoaderModelOnly`、`KSampler`、`LayerUtility: PurgeVRAM V2`、`SeedVR2`、`ClothesSegment`、`easy int`、`CR Text`、`LayerUtility: CropByMask V2`、`FluxKontextImageScale`、`ImageScaleToTotalPixels`、`LayerUtility: ImageScaleByAspectRatio V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、LoadImage、CFGNorm
