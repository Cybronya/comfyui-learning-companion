---
key: 视频生成/图生视频/V2 Wan2.2 Animate 视频替换人物_产品_背景 (3)_1997005381832478722.json
name: V2 Wan2.2 Animate 视频替换人物_产品_背景 (3)_1997005381832478722.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/V2 Wan2.2 Animate 视频替换人物_产品_背景 (3)_1997005381832478722.json
hash: 030a72139b124ba5
coverage: 0.516484
learned_at: 2026-10-15 22:33:28
nodes: [WanVideoTorchCompileSettings, SetNode, SetNode, SetNode, SetNode, WanVideoVAELoader, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, CLIPVisionLoader, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, easy cleanGpuUsed, easy cleanGpuUsed, VHS_VideoInfoLoaded, WanVideoDecode, GetNode, WanVideoSampler, easy showAnything, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoAnimateEmbeds, GetNode, VHS_VideoCombine, GetNode, SetNode, SetNode, VHS_VideoCombine, OnnxDetectionModelLoader, GetImageSizeAndCount, GetNode, PoseAndFaceDetection, Reroute, GetNode, GetNode, GetNode, BlockifyMask, SetNode, DrawMaskOnImage, GetNode, VHS_VideoCombine, SetNode, Sam2Segmentation, DrawViTPose, ImageResizeKJv2, SetNode, GetImageSize, DownloadAndLoadSAM2Model, GrowMask, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, Float to Int, INTConstant, INTConstant, easy cleanGpuUsed, GetNode, VHS_LoadVideo, VHS_VideoCombine, ImageConcanate, ImageConcanate, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, PointsEditor, WanVideoTextEncodeCached, JjkText, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/V2 Wan2.2 Animate 视频替换人物_产品_背景 (3)_1997005381832478722.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1997005381832478722.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（91 个）：
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
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VHS_VideoInfoLoaded`
- `WanVideoDecode`
- `GetNode`
- `WanVideoSampler` ★核心
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
- `GrowMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `Float to Int`
- `INTConstant`
- `INTConstant`
- `easy cleanGpuUsed`
- `GetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `ImageConcanate`
- `ImageConcanate`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SetNode`
- `PointsEditor`
- `WanVideoTextEncodeCached`
- `JjkText`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **52%**（47/91）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`VHS_VideoInfoLoaded`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoAnimateEmbeds`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`BlockifyMask`、`DrawMaskOnImage`、`Sam2Segmentation`、`DrawViTPose`、`GetImageSize`、`DownloadAndLoadSAM2Model`、`GrowMask`、`Float to Int`、`INTConstant`、`VHS_LoadVideo`、`ImageConcanate`、`PointsEditor`、`WanVideoTextEncodeCached`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
