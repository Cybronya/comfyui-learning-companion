---
name: unknown_workflow_upscale_vae_76
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.913
common_nodes: [CM_NumberToInt, CR Simple Image Compare, Image Comparer (rgthree), ImageScale, JjkText, KOOK_ImageCompression, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM V2, LoadImage, SaveImage, SeargeIntegerConstant, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, Text to Number, easy imageSize, easy imageSizeBySide, easy mathInt]
problems: []
missing: []
members: [图片生成/图生图/放大丨图像高清放大修复2-8K_2005623812819480577.json, 平台全量/SeedVR2图像高清放大修复2-8K_2041171256426369025.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_76

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/放大丨图像高清放大修复2-8K_2005623812819480577.json、平台全量/SeedVR2图像高清放大修复2-8K_2041171256426369025.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CM_NumberToInt`
- `CR Simple Image Compare`
- `Image Comparer (rgthree)`
- `ImageScale`
- `JjkText`
- `KOOK_ImageCompression`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `SaveImage`
- `SeargeIntegerConstant`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `Text to Number`
- `easy imageSize`
- `easy imageSizeBySide`
- `easy mathInt`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
