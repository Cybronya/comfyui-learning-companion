---
key: 图片生成/图生图/4K高清放大 修复ttp+_+block+zoom+_+Noise_realism_2092779877316513793.json
name: 4K高清放大 修复ttp+_+block+zoom+_+Noise_realism_2092779877316513793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/4K高清放大 修复ttp+_+block+zoom+_+Noise_realism_2092779877316513793.json
hash: 3676154e6f683451
coverage: 0.822222
learned_at: 2026-10-21 00:38:30
nodes: [TTP_Image_Tile_Batch, CLIPTextEncode, ReferenceLatent, VAEEncode, BasicGuider, KSamplerSelect, BasicScheduler, easy imageListToImageBatch, easy imageBatchToImageList, SamplerCustomAdvanced, TTP_Image_Assy, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleBy, RandomNoise, VAELoader_Any, CLIPLoader_Any, UNETLoader_Any, LoraLoaderModelOnly, LayerMask: BiRefNetUltraV2, ImageScaleToTotalPixelsX, LayerMask: LoadBiRefNetModelV2, Mask Invert, easy imageColorMatch, LayerMask: SegmentAnythingUltra V2, Image Overlay, KuwaharaBlur, Image Overlay, VAEDecode, ImageScaleToTotalPixels, ImageNoiseAugmentation, easy imageSize, Mask Invert, easy imageColorMatch, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, Image Comparer (rgthree), SaveImageJPG_GH, SaveImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/4K高清放大 修复ttp+_+block+zoom+_+Noise_realism_2092779877316513793.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/4K高清放大 修复ttp+_+block+zoom+_+Noise_realism_2092779877316513793.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（45 个）：
- `TTP_Image_Tile_Batch`
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `VAEEncode` ★核心
- `BasicGuider`
- `KSamplerSelect` ★核心
- `BasicScheduler`
- `easy imageListToImageBatch`
- `easy imageBatchToImageList`
- `SamplerCustomAdvanced` ★核心
- `TTP_Image_Assy`
- `UpscaleModelLoader`
- `ImageUpscaleWithModel`
- `ImageScaleBy`
- `RandomNoise`
- `VAELoader_Any`
- `CLIPLoader_Any`
- `UNETLoader_Any` ★核心
- `LoraLoaderModelOnly` ★核心
- `LayerMask: BiRefNetUltraV2`
- `ImageScaleToTotalPixelsX`
- `LayerMask: LoadBiRefNetModelV2`
- `Mask Invert`
- `easy imageColorMatch`
- `LayerMask: SegmentAnythingUltra V2`
- `Image Overlay`
- `KuwaharaBlur`
- `Image Overlay`
- `VAEDecode` ★核心
- `ImageScaleToTotalPixels`
- `ImageNoiseAugmentation`
- `easy imageSize`
- `Mask Invert`
- `easy imageColorMatch`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Image Comparer (rgthree)`
- `SaveImageJPG_GH`
- `SaveImage`
- `LoadImage`

## 知识

覆盖率 **82%**（37/45）

**有卡**：`TTP_Image_Tile_Batch`、`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`easy imageListToImageBatch`、`easy imageBatchToImageList`、`SamplerCustomAdvanced`、`TTP_Image_Assy`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleBy`、`RandomNoise`、`VAELoader_Any`、`CLIPLoader_Any`、`UNETLoader_Any`、`LoraLoaderModelOnly`、`LayerMask: BiRefNetUltraV2`、`ImageScaleToTotalPixelsX`、`LayerMask: LoadBiRefNetModelV2`、`Mask Invert`、`easy imageColorMatch`、`LayerMask: SegmentAnythingUltra V2`、`Image Overlay`、`KuwaharaBlur`、`VAEDecode`、`ImageScaleToTotalPixels`、`ImageNoiseAugmentation`、`easy imageSize`、`SaveImageJPG_GH`、`SaveImage`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustomAdvanced、ReferenceLatent、VAEEncode
