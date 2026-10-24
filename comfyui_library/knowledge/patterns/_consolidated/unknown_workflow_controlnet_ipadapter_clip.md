---
name: unknown_workflow_controlnet_ipadapter_clip
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.638
common_nodes: [ACN_AdvancedControlNetApply, AnyLineArtPreprocessor_aux, ApplyInstantID, ApplyPulidAdvanced, CLIPTextEncode, CR Float To String, CR Image Input Switch, CR Text Concatenate, CheckpointLoaderSimple, ControlNetLoader, DF_Float, DF_Int_to_Float, DF_Integer, EG_RY_HT, EmptyImage, EnhanceImage, FaceAnalysisModels, FaceBoundingBox, FloatSlider, GetImageSize+, GrowMask, GrowMaskWithBlur, IPAdapterMS, IPAdapterUnifiedLoader, Image Batch, Image Crop Location, Image Paste Crop, ImageCompositeFromMaskBatch+, ImageCompositeMasked, ImageConcanate, ImageEffectsAdjustment, ImageFlip+, ImageResize+, ImageScale, ImageSmartSharpen+, ImageToMask, ImpactStringSelector, InstantIDFaceAnalysis, InstantIDModelLoader, LayerMask: MaskGrow, LayerMask: MaskPreview, LayerMask: PersonMaskUltra V2, LayerUtility: ImageBlend, LayerUtility: PurgeVRAM, LoadImage, Mask Crop Region, Mask Invert, MaskBlur+, MaskDetailerPipe, MaskPreview+, MaskToImage, MathExpression|pysssss, PreviewImage, PulidEvaClipLoader, PulidInsightFaceLoader, PulidModelLoader, RH_Translator, ReActorFaceBoost, ReActorFaceSwap, ReActorMaskHelper, SDXLPromptStylerAdvanced, SaveImage, ScaledSoftControlNetWeights, SetNode, ShowText|pysssss, SimpleMath+, TextCombinerSix, ToBasicPipe, easy showAnything, easy sliderControl]
problems: []
missing: []
members: [图片生成/图生图/Reactor+InstantID+Pulid+Ipadapter换脸-保持人物姿势背景不变_1952960472347774978.json, 图片生成/图生图/deep_Reactor_InstantID_Pulid_Ipadapter换脸_2002350934141353986.json]
source: knowledge_consolidation
---

# unknown_workflow_controlnet_ipadapter_clip

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/Reactor+InstantID+Pulid+Ipadapter换脸-保持人物姿势背景不变_1952960472347774978.json、图片生成/图生图/deep_Reactor_InstantID_Pulid_Ipadapter换脸_2002350934141353986.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：64%

## 共有节点

全部 2 个 workflow 都包含：
- `ACN_AdvancedControlNetApply`
- `AnyLineArtPreprocessor_aux`
- `ApplyInstantID`
- `ApplyPulidAdvanced`
- `CLIPTextEncode`
- `CR Float To String`
- `CR Image Input Switch`
- `CR Text Concatenate`
- `CheckpointLoaderSimple`
- `ControlNetLoader`
- `DF_Float`
- `DF_Int_to_Float`
- `DF_Integer`
- `EG_RY_HT`
- `EmptyImage`
- `EnhanceImage`
- `FaceAnalysisModels`
- `FaceBoundingBox`
- `FloatSlider`
- `GetImageSize+`
- `GrowMask`
- `GrowMaskWithBlur`
- `IPAdapterMS`
- `IPAdapterUnifiedLoader`
- `Image Batch`
- `Image Crop Location`
- `Image Paste Crop`
- `ImageCompositeFromMaskBatch+`
- `ImageCompositeMasked`
- `ImageConcanate`
- `ImageEffectsAdjustment`
- `ImageFlip+`
- `ImageResize+`
- `ImageScale`
- `ImageSmartSharpen+`
- `ImageToMask`
- `ImpactStringSelector`
- `InstantIDFaceAnalysis`
- `InstantIDModelLoader`
- `LayerMask: MaskGrow`
- `LayerMask: MaskPreview`
- `LayerMask: PersonMaskUltra V2`
- `LayerUtility: ImageBlend`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `Mask Crop Region`
- `Mask Invert`
- `MaskBlur+`
- `MaskDetailerPipe`
- `MaskPreview+`
- `MaskToImage`
- `MathExpression|pysssss`
- `PreviewImage`
- `PulidEvaClipLoader`
- `PulidInsightFaceLoader`
- `PulidModelLoader`
- `RH_Translator`
- `ReActorFaceBoost`
- `ReActorFaceSwap`
- `ReActorMaskHelper`
- `SDXLPromptStylerAdvanced`
- `SaveImage`
- `ScaledSoftControlNetWeights`
- `SetNode`
- `ShowText|pysssss`
- `SimpleMath+`
- `TextCombinerSix`
- `ToBasicPipe`
- `easy showAnything`
- `easy sliderControl`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 1 | - | 2 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
