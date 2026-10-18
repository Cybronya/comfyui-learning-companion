---
key: 视频生成/图生视频/V2 Wan2.3 Animate 超自然动作迁移_2008454973708832769.json
name: V2 Wan2.3 Animate 超自然动作迁移_2008454973708832769.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/V2 Wan2.3 Animate 超自然动作迁移_2008454973708832769.json
hash: d676024c9408c7d3
coverage: 0.511364
learned_at: 2026-10-15 22:34:07
nodes: [WanVideoTorchCompileSettings, SetNode, SetNode, SetNode, SetNode, WanVideoVAELoader, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, GetNode, SetNode, CLIPVisionLoader, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, easy cleanGpuUsed, easy cleanGpuUsed, VHS_VideoInfoLoaded, WanVideoDecode, GetNode, WanVideoSampler, easy showAnything, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoAnimateEmbeds, GetNode, VHS_VideoCombine, GetNode, SetNode, SetNode, VHS_VideoCombine, OnnxDetectionModelLoader, GetImageSizeAndCount, GetNode, PoseAndFaceDetection, Reroute, GetNode, GetNode, GetNode, BlockifyMask, SetNode, DrawMaskOnImage, GetNode, VHS_VideoCombine, SetNode, Sam2Segmentation, DrawViTPose, ImageResizeKJv2, SetNode, GetImageSize, DownloadAndLoadSAM2Model, GrowMask, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, INTConstant, INTConstant, easy cleanGpuUsed, GetNode, VHS_VideoCombine, ImageConcanate, ImageConcanate, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, WanVideoTextEncodeCached, JjkText, VHS_LoadVideo, PointsEditor, LoadImage, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/V2 Wan2.3 Animate 超自然动作迁移_2008454973708832769.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2008454973708832769.json`

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
- `VHS_VideoCombine`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `easy cleanGpuUsed`
- `GetNode`
- `VHS_VideoCombine`
- `ImageConcanate`
- `ImageConcanate`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `SetNode`
- `WanVideoTextEncodeCached`
- `JjkText`
- `VHS_LoadVideo`
- `PointsEditor`
- `LoadImage`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **51%**（45/88）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`ImageResizeKJv2`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`easy cleanGpuUsed`、`VHS_VideoInfoLoaded`、`WanVideoDecode`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoAnimateEmbeds`、`VHS_VideoCombine`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`BlockifyMask`、`DrawMaskOnImage`、`Sam2Segmentation`、`DrawViTPose`、`GetImageSize`、`DownloadAndLoadSAM2Model`、`GrowMask`、`INTConstant`、`ImageConcanate`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`PointsEditor`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
