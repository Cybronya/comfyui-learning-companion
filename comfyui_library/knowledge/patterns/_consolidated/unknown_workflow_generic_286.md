---
name: unknown_workflow_generic_286
type: Unknown Workflow
frequency: 8
level: moderate
coverage: 0.800375
common_nodes: [DF_Integer, Get Image Size, ImageCASharpening+, ImageResize+, ImpactMinMax, LoadImage, SaveImage, SeedVR2, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/多分镜&二次放大-Rubby_2007714930438443010.json, 图片生成/图生图/多分镜&二次放大-rubby_2008814429311340545.json, 图片生成/图生图/无损放大-最长边两万像素_2046129740641214466.json, 图片生成/图生图/最好用的8k放大工作流-放大的图片一点都不油腻和畸变（懂得自然懂)_1989240428505468930.json, 图片生成/图生图/最新3.0万物高清放大_2065014492030914562.json, 图片生成/图生图/高效精准高清放大2_2070751671319355393.json, 图片生成/图生图/高清修复万物高清放大修复不改变原细节（分块）seedVR2_1985569698718928898.json, 图片生成/图生图/高清放大修复不改变原细节_2039941695437021186.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_286

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（图片生成/图生图/多分镜&二次放大-Rubby_2007714930438443010.json、图片生成/图生图/多分镜&二次放大-rubby_2008814429311340545.json、图片生成/图生图/无损放大-最长边两万像素_2046129740641214466.json、图片生成/图生图/最好用的8k放大工作流-放大的图片一点都不油腻和畸变（懂得自然懂)_1989240428505468930.json、图片生成/图生图/最新3.0万物高清放大_2065014492030914562.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：中等可信
- **平均知识覆盖**：80%

## 共有节点

全部 8 个 workflow 都包含：
- `DF_Integer`
- `Get Image Size`
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `LoadImage`
- `SaveImage`
- `SeedVR2`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 6/8 个有
- `PreviewImage` —— 5/8 个有
- `SetNode` —— 5/8 个有
- `GetNode` —— 4/8 个有
- `Fast Groups Bypasser (rgthree)` —— 2/8 个有
- `RH_Nano_Banana2_Image2Image` —— 2/8 个有
- `Bilateral_Filter` —— 1/8 个有
- `ImageConcatMulti` —— 1/8 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
