---
name: unknown_workflow_generic_1905
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [Color (hexadecimal), LoadImage, RBGImageStitchPlus, SaveImage]
problems: []
missing: []
members: [平台全量/RBG图片拼接_1945074224065126401.json, 平台全量/RBG图片拼接多格图_1945649665012375553.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1905

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/RBG图片拼接_1945074224065126401.json、平台全量/RBG图片拼接多格图_1945649665012375553.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `Color (hexadecimal)`
- `LoadImage`
- `RBGImageStitchPlus`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/2 个有
- `RBGPadPro` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
