---
name: unknown_workflow_upscale_vae_23
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.733286
common_nodes: [GetImageSize+, ImageResize+, ImageScaleBy, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: []
members: [图片生成/图生图/全能图片2高清出图(2K单图编辑版)_2029008964146434050.json, 图片生成/图生图/全能图片2高清出图(2K多图编辑版)_2029179596117118978.json, 图片生成/图生图/图像8K放大-不变形_2004662548261728258.json, 图片生成/图生图/图片高清放大_SeedVR2放大_2077948514235142145.json, 图片生成/图生图/无损8k放大_2095771047361605633.json, 图片生成/图生图/无损8k放大_2096064513807306754.json, 图片生成/图生图/星绘-超清SeedVR2+无损耗压缩_2015623404509990914.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_23

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/全能图片2高清出图(2K单图编辑版)_2029008964146434050.json、图片生成/图生图/全能图片2高清出图(2K多图编辑版)_2029179596117118978.json、图片生成/图生图/图像8K放大-不变形_2004662548261728258.json、图片生成/图生图/图片高清放大_SeedVR2放大_2077948514235142145.json、图片生成/图生图/无损8k放大_2095771047361605633.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 7 个 workflow 都包含：
- `GetImageSize+`
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
- `KOOK_ImageCompression` —— 6/7 个有
- `LoadImage` —— 6/7 个有
- `easy showAnything` —— 6/7 个有
- `Image Comparer (rgthree)` —— 5/7 个有
- `PreviewImage` —— 3/7 个有
- `CR Text` —— 2/7 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/7 个有
- `PainterNode` —— 2/7 个有
- `RH_Nano_Banana2_Gemini31Flash` —— 2/7 个有
- `easy cleanGpuUsed` —— 2/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
