---
key: 平台全量/Change anything in photo_1868927411973685250.json
name: Change anything in photo_1868927411973685250
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Change anything in photo_1868927411973685250.json
hash: 2eb9758d92a3f832
coverage: 0.766355
learned_at: 2026-11-14 00:22:10
nodes: [Label (rgthree), Label (rgthree), Label (rgthree), EmptyImage, SetNode, SetNode, CR Text Replace, ImageConcatMulti, SAMModelLoader (segment anything), GroundingDinoModelLoader (segment anything), GetNode, SetNode, LayerMask: MaskGrow, SetNode, SetNode, GetImageSize+, LayerUtility: ImageRemoveAlpha, ImageResize+, ttN text, MaskToImage, VAELoader, DualCLIPLoader, Anything Everywhere, Anything Everywhere, CLIPTextEncode, ImageResize+, ImageCrop+, GroundingDinoSAMSegment (segment anything), ImageToMask, LayerMask: MaskGrow, CLIPVisionLoader, SetNode, InpaintStitch, ConditioningZeroOut, VAEDecode, GetNode, ResizeMask, GetImageSize+, GetNode, DownloadAndLoadFlorence2Model, Florence2Run, workflow>INPAIN, StyleModelLoader, CLIPVisionEncode, FluxGuidance, ImageConcanate, GetNode, LayerUtility: PurgeVRAM, RHHiddenNodes, InpaintModelConditioning, SetNode, ConstrainImage|pysssss, RHHiddenNodes, ImageUpscaleWithModel, UpscaleModelLoader, RHHiddenNodes, LoadImage, LoadImage, Int, ImageConcanate, ImageConcanate, Int, VAEDecode, ImageCrop+, InpaintStitchImproved, SaveImage, Label (rgthree), Label (rgthree), DifferentialDiffusion, MaskToImage, EmptyImage, MaskToImage, DF_Text, DF_Text, LoadImage, InpaintCropImproved, workflow>Pre-FIX, InpaintCropImproved, ImageConcanate, KSampler, LoraLoaderModelOnly, UNETLoader, LoraLoaderModelOnly, LoadImage, Note, Note, Note, Fast Groups Bypasser (rgthree), StyleModelApply, ImageResize+, LayerUtility: CropByMask, GetNode, Any Switch (rgthree), Any Switch (rgthree), ImageConcanate, SaveImage, DF_Text, Any Switch (rgthree), ShowText, GetNode, GetNode, GetNode, PreviewImage, Fast Bypasser (rgthree), Fast Bypasser (rgthree), workflow>Automask, RMBG]
patterns: []
missing: []
problems: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "normal", "seed": 489467056914178, "steps": 8}
discoveries: [[medium] Steps较低，可能导致细节不足 → 建议增加到20-30]
---

# 平台全量/Change anything in photo_1868927411973685250.json

> 来源文件 `comfyui_library/workflows/平台全量/Change anything in photo_1868927411973685250.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Output → Other

**节点**（107 个）：
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `EmptyImage`
- `SetNode`
- `SetNode`
- `CR Text Replace`
- `ImageConcatMulti`
- `SAMModelLoader (segment anything)`
- `GroundingDinoModelLoader (segment anything)`
- `GetNode`
- `SetNode`
- `LayerMask: MaskGrow`
- `SetNode`
- `SetNode`
- `GetImageSize+`
- `LayerUtility: ImageRemoveAlpha`
- `ImageResize+`
- `ttN text`
- `MaskToImage`
- `VAELoader`
- `DualCLIPLoader`
- `Anything Everywhere`
- `Anything Everywhere`
- `CLIPTextEncode` ★核心
- `ImageResize+`
- `ImageCrop+`
- `GroundingDinoSAMSegment (segment anything)`
- `ImageToMask`
- `LayerMask: MaskGrow`
- `CLIPVisionLoader`
- `SetNode`
- `InpaintStitch`
- `ConditioningZeroOut`
- `VAEDecode` ★核心
- `GetNode`
- `ResizeMask`
- `GetImageSize+`
- `GetNode`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `workflow>INPAIN`
- `StyleModelLoader`
- `CLIPVisionEncode`
- `FluxGuidance`
- `ImageConcanate`
- `GetNode`
- `LayerUtility: PurgeVRAM`
- `RHHiddenNodes`
- `InpaintModelConditioning`
- `SetNode`
- `ConstrainImage|pysssss`
- `RHHiddenNodes`
- `ImageUpscaleWithModel`
- `UpscaleModelLoader`
- `RHHiddenNodes`
- `LoadImage`
- `LoadImage`
- `Int`
- `ImageConcanate`
- `ImageConcanate`
- `Int`
- `VAEDecode` ★核心
- `ImageCrop+`
- `InpaintStitchImproved`
- `SaveImage`
- `Label (rgthree)`
- `Label (rgthree)`
- `DifferentialDiffusion`
- `MaskToImage`
- `EmptyImage`
- `MaskToImage`
- `DF_Text`
- `DF_Text`
- `LoadImage`
- `InpaintCropImproved`
- `workflow>Pre-FIX`
- `InpaintCropImproved`
- `ImageConcanate`
- `KSampler` ★核心
- `LoraLoaderModelOnly` ★核心
- `UNETLoader` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoadImage`
- `Note`
- `Note`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `StyleModelApply`
- `ImageResize+`
- `LayerUtility: CropByMask`
- `GetNode`
- `Any Switch (rgthree)`
- `Any Switch (rgthree)`
- `ImageConcanate`
- `SaveImage`
- `DF_Text`
- `Any Switch (rgthree)`
- `ShowText`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `Fast Bypasser (rgthree)`
- `Fast Bypasser (rgthree)`
- `workflow>Automask`
- `RMBG`

## 关键参数

- `seed` = `489467056914178`
- `steps` = `8`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `normal`
- `denoise` = `1`

## 知识

覆盖率 **77%**（82/107）

**有卡**：`Label (rgthree)`、`EmptyImage`、`CR Text Replace`、`ImageConcatMulti`、`SAMModelLoader (segment anything)`、`GroundingDinoModelLoader (segment anything)`、`LayerMask: MaskGrow`、`GetImageSize+`、`LayerUtility: ImageRemoveAlpha`、`ImageResize+`、`ttN text`、`MaskToImage`、`VAELoader`、`DualCLIPLoader`、`CLIPTextEncode`、`ImageCrop+`、`GroundingDinoSAMSegment (segment anything)`、`ImageToMask`、`CLIPVisionLoader`、`InpaintStitch`、`ConditioningZeroOut`、`VAEDecode`、`ResizeMask`、`DownloadAndLoadFlorence2Model`、`Florence2Run`、`workflow>INPAIN`、`StyleModelLoader`、`CLIPVisionEncode`、`FluxGuidance`、`ImageConcanate`、`LayerUtility: PurgeVRAM`、`RHHiddenNodes`、`InpaintModelConditioning`、`ConstrainImage|pysssss`、`ImageUpscaleWithModel`、`UpscaleModelLoader`、`LoadImage`、`Int`、`InpaintStitchImproved`、`SaveImage`、`DifferentialDiffusion`、`DF_Text`、`InpaintCropImproved`、`workflow>Pre-FIX`、`KSampler`、`LoraLoaderModelOnly`、`UNETLoader`、`StyleModelApply`、`LayerUtility: CropByMask`、`ShowText`、`Fast Bypasser (rgthree)`、`workflow>Automask`、`RMBG`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、UNETLoader、CLIPTextEncode、ConditioningZeroOut、LoadImage

## 参数体检

发现 1 个问题：
- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30

## 学习发现

- [medium] Steps较低，可能导致细节不足 → 建议增加到20-30
