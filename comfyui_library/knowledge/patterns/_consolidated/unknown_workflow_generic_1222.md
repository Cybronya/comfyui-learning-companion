---
name: unknown_workflow_generic_1222
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.847667
common_nodes: [LoadImage, PreviewImage, RH_Nano_Banana2_Gemini31Flash, SaveImage, SegmentV2, StringMergeNode, Text, 图像缩放V2_孤海]
problems: []
missing: []
members: [图片生成/图生图/秋水新脸洗图1_2110174760478011393.json, 平台全量/co换脸4k（新1）_2117891172709527553.json, 平台全量/co换脸4k（新3）_2117894912946556929.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1222

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/秋水新脸洗图1_2110174760478011393.json、平台全量/co换脸4k（新1）_2117891172709527553.json、平台全量/co换脸4k（新3）_2117894912946556929.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 3 个 workflow 都包含：
- `LoadImage`
- `PreviewImage`
- `RH_Nano_Banana2_Gemini31Flash`
- `SaveImage`
- `SegmentV2`
- `StringMergeNode`
- `Text`
- `图像缩放V2_孤海`

**可变部分**（部分 workflow 才有）：
- `ColorMatchPro` —— 2/3 个有
- `GetImageSize` —— 2/3 个有
- `Image Crop Location` —— 2/3 个有
- `ResolutionSelector` —— 2/3 个有
- `SimpleMath+` —— 2/3 个有
- `图像遮罩比例裁剪` —— 2/3 个有
- `JoinImageWithAlpha` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
