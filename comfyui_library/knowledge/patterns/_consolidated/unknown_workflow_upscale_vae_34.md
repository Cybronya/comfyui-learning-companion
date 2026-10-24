---
name: unknown_workflow_upscale_vae_34
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7015
common_nodes: [Image Comparer (rgthree), ImageScaleToTotalPixels, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/sim_Z-Seed 人像修复放大_2093662606916673537.json, 图片生成/图生图/▶SeedVR2无损高清放大-新_2011468531019292673.json, 图片生成/图生图/▶SeedVR2无损高清放大-新_二次放大_2048366313147469826.json, 图片生成/图生图/▶SeedVR2无损高清放大-新（高清换为超清）_2019944447726854146.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_34

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/sim_Z-Seed 人像修复放大_2093662606916673537.json、图片生成/图生图/▶SeedVR2无损高清放大-新_2011468531019292673.json、图片生成/图生图/▶SeedVR2无损高清放大-新_二次放大_2048366313147469826.json、图片生成/图生图/▶SeedVR2无损高清放大-新（高清换为超清）_2019944447726854146.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageScaleToTotalPixels`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 3/4 个有
- `PreviewImage` —— 3/4 个有
- `CompressImages` —— 1/4 个有
- `DuckHideNode` —— 1/4 个有
- `HAIGC_LoadImagesFromZip` —— 1/4 个有
- `HAIGC_SaveImagesToZip` —— 1/4 个有
- `ImageSharpenKJ` —— 1/4 个有
- `PurgeVRAM_UTK` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
