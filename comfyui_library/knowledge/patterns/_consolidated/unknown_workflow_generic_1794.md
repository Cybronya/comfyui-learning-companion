---
name: unknown_workflow_generic_1794
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9125
common_nodes: [AILab_MaskCombiner, BlurMaskFast, CR Image Input Switch (4 way), ComfySwitchNode, EmptyImage, GetImageSize, GrowMask, Image Generate Gradient, ImageCompositeMasked, InvertMask, JoinImageWithAlpha, LoadBackgroundRemovalModel, LoadImage, Mask Fill Holes, MaskComposite, MaskSplitFilter, MaskToImage, PreviewTextNode, RH_Translator, RemapMaskRange, RemoveBackground, SAM3Segment, SaveImage, StringConstant, ThresholdMask, mask_select_mask, string_util_StrLower]
problems: []
missing: []
members: [图片生成/图生图/超级抠图工作流_2081756633809637377.json, 平台全量/图图原创｜完美可控抠图工作流_2080467167908294657.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1794

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/超级抠图工作流_2081756633809637377.json、平台全量/图图原创｜完美可控抠图工作流_2080467167908294657.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `AILab_MaskCombiner`
- `BlurMaskFast`
- `CR Image Input Switch (4 way)`
- `ComfySwitchNode`
- `EmptyImage`
- `GetImageSize`
- `GrowMask`
- `Image Generate Gradient`
- `ImageCompositeMasked`
- `InvertMask`
- `JoinImageWithAlpha`
- `LoadBackgroundRemovalModel`
- `LoadImage`
- `Mask Fill Holes`
- `MaskComposite`
- `MaskSplitFilter`
- `MaskToImage`
- `PreviewTextNode`
- `RH_Translator`
- `RemapMaskRange`
- `RemoveBackground`
- `SAM3Segment`
- `SaveImage`
- `StringConstant`
- `ThresholdMask`
- `mask_select_mask`
- `string_util_StrLower`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
