---
name: unknown_workflow_generic_1697
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [LoadAudio, LoadImage, LoadVideo, RH_AlibabaWan30PrimeImageToVideo, SaveVideo, Text]
problems: []
missing: []
members: [视频生成/图生视频/Wan3.0高速版-直出30秒-单图_首尾帧生视频_2093005951082262529.json, 视频生成/图生视频/阿里最强视频模型wan3.0 Prime多模态生视频低至0.43元_秒_2092420381729714178.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1697

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/Wan3.0高速版-直出30秒-单图_首尾帧生视频_2093005951082262529.json、视频生成/图生视频/阿里最强视频模型wan3.0 Prime多模态生视频低至0.43元_秒_2092420381729714178.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `RH_AlibabaWan30PrimeImageToVideo`
- `SaveVideo`
- `Text`

**可变部分**（部分 workflow 才有）：
- `RH_AlibabaWan30PrimeReferenceToVideo` —— 1/2 个有
- `easy saveText` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
