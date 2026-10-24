---
name: unknown_workflow_upscale_vae_40
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.677667
common_nodes: [GetImageSize+, ImageResize+, ImageScaleBy, KOOK_ImageCompression, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy showAnything]
problems: []
missing: []
members: [图片生成/图生图/全能图片2高清出图(2K单图编辑版)_2029008964146434050.json, 图片生成/图生图/全能图片2高清出图(2K多图编辑版)_2029179596117118978.json, 图片生成/图生图/图片放大-rh-SeedVR2+TTP-模板_2013152289002885122.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_40

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/全能图片2高清出图(2K单图编辑版)_2029008964146434050.json、图片生成/图生图/全能图片2高清出图(2K多图编辑版)_2029179596117118978.json、图片生成/图生图/图片放大-rh-SeedVR2+TTP-模板_2013152289002885122.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：68%

## 共有节点

全部 3 个 workflow 都包含：
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `KOOK_ImageCompression`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Text` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `PainterNode` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `PrimitiveFloat` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
