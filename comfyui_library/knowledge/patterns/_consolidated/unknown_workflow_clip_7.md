---
name: unknown_workflow_clip_7
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8
common_nodes: [PreviewImage, SaveImage, workflow/模型组, workflow/采样器]
problems: []
missing: []
members: [图片生成/文生图/一键批量人物一致性_1900917256862187522.json, 图片生成/文生图/文生图油画风格_1901150306908913665.json]
source: knowledge_consolidation
---

# unknown_workflow_clip_7

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/一键批量人物一致性_1900917256862187522.json、图片生成/文生图/文生图油画风格_1901150306908913665.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：80%

## 共有节点

全部 2 个 workflow 都包含：
- `PreviewImage`
- `SaveImage`
- `workflow/模型组`
- `workflow/采样器`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 1/2 个有
- `String Literal` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
