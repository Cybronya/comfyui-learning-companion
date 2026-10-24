---
name: unknown_workflow_generic_1577
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.775
common_nodes: [LoadImage, PrimitiveStringMultiline, SaveVideo]
problems: []
missing: []
members: [视频生成/图生视频/图生视频工作流｜Gemini Omni 1.1 Flash 稳定版 可上 4K_2100471517942468610.json, 视频生成/图生视频/图生视频工作流｜Gen4 Turbo 快速出片版_2099690013071077378.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1577

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/图生视频工作流｜Gemini Omni 1.1 Flash 稳定版 可上 4K_2100471517942468610.json、视频生成/图生视频/图生视频工作流｜Gen4 Turbo 快速出片版_2099690013071077378.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `PrimitiveStringMultiline`
- `SaveVideo`

**可变部分**（部分 workflow 才有）：
- `RH_GoogleGeminiOmni11FlashImageToVideo` —— 1/2 个有
- `RH_RhartVideoRGen4TurboImageToVideo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
