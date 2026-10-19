---
name: unknown_workflow_video_84
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CR Prompt Text, GetVideoComponents, LoadImage, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/2062201896533839874.json, 视频生成/图生视频/2062197611167309826.json]
source: knowledge_consolidation
---

# unknown_workflow_video_84

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2062201896533839874.json、视频生成/图生视频/2062197611167309826.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Prompt Text`
- `GetVideoComponents`
- `LoadImage`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `RH_RhartVideoV31FastImageToVideo` —— 1/2 个有
- `RH_RhartVideoV31FastStartEndToVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
