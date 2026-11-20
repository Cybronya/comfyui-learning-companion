---
name: unknown_workflow_video_inpaint_5
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.95
common_nodes: [ImageResize+, ImageToMask, LoadImage, ProPainterInpaint, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/峰上智行_1926231050593452033.json, 平台全量/视频去logo，效果好，速度快，操作简单_1972129989384663042.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_5

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/峰上智行_1926231050593452033.json、平台全量/视频去logo，效果好，速度快，操作简单_1972129989384663042.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：95%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageResize+`
- `ImageToMask`
- `LoadImage`
- `ProPainterInpaint`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
