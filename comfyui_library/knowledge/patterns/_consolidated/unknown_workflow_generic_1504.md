---
name: unknown_workflow_generic_1504
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.75
common_nodes: [Image Comparer (rgthree), RH_Nano_Banana2_Image2Image, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/在线 -  全能图片V12-双图_1994391204693483522.json, 图片生成/文生图/全能图像编辑0410_2038887358690496513.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1504

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/在线 -  全能图片V12-双图_1994391204693483522.json、图片生成/文生图/全能图像编辑0410_2038887358690496513.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：75%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `RH_Nano_Banana2_Image2Image`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 1/2 个有
- `LoadImagesFromURL` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
