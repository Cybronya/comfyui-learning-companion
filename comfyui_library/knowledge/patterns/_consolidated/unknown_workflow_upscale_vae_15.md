---
name: unknown_workflow_upscale_vae_15
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.825625
common_nodes: [Image Comparer (rgthree), ImageScale, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PrimitiveInt, SaveImage, SeedVR2BlockSwap, SeedVR2ExtraArgs, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSize, easy imageSizeBySide]
problems: []
missing: []
members: [图片生成/图生图/QT106-图像高清放大 超分放大_2046444473789452289.json, 图片生成/图生图/SeedVR2_四版本高清放大_2054841174053138433.json, 图片生成/图生图/SeedVR2——适用于高清的增加细节_2031549216664850433.json, 图片生成/图生图/SeedVR2图像_1990614296726048770.json, 图片生成/图生图/SeedVR2放大（一）——适用于不清晰的图像_2031541186091028482.json, 图片生成/图生图/⭐️ SeedVR2 四版本高清放大_1988399778717417474.json, 图片生成/图生图/⭐️_SeedVR2_四版本高清放大_2054759441928597506.json, 图片生成/图生图/⭐️_SeedVR2_四版本高清放大_2055158088608567298.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_15

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/QT106-图像高清放大 超分放大_2046444473789452289.json、图片生成/图生图/SeedVR2_四版本高清放大_2054841174053138433.json、图片生成/图生图/SeedVR2——适用于高清的增加细节_2031549216664850433.json、图片生成/图生图/SeedVR2图像_1990614296726048770.json、图片生成/图生图/SeedVR2放大（一）——适用于不清晰的图像_2031541186091028482.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 8 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PrimitiveInt`
- `SaveImage`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSize`
- `easy imageSizeBySide`

**可变部分**（部分 workflow 才有）：
- `SeedVR2GGUF` —— 7/8 个有
- `SeedVR2` —— 5/8 个有
- `Fast Groups Muter (rgthree)` —— 4/8 个有
- `GetImageSize+` —— 4/8 个有
- `ImageResize+` —— 4/8 个有
- `ImageScaleBy` —— 4/8 个有
- `SeedVR2LoadDiTModel` —— 4/8 个有
- `SeedVR2LoadVAEModel` —— 4/8 个有
- `SeedVR2VideoUpscaler` —— 4/8 个有
- `PreviewImage` —— 3/8 个有
- `PlaySound|pysssss` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
