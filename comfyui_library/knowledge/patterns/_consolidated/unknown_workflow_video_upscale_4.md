---
name: unknown_workflow_video_upscale_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.726
common_nodes: [Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, LoadImage, PreviewImage, SaveImage, SeedVR2, SeedVR2BlockSwap, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2-V2-图片视频修复_1991874494327484418.json, 图片生成/图生图/图片超清放大SeedVR2_1971421765958320129.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/图生图/SeedVR2-V2-图片视频修复_1991874494327484418.json、图片生成/图生图/图片超清放大SeedVR2_1971421765958320129.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：73%

## 共有节点

全部 2 个 workflow 都包含：
- `Image Comparer (rgthree)`
- `ImageScaleBy`
- `ImageUpscaleWithModel`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `SeedVR2`
- `SeedVR2BlockSwap`
- `UpscaleModelLoader`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 1/2 个有
- `GetImageRangeFromBatch` —— 1/2 个有
- `ImageScaleToTotalPixels` —— 1/2 个有
- `Int` —— 1/2 个有
- `PlaySound|pysssss` —— 1/2 个有
- `SeedVR2ExtraArgs` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
