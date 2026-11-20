---
name: unknown_workflow_generic_1281
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7685
common_nodes: [DownloadAndLoadFlorence2Model, Florence2Run, LoadImage, SaveImage, ShowText|pysssss]
problems: []
missing: []
members: [图片生成/反推提示词/Florence 2 图像反推合集_1980101031394709505.json, 图片生成/反推提示词/蒜-图生文工作流_1994991261130141698.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1281

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/反推提示词/Florence 2 图像反推合集_1980101031394709505.json、图片生成/反推提示词/蒜-图生文工作流_1994991261130141698.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `LoadImage`
- `SaveImage`
- `ShowText|pysssss`

**可变部分**（部分 workflow 才有）：
- `MaskPreview` —— 1/2 个有
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
