---
key: 图片生成/图生图/klein+ttp block+zoom Noise_realism 极致高清放大_2101482763407941633.json
name: klein+ttp block+zoom Noise_realism 极致高清放大_2101482763407941633
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/klein+ttp block+zoom Noise_realism 极致高清放大_2101482763407941633.json
hash: d22f08e7c71843b4
coverage: 0.803922
learned_at: 2026-10-21 00:45:34
nodes: [TTP_Image_Tile_Batch, CLIPTextEncode, ReferenceLatent, VAEEncode, BasicGuider, KSamplerSelect, BasicScheduler, easy imageListToImageBatch, easy imageBatchToImageList, SamplerCustomAdvanced, TTP_Image_Assy, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleBy, RandomNoise, VAELoader_Any, CLIPLoader_Any, UNETLoader_Any, LoraLoaderModelOnly, LayerMask: BiRefNetUltraV2, ImageScaleToTotalPixelsX, LayerMask: LoadBiRefNetModelV2, Mask Invert, easy imageColorMatch, LayerMask: SegmentAnythingUltra V2, Image Overlay, KuwaharaBlur, Image Overlay, VAEDecode, MaskPreview+, SaveImage, SaveImage, ImageScaleToTotalPixels, ImageNoiseAugmentation, easy imageSize, Mask Invert, easy imageColorMatch, GetNode, SetNode, GetNode, SetNode, GetNode, GetNode, SetNode, SaveImageJPG_GH, SaveImage, Image Comparer (rgthree), PreviewImage, MaskPreview+, PreviewImage, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/klein+ttp block+zoom Noise_realism 极致高清放大_2101482763407941633.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/klein+ttp block+zoom Noise_realism 极致高清放大_2101482763407941633.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（51 个）：
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
- `MaskPreview+`
- `SaveImage`
- `SaveImage`
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
- `SaveImageJPG_GH`
- `SaveImage`
- `Image Comparer (rgthree)`
- `PreviewImage`
- `MaskPreview+`
- `PreviewImage`
- `LoadImage`

## 知识

覆盖率 **80%**（41/51）

**有卡**：`TTP_Image_Tile_Batch`、`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`easy imageListToImageBatch`、`easy imageBatchToImageList`、`SamplerCustomAdvanced`、`TTP_Image_Assy`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleBy`、`RandomNoise`、`VAELoader_Any`、`CLIPLoader_Any`、`UNETLoader_Any`、`LoraLoaderModelOnly`、`LayerMask: BiRefNetUltraV2`、`ImageScaleToTotalPixelsX`、`LayerMask: LoadBiRefNetModelV2`、`Mask Invert`、`easy imageColorMatch`、`LayerMask: SegmentAnythingUltra V2`、`Image Overlay`、`KuwaharaBlur`、`VAEDecode`、`MaskPreview+`、`SaveImage`、`ImageScaleToTotalPixels`、`ImageNoiseAugmentation`、`easy imageSize`、`SaveImageJPG_GH`、`LoadImage`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustomAdvanced、ReferenceLatent、VAEEncode
