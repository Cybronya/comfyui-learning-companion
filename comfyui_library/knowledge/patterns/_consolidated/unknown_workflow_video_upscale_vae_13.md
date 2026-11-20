---
name: unknown_workflow_video_upscale_vae_13
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.537
common_nodes: [GetNode, ImageFromBatch, ImageScaleBy, PreviewImage, SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler, SetNode, VHS_LoadVideo, VHS_VideoCombine, easy cleanGpuUsed]
problems: []
missing: []
members: [平台全量/22 SeedVR2 视频高清放大 (1)_2022190638447468546.json, 平台全量/SeedVR2图片视频放大_1999117657657966594.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_vae_13

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/22 SeedVR2 视频高清放大 (1)_2022190638447468546.json、平台全量/SeedVR2图片视频放大_1999117657657966594.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：54%

## 共有节点

全部 2 个 workflow 都包含：
- `GetNode`
- `ImageFromBatch`
- `ImageScaleBy`
- `PreviewImage`
- `SeedVR2LoadDiTModel`
- `SeedVR2LoadVAEModel`
- `SeedVR2VideoUpscaler`
- `SetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `Image Comparer (rgthree)` —— 1/2 个有
- `ImageConcanate` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `SaveImage` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
