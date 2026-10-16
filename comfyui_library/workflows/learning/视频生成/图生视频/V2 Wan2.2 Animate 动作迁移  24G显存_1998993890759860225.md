---
key: 视频生成/图生视频/V2 Wan2.2 Animate 动作迁移  24G显存_1998993890759860225.json
name: V2 Wan2.2 Animate 动作迁移  24G显存_1998993890759860225.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1998993890759860225.json
hash: ff15dcff358225bd
coverage: 0.516854
learned_at: 2026-10-15 22:33:35
nodes: [WanVideoTorchCompileSettings, SetNode, SetNode, SetNode, WanVideoVAELoader, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, CLIPVisionLoader, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, easy cleanGpuUsed, easy cleanGpuUsed, VHS_VideoInfoLoaded, WanVideoDecode, GetNode, easy showAnything, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, GetNode, GetNode, SetNode, SetNode, OnnxDetectionModelLoader, GetImageSizeAndCount, GetNode, PoseAndFaceDetection, Reroute, GetNode, GetNode, BlockifyMask, SetNode, GetNode, GrowMask, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, ImageConcanate, ImageConcanate, easy cleanGpuUsed, easy cleanGpuUsed, VHS_LoadVideo, WanVideoTeaCache, SetNode, WanVideoSampler, DrawViTPose, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, Sam2Segmentation, DownloadAndLoadSAM2Model, WanVideoAnimateEmbeds, GetNode, LoadImage, GetImageSize, ImageResizeKJv2, SetNode, JjkText, WanVideoTextEncodeCached, INTConstant, INTConstant, SetNode, SetNode, DrawMaskOnImage, PointsEditor, MuyeLoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/V2 Wan2.2 Animate 动作迁移  24G显存_1998993890759860225.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998993890759860225.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（89 个）：
- `WanVideoTorchCompileSettings`
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
- `easy showAnything`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `GetImageSizeAndCount`
- `GetNode`
- `PoseAndFaceDetection`
- `Reroute`
- `GetNode`
- `GetNode`
- `BlockifyMask`
- `SetNode`
- `GetNode`
- `GrowMask`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `ImageConcanate`
- `ImageConcanate`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `VHS_LoadVideo`
- `WanVideoTeaCache`
- `SetNode`
- `WanVideoSampler` ★核心
- `DrawViTPose`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `Sam2Segmentation`
- `DownloadAndLoadSAM2Model`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `LoadImage`
- `GetImageSize`
- `ImageResizeKJv2`
- `SetNode`
- `JjkText`
- `WanVideoTextEncodeCached`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `PointsEditor`
- `MuyeLoadImage`

## 知识

覆盖率 **52%**（46/89）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`VHS_VideoInfoLoaded`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`BlockifyMask`、`GrowMask`、`ImageConcanate`、`VHS_LoadVideo`、`WanVideoTeaCache`、`WanVideoSampler`、`DrawViTPose`、`VHS_VideoCombine`、`Sam2Segmentation`、`DownloadAndLoadSAM2Model`、`WanVideoAnimateEmbeds`、`LoadImage`、`GetImageSize`、`WanVideoTextEncodeCached`、`INTConstant`、`DrawMaskOnImage`、`PointsEditor`、`MuyeLoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
