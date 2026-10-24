---
name: unknown_workflow_generic_1245
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.932
common_nodes: [FastCanvas, FastCanvasTool, Get resolution [Crystools], LayerUtility: ColorImage, LayerUtility: ImageBlend, LayerUtility: ImageOpacity, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, MaskToImage, MuyeTextEditOutput, SaveImage, easy imageRemBg]
problems: []
missing: []
members: [图片生成/图生图/KMQ-LOGO样图定制_2041044001616302081.json, 图片生成/图生图/KMQ-LOGO样图定制_2041062606558990337.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1245

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/KMQ-LOGO样图定制_2041044001616302081.json、图片生成/图生图/KMQ-LOGO样图定制_2041062606558990337.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 2 个 workflow 都包含：
- `FastCanvas`
- `FastCanvasTool`
- `Get resolution [Crystools]`
- `LayerUtility: ColorImage`
- `LayerUtility: ImageBlend`
- `LayerUtility: ImageOpacity`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `MaskToImage`
- `MuyeTextEditOutput`
- `SaveImage`
- `easy imageRemBg`

**可变部分**（部分 workflow 才有）：
- `Image Remove Background (Alpha)` —— 1/2 个有
- `ImageToMask` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `Int` —— 1/2 个有
- `ZML_AnyTypeSwitch` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
