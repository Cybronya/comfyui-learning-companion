---
name: unknown_workflow_video_98
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.778
common_nodes: [GetVideoComponents, JjkText, LoadImage, SaveVideo, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/Seedance2.5min前后帧室内白天夜晚光影变化_2074319853363752961.json, 视频生成/图生视频/Seedance2.5min多图生视频_2083009273801564162.json]
source: knowledge_consolidation
---

# unknown_workflow_video_98

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Seedance2.5min前后帧室内白天夜晚光影变化_2074319853363752961.json、视频生成/图生视频/Seedance2.5min多图生视频_2083009273801564162.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `GetVideoComponents`
- `JjkText`
- `LoadImage`
- `SaveVideo`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `RHLLMChatNode` —— 1/2 个有
- `RH_RhartVideoSparkvideo20MiniImageToVideo` —— 1/2 个有
- `RH_RhartVideoSparkvideo20MiniMultimodalVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
