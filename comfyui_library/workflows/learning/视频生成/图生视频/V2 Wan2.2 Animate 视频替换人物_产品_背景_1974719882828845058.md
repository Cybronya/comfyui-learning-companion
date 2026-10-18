---
key: 视频生成/图生视频/V2 Wan2.2 Animate 视频替换人物_产品_背景_1974719882828845058.json
name: V2 Wan2.2 Animate 视频替换人物_产品_背景_1974719882828845058.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/V2 Wan2.2 Animate 视频替换人物_产品_背景_1974719882828845058.json
hash: 3df1d24483e95adf
coverage: 0.511364
learned_at: 2026-10-15 22:32:05
nodes: [WanVideoTorchCompileSettings, SetNode, SetNode, SetNode, SetNode, WanVideoVAELoader, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, GetNode, easy cleanGpuUsed, SetNode, CLIPVisionLoader, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, SetNode, easy cleanGpuUsed, SetNode, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, easy cleanGpuUsed, easy cleanGpuUsed, VHS_VideoInfoLoaded, INTConstant, INTConstant, WanVideoDecode, GetNode, GetNode, WanVideoSampler, VHS_VideoCombine, SetNode, easy showAnything, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoAnimateEmbeds, GetNode, VHS_VideoCombine, GetNode, SetNode, SetNode, VHS_VideoCombine, OnnxDetectionModelLoader, GetImageSizeAndCount, LoadImage, GetNode, PoseAndFaceDetection, Reroute, GetNode, GetNode, GetNode, BlockifyMask, SetNode, DrawMaskOnImage, GetNode, VHS_VideoCombine, SetNode, Sam2Segmentation, DrawViTPose, ImageResizeKJv2, SetNode, GetImageSize, DownloadAndLoadSAM2Model, PointsEditor, GrowMask, WanVideoTextEncodeCached, GetNode, GetNode, GetNode, ImageConcanate, GetNode, VHS_LoadVideo, VHS_VideoCombine, VHS_LoadVideoPath, ImageConcanate]
patterns: []
missing: []
---

# 视频生成/图生视频/V2 Wan2.2 Animate 视频替换人物_产品_背景_1974719882828845058.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1974719882828845058.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（88 个）：
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
- `easy cleanGpuUsed`
- `SetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VHS_VideoInfoLoaded`
- `INTConstant`
- `INTConstant`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `easy showAnything`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
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
- `LoadImage`
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
- `SetNode`
- `GetImageSize`
- `DownloadAndLoadSAM2Model`
- `PointsEditor`
- `GrowMask`
- `WanVideoTextEncodeCached`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageConcanate`
- `GetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_LoadVideoPath`
- `ImageConcanate`

## 知识

覆盖率 **51%**（45/88）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`VHS_VideoInfoLoaded`、`INTConstant`、`WanVideoDecode`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoAnimateEmbeds`、`OnnxDetectionModelLoader`、`LoadImage`、`PoseAndFaceDetection`、`BlockifyMask`、`DrawMaskOnImage`、`Sam2Segmentation`、`DrawViTPose`、`GetImageSize`、`DownloadAndLoadSAM2Model`、`PointsEditor`、`GrowMask`、`WanVideoTextEncodeCached`、`ImageConcanate`、`VHS_LoadVideo`、`VHS_LoadVideoPath`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
