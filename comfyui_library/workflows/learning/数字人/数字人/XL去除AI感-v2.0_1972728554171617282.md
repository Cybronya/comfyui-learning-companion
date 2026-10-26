---
key: 数字人/数字人/XL去除AI感-v2.0_1972728554171617282.json
name: XL去除AI感-v2.0_1972728554171617282
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/XL去除AI感-v2.0_1972728554171617282.json
hash: 23580fb060505fd5
coverage: 0.636364
learned_at: 2026-10-26 01:58:11
nodes: [BBoxDetect(FaceParsing), BBoxListItemSelect(FaceParsing), ImageCropWithBBox(FaceParsing), BBoxDetectorLoader(FaceParsing), FaceParsingProcessorLoader(FaceParsing), FaceParse(FaceParsing), Label (rgthree), PrimitiveFloat, Seed (rgthree), Label (rgthree), UpscaleModelLoader, FaceParsingResultsParser(FaceParsing), PrimitiveNode, MaskPreview, GrowMaskWithBlur, ImageResizeKJv2, Reroute, PreviewImage, Reroute, Reroute, Reroute, Reroute, PreviewImage, Image Comparer (rgthree), ImageInsertWithBBox(FaceParsing), ProPostFilmGrain, Image Comparer (rgthree), easy imageSave, easy imageSave, FaceParsingModelLoader(FaceParsing), CheckpointLoaderSimple, Power Lora Loader (rgthree), SetNode, CLIPTextEncode, Note, LoadImage, MarkdownNote, Note Plus (mtb), GetNode, UltimateSDUpscale, CLIPTextEncode, PrimitiveNode, GetImageSize, ImageCompositeMasked]
patterns: []
missing: []
parameters: {"checkpoint": "realvisxlV50_v50Bakedvae_fp32.safetensors"}
---

# 数字人/数字人/XL去除AI感-v2.0_1972728554171617282.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/XL去除AI感-v2.0_1972728554171617282.json`

## 结构

**生成流程**：Model → Condition → Process → Output → Other

**节点**（44 个）：
- `BBoxDetect(FaceParsing)`
- `BBoxListItemSelect(FaceParsing)`
- `ImageCropWithBBox(FaceParsing)`
- `BBoxDetectorLoader(FaceParsing)`
- `FaceParsingProcessorLoader(FaceParsing)`
- `FaceParse(FaceParsing)`
- `Label (rgthree)`
- `PrimitiveFloat`
- `Seed (rgthree)`
- `Label (rgthree)`
- `UpscaleModelLoader`
- `FaceParsingResultsParser(FaceParsing)`
- `PrimitiveNode`
- `MaskPreview`
- `GrowMaskWithBlur`
- `ImageResizeKJv2`
- `Reroute`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `Image Comparer (rgthree)`
- `ImageInsertWithBBox(FaceParsing)`
- `ProPostFilmGrain`
- `Image Comparer (rgthree)`
- `easy imageSave`
- `easy imageSave`
- `FaceParsingModelLoader(FaceParsing)`
- `CheckpointLoaderSimple` ★核心
- `Power Lora Loader (rgthree)`
- `SetNode`
- `CLIPTextEncode` ★核心
- `Note`
- `LoadImage`
- `MarkdownNote`
- `Note Plus (mtb)`
- `GetNode`
- `UltimateSDUpscale`
- `CLIPTextEncode` ★核心
- `PrimitiveNode`
- `GetImageSize`
- `ImageCompositeMasked`

## 关键参数

- `checkpoint` = `realvisxlV50_v50Bakedvae_fp32.safetensors`

## 知识

覆盖率 **64%**（28/44）

**有卡**：`BBoxDetect(FaceParsing)`、`BBoxListItemSelect(FaceParsing)`、`ImageCropWithBBox(FaceParsing)`、`BBoxDetectorLoader(FaceParsing)`、`FaceParsingProcessorLoader(FaceParsing)`、`FaceParse(FaceParsing)`、`Label (rgthree)`、`Seed (rgthree)`、`UpscaleModelLoader`、`FaceParsingResultsParser(FaceParsing)`、`MaskPreview`、`GrowMaskWithBlur`、`ImageResizeKJv2`、`ImageInsertWithBBox(FaceParsing)`、`ProPostFilmGrain`、`easy imageSave`、`FaceParsingModelLoader(FaceParsing)`、`CheckpointLoaderSimple`、`Power Lora Loader (rgthree)`、`CLIPTextEncode`、`LoadImage`、`Note Plus (mtb)`、`UltimateSDUpscale`、`GetImageSize`、`ImageCompositeMasked`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Seed (rgthree)、Power Lora Loader (rgthree)、UltimateSDUpscale、UpscaleModelLoader、UpscaleModelLoader
