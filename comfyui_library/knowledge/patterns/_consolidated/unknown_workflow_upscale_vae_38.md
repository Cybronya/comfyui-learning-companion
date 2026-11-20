---
name: unknown_workflow_upscale_vae_38
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7936
common_nodes: [GetImageSize, Image Comparer (rgthree), ImageScaleBy, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: []
members: [图片生成/图生图/TTP-SEEDVR2分块8倍放大_2063088756915265538.json, 图片生成/图生图/TTP-SEEDVR2分块8倍放大_2064161314121019393.json, 图片生成/图生图/seedvr2图像放大_2045732584243601409.json, 平台全量/TTP-SEEDVR2分块4倍放大_2061375490602135553.json, 平台全量/TTP-SEEDVR2分块8倍放大_2062913146871963649.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_38

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/TTP-SEEDVR2分块8倍放大_2063088756915265538.json、图片生成/图生图/TTP-SEEDVR2分块8倍放大_2064161314121019393.json、图片生成/图生图/seedvr2图像放大_2045732584243601409.json、平台全量/TTP-SEEDVR2分块4倍放大_2061375490602135553.json、平台全量/TTP-SEEDVR2分块8倍放大_2062913146871963649.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：79%

## 共有节点

全部 5 个 workflow 都包含：
- `GetImageSize`
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`

**可变部分**（部分 workflow 才有）：
- `easy compare` —— 4/5 个有
- `easy ifElse` —— 4/5 个有
- `KOOK_ImageCompression` —— 3/5 个有
- `Any Switch (rgthree)` —— 1/5 个有
- `Fast Groups Bypasser (rgthree)` —— 1/5 个有
- `ImageResize+` —— 1/5 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
