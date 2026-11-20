---
name: unknown_workflow_upscale_9
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.797286
common_nodes: [ImageUpscaleWithModel, LoadImage, SaveImage, UpscaleModelLoader]
problems: []
missing: []
members: [图片生成/图生图/图片清晰锻造_2082474759727697922.json, 图片生成/图生图/基础超分算法（模型放大）工作流（自用）_2004573662835605505.json, 图片生成/图生图/文字无损高清放大（超简单高效工作流）_2077032201287462914.json, 图片生成/图生图/文字高清放大_文本修复_高清放大_1979195991507243009.json, 图片生成/图生图/文字高清放大_文本修复_高清放大_2084102513225199618.json, 图片生成/图生图/文本修复-文字无损高清放大_2061708019309826049.json, 图片生成/图生图/模糊文字变高清化_1916792207783956482.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_9

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/图片清晰锻造_2082474759727697922.json、图片生成/图生图/基础超分算法（模型放大）工作流（自用）_2004573662835605505.json、图片生成/图生图/文字无损高清放大（超简单高效工作流）_2077032201287462914.json、图片生成/图生图/文字高清放大_文本修复_高清放大_1979195991507243009.json、图片生成/图生图/文字高清放大_文本修复_高清放大_2084102513225199618.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 7 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `LoadImage`
- `SaveImage`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 6/7 个有
- `ImageTile+` —— 5/7 个有
- `ImageUntile+` —— 5/7 个有
- `easy imageColorMatch` —— 5/7 个有
- `PreviewImage` —— 3/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
