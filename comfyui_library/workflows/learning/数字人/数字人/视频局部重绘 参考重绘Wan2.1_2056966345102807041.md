---
key: 数字人/数字人/视频局部重绘 参考重绘Wan2.1_2056966345102807041.json
name: 视频局部重绘 参考重绘Wan2.1_2056966345102807041
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/视频局部重绘 参考重绘Wan2.1_2056966345102807041.json
hash: 0011b5c568d41e5f
coverage: 0.622642
learned_at: 2026-10-26 02:05:13
nodes: [GetNode, GetImageSizeAndCount, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVAELoader, WanVideoTextEncode, Text, DownloadAndLoadSAM2Model, Sam2Segmentation, VHS_VideoCombine, LoadImage, SetNode, PreviewAny, PreviewAny, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, GrowMask, WanVideoDecode, INPAINT_MaskedFill, LoadWanVideoT5TextEncoder, GetNode, VHS_VideoCombine, SetNode, SetNode, GetImageRangeFromBatch, PreviewImage, GetNode, GetNode, GetNode, SetNode, VHS_VideoCombine, DrawMaskOnImage, BlockifyMask, easy cleanGpuUsed, SetNode, GetNode, GetNode, SetNode, WanVideoBlockSwap, WanVideoModelLoader, VHS_VideoInfo, Int, PointsEditor, Float, LayerMask: BiRefNetUltra, InvertMask, INPAINT_MaskedFill, PreviewImage, WanVideoSampler, WanVideoLoraSelectMulti, PreviewAny, PreviewAny, Note]
patterns: []
missing: []
---

# 数字人/数字人/视频局部重绘 参考重绘Wan2.1_2056966345102807041.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/视频局部重绘 参考重绘Wan2.1_2056966345102807041.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（53 个）：
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `Text`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `VHS_VideoCombine`
- `LoadImage`
- `SetNode`
- `PreviewAny`
- `PreviewAny`
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GrowMask`
- `WanVideoDecode`
- `INPAINT_MaskedFill`
- `LoadWanVideoT5TextEncoder`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `GetImageRangeFromBatch`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `BlockifyMask`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `VHS_VideoInfo`
- `Int`
- `PointsEditor`
- `Float`
- `LayerMask: BiRefNetUltra`
- `InvertMask`
- `INPAINT_MaskedFill`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelectMulti`
- `PreviewAny`
- `PreviewAny`
- `Note`

## 知识

覆盖率 **62%**（33/53）

**有卡**：`GetImageSizeAndCount`、`WanVideoVACEEncode`、`WanVideoVACEModelSelect`、`WanVideoVAELoader`、`WanVideoTextEncode`、`Text`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`VHS_VideoCombine`、`LoadImage`、`VHS_LoadVideo`、`LayerUtility: ImageScaleByAspectRatio V2`、`GrowMask`、`WanVideoDecode`、`INPAINT_MaskedFill`、`LoadWanVideoT5TextEncoder`、`GetImageRangeFromBatch`、`DrawMaskOnImage`、`BlockifyMask`、`easy cleanGpuUsed`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`VHS_VideoInfo`、`Int`、`PointsEditor`、`Float`、`LayerMask: BiRefNetUltra`、`InvertMask`、`WanVideoSampler`、`WanVideoLoraSelectMulti`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoLoraSelectMulti
