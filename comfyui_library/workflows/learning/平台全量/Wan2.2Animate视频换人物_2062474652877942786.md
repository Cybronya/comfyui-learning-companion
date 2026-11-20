---
key: 平台全量/Wan2.2Animate视频换人物_2062474652877942786.json
name: Wan2.2Animate视频换人物_2062474652877942786
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2Animate视频换人物_2062474652877942786.json
hash: 43abfdaa65dd5de4
coverage: 0.511111
learned_at: 2026-11-14 01:06:12
nodes: [WanVideoTorchCompileSettings, SetNode, SetNode, SetNode, SetNode, WanVideoVAELoader, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, CLIPVisionLoader, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, easy cleanGpuUsed, easy cleanGpuUsed, VHS_VideoInfoLoaded, WanVideoDecode, WanVideoSampler, easy showAnything, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoAnimateEmbeds, GetNode, VHS_VideoCombine, GetNode, SetNode, SetNode, VHS_VideoCombine, OnnxDetectionModelLoader, GetImageSizeAndCount, GetNode, PoseAndFaceDetection, Reroute, GetNode, GetNode, GetNode, BlockifyMask, SetNode, DrawMaskOnImage, GetNode, VHS_VideoCombine, SetNode, Sam2Segmentation, DrawViTPose, ImageResizeKJv2, GetImageSize, DownloadAndLoadSAM2Model, GrowMask, GetNode, GetNode, GetNode, GetNode, Float to Int, easy cleanGpuUsed, ImageConcanate, ImageConcanate, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, WanVideoTextEncodeCached, VHS_VideoCombine, JjkText, SetNode, INTConstant, VHS_LoadVideo, VHS_VideoCombine, INTConstant, PointsEditor, LoadImage, VHS_LoadVideo, GetNode, GetNode, SetNode, GetNode]
patterns: []
missing: []
---

# 平台全量/Wan2.2Animate视频换人物_2062474652877942786.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2Animate视频换人物_2062474652877942786.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（90 个）：
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VHS_VideoInfoLoaded`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `easy showAnything`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `PoseAndFaceDetection`
- `Reroute`
- `GetNode`
- `GetNode`
- `GetNode`
- `BlockifyMask`
- `SetNode`
- `DrawMaskOnImage`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `Sam2Segmentation`
- `DrawViTPose`
- `ImageResizeKJv2`
- `GetImageSize`
- `DownloadAndLoadSAM2Model`
- `GrowMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Float to Int`
- `easy cleanGpuUsed`
- `ImageConcanate`
- `ImageConcanate`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SetNode`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `JjkText`
- `SetNode`
- `INTConstant`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `INTConstant`
- `PointsEditor`
- `LoadImage`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`

## 知识

覆盖率 **51%**（46/90）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`VHS_VideoInfoLoaded`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoAnimateEmbeds`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`BlockifyMask`、`DrawMaskOnImage`、`Sam2Segmentation`、`DrawViTPose`、`GetImageSize`、`DownloadAndLoadSAM2Model`、`GrowMask`、`Float to Int`、`ImageConcanate`、`WanVideoTextEncodeCached`、`INTConstant`、`VHS_LoadVideo`、`PointsEditor`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
