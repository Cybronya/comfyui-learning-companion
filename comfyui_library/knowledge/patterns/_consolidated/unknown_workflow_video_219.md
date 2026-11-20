---
name: unknown_workflow_video_219
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.606
common_nodes: [DF_Get_image_size, DF_Image_scale_to_side, DownloadAndLoadFlorence2Model, DownloadAndLoadSAM2Model, Fast Groups Bypasser (rgthree), Florence2Run, Florence2toCoordinates, GetImageRangeFromBatch, ImpactSwitch, InvertMask, JoinImageWithAlpha, LoadImage, MaskPreview+, MaskToImage, PreviewImage, Sam2Segmentation, ShowText|pysssss, SplineEditor, VHS_LoadVideo, VHS_VideoCombine, easy positive]
problems: []
missing: []
members: [平台全量/基于SAM2实现图片以及视频分割 _ SAM2 for pictures & viideos_1864499239568211970.json, 平台全量/星途AI-点选主体高质量抠图_2078085837954306049.json]
source: knowledge_consolidation
---

# unknown_workflow_video_219

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（平台全量/基于SAM2实现图片以及视频分割 _ SAM2 for pictures & viideos_1864499239568211970.json、平台全量/星途AI-点选主体高质量抠图_2078085837954306049.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：61%

## 共有节点

全部 2 个 workflow 都包含：
- `DF_Get_image_size`
- `DF_Image_scale_to_side`
- `DownloadAndLoadFlorence2Model`
- `DownloadAndLoadSAM2Model`
- `Fast Groups Bypasser (rgthree)`
- `Florence2Run`
- `Florence2toCoordinates`
- `GetImageRangeFromBatch`
- `ImpactSwitch`
- `InvertMask`
- `JoinImageWithAlpha`
- `LoadImage`
- `MaskPreview+`
- `MaskToImage`
- `PreviewImage`
- `Sam2Segmentation`
- `ShowText|pysssss`
- `SplineEditor`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `easy positive`

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
