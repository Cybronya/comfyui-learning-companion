---
key: 平台全量/基于SAM2实现图片以及视频分割 _ SAM2 for pictures & viideos_1864499239568211970.json
name: 基于SAM2实现图片以及视频分割 _ SAM2 for pictures & viideos_1864499239568211970
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/基于SAM2实现图片以及视频分割 _ SAM2 for pictures & viideos_1864499239568211970.json
hash: a5087b3f9f042ee0
coverage: 0.6
learned_at: 2026-11-14 01:56:54
nodes: [Sam2Segmentation, InvertMask, JoinImageWithAlpha, MaskPreview+, Fast Groups Bypasser (rgthree), Florence2toCoordinates, DF_Image_scale_to_side, ShowText|pysssss, Note, Florence2Run, DownloadAndLoadSAM2Model, DF_Image_scale_to_side, VHS_VideoCombine, VHS_VideoCombine, InvertMask, Note, Note, Florence2toCoordinates, PreviewImage, SplineEditor, ShowText|pysssss, PreviewImage, ShowText|pysssss, ShowText|pysssss, Note, PreviewImage, DF_Get_image_size, GetImageRangeFromBatch, Note, MaskToImage, SplineEditor, easy positive, easy positive, DF_Get_image_size, ImpactSwitch, PreviewImage, Sam2Segmentation, JoinImageWithAlpha, MaskPreview+, ImpactSwitch, Note, Note, DownloadAndLoadFlorence2Model, Florence2Run, DownloadAndLoadSAM2Model, Note, DownloadAndLoadFlorence2Model, PreviewImage, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 平台全量/基于SAM2实现图片以及视频分割 _ SAM2 for pictures & viideos_1864499239568211970.json

> 来源文件 `comfyui_library/workflows/平台全量/基于SAM2实现图片以及视频分割 _ SAM2 for pictures & viideos_1864499239568211970.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（50 个）：
- `Sam2Segmentation`
- `InvertMask`
- `JoinImageWithAlpha`
- `MaskPreview+`
- `Fast Groups Bypasser (rgthree)`
- `Florence2toCoordinates`
- `DF_Image_scale_to_side`
- `ShowText|pysssss`
- `Note`
- `Florence2Run`
- `DownloadAndLoadSAM2Model`
- `DF_Image_scale_to_side`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `InvertMask`
- `Note`
- `Note`
- `Florence2toCoordinates`
- `PreviewImage`
- `SplineEditor`
- `ShowText|pysssss`
- `PreviewImage`
- `ShowText|pysssss`
- `ShowText|pysssss`
- `Note`
- `PreviewImage`
- `DF_Get_image_size`
- `GetImageRangeFromBatch`
- `Note`
- `MaskToImage`
- `SplineEditor`
- `easy positive`
- `easy positive`
- `DF_Get_image_size`
- `ImpactSwitch`
- `PreviewImage`
- `Sam2Segmentation`
- `JoinImageWithAlpha`
- `MaskPreview+`
- `ImpactSwitch`
- `Note`
- `Note`
- `DownloadAndLoadFlorence2Model`
- `Florence2Run`
- `DownloadAndLoadSAM2Model`
- `Note`
- `DownloadAndLoadFlorence2Model`
- `PreviewImage`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **60%**（30/50）

**有卡**：`Sam2Segmentation`、`InvertMask`、`JoinImageWithAlpha`、`MaskPreview+`、`Florence2toCoordinates`、`DF_Image_scale_to_side`、`Florence2Run`、`DownloadAndLoadSAM2Model`、`VHS_VideoCombine`、`SplineEditor`、`DF_Get_image_size`、`GetImageRangeFromBatch`、`MaskToImage`、`easy positive`、`DownloadAndLoadFlorence2Model`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、DF_Get_image_size、MaskPreview+、DF_Image_scale_to_side、DownloadAndLoadFlorence2Model、DownloadAndLoadSAM2Model、easy positive、Florence2Run
