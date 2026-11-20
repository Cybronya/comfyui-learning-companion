---
name: unknown_workflow_video_139
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.636333
common_nodes: [LoadImage, PreviewImage, ReActorFaceSwap, SaveImage, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/ReActor图片换脸+视频换脸_1924829234173255682.json, 平台全量/视频换脸图片换脸工作流1.0_1921042292969242626.json, 平台全量/视频换脸图片换脸工作流1.0_1980147226402000897.json]
source: knowledge_consolidation
---

# unknown_workflow_video_139

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/ReActor图片换脸+视频换脸_1924829234173255682.json、平台全量/视频换脸图片换脸工作流1.0_1921042292969242626.json、平台全量/视频换脸图片换脸工作流1.0_1980147226402000897.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：64%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `PreviewImage`
- `ReActorFaceSwap`
- `SaveImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Load Image Batch` —— 2/3 个有
- `ReActorFaceBoost` —— 2/3 个有
- `FaceAnalysisModels` —— 1/3 个有
- `FaceBoundingBox` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
