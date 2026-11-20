---
key: 平台全量/Kontext换装6.0 - beta_1960143968967274497.json
name: Kontext换装6.0 - beta_1960143968967274497
type: Image To Image
status: completed
source: json
file: comfyui_library/workflows/平台全量/Kontext换装6.0 - beta_1960143968967274497.json
hash: 8f0b1ae949cb6e32
coverage: 0.710526
learned_at: 2026-11-14 00:35:45
nodes: [DualCLIPLoader, UNETLoader, VAEEncode, LayerUtility: ImageReelComposit, FluxGuidance, ConditioningZeroOut, VAELoader, ReferenceLatent, VAEEncode, CLIPTextEncode, LayerUtility: CropByMask V2, easy anythingIndexSwitch, Reroute, Reroute, PreviewImage, CM_BoolToInt, easy showAnything, LayerMask: LoadBenModel, easy isMaskEmpty, easy showAnything, Reroute, easy showAnything, easy isMaskEmpty, easy showAnything, Reroute, CM_BoolToInt, easy anythingIndexSwitch, PreviewImage, LayerMask: BenUltra, ImageAndMaskPreview, LayerUtility: ImageScaleByAspectRatio V2, DownloadAndLoadQwenModel, Sam2Segmentation, ImageAndMaskPreview, PreviewImage, DownloadAndLoadSAM2Model, easy showAnything, ImageStitch, LoadImage, LoadImage, SegsToCombinedMask, MaskPreview, MaskPreview, PreviewImage, Note Plus (mtb), Image Comparer (rgthree), SaveImage, SaveImage, VAEDecode, LayerUtility: ImageReel, SaveImage, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, SaveImage, VAEDecode, Image Comparer (rgthree), LoraLoaderModelOnly, LoraLoaderModelOnly, KSampler, Image Comparer (rgthree), Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, Reroute, KSampler, RH_Captioner, TextInput_, easy showAnything, TextInput_, Text Concatenate (JPS), Reroute, QwenVLDetection, Reroute, GrowMaskWithBlur, MaskToSEGS, LayerMask: SegmentAnythingUltra V2, PreviewImage]
patterns: [image_to_image]
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 888888, "steps": 20}
---

# 平台全量/Kontext换装6.0 - beta_1960143968967274497.json

> 来源文件 `comfyui_library/workflows/平台全量/Kontext换装6.0 - beta_1960143968967274497.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（76 个）：
- `DualCLIPLoader`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `LayerUtility: ImageReelComposit`
- `FluxGuidance`
- `ConditioningZeroOut`
- `VAELoader`
- `ReferenceLatent`
- `VAEEncode` ★核心
- `CLIPTextEncode` ★核心
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
- `ImageAndMaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `DownloadAndLoadQwenModel`
- `Sam2Segmentation`
- `ImageAndMaskPreview`
- `PreviewImage`
- `DownloadAndLoadSAM2Model`
- `easy showAnything`
- `ImageStitch`
- `LoadImage`
- `LoadImage`
- `SegsToCombinedMask`
- `MaskPreview`
- `MaskPreview`
- `PreviewImage`
- `Note Plus (mtb)`
- `Image Comparer (rgthree)`
- `SaveImage`
- `SaveImage`
- `VAEDecode` ★核心
- `LayerUtility: ImageReel`
- `SaveImage`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `SaveImage`
- `VAEDecode` ★核心
- `Image Comparer (rgthree)`
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `KSampler` ★核心
- `Image Comparer (rgthree)`
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `KSampler` ★核心
- `RH_Captioner`
- `TextInput_`
- `easy showAnything`
- `TextInput_`
- `Text Concatenate (JPS)`
- `Reroute`
- `QwenVLDetection`
- `Reroute`
- `GrowMaskWithBlur`
- `MaskToSEGS`
- `LayerMask: SegmentAnythingUltra V2`
- `PreviewImage`

**识别到的模式**：image_to_image

## 关键参数

- `seed` = `888888`
- `steps` = `20`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **71%**（54/76）

**有卡**：`DualCLIPLoader`、`UNETLoader`、`VAEEncode`、`LayerUtility: ImageReelComposit`、`FluxGuidance`、`ConditioningZeroOut`、`VAELoader`、`ReferenceLatent`、`CLIPTextEncode`、`LayerUtility: CropByMask V2`、`easy anythingIndexSwitch`、`CM_BoolToInt`、`LayerMask: LoadBenModel`、`easy isMaskEmpty`、`LayerMask: BenUltra`、`ImageAndMaskPreview`、`LayerUtility: ImageScaleByAspectRatio V2`、`DownloadAndLoadQwenModel`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`ImageStitch`、`LoadImage`、`SegsToCombinedMask`、`MaskPreview`、`Note Plus (mtb)`、`SaveImage`、`VAEDecode`、`LayerUtility: ImageReel`、`LoraLoaderModelOnly`、`KSampler`、`RH_Captioner`、`TextInput_`、`Text Concatenate (JPS)`、`QwenVLDetection`、`GrowMaskWithBlur`、`MaskToSEGS`、`LayerMask: SegmentAnythingUltra V2`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage
