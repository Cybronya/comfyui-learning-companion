---
name: unknown_workflow_generic_512
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 1
common_nodes: [LoadImage, RH_RhartImageG2ImageToImage, SaveImage, Text]
problems: []
missing: []
members: [图片生成/图生图/YJ-APP-全能图片G--image-单图编辑_2047138899423662081.json, 图片生成/图生图/YJ-APP-全能图片G--image-双图编辑_2047127324696518658.json, 图片生成/图生图/xxx-image2_2053839405277827073.json, 图片生成/图生图/提取头部_2095356769915727873.json, 图片生成/图生图/道具图生成_2094712567414476802.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_512

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/YJ-APP-全能图片G--image-单图编辑_2047138899423662081.json、图片生成/图生图/YJ-APP-全能图片G--image-双图编辑_2047127324696518658.json、图片生成/图生图/xxx-image2_2053839405277827073.json、图片生成/图生图/提取头部_2095356769915727873.json、图片生成/图生图/道具图生成_2094712567414476802.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadImage`
- `RH_RhartImageG2ImageToImage`
- `SaveImage`
- `Text`

**可变部分**（部分 workflow 才有）：
- `TextConcatenator` —— 3/5 个有
- `ratio_selector` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
