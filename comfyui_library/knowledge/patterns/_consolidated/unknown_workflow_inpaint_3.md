---
name: unknown_workflow_inpaint_3
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.6
common_nodes: [CR Text, GetNode, GrowMaskWithBlur, INPAINT_MaskedFill, ImageScale, LayerMask: MaskPreview, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, RH_Nano_Banana2_Image2Image, SaveImage, SetNode, easy imageConcat]
problems: []
missing: []
members: [图片生成/图生图/元素迁移（改图版）_2015276923118686210.json, 图片生成/图生图/香蕉2-全能图片V12-双图精准局部编辑（限时优惠0.25元1k到2k-0.5元4k）_1991528762282090497.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint_3

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/元素迁移（改图版）_2015276923118686210.json、图片生成/图生图/香蕉2-全能图片V12-双图精准局部编辑（限时优惠0.25元1k到2k-0.5元4k）_1991528762282090497.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：60%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Text`
- `GetNode`
- `GrowMaskWithBlur`
- `INPAINT_MaskedFill`
- `ImageScale`
- `LayerMask: MaskPreview`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`
- `SetNode`
- `easy imageConcat`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
