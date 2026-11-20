---
name: unknown_workflow_upscale_vae_59
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.674333
common_nodes: [Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2 无损高清放大-高速版_2015724793345085441.json, 平台全量/SeedVR2高清放大方法_2039906549329563649.json, 平台全量/节点系列22-SeedVR2放大节点组_2040761074454110210.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_59

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/SeedVR2 无损高清放大-高速版_2015724793345085441.json、平台全量/SeedVR2高清放大方法_2039906549329563649.json、平台全量/节点系列22-SeedVR2放大节点组_2040761074454110210.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：67%

## 共有节点

全部 3 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 2/3 个有
- `Fast Groups Bypasser (rgthree)` —— 1/3 个有
- `ImpactInt` —— 1/3 个有
- `KepStringLiteral` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
