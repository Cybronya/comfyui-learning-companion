---
name: unknown_workflow_upscale_vae_73
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.7145
common_nodes: [Image Comparer (rgthree), LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, SaveImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, easy int]
problems: []
missing: []
members: [图片生成/图生图/一键高清放大至指定分辨率_2030919114818064385.json, 平台全量/SeedRV2高清_2000462062679715842.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_vae_73

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/一键高清放大至指定分辨率_2030919114818064385.json、平台全量/SeedRV2高清_2000462062679715842.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：71%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `ImpactMinMax` —— 1/2 个有
- `LayerFilter: GaussianBlurV2` —— 1/2 个有
- `RHHiddenNodes` —— 1/2 个有
- `easy seed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
