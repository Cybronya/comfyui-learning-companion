---
name: unknown_workflow_generic_1960
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.75
common_nodes: [Image Save, LoadImage, SaveImage]
problems: []
missing: []
members: [平台全量/批量放大（请下载后本地使用）_2044407521544245250.json, 平台全量/节点系列61-image save_2056925327800229889.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1960

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/批量放大（请下载后本地使用）_2044407521544245250.json、平台全量/节点系列61-image save_2056925327800229889.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Save`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/2 个有
- `LoadImageListFromDir //Inspire` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
