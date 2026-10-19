---
name: unknown_workflow_generic_732
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8395
common_nodes: [GetVideoComponents, ImageFromBatch, LoadVideo, PreviewAny, RHHiddenNodes, RH_RhartTextG3ProPreviewVideoToText, RH_RhartVideoSImageToVideo, RunningHub Deepcleaner, SaveVideo, ShellAgentPluginOutputText, ShowText|pysssss, easy saveText]
problems: []
missing: []
members: [视频生成/图生视频/2034923500376428545.json, 视频生成/图生视频/2034962984606375938.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_732

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/2034923500376428545.json、视频生成/图生视频/2034962984606375938.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：84%

## 共有节点

全部 2 个 workflow 都包含：
- `GetVideoComponents`
- `ImageFromBatch`
- `LoadVideo`
- `PreviewAny`
- `RHHiddenNodes`
- `RH_RhartTextG3ProPreviewVideoToText`
- `RH_RhartVideoSImageToVideo`
- `RunningHub Deepcleaner`
- `SaveVideo`
- `ShellAgentPluginOutputText`
- `ShowText|pysssss`
- `easy saveText`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
