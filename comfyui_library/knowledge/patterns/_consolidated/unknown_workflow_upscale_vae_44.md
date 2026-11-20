---
name: unknown_workflow_upscale_vae_44
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.89175
common_nodes: [DF_Integer, Get Image Size, ImageCASharpening+, ImageResize+, ImpactMinMax, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/seedVR2 高清放大（TTP）_2014722740112072705.json, 图片生成/图生图/自用seedVR2.5_2003502446167113729.json, 图片生成/图生图/详情图到白底图+高清_2061726060374487042.json, 平台全量/seedVR2.5.24-万物高清放大修复不改变原细节(显存8G可用 可单图可批量)_2016866828680695809.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_44

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/seedVR2 高清放大（TTP）_2014722740112072705.json、图片生成/图生图/自用seedVR2.5_2003502446167113729.json、图片生成/图生图/详情图到白底图+高清_2061726060374487042.json、平台全量/seedVR2.5.24-万物高清放大修复不改变原细节(显存8G可用 可单图可批量)_2016866828680695809.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：89%

## 共有节点

全部 4 个 workflow 都包含：
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
- `Image Comparer (rgthree)` —— 3/4 个有
- `LoadImage` —— 3/4 个有
- `PreviewImage` —— 2/4 个有
- `CR Integer To String` —— 1/4 个有
- `GetNode` —— 1/4 个有
- `ImageScale` —— 1/4 个有
- `Load Image Batch` —— 1/4 个有
- `LoadAndResizeImage` —— 1/4 个有
- `RH_RhartImageG2ImageToImage` —— 1/4 个有
- `SetNode` —— 1/4 个有
- `TextPreview` —— 1/4 个有
- `easy imageRemBg` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
