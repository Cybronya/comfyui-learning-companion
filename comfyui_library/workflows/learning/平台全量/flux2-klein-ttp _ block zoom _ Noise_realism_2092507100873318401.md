---
key: 平台全量/flux2-klein-ttp _ block zoom _ Noise_realism_2092507100873318401.json
name: flux2-klein-ttp _ block zoom _ Noise_realism_2092507100873318401
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/flux2-klein-ttp _ block zoom _ Noise_realism_2092507100873318401.json
hash: 0d092c70b0c7301d
coverage: 0.803922
learned_at: 2026-11-14 01:11:15
nodes: [TTP_Image_Tile_Batch, CLIPTextEncode, ReferenceLatent, VAEEncode, BasicGuider, KSamplerSelect, BasicScheduler, easy imageListToImageBatch, easy imageBatchToImageList, SamplerCustomAdvanced, TTP_Image_Assy, UpscaleModelLoader, ImageUpscaleWithModel, ImageScaleBy, RandomNoise, VAELoader_Any, CLIPLoader_Any, UNETLoader_Any, LoraLoaderModelOnly, LayerMask: BiRefNetUltraV2, ImageScaleToTotalPixelsX, LayerMask: LoadBiRefNetModelV2, Mask Invert, MaskPreview+, easy imageColorMatch, LayerMask: SegmentAnythingUltra V2, Image Overlay, KuwaharaBlur, Image Overlay, VAEDecode, MaskPreview+, SaveImage, SaveImage, ImageScaleToTotalPixels, PreviewImage, ImageNoiseAugmentation, easy imageSize, PreviewImage, Mask Invert, easy imageColorMatch, GetNode, SetNode, GetNode, Image Comparer (rgthree), SetNode, GetNode, GetNode, SetNode, LoadImage, SaveImageJPG_GH, SaveImage]
patterns: []
missing: []
---

# 平台全量/flux2-klein-ttp _ block zoom _ Noise_realism_2092507100873318401.json

> 来源文件 `comfyui_library/workflows/平台全量/flux2-klein-ttp _ block zoom _ Noise_realism_2092507100873318401.json`

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
- `MaskPreview+`
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
- `PreviewImage`
- `ImageNoiseAugmentation`
- `easy imageSize`
- `PreviewImage`
- `Mask Invert`
- `easy imageColorMatch`
- `GetNode`
- `SetNode`
- `GetNode`
- `Image Comparer (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `SaveImageJPG_GH`
- `SaveImage`

## 知识

覆盖率 **80%**（41/51）

**有卡**：`TTP_Image_Tile_Batch`、`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`BasicGuider`、`KSamplerSelect`、`BasicScheduler`、`easy imageListToImageBatch`、`easy imageBatchToImageList`、`SamplerCustomAdvanced`、`TTP_Image_Assy`、`UpscaleModelLoader`、`ImageUpscaleWithModel`、`ImageScaleBy`、`RandomNoise`、`VAELoader_Any`、`CLIPLoader_Any`、`UNETLoader_Any`、`LoraLoaderModelOnly`、`LayerMask: BiRefNetUltraV2`、`ImageScaleToTotalPixelsX`、`LayerMask: LoadBiRefNetModelV2`、`Mask Invert`、`MaskPreview+`、`easy imageColorMatch`、`LayerMask: SegmentAnythingUltra V2`、`Image Overlay`、`KuwaharaBlur`、`VAEDecode`、`SaveImage`、`ImageScaleToTotalPixels`、`ImageNoiseAugmentation`、`easy imageSize`、`LoadImage`、`SaveImageJPG_GH`

**用到的条目**：VAEDecode、LoraLoaderModelOnly、CLIPTextEncode、LoadImage、KSamplerSelect、SamplerCustomAdvanced、ReferenceLatent、VAEEncode
