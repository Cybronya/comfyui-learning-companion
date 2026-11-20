---
name: unknown_workflow_generic_1190
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.878333
common_nodes: [ImageScale, Int, JjkText, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/单分镜图切分拆分工具（4宫格9宫格拆分单独图片分镜拆分）_2111089921892114433.json, 平台全量/分镜图切分拆分工具（4宫格9宫格等多种拼合图像拆分单独图片分镜拆分）_2043942356822528002.json, 平台全量/批量分镜图切分拆分工具（4宫格9宫格拆分单独图片分镜拆分）_2043923667276537857.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_1190

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/单分镜图切分拆分工具（4宫格9宫格拆分单独图片分镜拆分）_2111089921892114433.json、平台全量/分镜图切分拆分工具（4宫格9宫格等多种拼合图像拆分单独图片分镜拆分）_2043942356822528002.json、平台全量/批量分镜图切分拆分工具（4宫格9宫格拆分单独图片分镜拆分）_2043923667276537857.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 3 个 workflow 都包含：
- `ImageScale`
- `Int`
- `JjkText`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `CompressImages` —— 2/3 个有
- `HAIGC_LoadImagesFromZip` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `SaveImage` —— 2/3 个有
- `easy imageListToImageBatch` —— 2/3 个有
- `HAIGC_SaveImagesToZip` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
