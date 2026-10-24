---
name: unknown_workflow_generic_1399
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.656
common_nodes: [ImageResizeKJv2, ImageScaleToTotalPixels, LoadImage, PreviewImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/提取姿势_2103116858198155265.json, 图片生成/文生图/节点系列02-resize_v2节点_2010905425004208129.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1399

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/提取姿势_2103116858198155265.json、图片生成/文生图/节点系列02-resize_v2节点_2010905425004208129.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：66%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageResizeKJv2`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `PreviewImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `AIO_Preprocessor` —— 1/2 个有
- `ConstrainResolution` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
