---
name: unknown_workflow_generic_685
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.707
common_nodes: [EmptyImage, LoadImage, PreviewImage, PrimitiveStringMultiline, RH_MinimaxHailuoH3MultimodalToVideo, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/H3官方多模态换品-仅大于15秒双段_2102316839295606786.json, 视频生成/图生视频/MiniMax_H3上下文参考视频+图生视频-融合运镜与角色工作流_2101304865048846337.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_685

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/H3官方多模态换品-仅大于15秒双段_2102316839295606786.json、视频生成/图生视频/MiniMax_H3上下文参考视频+图生视频-融合运镜与角色工作流_2101304865048846337.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `EmptyImage`
- `LoadImage`
- `PreviewImage`
- `PrimitiveStringMultiline`
- `RH_MinimaxHailuoH3MultimodalToVideo`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 1/2 个有
- `RH_MinimaxHailuoH3ContextIrMultimodal` —— 1/2 个有
- `VideoConcatenate` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
