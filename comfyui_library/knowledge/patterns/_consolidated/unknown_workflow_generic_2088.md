---
name: unknown_workflow_generic_2088
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.794
common_nodes: [LoadAudio, LoadImage, LoadVideo, RH_MinimaxHailuoH3ImageToVideo, RH_MinimaxHailuoH3MultimodalToVideo, SaveVideo]
problems: []
missing: []
members: [视频生成/文生视频/海螺Hailuo H3文生视频、多图参考、视频复刻、首尾帧_2083373180177174529.json, 视频生成/文生视频/海螺Hailuo+H3文生视频、多图参考、视频参考、首尾帧_2083782686950387713.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_2088

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/文生视频/海螺Hailuo H3文生视频、多图参考、视频复刻、首尾帧_2083373180177174529.json、视频生成/文生视频/海螺Hailuo+H3文生视频、多图参考、视频参考、首尾帧_2083782686950387713.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：79%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadAudio`
- `LoadImage`
- `LoadVideo`
- `RH_MinimaxHailuoH3ImageToVideo`
- `RH_MinimaxHailuoH3MultimodalToVideo`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
