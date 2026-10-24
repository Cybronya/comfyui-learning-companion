---
name: unknown_workflow_inpaint
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.86825
common_nodes: [CR Text, GrowMaskWithBlur, INPAINT_MaskedFill, ImageScale, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, RH_Nano_Banana2_Image2Image, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/hs_ 全能图片V1 2，效果图配景局部迁移_1991862778034188289.json, 图片生成/图生图/全能图片V1局部修改_1994970971058659329.json, 图片生成/文生图/全能图片V12-0.25元一次_1991544351375441921.json, 图片生成/文生图/全能图片V12-0.25元一次_1997470281025404930.json]
source: knowledge_consolidation
---

# unknown_workflow_inpaint

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/hs_ 全能图片V1 2，效果图配景局部迁移_1991862778034188289.json、图片生成/图生图/全能图片V1局部修改_1994970971058659329.json、图片生成/文生图/全能图片V12-0.25元一次_1991544351375441921.json、图片生成/文生图/全能图片V12-0.25元一次_1997470281025404930.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Text`
- `GrowMaskWithBlur`
- `INPAINT_MaskedFill`
- `ImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
