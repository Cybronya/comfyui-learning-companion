---
name: unknown_workflow_generic_1714
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8875
common_nodes: [LoadVideoFromURL, MathExpression|pysssss, PreviewImage, RH_Utils, SaveImage, SaveVideo, VHS_SelectImages]
problems: []
missing: []
members: [视频生成/图生视频/全能视频V3 API图生视频，保存尾帧，可用于后续视频连续生成_1980894179444310017.json, 视频生成/文生视频/全能视频V3 API文生视频，保存尾帧，可用于后续视频连续生成_1971568471970672641.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1714

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/全能视频V3 API图生视频，保存尾帧，可用于后续视频连续生成_1980894179444310017.json、视频生成/文生视频/全能视频V3 API文生视频，保存尾帧，可用于后续视频连续生成_1971568471970672641.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：89%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadVideoFromURL`
- `MathExpression|pysssss`
- `PreviewImage`
- `RH_Utils`
- `SaveImage`
- `SaveVideo`
- `VHS_SelectImages`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 1/2 个有
- `RH_Veo3_Image2Video` —— 1/2 个有
- `RH_Veo3_Text2Video` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
