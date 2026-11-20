---
key: 平台全量/视频-生成遮罩自动-Qwen2.5-VL-SeC_1979579953714991106.json
name: 视频-生成遮罩自动-Qwen2.5-VL-SeC_1979579953714991106
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-生成遮罩自动-Qwen2.5-VL-SeC_1979579953714991106.json
hash: bc2af13d3bfb3c2f
coverage: 0.875
learned_at: 2026-11-14 02:34:25
nodes: [ImageFromBatch, VHS_VideoInfoLoaded, VHS_VideoCombine, easy showAnything, easy showAnything, GetImageSizeAndCount, ImageConcanate, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, VHS_VideoCombine, MaskToImage, SeCModelLoader, DownloadAndLoadQwenModel, SeCVideoSegmentation, easy positive, QwenVLDetection]
patterns: []
missing: []
---

# 平台全量/视频-生成遮罩自动-Qwen2.5-VL-SeC_1979579953714991106.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-生成遮罩自动-Qwen2.5-VL-SeC_1979579953714991106.json`

## 结构

**生成流程**：Model → Process → Other

**节点**（16 个）：
- `ImageFromBatch`
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
- `SeCModelLoader`
- `DownloadAndLoadQwenModel`
- `SeCVideoSegmentation`
- `easy positive`
- `QwenVLDetection`

## 知识

覆盖率 **88%**（14/16）

**有卡**：`ImageFromBatch`、`VHS_VideoInfoLoaded`、`VHS_VideoCombine`、`GetImageSizeAndCount`、`ImageConcanate`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`MaskToImage`、`SeCModelLoader`、`DownloadAndLoadQwenModel`、`SeCVideoSegmentation`、`easy positive`、`QwenVLDetection`

**用到的条目**：GetImageSizeAndCount、DownloadAndLoadQwenModel、easy positive、ImageConcanate、ImageFromBatch、LayerUtility: ImageScaleByAspectRatio V2、MaskToImage、QwenVLDetection
