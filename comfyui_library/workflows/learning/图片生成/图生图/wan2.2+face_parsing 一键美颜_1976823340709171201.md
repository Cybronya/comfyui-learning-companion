---
key: 图片生成/图生图/wan2.2+face_parsing 一键美颜_1976823340709171201.json
name: wan2.2+face_parsing 一键美颜_1976823340709171201
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/wan2.2+face_parsing 一键美颜_1976823340709171201.json
hash: 1871c1e8013ef446
coverage: 0.744186
learned_at: 2026-10-23 11:45:57
nodes: [SetNode, VAEDecode, easy cleanGpuUsed, ModelSamplingSD3, MaskPreview+, PathchSageAttentionKJ, CLIPTextEncode, VAELoader, CLIPLoader, CLIPTextEncode, ImageCropWithBBox(FaceParsing), SetNode, PreviewImage, GetNode, UNETLoader, BBoxDetect(FaceParsing), FaceParsingModelLoader(FaceParsing), BBoxDetectorLoader(FaceParsing), BBoxDetectorLoader(FaceParsing), BBoxListItemSelect(FaceParsing), PreviewImage, GrowMaskWithBlur, FaceParsingProcessorLoader(FaceParsing), FaceParse(FaceParsing), FaceParsingResultsParser(FaceParsing), LayerUtility: ImageScaleRestore V2, LayerFilter: AddGrain, Image Blend by Mask, ImageInsertWithBBox(FaceParsing), PreviewImage, Image Comparer (rgthree), SetNode, GetNode, MaskToImage, KSampler, VAEEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerFilter: SkinBeauty, ColorAdjust(FaceParsing), GetNode, Note, SaveImage, LoadImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 3.5, "denoise": 0.25, "sampler_name": "euler", "scheduler": "simple", "seed": 282265729470294, "steps": 15}
---

# 图片生成/图生图/wan2.2+face_parsing 一键美颜_1976823340709171201.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/wan2.2+face_parsing 一键美颜_1976823340709171201.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（43 个）：
- `SetNode`
- `VAEDecode` ★核心
- `easy cleanGpuUsed`
- `ModelSamplingSD3`
- `MaskPreview+`
- `PathchSageAttentionKJ`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `CLIPLoader`
- `CLIPTextEncode` ★核心
- `ImageCropWithBBox(FaceParsing)`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `UNETLoader` ★核心
- `BBoxDetect(FaceParsing)`
- `FaceParsingModelLoader(FaceParsing)`
- `BBoxDetectorLoader(FaceParsing)`
- `BBoxDetectorLoader(FaceParsing)`
- `BBoxListItemSelect(FaceParsing)`
- `PreviewImage`
- `GrowMaskWithBlur`
- `FaceParsingProcessorLoader(FaceParsing)`
- `FaceParse(FaceParsing)`
- `FaceParsingResultsParser(FaceParsing)`
- `LayerUtility: ImageScaleRestore V2`
- `LayerFilter: AddGrain`
- `Image Blend by Mask`
- `ImageInsertWithBBox(FaceParsing)`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `SetNode`
- `GetNode`
- `MaskToImage`
- `KSampler` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerFilter: SkinBeauty`
- `ColorAdjust(FaceParsing)`
- `GetNode`
- `Note`
- `SaveImage`
- `LoadImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `282265729470294`
- `steps` = `15`
- `cfg` = `3.5`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `0.25`

## 知识

覆盖率 **74%**（32/43）

**有卡**：`VAEDecode`、`easy cleanGpuUsed`、`ModelSamplingSD3`、`MaskPreview+`、`PathchSageAttentionKJ`、`CLIPTextEncode`、`VAELoader`、`CLIPLoader`、`ImageCropWithBBox(FaceParsing)`、`UNETLoader`、`BBoxDetect(FaceParsing)`、`FaceParsingModelLoader(FaceParsing)`、`BBoxDetectorLoader(FaceParsing)`、`BBoxListItemSelect(FaceParsing)`、`GrowMaskWithBlur`、`FaceParsingProcessorLoader(FaceParsing)`、`FaceParse(FaceParsing)`、`FaceParsingResultsParser(FaceParsing)`、`LayerUtility: ImageScaleRestore V2`、`LayerFilter: AddGrain`、`Image Blend by Mask`、`ImageInsertWithBBox(FaceParsing)`、`MaskToImage`、`KSampler`、`VAEEncode`、`LayerUtility: ImageScaleByAspectRatio V2`、`LayerFilter: SkinBeauty`、`ColorAdjust(FaceParsing)`、`SaveImage`、`LoadImage`

**用到的条目**：KSampler、VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、LoadImage、UNETLoader、VAEEncode
