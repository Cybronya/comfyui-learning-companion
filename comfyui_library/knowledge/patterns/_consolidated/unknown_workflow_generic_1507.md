---
name: unknown_workflow_generic_1507
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.922
common_nodes: [LoadImage, PreviewImage, SaveImage, easy imageConcat]
problems: []
missing: []
members: [图片生成/图生图/多图拼接_1992877878245388289.json, 图片生成/图生图/拼图工作流（2×4、5×2）_2112550774663368706.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1507

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/多图拼接_1992877878245388289.json、图片生成/图生图/拼图工作流（2×4、5×2）_2112550774663368706.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：92%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `easy imageConcat`

**可变部分**（部分 workflow 才有）：
- `Image Batch` —— 1/2 个有
- `YuanImageGridComposite` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
