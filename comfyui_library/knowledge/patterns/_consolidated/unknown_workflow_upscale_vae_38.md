---
name: unknown_workflow_upscale_vae_38
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.703
common_nodes: [Fast Groups Bypasser (rgthree), GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: []
members: [图片生成/图生图/（漫剧人物）放大细节修复（极速版）_2045585679790379010.json, 图片生成/图生图/（超好用！）SeedVR2+TTP一亿像素极限放大+0损耗压缩_2004539129138475009.json, 图片生成/图生图/🍭老许Gary：SeedVR2.5图像放大修复_2018018624648253441.json, 图片生成/文生图/SeedVR2+TTP放大+0损耗压缩_2001561615235444738.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_38

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/（漫剧人物）放大细节修复（极速版）_2045585679790379010.json、图片生成/图生图/（超好用！）SeedVR2+TTP一亿像素极限放大+0损耗压缩_2004539129138475009.json、图片生成/图生图/🍭老许Gary：SeedVR2.5图像放大修复_2018018624648253441.json、图片生成/文生图/SeedVR2+TTP放大+0损耗压缩_2001561615235444738.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `Fast Groups Bypasser (rgthree)`
- `GetImageSize+`
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

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 3/4 个有
- `INTConstant` —— 2/4 个有
- `ImageScaleToTotalPixels` —— 2/4 个有
- `KOOK_ImageCompression` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `CR Simple Image Compare` —— 1/4 个有
- `Float` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
