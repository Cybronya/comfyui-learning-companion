---
name: unknown_workflow_generic_1387
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7735
common_nodes: [LoadImage, LoadOOTDPipelineHub, OOTDGenerate, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/OOTD一键换装_1887474966970171394.json, 图片生成/图生图/ootd上半身全是连衣裙换装工作流_1946924755540959234.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1387

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/OOTD一键换装_1887474966970171394.json、图片生成/图生图/ootd上半身全是连衣裙换装工作流_1946924755540959234.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：77%

## 共有节点

全部 2 个 workflow 都包含：
- `LoadImage`
- `LoadOOTDPipelineHub`
- `OOTDGenerate`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
