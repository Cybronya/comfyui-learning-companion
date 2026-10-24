---
name: unknown_workflow_upscale_vae_24
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.8834
common_nodes: [ImageScaleBy, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2_高清放大可批量_2097170882073546754.json, 图片生成/图生图/SeedVR2_高清放大可批量_2097509265190768641.json, 图片生成/图生图/单图放大_seedVR2_4K_2005946235443970049.json, 图片生成/图生图/最好的高清放大_2011245583637422082.json, 图片生成/图生图/电商高清放大・精修处理-SeedVR2 Video Upscaler_2015100982383878146.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_24

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/SeedVR2_高清放大可批量_2097170882073546754.json、图片生成/图生图/SeedVR2_高清放大可批量_2097509265190768641.json、图片生成/图生图/单图放大_seedVR2_4K_2005946235443970049.json、图片生成/图生图/最好的高清放大_2011245583637422082.json、图片生成/图生图/电商高清放大・精修处理-SeedVR2 Video Upscaler_2015100982383878146.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：88%

## 共有节点

全部 5 个 workflow 都包含：
- `ImageScaleBy`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `Image Comparer (rgthree)` —— 3/5 个有
- `Fast Groups Bypasser (rgthree)` —— 2/5 个有
- `HAIGC_SaveImagesToZip` —— 2/5 个有
- `RHUploadZip_V2` —— 2/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
