---
name: unknown_workflow_upscale_vae_64
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.823667
common_nodes: [Image Comparer (rgthree), ImageResize+, ImageScaleBy, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageSize]
problems: []
missing: []
members: [图片生成/图生图/多宫格图片高清放大裁切，短剧分镜故事板使用_2064073208059486209.json, 图片生成/图生图/多宫格高清放大裁切！开源短剧必备功能！_2061765655824785409.json, 平台全量/TTP+seedVR2超分放大_2059627075086143489.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_64

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/多宫格图片高清放大裁切，短剧分镜故事板使用_2064073208059486209.json、图片生成/图生图/多宫格高清放大裁切！开源短剧必备功能！_2061765655824785409.json、平台全量/TTP+seedVR2超分放大_2059627075086143489.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：82%

## 共有节点

全部 3 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `GuHaiAutoImageSplit` —— 2/3 个有
- `孤海注释` —— 2/3 个有
- `DF_Integer` —— 1/3 个有
- `JWInteger` —— 1/3 个有
- `Label (rgthree)` —— 1/3 个有
- `LayerUtility: PurgeVRAM` —— 1/3 个有
- `PreviewImage` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
