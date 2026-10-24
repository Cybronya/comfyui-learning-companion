---
name: unknown_workflow_sampler_83
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.812
common_nodes: [Fast Groups Muter (rgthree), ImageConcanate, LoadImage, PreviewAny, SaveImage, SenseNova_SM_Model, SenseNova_SM_Sampler]
problems: []
missing: []
members: [图片生成/文生图/SenseNova U1 图像编辑 文生图 视觉理解集合 商汤大模型_2053080764119560193.json, 图片生成/文生图/SenseNova图像生成、图像编辑与问答三合一工作流_2052920004227674114.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_83

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/SenseNova U1 图像编辑 文生图 视觉理解集合 商汤大模型_2053080764119560193.json、图片生成/文生图/SenseNova图像生成、图像编辑与问答三合一工作流_2052920004227674114.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：81%

## 共有节点

全部 2 个 workflow 都包含：
- `Fast Groups Muter (rgthree)`
- `ImageConcanate`
- `LoadImage`
- `PreviewAny`
- `SaveImage`
- `SenseNova_SM_Model`
- `SenseNova_SM_Sampler`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
