---
name: unknown_workflow_sampler_19
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.653333
common_nodes: [LoadImage, RunningHub USO Loader, RunningHub USO Sampler, SaveImage]
problems: []
missing: [RunningHub USO Loader, RunningHub USO Sampler]
members: [图片生成/文生图/1962533944346456065.json, 图片生成/文生图/1964595430032068610.json, 图片生成/文生图/1965031029104889857.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_19

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/1962533944346456065.json、图片生成/文生图/1964595430032068610.json、图片生成/文生图/1965031029104889857.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：65%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `RunningHub USO Loader`
- `RunningHub USO Sampler`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `RH_Translator` —— 2/3 个有
- `DF_Get_image_size` —— 1/3 个有
- `ImageConcanate` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：RunningHub USO Loader、RunningHub USO Sampler
