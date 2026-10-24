---
name: unknown_workflow_checkpoint_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6585
common_nodes: [CheckpointLoaderSimple, ColorMatch, DF_Float, ExpressionEditor, Fast Groups Bypasser (rgthree), FeatherMask, GetImageSize, GetNode, Image Comparer (rgthree), ImageCASharpening+, ImageResize+, ImageToMask, ImpactInt, ImpactSimpleDetectorSEGS, LayerUtility: ColorImage, LayerUtility: CropByMask, LayerUtility: ImageScaleRestore, LayerUtility: RestoreCropBox, LoadImage, PreviewImage, SAMLoader, SUPIR_conditioner, SUPIR_decode, SUPIR_encode, SUPIR_first_stage, SUPIR_model_loader_v2, SUPIR_sample, SaveImage, Seed (rgthree), SegsToCombinedMask, SetNode, SimpleMathDual+, String Literal, UltralyticsDetectorProvider, easy getNode, easy setNode]
problems: []
missing: []
members: [图片生成/图生图/人像表情控制微调01_2092229890107076610.json, 图片生成/图生图/人像表情控制微调02_2087188740228870145.json]
source: knowledge_consolidation
---

# unknown_workflow_checkpoint_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/人像表情控制微调01_2092229890107076610.json、图片生成/图生图/人像表情控制微调02_2087188740228870145.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `CheckpointLoaderSimple`
- `ColorMatch`
- `DF_Float`
- `ExpressionEditor`
- `Fast Groups Bypasser (rgthree)`
- `FeatherMask`
- `GetImageSize`
- `GetNode`
- `Image Comparer (rgthree)`
- `ImageCASharpening+`
- `ImageResize+`
- `ImageToMask`
- `ImpactInt`
- `ImpactSimpleDetectorSEGS`
- `LayerUtility: ColorImage`
- `LayerUtility: CropByMask`
- `LayerUtility: ImageScaleRestore`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `PreviewImage`
- `SAMLoader`
- `SUPIR_conditioner`
- `SUPIR_decode`
- `SUPIR_encode`
- `SUPIR_first_stage`
- `SUPIR_model_loader_v2`
- `SUPIR_sample`
- `SaveImage`
- `Seed (rgthree)`
- `SegsToCombinedMask`
- `SetNode`
- `SimpleMathDual+`
- `String Literal`
- `UltralyticsDetectorProvider`
- `easy getNode`
- `easy setNode`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
