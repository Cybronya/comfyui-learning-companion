---
key: 图片生成/图生图/deep_Reactor_InstantID_Pulid_Ipadapter换脸_2002350934141353986.json
name: deep_Reactor_InstantID_Pulid_Ipadapter换脸_2002350934141353986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/deep_Reactor_InstantID_Pulid_Ipadapter换脸_2002350934141353986.json
hash: 286197c480c3f1aa
coverage: 0.636943
learned_at: 2026-10-23 11:34:36
nodes: [ApplyInstantID, ImageToMask, easy showAnything, RH_Translator, easy showAnything, FloatSlider, ImpactStringSelector, TextCombinerSix, CR Float To String, easy showAnything, ShowText|pysssss, CR Text Concatenate, SetNode, SetNode, RH_Translator, SimpleMath+, DF_Integer, Note, SDXLPromptStylerAdvanced, easy showAnything, FaceBoundingBox, MaskBlur+, ImageCompositeMasked, ControlNetLoader, InstantIDFaceAnalysis, EnhanceImage, PulidEvaClipLoader, PreviewImage, ScaledSoftControlNetWeights, easy sliderControl, LayerUtility: PurgeVRAM, CLIPTextEncode, CLIPTextEncode, PreviewImage, PreviewImage, LayerMask: MaskPreview, LayerMask: MaskGrow, Mask Crop Region, Image Crop Location, PreviewImage, easy showAnything, LayerMask: MaskPreview, MathExpression|pysssss, ImageScale, Reroute, Reroute, Reroute, easy showAnything, EmptyImage, DF_Integer, DF_Float, Reroute, GrowMaskWithBlur, Reroute, Reroute, DF_Int_to_Float, DF_Integer, Reroute, ReActorFaceSwap, Reroute, Reroute, ReActorFaceBoost, PreviewImage, CR Image Input Switch, PreviewImage, ACN_AdvancedControlNetApply, SimpleMath+, ImageEffectsAdjustment, Image Batch, PreviewImage, Reroute, PreviewImage, Reroute, LayerMask: PersonMaskUltra V2, PreviewImage, MaskPreview+, MaskPreview+, Reroute, InstantIDModelLoader, PreviewImage, ImageSmartSharpen+, PreviewImage, ImageFlip+, PreviewImage, PulidInsightFaceLoader, PulidModelLoader, Mask Invert, Reroute, AnyLineArtPreprocessor_aux, GrowMask, MaskToImage, GetImageSize+, ImageResize+, Note, LayerUtility: ImageBlend, ControlNetLoader, LayerUtility: PurgeVRAM, EmptyImage, LayerMask: MaskPreview, IPAdapterUnifiedLoader, ImageCompositeFromMaskBatch+, IPAdapterMS, ToBasicPipe, SetNode, ImageCompositeFromMaskBatch+, Reroute, GrowMask, Reroute, ApplyPulidAdvanced, ImageSmartSharpen+, ReActorMaskHelper, Mask Crop Region, Image Paste Crop, Reroute, EmptyImage, SetNode, ImageResize+, Reroute, GrowMask, SetNode, CR Image Input Switch, ImageResize+, MaskDetailerPipe, PreviewImage, FaceAnalysisModels, PrimitiveNode, DF_Integer, DF_Integer, EG_RY_HT, EG_RY_HT, ImageResize+, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, LayerMask: MaskPreview, EG_RY_HT, PreviewImage, PreviewImage, LayerMask: MaskPreview, MaskPreview+, PrimitiveNode, DF_Integer, PrimitiveNode, PrimitiveNode, ImageConcanate, ImageResize+, ImageConcanate, Reroute, CheckpointLoaderSimple, SaveImage, LayerMask: PersonMaskUltra V2, SaveImage, LoadImage, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "dreamshaperXL_lightningDPMSDE.safetensors", "controlnet_strength": 1}
---

# 图片生成/图生图/deep_Reactor_InstantID_Pulid_Ipadapter换脸_2002350934141353986.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/deep_Reactor_InstantID_Pulid_Ipadapter换脸_2002350934141353986.json`

## 结构

**生成流程**：Model → Condition → Control → Process → Output → Other

**节点**（157 个）：
- `ApplyInstantID`
- `ImageToMask`
- `easy showAnything`
- `RH_Translator`
- `easy showAnything`
- `FloatSlider`
- `ImpactStringSelector`
- `TextCombinerSix`
- `CR Float To String`
- `easy showAnything`
- `ShowText|pysssss`
- `CR Text Concatenate`
- `SetNode`
- `SetNode`
- `RH_Translator`
- `SimpleMath+`
- `DF_Integer`
- `Note`
- `SDXLPromptStylerAdvanced`
- `easy showAnything`
- `FaceBoundingBox`
- `MaskBlur+`
- `ImageCompositeMasked`
- `ControlNetLoader`
- `InstantIDFaceAnalysis`
- `EnhanceImage`
- `PulidEvaClipLoader`
- `PreviewImage`
- `ScaledSoftControlNetWeights`
- `easy sliderControl`
- `LayerUtility: PurgeVRAM`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `PreviewImage`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `LayerMask: MaskGrow`
- `Mask Crop Region`
- `Image Crop Location`
- `PreviewImage`
- `easy showAnything`
- `LayerMask: MaskPreview`
- `MathExpression|pysssss`
- `ImageScale`
- `Reroute`
- `Reroute`
- `Reroute`
- `easy showAnything`
- `EmptyImage`
- `DF_Integer`
- `DF_Float`
- `Reroute`
- `GrowMaskWithBlur`
- `Reroute`
- `Reroute`
- `DF_Int_to_Float`
- `DF_Integer`
- `Reroute`
- `ReActorFaceSwap`
- `Reroute`
- `Reroute`
- `ReActorFaceBoost`
- `PreviewImage`
- `CR Image Input Switch`
- `PreviewImage`
- `ACN_AdvancedControlNetApply` ★核心
- `SimpleMath+`
- `ImageEffectsAdjustment`
- `Image Batch`
- `PreviewImage`
- `Reroute`
- `PreviewImage`
- `Reroute`
- `LayerMask: PersonMaskUltra V2`
- `PreviewImage`
- `MaskPreview+`
- `MaskPreview+`
- `Reroute`
- `InstantIDModelLoader`
- `PreviewImage`
- `ImageSmartSharpen+`
- `PreviewImage`
- `ImageFlip+`
- `PreviewImage`
- `PulidInsightFaceLoader`
- `PulidModelLoader`
- `Mask Invert`
- `Reroute`
- `AnyLineArtPreprocessor_aux`
- `GrowMask`
- `MaskToImage`
- `GetImageSize+`
- `ImageResize+`
- `Note`
- `LayerUtility: ImageBlend`
- `ControlNetLoader`
- `LayerUtility: PurgeVRAM`
- `EmptyImage`
- `LayerMask: MaskPreview`
- `IPAdapterUnifiedLoader`
- `ImageCompositeFromMaskBatch+`
- `IPAdapterMS`
- `ToBasicPipe`
- `SetNode`
- `ImageCompositeFromMaskBatch+`
- `Reroute`
- `GrowMask`
- `Reroute`
- `ApplyPulidAdvanced`
- `ImageSmartSharpen+`
- `ReActorMaskHelper`
- `Mask Crop Region`
- `Image Paste Crop`
- `Reroute`
- `EmptyImage`
- `SetNode`
- `ImageResize+`
- `Reroute`
- `GrowMask`
- `SetNode`
- `CR Image Input Switch`
- `ImageResize+`
- `MaskDetailerPipe`
- `PreviewImage`
- `FaceAnalysisModels`
- `PrimitiveNode`
- `DF_Integer`
- `DF_Integer`
- `EG_RY_HT`
- `EG_RY_HT`
- `ImageResize+`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `EG_RY_HT`
- `PreviewImage`
- `PreviewImage`
- `LayerMask: MaskPreview`
- `MaskPreview+`
- `PrimitiveNode`
- `DF_Integer`
- `PrimitiveNode`
- `PrimitiveNode`
- `ImageConcanate`
- `ImageResize+`
- `ImageConcanate`
- `Reroute`
- `CheckpointLoaderSimple` ★核心
- `SaveImage`
- `LayerMask: PersonMaskUltra V2`
- `SaveImage`
- `LoadImage`
- `LoadImage`

## 关键参数

- `controlnet_strength` = `1`
- `checkpoint` = `dreamshaperXL_lightningDPMSDE.safetensors`

## 知识

覆盖率 **64%**（100/157）

**有卡**：`ApplyInstantID`、`ImageToMask`、`RH_Translator`、`FloatSlider`、`ImpactStringSelector`、`TextCombinerSix`、`CR Float To String`、`CR Text Concatenate`、`SimpleMath+`、`DF_Integer`、`SDXLPromptStylerAdvanced`、`FaceBoundingBox`、`MaskBlur+`、`ImageCompositeMasked`、`ControlNetLoader`、`InstantIDFaceAnalysis`、`EnhanceImage`、`PulidEvaClipLoader`、`ScaledSoftControlNetWeights`、`easy sliderControl`、`LayerUtility: PurgeVRAM`、`CLIPTextEncode`、`LayerMask: MaskPreview`、`LayerMask: MaskGrow`、`Mask Crop Region`、`Image Crop Location`、`MathExpression|pysssss`、`ImageScale`、`EmptyImage`、`DF_Float`、`GrowMaskWithBlur`、`DF_Int_to_Float`、`ReActorFaceSwap`、`ReActorFaceBoost`、`CR Image Input Switch`、`ACN_AdvancedControlNetApply`、`ImageEffectsAdjustment`、`Image Batch`、`LayerMask: PersonMaskUltra V2`、`MaskPreview+`、`InstantIDModelLoader`、`ImageSmartSharpen+`、`ImageFlip+`、`PulidInsightFaceLoader`、`PulidModelLoader`、`Mask Invert`、`AnyLineArtPreprocessor_aux`、`GrowMask`、`MaskToImage`、`GetImageSize+`、`ImageResize+`、`LayerUtility: ImageBlend`、`IPAdapterUnifiedLoader`、`ImageCompositeFromMaskBatch+`、`IPAdapterMS`、`ToBasicPipe`、`ApplyPulidAdvanced`、`ReActorMaskHelper`、`Image Paste Crop`、`MaskDetailerPipe`、`FaceAnalysisModels`、`EG_RY_HT`、`ImageConcanate`、`CheckpointLoaderSimple`、`SaveImage`、`LoadImage`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、ControlNetLoader、ACN_AdvancedControlNetApply、ScaledSoftControlNetWeights、SDXLPromptStylerAdvanced、IPAdapterMS
