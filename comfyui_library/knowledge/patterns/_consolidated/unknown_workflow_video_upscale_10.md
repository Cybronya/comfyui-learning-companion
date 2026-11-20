---
name: unknown_workflow_video_upscale_10
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.7704
common_nodes: [Image Comparer (rgthree), ImageScaleBy, ImageUpscaleWithModel, LoadImage, PreviewImage, SaveImage, SeedVR2, SeedVR2BlockSwap, UpscaleModelLoader, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [图片生成/图生图/SeedVR2-V2-图片视频修复_1991874494327484418.json, 图片生成/图生图/图片超清放大SeedVR2_1971421765958320129.json, 平台全量/Work-Fisher_SeedVR2-V2_1975855499423952897.json, 平台全量/Work-Fisher_SeedVR2-V2（高清放大修复）_1979913143507914753.json, 平台全量/yj真人超分_2004443068759769090.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_10

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/SeedVR2-V2-图片视频修复_1991874494327484418.json、图片生成/图生图/图片超清放大SeedVR2_1971421765958320129.json、平台全量/Work-Fisher_SeedVR2-V2_1975855499423952897.json、平台全量/Work-Fisher_SeedVR2-V2（高清放大修复）_1979913143507914753.json、平台全量/yj真人超分_2004443068759769090.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 5 个 workflow 都包含：
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
- `Fast Groups Bypasser (rgthree)` —— 4/5 个有
- `ImageScaleToTotalPixels` —— 4/5 个有
- `PlaySound|pysssss` —— 4/5 个有
- `SeedVR2ExtraArgs` —— 4/5 个有
- `GetImageRangeFromBatch` —— 1/5 个有
- `Int` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
