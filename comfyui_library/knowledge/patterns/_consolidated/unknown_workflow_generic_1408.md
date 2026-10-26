---
name: unknown_workflow_generic_1408
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.55
common_nodes: [BBoxesToSAM2, CM_BoolToInt, CR Text, DeepTranslatorTextNode, DownloadAndLoadQwenModel, Fast Groups Bypasser (rgthree), GetImageSize, GetImageSize+, GetNode, GrowMask, Image Comparer (rgthree), ImageResize+, ImpactSwitch, Int, InvertMask, JjkText, LayerMask: LoadSAM2Model, LayerMask: SAM2UltraV2, LayerUtility: ColorPicker, LayerUtility: ImageReel, LayerUtility: ImageReelComposit, LayerUtility: ImageRemoveAlpha, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, QwenVLDetection, RH_Nano_Banana_Image2Image, SaveImage, SeedVR2, SeedVR2BlockSwap, SetNode, easy isNone, easy mathInt, easy showAnything, int _O]
problems: []
missing: []
members: [图片生成/图生图/hz工作流_v001_1981035333783523329.json, 图片生成/图生图/hz工作流_v001_1981065405626204161.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1408

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/hz工作流_v001_1981035333783523329.json、图片生成/图生图/hz工作流_v001_1981065405626204161.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：55%

## 共有节点

全部 2 个 workflow 都包含：
- `BBoxesToSAM2`
- `CM_BoolToInt`
- `CR Text`
- `DeepTranslatorTextNode`
- `DownloadAndLoadQwenModel`
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize`
- `GetImageSize+`
- `GetNode`
- `GrowMask`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImpactSwitch`
- `Int`
- `InvertMask`
- `JjkText`
- `LayerMask: LoadSAM2Model`
- `LayerMask: SAM2UltraV2`
- `LayerUtility: ColorPicker`
- `LayerUtility: ImageReel`
- `LayerUtility: ImageReelComposit`
- `LayerUtility: ImageRemoveAlpha`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `QwenVLDetection`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `SetNode`
- `easy isNone`
- `easy mathInt`
- `easy showAnything`
- `int _O`

**可变部分**（部分 workflow 才有）：
- `easy imageConcat` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
