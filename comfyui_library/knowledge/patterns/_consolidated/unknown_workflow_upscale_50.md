---
name: unknown_workflow_upscale_50
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [LoadImage, LoadVideo, SaveVideo]
problems: []
missing: []
members: [数字人/数字人/专业视频超分 TopazLabs_2063138098481029122.json, 数字人/数字人/动作迁移·角色替换-AI视频换人_2093885220666822658.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_50

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（数字人/数字人/专业视频超分 TopazLabs_2063138098481029122.json、数字人/数字人/动作迁移·角色替换-AI视频换人_2093885220666822658.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `LoadVideo`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `RHBerniniFullReferenceVideoToVideo` —— 1/2 个有
- `RH_TopazLabs_VideoUpscale` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
