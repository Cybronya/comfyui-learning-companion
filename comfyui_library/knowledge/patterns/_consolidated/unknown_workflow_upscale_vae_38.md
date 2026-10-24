---
name: unknown_workflow_upscale_vae_38
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.951
common_nodes: [DF_Integer, Get Image Size, ImageCASharpening+, ImageResize+, ImpactMinMax, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/seedVR2 高清放大（TTP）_2014722740112072705.json, 图片生成/图生图/自用seedVR2.5_2003502446167113729.json, 图片生成/图生图/详情图到白底图+高清_2061726060374487042.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_38

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/seedVR2 高清放大（TTP）_2014722740112072705.json、图片生成/图生图/自用seedVR2.5_2003502446167113729.json、图片生成/图生图/详情图到白底图+高清_2061726060374487042.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 3 个 workflow 都包含：
- `DF_Integer`
- `Get Image Size`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 2/3 个有
- `LoadImage` —— 2/3 个有
- `ImageScale` —— 1/3 个有
- `LoadAndResizeImage` —— 1/3 个有
- `PreviewImage` —— 1/3 个有
- `RH_RhartImageG2ImageToImage` —— 1/3 个有
- `easy imageRemBg` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
