---
name: unknown_workflow_upscale_vae_60
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.729333
common_nodes: [Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleComparison+, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageBatchToImageList, easy imageListToImageBatch]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2-图片高清放大工作流（针对不同分辨率的图片）_2048781148674854914.json, 平台全量/SeedVR2+TTP无损高清放大通用版【阿夕AI】_2045886341048705025.json, 平台全量/【ComfyUI】SEEDVR2高清放大-模糊图片拯救计划_2017928413452967937.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_60

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SeedVR2-图片高清放大工作流（针对不同分辨率的图片）_2048781148674854914.json、平台全量/SeedVR2+TTP无损高清放大通用版【阿夕AI】_2045886341048705025.json、平台全量/【ComfyUI】SEEDVR2高清放大-模糊图片拯救计划_2017928413452967937.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：73%

## 共有节点

全部 3 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleComparison+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `ImageScaleToTotalPixels` —— 2/3 个有
- `LayerUtility: If ` —— 2/3 个有
- `GoohaiUniversalSlider` —— 1/3 个有
- `INTConstant` —— 1/3 个有
- `IfInnerExecute` —— 1/3 个有
- `孤海注释` —— 1/3 个有
- `忽略多组孤海` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
