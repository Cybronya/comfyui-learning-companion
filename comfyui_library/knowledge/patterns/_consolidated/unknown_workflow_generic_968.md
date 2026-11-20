---
name: unknown_workflow_generic_968
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.79
common_nodes: [LoadImage, RH_MinimaxHailuoH3MultimodalToVideo, SaveVideo]
problems: []
missing: []
members: [平台全量/H3官方多模态换品-仅大于15秒双段_2102232689838477313.json, 平台全量/MiniMax H3 多模态参考视频生成工作流_2083454876222316545.json, 视频生成/图生视频/H3全能参考工作流｜MiniMax H3 多图参考生成视频_2099348938208927746.json, 视频生成/图生视频/H3官方多模态换品-仅大于15秒双段_2102316839295606786.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_968

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（平台全量/H3官方多模态换品-仅大于15秒双段_2102232689838477313.json、平台全量/MiniMax H3 多模态参考视频生成工作流_2083454876222316545.json、视频生成/图生视频/H3全能参考工作流｜MiniMax H3 多图参考生成视频_2099348938208927746.json、视频生成/图生视频/H3官方多模态换品-仅大于15秒双段_2102316839295606786.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `RH_MinimaxHailuoH3MultimodalToVideo`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `LoadVideo` —— 3/4 个有
- `PrimitiveStringMultiline` —— 3/4 个有
- `VideoConcatenate` —— 2/4 个有
- `EmptyImage` —— 1/4 个有
- `PreviewImage` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
