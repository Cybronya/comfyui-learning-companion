---
name: unknown_workflow_generic_1300
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.866
common_nodes: [CR Simple Image Compare, LoadImage, Note Plus (mtb), PrimitiveStringMultiline, RH_ComfyFluxKontext, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/【橘子AI】FLUX KONTEXT 全能图像修改工作流（单图+多图参考）_1929757301459292161.json, 图片生成/文生图/FLUX KONTEXT 全能图像修改工作流单图_1930155063808004097.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1300

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/【橘子AI】FLUX KONTEXT 全能图像修改工作流（单图+多图参考）_1929757301459292161.json、图片生成/文生图/FLUX KONTEXT 全能图像修改工作流单图_1930155063808004097.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：87%

## 共有节点

全部 2 个 workflow 都包含：
- `CR Simple Image Compare`
- `LoadImage`
- `Note Plus (mtb)`
- `PrimitiveStringMultiline`
- `RH_ComfyFluxKontext`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 1/2 个有
- `easy imageScaleDownToSize` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
