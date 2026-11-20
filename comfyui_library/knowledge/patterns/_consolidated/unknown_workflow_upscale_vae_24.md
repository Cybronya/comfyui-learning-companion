---
name: unknown_workflow_upscale_vae_24
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.911333
common_nodes: [GetImageSize+, ImageResize+, ImageScaleBy, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: []
members: [图片生成/图生图/放大_2107022066804420610.json, 图片生成/文生图/百万像素超绝放大_2005617652724891650.json, 平台全量/SEEDVR2+TTP极速一亿像素放大_1993982344061190146.json, 平台全量/SeedVR2 8K高清放大  Real HD 2k 真实高清修复 恢复高频细节_2059089673254957057.json, 平台全量/SeedVR2+TTP极速高清放大_1997218188532334593.json, 平台全量/SeedVR2+TTP极速高清放大_1997517070218760193.json, 平台全量/SeedVR2+TTP高清放大_2029807799768719362.json, 平台全量/SeedVR2-Image_2068707271437279233.json, 平台全量/亿级像素-超高清放大TTP+Seed VR2放大 -高清放大天花板_2044315232083906561.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_24

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/放大_2107022066804420610.json、图片生成/文生图/百万像素超绝放大_2005617652724891650.json、平台全量/SEEDVR2+TTP极速一亿像素放大_1993982344061190146.json、平台全量/SeedVR2 8K高清放大  Real HD 2k 真实高清修复 恢复高频细节_2059089673254957057.json、平台全量/SeedVR2+TTP极速高清放大_1997218188532334593.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：91%

## 共有节点

全部 9 个 workflow 都包含：
- `GetImageSize+`
- `ImageResize+`
- `ImageScaleBy`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 7/9 个有
- `PreviewImage` —— 2/9 个有
- `easy cleanGpuUsed` —— 2/9 个有
- `LayerUtility: PurgeVRAM V2` —— 1/9 个有
- `PrimitiveFloat` —— 1/9 个有
- `SaveImageJPG_GH` —— 1/9 个有
- `easy clearCacheAll` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
