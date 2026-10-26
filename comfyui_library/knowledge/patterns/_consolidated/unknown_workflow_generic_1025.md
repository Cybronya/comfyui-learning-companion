---
name: unknown_workflow_generic_1025
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.772
common_nodes: [ConstrainImage|pysssss, Get Image Size, Image Comparer (rgthree), ImageFromBatch, ImageResize+, ImageScaleBy, LoadImage, PreviewImage, RHHiddenNodes, SaveImage, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy forLoopEnd, easy forLoopStart, easy joinImageBatch]
problems: []
missing: []
members: [图片生成/图生图/分镜切割机-2k_2008082317960552450.json, 图片生成/图生图/新年表情包一键生成器_2065144681117343746.json, 图片生成/图生图/表情包变身相机-新春贺岁_2010150238945808385.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1025

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/分镜切割机-2k_2008082317960552450.json、图片生成/图生图/新年表情包一键生成器_2065144681117343746.json、图片生成/图生图/表情包变身相机-新春贺岁_2010150238945808385.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `ConstrainImage|pysssss`
- `Get Image Size`
- `Image Comparer (rgthree)`
- `ImageFromBatch`
- `ImageResize+`
- `ImageScaleBy`
- `LoadImage`
- `PreviewImage`
- `RHHiddenNodes`
- `SaveImage`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy forLoopEnd`
- `easy forLoopStart`
- `easy joinImageBatch`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Muter (rgthree)` —— 2/3 个有
- `JjkText` —— 2/3 个有
- `RH_Nano_Banana2_Image2Image` —— 2/3 个有
- `easy anythingIndexSwitch` —— 2/3 个有
- `CR Image Grid Panel` —— 1/3 个有
- `ImageListToBatch+` —— 1/3 个有
- `TT_img_enc` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
