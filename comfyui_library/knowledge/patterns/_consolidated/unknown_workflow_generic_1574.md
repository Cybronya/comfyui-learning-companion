---
name: unknown_workflow_generic_1574
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8365
common_nodes: [CR Color Panel, CR Text, FastCanvas, FastCanvasTool, GetImageSize+, Image Blend, Image Comparer (rgthree), ImageCompositeMasked, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, easy textSwitch]
problems: []
missing: []
members: [图片生成/图生图/谷歌局部重绘百分百不偏移_1994657556880629761.json, 图片生成/图生图/香蕉局部重绘迁移工作流自用流程_1985749160219615233.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1574

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/谷歌局部重绘百分百不偏移_1994657556880629761.json、图片生成/图生图/香蕉局部重绘迁移工作流自用流程_1985749160219615233.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Color Panel`
- `CR Text`
- `FastCanvas`
- `FastCanvasTool`
- `GetImageSize+`
- `Image Blend`
- `Image Comparer (rgthree)`
- `ImageCompositeMasked`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `easy textSwitch`

**可变部分**（部分 workflow 才有）：
- `Comfly_api_set` —— 1/2 个有
- `Comfly_nano_banana` —— 1/2 个有
- `JjkText` —— 1/2 个有
- `PIP_图像联结` —— 1/2 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
