---
name: unknown_workflow_upscale_vae_67
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.901333
common_nodes: [Get Image Size, ImageCASharpening+, ImageResize+, ImpactMinMax, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch]
problems: []
missing: []
members: [平台全量/放大_2041717959957155842.json, 平台全量/最新放大（简单图案）_2057028792689979394.json, 平台全量/高清放大SeedVR2 Video Upscaler 人像物品通用_2043516238512529410.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_67

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/放大_2041717959957155842.json、平台全量/最新放大（简单图案）_2057028792689979394.json、平台全量/高清放大SeedVR2 Video Upscaler 人像物品通用_2043516238512529410.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：90%

## 共有节点

全部 3 个 workflow 都包含：
- `Get Image Size`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`

**可变部分**（部分 workflow 才有）：
- `Image Save` —— 2/3 个有
- `PrimitiveInt` —— 2/3 个有
- `easy cleanGpuUsed` —— 2/3 个有
- `DF_Integer` —— 1/3 个有
- `Image Comparer (rgthree)` —— 1/3 个有
- `ImageScaleBy` —— 1/3 个有
- `SeedVR2` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
