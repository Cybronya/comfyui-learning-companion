---
name: unknown_workflow_video_146
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.765
common_nodes: [ImageFromBatch+, PrimitiveInt, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/空白工作流_2011700877723176962.json, 平台全量/获取开头部分视频_视频剪辑_2011696880283029505.json, 平台全量/获取视频部分帧数_1981287882684006402.json]
source: knowledge_consolidation
---

# unknown_workflow_video_146

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/空白工作流_2011700877723176962.json、平台全量/获取开头部分视频_视频剪辑_2011696880283029505.json、平台全量/获取视频部分帧数_1981287882684006402.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageFromBatch+`
- `PrimitiveInt`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `ImageScale` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `LoadImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
