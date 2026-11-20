---
name: unknown_workflow_generic_1532
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.758
common_nodes: [CR Text, Image Comparer (rgthree), LayerMask: MaskGrow, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskPreview, RH_Nano_Banana2_Gemini31Flash, SaveImage, easy imageDetailTransfer, easy imageRemBg, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/换背景_2045416894164901890.json, 图片生成/图生图/溶图_2012039867399675905.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1532

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/换背景_2045416894164901890.json、图片生成/图生图/溶图_2012039867399675905.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：76%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `Image Comparer (rgthree)`
- `LayerMask: MaskGrow`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskPreview`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `easy imageDetailTransfer`
- `easy imageRemBg`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `HAIGC_SavePSD` —— 1/2 个有
- `LayerStyle: Stroke V2` —— 1/2 个有
- `PreviewImage` —— 1/2 个有
- `RH_LLMAPI_Pro_Node` —— 1/2 个有
- `RH_RhartImageNG31FlashImageToImage` —— 1/2 个有
- `easy showAnything` —— 1/2 个有
- `取色器_孤海` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
