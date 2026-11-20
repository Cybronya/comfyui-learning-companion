---
name: unknown_workflow_generic_1879
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7775
common_nodes: [BiRefNetRMBG, LayerMask: Shadow & Highlight Mask, RHHiddenNodes, SDMatteApply, SaveImage]
problems: []
missing: []
members: [平台全量/AI 抠图-半透明_2005991780527063041.json, 平台全量/批量 AI 抠图-半透明_2005829441517481986.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1879

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/AI 抠图-半透明_2005991780527063041.json、平台全量/批量 AI 抠图-半透明_2005829441517481986.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：78%

## 共有节点

全部 2 个 workflow 都包含：
- `BiRefNetRMBG`
- `LayerMask: Shadow & Highlight Mask`
- `RHHiddenNodes`
- `SDMatteApply`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `RHUploadZip_V2` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
