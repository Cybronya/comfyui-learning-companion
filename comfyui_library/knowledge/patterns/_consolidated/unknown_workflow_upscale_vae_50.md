---
name: unknown_workflow_upscale_vae_50
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8605
common_nodes: [GuHaiAutoImageSplit, Image Comparer (rgthree), ImageResize+, ImageScaleBy, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageSize, 孤海注释]
problems: []
missing: []
members: [图片生成/图生图/多宫格图片高清放大裁切，短剧分镜故事板使用_2064073208059486209.json, 图片生成/图生图/多宫格高清放大裁切！开源短剧必备功能！_2061765655824785409.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_50

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/多宫格图片高清放大裁切，短剧分镜故事板使用_2064073208059486209.json、图片生成/图生图/多宫格高清放大裁切！开源短剧必备功能！_2061765655824785409.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：86%

## 共有节点

全部 2 个 workflow 都包含：
- `GuHaiAutoImageSplit`
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
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `Label (rgthree)` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
