---
key: 平台全量/Kontext换装5.0_1956568726797733889.json
name: Kontext换装5.0_1956568726797733889
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Kontext换装5.0_1956568726797733889.json
hash: f4509970c4638792
coverage: 0.724638
learned_at: 2026-11-14 00:35:44
nodes: [Note Plus (mtb), DualCLIPLoader, UNETLoader, VAEEncode, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, FluxGuidance, ConditioningZeroOut, VAELoader, SaveImage, ReferenceLatent, VAEEncode, CLIPTextEncode, Image Comparer (rgthree), Image Comparer (rgthree), LayerUtility: CropByMask V2, easy anythingIndexSwitch, Reroute, Reroute, PreviewImage, CM_BoolToInt, easy showAnything, LayerMask: LoadBenModel, easy isMaskEmpty, easy showAnything, Reroute, easy showAnything, easy isMaskEmpty, easy showAnything, Reroute, CM_BoolToInt, easy anythingIndexSwitch, PreviewImage, LayerMask: BenUltra, QwenVLDetection, ImageAndMaskPreview, KSampler, LayerUtility: ImageScaleByAspectRatio V2, VAEDecode, Reroute, DownloadAndLoadQwenModel, Sam2Segmentation, ImageAndMaskPreview, PreviewImage, DownloadAndLoadSAM2Model, easy showAnything, LayerUtility: JoyCaptionBeta1, easy showAnything, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1ExtraOptions, easy showAnything, ImageStitch, LayerUtility: ImageScaleByAspectRatio V2, Reroute, LoadImage, LoadImage, SaveImage, easy cleanGpuUsed, LoraLoaderModelOnly, RH_Captioner, MaskToSEGS, SegsToCombinedMask, MaskPreview, MaskPreview, GrowMaskWithBlur, PreviewImage, Text Concatenate (JPS), TextInput_, TextInput_]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 1041894943294311, "steps": 20}
---

# 平台全量/Kontext换装5.0_1956568726797733889.json

> 来源文件 `comfyui_library/workflows/平台全量/Kontext换装5.0_1956568726797733889.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（69 个）：
- `Note Plus (mtb)`
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAELoader`
- `SaveImage`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `LayerUtility: CropByMask V2`
- `easy anythingIndexSwitch`
- `Reroute`
- `Reroute`
- `PreviewImage`
- `CM_BoolToInt`
- `easy showAnything`
- `LayerMask: LoadBenModel`
- `easy isMaskEmpty`
- `easy showAnything`
- `Reroute`
- `easy showAnything`
- `easy isMaskEmpty`
- `easy showAnything`
- `Reroute`
- `CM_BoolToInt`
- `easy anythingIndexSwitch`
- `PreviewImage`
- `LayerMask: BenUltra`
- `QwenVLDetection`
- `ImageAndMaskPreview`
- `KSampler` ★核心
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VAEDecode` ★核心
- `Reroute`
- `DownloadAndLoadQwenModel`
- `Sam2Segmentation`
- `ImageAndMaskPreview`
- `PreviewImage`
- `DownloadAndLoadSAM2Model`
- `easy showAnything`
- `LayerUtility: JoyCaptionBeta1`
- `easy showAnything`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `easy showAnything`
- `ImageStitch`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `SaveImage`
- `easy cleanGpuUsed`
- `LoraLoaderModelOnly` ★核心
- `RH_Captioner`
- `MaskToSEGS`
- `SegsToCombinedMask`
- `MaskPreview`
- `MaskPreview`
- `GrowMaskWithBlur`
- `PreviewImage`
- `Text Concatenate (JPS)`
- `TextInput_`
- `TextInput_`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `1041894943294311`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **72%**（50/69）

**有卡**：`Note Plus (mtb)`、`DualCLIPLoader`、`UNETLoader`、`VAEEncode`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`FluxGuidance`、`ConditioningZeroOut`、`VAELoader`、`SaveImage`、`ReferenceLatent`、`CLIPTextEncode`、`LayerUtility: CropByMask V2`、`easy anythingIndexSwitch`、`CM_BoolToInt`、`LayerMask: LoadBenModel`、`easy isMaskEmpty`、`LayerMask: BenUltra`、`QwenVLDetection`、`ImageAndMaskPreview`、`KSampler`、`LayerUtility: ImageScaleByAspectRatio V2`、`VAEDecode`、`DownloadAndLoadQwenModel`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`LayerUtility: JoyCaptionBeta1`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`ImageStitch`、`LoadImage`、`easy cleanGpuUsed`、`LoraLoaderModelOnly`、`RH_Captioner`、`MaskToSEGS`、`SegsToCombinedMask`、`MaskPreview`、`GrowMaskWithBlur`、`Text Concatenate (JPS)`、`TextInput_`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
