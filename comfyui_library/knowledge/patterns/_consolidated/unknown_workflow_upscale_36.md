---
name: unknown_workflow_upscale_36
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7085
common_nodes: [Image Comparer (rgthree), LoadImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/CCSR放大_1980683599676620801.json, 图片生成/图生图/滑块图像对比_2091034902765588482.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_36

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/CCSR放大_1980683599676620801.json、图片生成/图生图/滑块图像对比_2091034902765588482.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `CCSR_Model_Select` —— 1/2 个有
- `CCSR_Upscale` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
