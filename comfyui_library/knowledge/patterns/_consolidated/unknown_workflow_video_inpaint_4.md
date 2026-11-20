---
name: unknown_workflow_video_inpaint_4
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.938
common_nodes: [GetImageRangeFromBatch, GrowMaskWithBlur, ImageGenResolutionFromImage, ImageToMask, Int, LayerUtility: CropByMask V2, LayerUtility: RestoreCropBox, LoadImage, MaskToImage, PreviewImage, ProPainterInpaint, RepeatImageBatch, VHS_LoadVideo, VHS_VideoCombine]
problems: []
missing: []
members: [平台全量/ProPainter+DiffuEraserSampler视频去水印_2004778096714805249.json, 平台全量/最强最快效果最好！ProPainter局部重绘极速视频去水印_1967948910406828033.json]
source: knowledge_consolidation
---

# unknown_workflow_video_inpaint_4

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/ProPainter+DiffuEraserSampler视频去水印_2004778096714805249.json、平台全量/最强最快效果最好！ProPainter局部重绘极速视频去水印_1967948910406828033.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `GetImageRangeFromBatch`
- `GrowMaskWithBlur`
- `ImageGenResolutionFromImage`
- `ImageToMask`
- `Int`
- `LayerUtility: CropByMask V2`
- `LayerUtility: RestoreCropBox`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `ProPainterInpaint`
- `RepeatImageBatch`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `DiffuEraserLoader` —— 1/2 个有
- `DiffuEraserSampler` —— 1/2 个有
- `VHS_VideoInfo` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
