---
name: unknown_workflow_upscale_73
type: Unknown Workflow
frequency: 2
level: weak
coverage: 1
common_nodes: [CR Overlay Text, LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/图片添加文字 - 基础工作流_1931643608393252865.json, 平台全量/文字覆盖_1917392964132474882.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_73

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/图片添加文字 - 基础工作流_1931643608393252865.json、平台全量/文字覆盖_1917392964132474882.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：100%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Overlay Text`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `UpscaleImageByUsingModel` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
