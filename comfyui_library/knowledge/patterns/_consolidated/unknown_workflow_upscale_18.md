---
name: unknown_workflow_upscale_18
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.833
common_nodes: [Image Comparer (rgthree), LoadImage, RH_RFMSR_ModelLoader, RH_RFMSR_Upscale, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/RFMSR Upscale 高清放大_2026216768892571649.json, 图片生成/图生图/图片放大修复_RFMSR_2082377090774687745.json, 图片生成/图生图/图片放大修复_RFMSR_2084971950656548865.json, 图片生成/图生图/图片放大修复_RFMSR_2085175418247798786.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_18

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/RFMSR Upscale 高清放大_2026216768892571649.json、图片生成/图生图/图片放大修复_RFMSR_2082377090774687745.json、图片生成/图生图/图片放大修复_RFMSR_2084971950656548865.json、图片生成/图生图/图片放大修复_RFMSR_2085175418247798786.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 4 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `RH_RFMSR_ModelLoader`
- `RH_RFMSR_Upscale`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 3/4 个有
- `JWImageResizeByLongerSide` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
