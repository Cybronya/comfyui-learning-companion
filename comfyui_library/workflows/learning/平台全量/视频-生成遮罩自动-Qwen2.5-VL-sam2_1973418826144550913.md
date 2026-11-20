---
key: 平台全量/视频-生成遮罩自动-Qwen2.5-VL-sam2_1973418826144550913.json
name: 视频-生成遮罩自动-Qwen2.5-VL-sam2_1973418826144550913
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-生成遮罩自动-Qwen2.5-VL-sam2_1973418826144550913.json
hash: cd93364ddd770f5e
coverage: 0.875
learned_at: 2026-11-14 02:34:25
nodes: [ImageFromBatch, BBoxesToSAM2, VHS_VideoInfoLoaded, VHS_VideoCombine, easy showAnything, easy showAnything, GetImageSizeAndCount, ImageConcanate, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, MaskToImage, LayerMask: SAM2VideoUltra, easy positive, QwenVLDetection, DownloadAndLoadQwenModel]
patterns: []
missing: []
---

# 平台全量/视频-生成遮罩自动-Qwen2.5-VL-sam2_1973418826144550913.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-生成遮罩自动-Qwen2.5-VL-sam2_1973418826144550913.json`

## 结构

**生成流程**：Process → Other

**节点**（16 个）：
- `ImageFromBatch`
- `BBoxesToSAM2`
- `VHS_VideoInfoLoaded`
- `VHS_VideoCombine`
- `easy showAnything`
- `easy showAnything`
- `GetImageSizeAndCount`
- `ImageConcanate`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_VideoCombine`
- `MaskToImage`
- `LayerMask: SAM2VideoUltra`
- `easy positive`
- `QwenVLDetection`
- `DownloadAndLoadQwenModel`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`ImageFromBatch`、`BBoxesToSAM2`、`VHS_VideoInfoLoaded`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`ImageConcanate`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`MaskToImage`、`LayerMask: SAM2VideoUltra`、`easy positive`、`QwenVLDetection`、`DownloadAndLoadQwenModel`

**用到的条目**：GetImageSizeAndCount、BBoxesToSAM2、DownloadAndLoadQwenModel、easy positive、ImageConcanate、ImageFromBatch、LayerMask: SAM2VideoUltra、LayerUtility: ImageScaleByAspectRatio V2
