---
name: unknown_workflow_upscale_2
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.703
common_nodes: [Image Comparer (rgthree), LoadImage, SaveImage, VOSR2ModelLoader, VOSR2Upscale]
problems: []
missing: [LayerUtility: ImageScaleByAspectRatio V2]
members: [图片生成/图生图/2097239382121078785.json, 图片生成/图生图/2102213109866909697.json, 图片生成/图生图/2102323097541107714.json, 数字人/数字人/图像无损高清放大 - Vosr2_2097147455497400321.json, 数字人/数字人/图像高清放大  Vosr 2_2097144545875161090.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_2

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/2097239382121078785.json、图片生成/图生图/2102213109866909697.json、图片生成/图生图/2102323097541107714.json、数字人/数字人/图像无损高清放大 - Vosr2_2097147455497400321.json、数字人/数字人/图像高清放大  Vosr 2_2097144545875161090.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 5 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `SaveImage`
- `VOSR2ModelLoader`
- `VOSR2Upscale`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/5 个有
- `Int` —— 2/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/5 个有
- `EmptyImage` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：LayerUtility: ImageScaleByAspectRatio V2
