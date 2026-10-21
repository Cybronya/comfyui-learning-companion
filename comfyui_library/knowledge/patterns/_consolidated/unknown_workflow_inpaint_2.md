---
name: unknown_workflow_inpaint_2
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9
common_nodes: [CR Text, GrowMaskWithBlur, INPAINT_MaskedFill, ImageScale, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RH_Nano_Banana2_Image2Image, SaveImage]
problems: []
missing: []
members: [图片生成/文生图/全能图片V12-0.25元一次_1991544351375441921.json, 图片生成/文生图/全能图片V12-0.25元一次_1997470281025404930.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_2

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/全能图片V12-0.25元一次_1991544351375441921.json、图片生成/文生图/全能图片V12-0.25元一次_1997470281025404930.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `GrowMaskWithBlur`
- `INPAINT_MaskedFill`
- `ImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
