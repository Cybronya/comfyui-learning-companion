---
name: unknown_workflow_video_214
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9705
common_nodes: [ImageResizeKJv2, ImageToMask, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: LaMa, LoadImage, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/全能视频S去水印加强版（高清放大），全新版本，适用新水印_1967776162174894081.json, 平台全量/全能视频S去水印竖版视频_精准水印遮罩（仅适用全能视频s）v1.1_1985645040955531265.json]
source: knowledge_consolidation
---

# unknown_workflow_video_214

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/全能视频S去水印加强版（高清放大），全新版本，适用新水印_1967776162174894081.json、平台全量/全能视频S去水印竖版视频_精准水印遮罩（仅适用全能视频s）v1.1_1985645040955531265.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：97%

## 共有节点

全部 2 个 workflow 都包含：
- `ImageResizeKJv2`
- `ImageToMask`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: LaMa`
- `LoadImage`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `ImageUpscaleWithModel` —— 1/2 个有
- `JWInteger` —— 1/2 个有
- `LayerUtility: PurgeVRAM V2` —— 1/2 个有
- `UpscaleModelLoader` —— 1/2 个有
- `easy compare` —— 1/2 个有
- `easy ifElse` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
