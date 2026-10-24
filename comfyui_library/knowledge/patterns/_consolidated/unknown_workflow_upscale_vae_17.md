---
name: unknown_workflow_upscale_vae_17
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.762571
common_nodes: [GetImageSize+, Image Comparer (rgthree), ImageResize+, ImageScaleBy, LoadImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: []
members: [图片生成/图生图/8K极致高清放大（TTP+Seedvsr2）_2007683849572061185.json, 图片生成/图生图/AIGC人像系列04-人像超高清基于TTP+SeedVR2实现放大_2028739110755639297.json, 图片生成/图生图/B-LANSEDUONAOHE-SEEDVR2+TTP极速一亿像素放大_1992893002534244353.json, 图片生成/图生图/SeedVR2+TTP放大+0损耗压缩_2001611198548307969.json, 图片生成/图生图/九宫格电商详情高端产品分镜+放大(内置免费的全能图片通道)_2071905182362988545.json, 图片生成/图生图/动漫转真实，超低消耗_2071497174474645506.json, 图片生成/文生图/SeedVR2+TTP放大+0损耗压缩_2001561615235444738.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_17

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/8K极致高清放大（TTP+Seedvsr2）_2007683849572061185.json、图片生成/图生图/AIGC人像系列04-人像超高清基于TTP+SeedVR2实现放大_2028739110755639297.json、图片生成/图生图/B-LANSEDUONAOHE-SEEDVR2+TTP极速一亿像素放大_1992893002534244353.json、图片生成/图生图/SeedVR2+TTP放大+0损耗压缩_2001611198548307969.json、图片生成/图生图/九宫格电商详情高端产品分镜+放大(内置免费的全能图片通道)_2071905182362988545.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 7 个 workflow 都包含：
- `GetImageSize+`
- `Image Comparer (rgthree)`
- `ImageResize+`
- `ImageScaleBy`
- `LoadImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 6/7 个有
- `KOOK_ImageCompression` —— 5/7 个有
- `easy showAnything` —— 4/7 个有
- `Fast Groups Bypasser (rgthree)` —— 2/7 个有
- `PreviewImage` —— 2/7 个有
- `RHHiddenNodes` —— 2/7 个有
- `KOOK_SaveJPGImage` —— 1/7 个有
- `easy float` —— 1/7 个有
- `easy int` —— 1/7 个有
- `easy mathInt` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
