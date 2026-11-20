---
name: unknown_workflow_generic_761
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.805
common_nodes: [ImageBatch, ImageScaleToTotalPixels, LoadImage, PreviewImage, RH_Nano_Banana_Image2Image, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/全能融图url_1991042974500986882.json, 图片生成/图生图/全能融图url_1991044291315343362.json, 图片生成/图生图/全能融图本地_1991793529317961729.json, 图片生成/图生图/全能融图本地_2000747780865916929.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_761

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/全能融图url_1991042974500986882.json、图片生成/图生图/全能融图url_1991044291315343362.json、图片生成/图生图/全能融图本地_1991793529317961729.json、图片生成/图生图/全能融图本地_2000747780865916929.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 4 个 workflow 都包含：
- `ImageBatch`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `PreviewImage`
- `RH_Nano_Banana_Image2Image`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LoadImagesFromURL` —— 2/4 个有
- `MaskToImage` —— 2/4 个有
- `Mix Color By Mask` —— 2/4 个有
- `RH_Nano_Banana2_Image2Image` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
