---
key: 平台全量/人物换装全自动全身换装+wan2.2for循环高清放大v1_1967796432650534914.json
name: 人物换装全自动全身换装+wan2.2for循环高清放大v1_1967796432650534914
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/人物换装全自动全身换装+wan2.2for循环高清放大v1_1967796432650534914.json
hash: 12f11acb4086d357
coverage: 0.847619
learned_at: 2026-11-14 01:37:29
nodes: [LayerMask: LoadBiRefNetModelV2, Switch any [Crystools], ImageResizeKJ, MaskToImage, Switch any [Crystools], PreviewImage, ImageConcanate, ImageToMask, GetImageSize+, ImageConcanate, PreviewImage, PreviewImage, Note, ImageResizeKJ, CLIPTextEncode, VAELoader, StyleModelLoader, CLIPVisionLoader, LayerMask: ObjectDetectorYOLO8, LayerStyle: ColorOverlay V2, LayerMask: BiRefNetUltraV2, ImageResizeKJ, LayerUtility: ColorImage V2, ImageScaleToTotalPixels, easy cleanGpuUsed, easy compare, easy int, easy int, easy ifElse, easy ifElse, CLIPLoader, UNETLoader, CLIPTextEncode, VAEEncodeTiled, CLIPTextEncode, LoraLoaderModelOnly, TTP_Tile_image_size, TTP_Image_Tile_Batch, easy imageSize, easy imageCount, ImageUpscaleWithModel, UpscaleModelLoader, PathchSageAttentionKJ, ModelSamplingSD3, VAELoader, ImageSharpen, easy forLoopStart, ImageFromBatch, easy batchAnything, easy forLoopEnd, KSampler, easy imageListToImageBatch, easy showAnything, easy showAnything, easy imageBatchToImageList, VAEDecodeTiled, SaveImage, TTP_Image_Assy, ImageResize+, Image Comparer (rgthree), SaveImage, PreviewImage, PreviewImage, PreviewImage, MaskPreview+, MaskPreview+, MaskPreview+, MaskToImage, Mask Threshold Region, PreviewImage, SubtractMask, SubtractMask, AddMask, AddMask, LayerMask: PersonMaskUltra V2, LayerMask: SAM2Ultra, LayerMask: SAM2Ultra, LayerMask: SAM2Ultra, LayerMask: MaskGrow, LayerUtility: ColorImage V2, LayerMask: MaskGrow, LayerMask: ObjectDetectorYOLO8, LayerMask: ObjectDetectorYOLO8, InpaintModelConditioning, ImageConcanate, ImageConcanate, VAEDecode, FluxGuidance, DualCLIPLoader, LoadImage, LoraLoaderModelOnly, LoraLoaderModelOnly, ImageCrop+, PreviewImage, LayerUtility: CropByMask, TeaCache, ImageResizeKJ, PreviewImage, ReduxAdvanced, CLIPTextEncode, UNETLoader, KSampler, LoadImage, Note, easy imageColorMatch]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1.5, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 822557467307747, "steps": 25}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/人物换装全自动全身换装+wan2.2for循环高清放大v1_1967796432650534914.json

> 来源文件 `comfyui_library/workflows/平台全量/人物换装全自动全身换装+wan2.2for循环高清放大v1_1967796432650534914.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（105 个）：
- `LayerMask: LoadBiRefNetModelV2`
- `Switch any [Crystools]`
- `ImageResizeKJ`
- `MaskToImage`
- `Switch any [Crystools]`
- `PreviewImage`
- `ImageConcanate`
- `ImageToMask`
- `GetImageSize+`
- `ImageConcanate`
- `PreviewImage`
- `PreviewImage`
- `Note`
- `ImageResizeKJ`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `StyleModelLoader`
- `CLIPVisionLoader`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerStyle: ColorOverlay V2`
- `LayerMask: BiRefNetUltraV2`
- `ImageResizeKJ`
- `LayerUtility: ColorImage V2`
- `ImageScaleToTotalPixels`
- `easy cleanGpuUsed`
- `easy compare`
- `easy int`
- `easy int`
- `easy ifElse`
- `easy ifElse`
- `CLIPLoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `VAEEncodeTiled` ★核心
- `CLIPTextEncode` ★核心
- `LoraLoaderModelOnly` ★核心
- `TTP_Tile_image_size`
- `TTP_Image_Tile_Batch`
- `easy imageSize`
- `easy imageCount`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `PathchSageAttentionKJ`
- `ModelSamplingSD3`
- `VAELoader`
- `ImageSharpen`
- `easy forLoopStart`
- `ImageFromBatch`
- `easy batchAnything`
- `easy forLoopEnd`
- `KSampler` ★核心
- `easy imageListToImageBatch`
- `easy showAnything`
- `easy showAnything`
- `easy imageBatchToImageList`
- `VAEDecodeTiled` ★核心
- `SaveImage`
- `TTP_Image_Assy`
- `ImageResize+`
- `Image Comparer (rgthree)`
- `SaveImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `MaskPreview+`
- `MaskPreview+`
- `MaskPreview+`
- `MaskToImage`
- `Mask Threshold Region`
- `PreviewImage`
- `SubtractMask`
- `SubtractMask`
- `AddMask`
- `AddMask`
- `LayerMask: PersonMaskUltra V2`
- `LayerMask: SAM2Ultra`
- `LayerMask: SAM2Ultra`
- `LayerMask: SAM2Ultra`
- `LayerMask: MaskGrow`
- `LayerUtility: ColorImage V2`
- `LayerMask: MaskGrow`
- `LayerMask: ObjectDetectorYOLO8`
- `LayerMask: ObjectDetectorYOLO8`
- `InpaintModelConditioning`
- `ImageConcanate`
- `ImageConcanate`
- `VAEDecode` ★核心
- `FluxGuidance`
- `DualCLIPLoader`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `ImageCrop+`
- `PreviewImage`
- `LayerUtility: CropByMask`
- `TeaCache`
- `ImageResizeKJ`
- `PreviewImage`
- `ReduxAdvanced`
- `CLIPTextEncode` ★核心
- `UNETLoader` ★核心
- `KSampler` ★核心
- `LoadImage`
- `Note`
- `easy imageColorMatch`

## 关键参数

- `seed` = `822557467307747`
- `steps` = `25`
- `cfg` = `1.5`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **85%**（89/105）

**有卡**：`LayerMask: LoadBiRefNetModelV2`、`Switch any [Crystools]`、`ImageResizeKJ`、`MaskToImage`、`ImageConcanate`、`ImageToMask`、`GetImageSize+`、`CLIPTextEncode`、`VAELoader`、`StyleModelLoader`、`CLIPVisionLoader`、`LayerMask: ObjectDetectorYOLO8`、`LayerStyle: ColorOverlay V2`、`LayerMask: BiRefNetUltraV2`、`LayerUtility: ColorImage V2`、`ImageScaleToTotalPixels`、`easy cleanGpuUsed`、`easy compare`、`easy int`、`CLIPLoader`、`UNETLoader`、`VAEEncodeTiled`、`LoraLoaderModelOnly`、`TTP_Tile_image_size`、`TTP_Image_Tile_Batch`、`easy imageSize`、`easy imageCount`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`PathchSageAttentionKJ`、`ModelSamplingSD3`、`ImageSharpen`、`easy forLoopStart`、`ImageFromBatch`、`easy batchAnything`、`easy forLoopEnd`、`KSampler`、`easy imageListToImageBatch`、`easy imageBatchToImageList`、`VAEDecodeTiled`、`SaveImage`、`TTP_Image_Assy`、`ImageResize+`、`MaskPreview+`、`Mask Threshold Region`、`SubtractMask`、`AddMask`、`LayerMask: PersonMaskUltra V2`、`LayerMask: SAM2Ultra`、`LayerMask: MaskGrow`、`InpaintModelConditioning`、`VAEDecode`、`FluxGuidance`、`DualCLIPLoader`、`LoadImage`、`ImageCrop+`、`LayerUtility: CropByMask`、`TeaCache`、`ReduxAdvanced`、`easy imageColorMatch`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPLoader、CLIPTextEncode、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
