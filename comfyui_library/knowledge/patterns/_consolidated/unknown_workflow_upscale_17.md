---
name: unknown_workflow_upscale_17
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.623
common_nodes: [Image Comparer (rgthree), LoadImage, PreviewImage, SaveImage, VOSR2Upscale]
problems: []
missing: []
members: [图片生成/图生图/LEON_无损放大_细节恢复_强化文字_2097209556941230081.json, 图片生成/图生图/VOSR图像文字4K超快速放大_2112161469726027778.json, 数字人/数字人/图像无损高清放大 - Vosr2_2097147455497400321.json, 数字人/数字人/图像高清放大  Vosr 2_2097144545875161090.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_17

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/LEON_无损放大_细节恢复_强化文字_2097209556941230081.json、图片生成/图生图/VOSR图像文字4K超快速放大_2112161469726027778.json、数字人/数字人/图像无损高清放大 - Vosr2_2097147455497400321.json、数字人/数字人/图像高清放大  Vosr 2_2097144545875161090.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：62%

## 共有节点

全部 4 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VOSR2Upscale`

**可变部分**（部分 workflow 才有）：
- `VOSR2ModelLoader` —— 3/4 个有
- `ImageScaleBy` —— 1/4 个有
- `RHHiddenNodes` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
