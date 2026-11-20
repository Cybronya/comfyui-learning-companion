---
key: 平台全量/Qwen2.5 VL 视频元素提取_分割_1949467057036918786.json
name: Qwen2.5 VL 视频元素提取_分割_1949467057036918786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Qwen2.5 VL 视频元素提取_分割_1949467057036918786.json
hash: d29f1e33c930b415
coverage: 0.842105
learned_at: 2026-11-14 00:52:23
nodes: [QwenVLDetection, DownloadAndLoadQwenModel, LoadImage, LayerMask: SAM2UltraV2, BBoxesToSAM2, ImageBatchToList+, VHS_VideoCombine, VHS_VideoInfoSource, JjkText, LayerMask: MaskPreview, PreviewImage, VHS_LoadVideo, VHS_VideoCombine, ImageConcanate, LayerMask: LoadSAM2Model, ImageListToBatch+, VHS_VideoCombine, PreviewImage, SaveImage]
patterns: []
missing: []
---

# 平台全量/Qwen2.5 VL 视频元素提取_分割_1949467057036918786.json

> 来源文件 `comfyui_library/workflows/平台全量/Qwen2.5 VL 视频元素提取_分割_1949467057036918786.json`

## 结构

**生成流程**：Process → Output → Other

**节点**（19 个）：
- `QwenVLDetection`
- `DownloadAndLoadQwenModel`
- `LoadImage`
- `LayerMask: SAM2UltraV2`
- `BBoxesToSAM2`
- `ImageBatchToList+`
- `VHS_VideoCombine`
- `VHS_VideoInfoSource`
- `JjkText`
- `LayerMask: MaskPreview`
- `PreviewImage`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `ImageConcanate`
- `LayerMask: LoadSAM2Model`
- `ImageListToBatch+`
- `VHS_VideoCombine`
- `PreviewImage`
- `SaveImage`

## 知识

覆盖率 **84%**（16/19）

**有卡**：`QwenVLDetection`、`DownloadAndLoadQwenModel`、`LoadImage`、`LayerMask: SAM2UltraV2`、`BBoxesToSAM2`、`ImageBatchToList+`、`VHS_VideoCombine`、`VHS_VideoInfoSource`、`LayerMask: MaskPreview`、`VHS_LoadVideo`、`ImageConcanate`、`LayerMask: LoadSAM2Model`、`ImageListToBatch+`、`SaveImage`

**用到的条目**：LoadImage、LayerMask: MaskPreview、SaveImage、BBoxesToSAM2、DownloadAndLoadQwenModel、ImageBatchToList+、ImageConcanate、ImageListToBatch+
