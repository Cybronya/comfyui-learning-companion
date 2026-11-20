---
name: unknown_workflow_upscale_vae_35
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.704
common_nodes: [Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, TTP_Image_Assy, TTP_Image_Tile_Batch, TTP_Tile_image_size]
problems: []
missing: []
members: [图片生成/图生图/TTP+SEEDVR2超清无损放大-8K_2016403959757414401.json, 图片生成/图生图/TTP分块+SeedVR2放大工作流_2026145278633451521.json, 图片生成/图生图/TTP分块+SeedVR2放大工作流_2036412002213568513.json, 图片生成/图生图/🎯天下无腰TTP+SEEDVR2超清无损放大_2021978500932046850.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_35

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/TTP+SEEDVR2超清无损放大-8K_2016403959757414401.json、图片生成/图生图/TTP分块+SeedVR2放大工作流_2026145278633451521.json、图片生成/图生图/TTP分块+SeedVR2放大工作流_2036412002213568513.json、图片生成/图生图/🎯天下无腰TTP+SEEDVR2超清无损放大_2021978500932046850.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：70%

## 共有节点

全部 4 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `TTP_Image_Assy`
- `TTP_Image_Tile_Batch`
- `TTP_Tile_image_size`

**可变部分**（部分 workflow 才有）：
- `IfInnerExecute` —— 2/4 个有
- `ImpactMinMax` —— 2/4 个有
- `SimpleComparison+` —— 2/4 个有
- `easy imageScaleDownBy` —— 2/4 个有
- `easy showAnything` —— 2/4 个有
- `Fast Groups Muter (rgthree)` —— 1/4 个有
- `Int` —— 1/4 个有
- `easy int` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
