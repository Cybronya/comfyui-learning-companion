---
name: unknown_workflow_video_30
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.782429
common_nodes: [LoadImage, LoadSharpModel, SaveImage, SharpPredict, YCGaussianPreview]
problems: []
missing: []
members: [图片生成/图生图/Sharp单图生成3d高斯模型_2039537850651254786.json, 图片生成/图生图/苹果Sharp单图生成3d高斯_2012127244717658113.json, 平台全量/Apple SHARP高斯泼溅ply点云生成_2005811243418087426.json, 平台全量/苹果Sharp 单图3d高斯模型_2046948814963089410.json, 平台全量/苹果Sharp单图生成 3d高斯模型-最新_2045878382646267905.json, 平台全量/苹果Sharp单图生成3d高斯模型_2008317430430437377.json, 平台全量/苹果Sharp：单图即可生成3d高斯模型_2026828722870947842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_30

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Sharp单图生成3d高斯模型_2039537850651254786.json、图片生成/图生图/苹果Sharp单图生成3d高斯_2012127244717658113.json、平台全量/Apple SHARP高斯泼溅ply点云生成_2005811243418087426.json、平台全量/苹果Sharp 单图3d高斯模型_2046948814963089410.json、平台全量/苹果Sharp单图生成 3d高斯模型-最新_2045878382646267905.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 7 个 workflow 都包含：
- `LoadImage`
- `LoadSharpModel`
- `SaveImage`
- `SharpPredict`
- `YCGaussianPreview`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/7 个有
- `VHS_LoadVideoPath` —— 6/7 个有
- `VHS_VideoCombine` —— 6/7 个有
- `PrimitiveFloat` —— 1/7 个有
- `PrimitiveInt` —— 1/7 个有
- `easy imageScaleDownToSize` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
