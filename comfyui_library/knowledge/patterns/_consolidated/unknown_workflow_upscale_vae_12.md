---
name: unknown_workflow_upscale_vae_12
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.942538
common_nodes: [ImageResize+, ImageScaleBy, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: []
members: [图片生成/图生图/无损放大工作流_2046887976344494082.json, 图片生成/图生图/老孙AI TTP+seed VR2放大 亿级像素_2114580383802159106.json, 图片生成/图生图/老孙AI_TTP+seed_VR2放大_亿级像素_2115627902225182722.json, 图片生成/图生图/老孙AI_TTP+seed_VR2放大_亿级像素_2115672787288412162.json, 图片生成/图生图/零偏差高清放大_SeedVR2_jex_2040343386443489281.json, 图片生成/图生图/高清放大 SeedVR2.5 + TTP分块放大_2071767145079468033.json, 图片生成/图生图/高清放大SeedVR2.5 + TTP 分块放大1.0_2061629043874820098.json, 图片生成/图生图/（毛孔级别）SeedVR2.5 + TTP 分块放大_2116887494741544961.json, 平台全量/SeedVR2.5 + TTP 分块放大 图像高清放大，人像放大去AI感，增加皮肤纹理，去瑕疵，图像_2001497756566994946.json, 平台全量/SeedVR2.5 + TTP 分块放大_1934785108039933953.json, 平台全量/TTP+SeedVR2高清放大_2057064716190703618.json, 平台全量/放大_2057068854257475586.json, 平台全量/高清重绘【TTP+SeedVR2】- 御川0730_2082745683559403521.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_12

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/无损放大工作流_2046887976344494082.json、图片生成/图生图/老孙AI TTP+seed VR2放大 亿级像素_2114580383802159106.json、图片生成/图生图/老孙AI_TTP+seed_VR2放大_亿级像素_2115627902225182722.json、图片生成/图生图/老孙AI_TTP+seed_VR2放大_亿级像素_2115672787288412162.json、图片生成/图生图/零偏差高清放大_SeedVR2_jex_2040343386443489281.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 13 个 workflow 都包含：
- `ImageResize+`
- `ImageScaleBy`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`

**可变部分**（部分 workflow 才有）：
- `LoadImage` —— 12/13 个有
- `Image Comparer (rgthree)` —— 11/13 个有
- `Get Image Size` —— 10/13 个有
- `ConstrainImage|pysssss` —— 9/13 个有
- `GetImageSize+` —— 4/13 个有
- `KOOK_SaveJPGImage` —— 1/13 个有
- `MuyeLoadImage` —— 1/13 个有
- `PreviewImage` —— 1/13 个有
- `easy cleanGpuUsed` —— 1/13 个有
- `easy imageScaleToNormPixels` —— 1/13 个有
- `数学运算_孤海` —— 1/13 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
