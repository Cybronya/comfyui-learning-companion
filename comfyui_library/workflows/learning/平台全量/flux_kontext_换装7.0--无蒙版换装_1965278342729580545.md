---
key: 平台全量/flux_kontext_换装7.0--无蒙版换装_1965278342729580545.json
name: flux_kontext_换装7.0--无蒙版换装_1965278342729580545
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/flux_kontext_换装7.0--无蒙版换装_1965278342729580545.json
hash: d9937bd788c0ab9a
coverage: 0.830189
learned_at: 2026-11-14 01:11:42
nodes: [ReferenceLatent, LayerUtility: ImageReelComposit, LayerUtility: ImageReel, DualCLIPLoader, VAELoader, PreviewImage, UNETLoader, VAEEncode, InvertMask, BiRefNetRMBG, LayerUtility: ImageScaleByAspectRatio V2, PreviewImage, ConditioningZeroOut, FluxGuidance, easy showAnything, KSamplerAdvanced, LayerUtility: NumberCalculatorV2, TextInput_, easy anythingIndexSwitch, TextInput_, TextInput_, TextInput_, TextInput_, easy showAnything, LayerUtility: JoyCaptionBeta1ExtraOptions, LayerUtility: LoadJoyCaptionBeta1Model, LayerUtility: JoyCaptionBeta1, TextInput_, easy showAnything, LayerUtility: JoyCaptionBeta1, Text Concatenate (JPS), Text Concatenate (JPS), LayerUtility: ImageScaleByAspectRatio V2, ImageStitch, easy showAnything, CLIPTextEncode, Text Concatenate (JPS), ImageAndMaskPreview, LayerUtility: CropByMask V2, TextInput_, Image Comparer (rgthree), VAEEncode, PreviewImage, TextInput_, easy seed, easy anythingIndexSwitch, Random Number, LoadImage, LoadImage, LoraLoaderModelOnly, Note, VAEDecode, SaveImage]
patterns: []
missing: []
parameters: {"cfg": 25, "denoise": "simple", "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize"}
---

# 平台全量/flux_kontext_换装7.0--无蒙版换装_1965278342729580545.json

> 来源文件 `comfyui_library/workflows/平台全量/flux_kontext_换装7.0--无蒙版换装_1965278342729580545.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（53 个）：
- `ReferenceLatent`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageReel`
- `DualCLIPLoader`
- `VAELoader`
- `PreviewImage`
- `UNETLoader` ★核心
- `VAEEncode` ★核心
- `InvertMask`
- `BiRefNetRMBG`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `PreviewImage`
- `ConditioningZeroOut`
- `FluxGuidance`
- `easy showAnything`
- `KSamplerAdvanced` ★核心
- `LayerUtility: NumberCalculatorV2`
- `TextInput_`
- `easy anythingIndexSwitch`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `TextInput_`
- `easy showAnything`
- `LayerUtility: JoyCaptionBeta1ExtraOptions`
- `LayerUtility: LoadJoyCaptionBeta1Model`
- `LayerUtility: JoyCaptionBeta1`
- `TextInput_`
- `easy showAnything`
- `LayerUtility: JoyCaptionBeta1`
- `Text Concatenate (JPS)`
- `Text Concatenate (JPS)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageStitch`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `Text Concatenate (JPS)`
- `ImageAndMaskPreview`
- `LayerUtility: CropByMask V2`
- `TextInput_`
- `Image Comparer (rgthree)`
- `VAEEncode` ★核心
- `PreviewImage`
- `TextInput_`
- `easy seed`
- `easy anythingIndexSwitch`
- `Random Number`
- `LoadImage`
- `LoadImage`
- `LoraLoaderModelOnly` ★核心
- `Note`
- `VAEDecode` ★核心
- `SaveImage`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `25`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **83%**（44/53）

**有卡**：`ReferenceLatent`、`LayerUtility: ImageReelComposit`、`LayerUtility: ImageReel`、`DualCLIPLoader`、`VAELoader`、`UNETLoader`、`VAEEncode`、`InvertMask`、`BiRefNetRMBG`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConditioningZeroOut`、`FluxGuidance`、`KSamplerAdvanced`、`LayerUtility: NumberCalculatorV2`、`TextInput_`、`easy anythingIndexSwitch`、`LayerUtility: JoyCaptionBeta1ExtraOptions`、`LayerUtility: LoadJoyCaptionBeta1Model`、`LayerUtility: JoyCaptionBeta1`、`Text Concatenate (JPS)`、`ImageStitch`、`CLIPTextEncode`、`ImageAndMaskPreview`、`LayerUtility: CropByMask V2`、`easy seed`、`Random Number`、`LoadImage`、`LoraLoaderModelOnly`、`VAEDecode`、`SaveImage`

**用到的条目**：VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage、easy seed
