---
name: unknown_workflow_generic_364
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.967857
common_nodes: [LoadImage, LongCatImageEdit, LongCatImageModelLoader, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Langcat 图片编辑工作流_1999675547762520066.json, 图片生成/图生图/LongCat Edit-单图像编辑_1997953637970272258.json, 图片生成/图生图/LongCat Edit单图像编辑_1997706385943146497.json, 图片生成/图生图/LongCat Edit单图像编辑_1997944364162777090.json, 图片生成/图生图/LongCat Edit单图像编辑_1998284496506093570.json, 图片生成/图生图/LongCat Edit单图像编辑_1998341204561551362.json, 图片生成/图生图/LongCat Edit图像编辑_2001778382910156802.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_364

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/Langcat 图片编辑工作流_1999675547762520066.json、图片生成/图生图/LongCat Edit-单图像编辑_1997953637970272258.json、图片生成/图生图/LongCat Edit单图像编辑_1997706385943146497.json、图片生成/图生图/LongCat Edit单图像编辑_1997944364162777090.json、图片生成/图生图/LongCat Edit单图像编辑_1998284496506093570.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 7 个 workflow 都包含：
- `LoadImage`
- `LongCatImageEdit`
- `LongCatImageModelLoader`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 6/7 个有
- `CR Prompt Text` —— 5/7 个有
- `LayerUtility: PurgeVRAM` —— 5/7 个有
- `easy imageConcat` —— 4/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/7 个有
- `Text` —— 1/7 个有
- `easy seed` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
