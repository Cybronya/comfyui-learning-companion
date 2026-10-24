---
name: unknown_workflow_upscale_vae_12
type: Unknown Workflow
frequency: 10
level: moderate
coverage: 0.8829
common_nodes: [ImageCASharpening+, ImageResize+, ImpactMinMax, LoadImage, SaveImage, SimpleMath+, TTP_Image_Assy, TTP_Image_Tile_Batch, easy cleanGpuUsed]
problems: []
missing: []
members: [图片生成/图生图/8K万物高清放大_1985157095685312513.json, 图片生成/图生图/8K高清放大_1984930957239205889.json, 图片生成/图生图/8K高清放大_2101267173766426625.json, 图片生成/图生图/8K高清放大工作流_1996028811970068482.json, 图片生成/图生图/SEED VR2 放大修复_2060278631062134785.json, 图片生成/图生图/SeedVR2 4K 高清放大_2048969468503658497.json, 图片生成/图生图/SeedVR2 万物高清放大（分块）_1998997214439559169.json, 图片生成/图生图/SeedVR2 目前最好的修复放大模型_1962453047794339841.json, 图片生成/图生图/SeedVR2 目前最好的高清修复模型_1991161332349140994.json, 图片生成/图生图/Seedvr2.5 图像变清晰_2001823950957101058.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_12

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/8K万物高清放大_1985157095685312513.json、图片生成/图生图/8K高清放大_1984930957239205889.json、图片生成/图生图/8K高清放大_2101267173766426625.json、图片生成/图生图/8K高清放大工作流_1996028811970068482.json、图片生成/图生图/SEED VR2 放大修复_2060278631062134785.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 10 个 workflow 都包含：
- `ImageCASharpening+`
- `ImageResize+`
- `ImpactMinMax`
- `LoadImage`
- `SaveImage`
- `SimpleMath+`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 9/10 个有
- `Get Image Size` —— 9/10 个有
- `Image Comparer (rgthree)` —— 9/10 个有
- `SeedVR2` —— 9/10 个有
- `PreviewImage` —— 4/10 个有
- `SeedVR2LoadDiTModel` —— 3/10 个有
- `SeedVR2LoadVAEModel` —— 3/10 个有
- `SeedVR2VideoUpscaler` —— 3/10 个有
- `SeedVR2BlockSwap` —— 2/10 个有
- `easy imageSize` —— 2/10 个有
- `Fast Groups Muter (rgthree)` —— 1/10 个有
- `ImageAddNoise` —— 1/10 个有
- `ImageScaleBy` —— 1/10 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 1/10 个有
- `PlaySound|pysssss` —— 1/10 个有
- `easy boolean` —— 1/10 个有
- `easy ifElse` —— 1/10 个有
- `easy int` —— 1/10 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
