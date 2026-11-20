---
name: unknown_workflow_upscale_vae_50
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7845
common_nodes: [GetImageSize+, GetNode, Image Comparer (rgthree), Image Tiled, ImageConcanate, ImageFromBatch, ImageListToBatch+, ImageUpscaleWithModel, Images to RGB, ImpactCompare, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, PrimitiveInt, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, UpscaleModelLoader, easy imageBatchToImageList]
problems: []
missing: []
members: [图片生成/图生图/无损放大 _ TTP拆分+SeedVR2 放大V3.0_2027255561305202689.json, 平台全量/图片放大工作流_2059813877088604162.json, 平台全量/无损放大 _ TTP拆分+SeedVR2 放大V1.0_2030629750456193025.json, 平台全量/无损放大 _ TTP拆分+SeedVR2 放大_2004185946495090690.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_50

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/无损放大 _ TTP拆分+SeedVR2 放大V3.0_2027255561305202689.json、平台全量/图片放大工作流_2059813877088604162.json、平台全量/无损放大 _ TTP拆分+SeedVR2 放大V1.0_2030629750456193025.json、平台全量/无损放大 _ TTP拆分+SeedVR2 放大_2004185946495090690.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 4 个 workflow 都包含：
- `GetImageSize+`
- `GetNode`
- `Image Comparer (rgthree)`
- `Image Tiled`
- `ImageConcanate`
- `ImageFromBatch`
- `ImageListToBatch+`
- `ImageUpscaleWithModel`
- `Images to RGB`
- `ImpactCompare`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `PrimitiveInt`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `UpscaleModelLoader`
- `easy imageBatchToImageList`

**可变部分**（部分 workflow 才有）：
- `If ANY execute A else B` —— 2/4 个有
- `ImageConcanateOfUtils` —— 2/4 个有
- `ShowText|pysssss` —— 2/4 个有
- `easy if` —— 2/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
