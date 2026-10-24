---
name: unknown_workflow_upscale_vae_2
type: Unknown Workflow
frequency: 25
level: moderate
coverage: 0.81112
common_nodes: [ImageScale, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size, easy imageBatchToImageList, easy imageListToImageBatch, easy imageSizeBySide]
problems: []
missing: []
members: [图片生成/图生图/SeedVR 2.5 + TTP 图像高清放大 4K（适合清晰图片）_2092539832940711937.json, 图片生成/图生图/SeedVR2 图像修复4K-8K放大(tapcomfy api 专用）_2049404866543493121.json, 图片生成/图生图/SeedVR2.5 分块高清放大 支持4K _ 8K_1995741418297634818.json, 图片生成/图生图/SeedVR2.5 图像高清修复_2075389402867650562.json, 图片生成/图生图/SeedVR2.5+高清修复_2081656815695253506.json, 图片生成/图生图/SeedVR2.5_图像高清修复_2054022542574276609.json, 图片生成/图生图/Texture Restoration质感修复SeedVR2.5+图像高清修复High_2107279324872265729.json, 图片生成/图生图/seedvr2-8K放大图生图（自用） (1)_2056559739747782657.json, 图片生成/图生图/seedvr2-8K放大（仅自用）_2055136886196326402.json, 图片生成/图生图/seedvr2-8K放大（自用）_2054804867037843457.json, 图片生成/图生图/人像高清放大 质感修复 SeedVR2.5+图像高清修复_2089159747038703618.json, 图片生成/图生图/千问AI工作台_高清放大_2048640767916253186.json, "图片生成/图生图/图像修复_ 支持SeedVR2.5,FlashVSR1.1 _ 4K_8K放大_2021142605890854914.json", "图片生成/图生图/图像修复方法支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2002620453640388609.json", 图片生成/图生图/图像放大工作流（SeedVR2.5和FlashVSR1.1放大）_2043258669537697794.json, 图片生成/图生图/图像高清放大-支持4K_8K放大_2039691276001484801.json, 图片生成/图生图/图片增强 细节放大工作流_2025899775761059842.json, 图片生成/图生图/最强图像修复-支持4K_8K放大-效果好-速度快_2001551085695299585.json, "图片生成/图生图/最强图像修复合集 _ SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2064159860840812545.json", "图片生成/图生图/最强图像修复合集 _ 支持SeedVR2.5,FlashVSR1.1 _ 支持4K_8K放大_2021442288882294785.json", "图片生成/图生图/最强图像修复合集_支持SeedVR2.5,FlashVSR1.1_支持4K_8K放大_2098980518737039361.json", "图片生成/图生图/最强图像修复合集_支持SeedVR2.5,FlashVSR1.1_支持4K_8K放大_2099140418318454786.json", 图片生成/图生图/（高清非常好可选 模型）SeedVR2.5 图像高清修复_2101440534790365186.json, 视频生成/图生视频/seedvr2-8K放大图生图_2056193969314385922.json, "视频生成/文生视频/高清修复SeedVR2.5,FlashVSR1.1（4K_8K）_2002479902790152193.json"]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_2

> 由 `engine/knowledge_consolidation` 从 25 个 workflow 归纳得出（图片生成/图生图/SeedVR 2.5 + TTP 图像高清放大 4K（适合清晰图片）_2092539832940711937.json、图片生成/图生图/SeedVR2 图像修复4K-8K放大(tapcomfy api 专用）_2049404866543493121.json、图片生成/图生图/SeedVR2.5 分块高清放大 支持4K _ 8K_1995741418297634818.json、图片生成/图生图/SeedVR2.5 图像高清修复_2075389402867650562.json、图片生成/图生图/SeedVR2.5+高清修复_2081656815695253506.json…）

- **类型**：Unknown Workflow
- **样本数**：25
- **可信度**：中等可信
- **平均知识覆盖**：81%

## 共有节点

全部 25 个 workflow 都包含：
- `ImageScale`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`
- `easy imageBatchToImageList`
- `easy imageListToImageBatch`
- `easy imageSizeBySide`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 23/25 个有
- `Image Comparer (rgthree)` —— 23/25 个有
- `easy imageSize` —— 23/25 个有
- `PreviewImage` —— 18/25 个有
- `ImageScaleToTotalPixels` —— 16/25 个有
- `Fast Groups Bypasser (rgthree)` —— 15/25 个有
- `FlashVSRNode` —— 10/25 个有
- `EmptyImage` —— 2/25 个有
- `easy int` —— 2/25 个有
- `FlashVSRInitPipe` —— 1/25 个有
- `FlashVSRNodeAdv` —— 1/25 个有
- `Int` —— 1/25 个有
- `VRAM_Debug` —— 1/25 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
