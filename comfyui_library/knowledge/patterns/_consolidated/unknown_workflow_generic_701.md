---
name: unknown_workflow_generic_701
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7945
common_nodes: [FiboEdit, FiboEdit_VLM, GetImageSize, LoadImage, ResizeMask, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Fibo-Edit 单图编辑_2019360229091188737.json, 图片生成/图生图/Fibo-Edit 图像编辑_2018881906758131714.json, 图片生成/图生图/Fibo-Edit 图生图_2018623034420109314.json, 图片生成/图生图/Fibo-Edit 基础工作流_2018521609757265922.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_701

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Fibo-Edit 单图编辑_2019360229091188737.json、图片生成/图生图/Fibo-Edit 图像编辑_2018881906758131714.json、图片生成/图生图/Fibo-Edit 图生图_2018623034420109314.json、图片生成/图生图/Fibo-Edit 基础工作流_2018521609757265922.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 4 个 workflow 都包含：
- `FiboEdit`
- `FiboEdit_VLM`
- `GetImageSize`
- `LoadImage`
- `ResizeMask`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageScaleToTotalPixels` —— 3/4 个有
- `JjkText` —— 3/4 个有
- `easy showAnything` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `ImageResize+` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
