---
key: 平台全量/Wan2.1视频局部重绘-物品迁移_1980574528835338242.json
name: Wan2.1视频局部重绘-物品迁移_1980574528835338242
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1视频局部重绘-物品迁移_1980574528835338242.json
hash: 78f5f0d330526c8b
coverage: 0.644068
learned_at: 2026-11-14 01:04:46
nodes: [GetNode, WanVideoDecode, GetNode, GetImageRangeFromBatch, GetNode, INPAINT_MaskedFill, WanVideoVACEEncode, GetImageSizeAndCount, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoVACEModelSelect, WanVideoBlockSwap, SetNode, SetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, SetNode, WanVideoModelLoader, GrowMask, BlockifyMask, DrawMaskOnImage, SetNode, SetNode, GetNode, PreviewImage, InvertMask, GetNode, GetImageSizeAndCount, easy cleanGpuUsed, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoCombine, AddLabel, GetNode, PreviewImage, PreviewImage, ImageConcatMulti, BiRefNetRMBG, MaskToImage, PreviewImage, PreviewImage, LayerMask: BiRefNetUltra, WanVideoSampler, LoadImage, WanVideoTextEncode, GetNode, GetNode, ImageResizeKJ, SetNode, SetNode, Note, DownloadAndLoadSAM2Model, EmptyImage, SeCVideoSegmentation, INPAINT_MaskedFill, SeCModelLoader, Sam2Segmentation, PointsEditor, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/Wan2.1视频局部重绘-物品迁移_1980574528835338242.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1视频局部重绘-物品迁移_1980574528835338242.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（59 个）：
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `INPAINT_MaskedFill`
- `WanVideoVACEEncode`
- `GetImageSizeAndCount`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEModelSelect`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `WanVideoModelLoader`
- `GrowMask`
- `BlockifyMask`
- `DrawMaskOnImage`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `InvertMask`
- `GetNode`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `AddLabel`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `ImageConcatMulti`
- `BiRefNetRMBG`
- `MaskToImage`
- `PreviewImage`
- `PreviewImage`
- `LayerMask: BiRefNetUltra`
- `WanVideoSampler` ★核心
- `LoadImage`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `ImageResizeKJ`
- `SetNode`
- `SetNode`
- `Note`
- `DownloadAndLoadSAM2Model`
- `EmptyImage`
- `SeCVideoSegmentation`
- `INPAINT_MaskedFill`
- `SeCModelLoader`
- `Sam2Segmentation`
- `PointsEditor`
- `VHS_LoadVideo`

## 知识

覆盖率 **64%**（38/59）

**有卡**：`WanVideoDecode`、`GetImageRangeFromBatch`、`INPAINT_MaskedFill`、`WanVideoVACEEncode`、`GetImageSizeAndCount`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoVACEModelSelect`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`GrowMask`、`BlockifyMask`、`DrawMaskOnImage`、`InvertMask`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`AddLabel`、`ImageConcatMulti`、`BiRefNetRMBG`、`MaskToImage`、`LayerMask: BiRefNetUltra`、`WanVideoSampler`、`LoadImage`、`WanVideoTextEncode`、`ImageResizeKJ`、`DownloadAndLoadSAM2Model`、`EmptyImage`、`SeCVideoSegmentation`、`SeCModelLoader`、`Sam2Segmentation`、`PointsEditor`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVACEEncode、WanVideoVAELoader、WanVideoLoraSelect
