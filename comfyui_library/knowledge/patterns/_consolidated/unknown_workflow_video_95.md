---
name: unknown_workflow_video_95
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.95
common_nodes: [LoadImage, RunningHub_FramePack, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/FramePack巨偶互动_1913408833358655489.json, 平台全量/FramePack首尾帧_1914904336642600962.json, 视频生成/图生视频/FramePack丝滑首尾帧图生视频_1915017542644002818.json, 视频生成/图生视频/framepack_首尾帧_1914526532704923650.json]
source: knowledge_consolidation
---

# unknown_workflow_video_95

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/FramePack巨偶互动_1913408833358655489.json、平台全量/FramePack首尾帧_1914904336642600962.json、视频生成/图生视频/FramePack丝滑首尾帧图生视频_1915017542644002818.json、视频生成/图生视频/framepack_首尾帧_1914526532704923650.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `RunningHub_FramePack`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `KepStringLiteral` —— 3/4 个有
- `ImageResizeKJ` —— 2/4 个有
- `PrimitiveInt` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
