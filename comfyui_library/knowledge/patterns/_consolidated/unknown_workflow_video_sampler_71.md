---
name: unknown_workflow_video_sampler_71
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.699
common_nodes: [Bookmark (rgthree), DiffuEraserLoader, DiffuEraserSampler, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo, easy compare, easy ifElse, easy showAnything]
problems: []
missing: []
members: [平台全量/全能视频S去水印10s+seedrv2二次高清视频-左上角左下角右边中间水印适合横屏16_9竖屏9_16的视频_1974665746296999938.json, 平台全量/全能视频S去水印10s-左上角左下角右边中间水印适合横屏16_9竖屏9_16的视频_1974518081919823874.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_71

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/全能视频S去水印10s+seedrv2二次高清视频-左上角左下角右边中间水印适合横屏16_9竖屏9_16的视频_1974665746296999938.json、平台全量/全能视频S去水印10s-左上角左下角右边中间水印适合横屏16_9竖屏9_16的视频_1974518081919823874.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：70%

## 共有节点

全部 2 个 workflow 都包含：
- `Bookmark (rgthree)`
- `DiffuEraserLoader`
- `DiffuEraserSampler`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`
- `easy compare`
- `easy ifElse`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `SeedVR2` —— 1/2 个有
- `easy cleanGpuUsed` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
