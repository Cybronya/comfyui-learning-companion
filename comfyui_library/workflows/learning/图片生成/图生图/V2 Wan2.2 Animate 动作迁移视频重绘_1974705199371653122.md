---
key: 图片生成/图生图/V2 Wan2.2 Animate 动作迁移视频重绘_1974705199371653122.json
name: V2 Wan2.2 Animate 动作迁移视频重绘_1974705199371653122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/V2 Wan2.2 Animate 动作迁移视频重绘_1974705199371653122.json
hash: 02bddb6a8426dc7f
coverage: 0.511628
learned_at: 2026-10-23 11:27:03
nodes: [WanVideoTorchCompileSettings, SetNode, SetNode, SetNode, SetNode, WanVideoVAELoader, SetNode, SetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, GetNode, GetNode, easy cleanGpuUsed, SetNode, CLIPVisionLoader, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, SetNode, easy cleanGpuUsed, SetNode, GetNode, GetNode, GetNode, GetNode, GetImageSizeAndCount, easy cleanGpuUsed, easy cleanGpuUsed, INTConstant, INTConstant, WanVideoDecode, GetNode, GetNode, WanVideoSampler, VHS_VideoCombine, SetNode, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoTextEncodeCached, SetNode, GetNode, VHS_VideoCombine, DrawViTPose, GetNode, SetNode, SetNode, VHS_VideoCombine, GetNode, OnnxDetectionModelLoader, PoseAndFaceDetection, GetNode, GetNode, WanVideoEncode, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, ImageResizeKJv2, GetImageSizeAndCount, GetNode, GetNode, VHS_VideoCombine, easy cleanGpuUsed, LoadImage, easy showAnything, VHS_LoadVideo, GetNode, GetNode, WanVideoLoraSelectMulti, ImageConcanate, ImageConcanate, WanVideoAnimateEmbeds, VHS_LoadVideoPath, INTConstant, SetNode, MathExpression|pysssss, SetNode, Bjornulf_ShowInt, VHS_VideoInfoLoaded, GetNode, GetNode, GetNode]
patterns: []
missing: []
---

# 图片生成/图生图/V2 Wan2.2 Animate 动作迁移视频重绘_1974705199371653122.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/V2 Wan2.2 Animate 动作迁移视频重绘_1974705199371653122.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（86 个）：
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
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
- `INTConstant`
- `INTConstant`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeCached`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `DrawViTPose`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `OnnxDetectionModelLoader`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `ImageResizeKJv2`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `LoadImage`
- `easy showAnything`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `WanVideoLoraSelectMulti`
- `ImageConcanate`
- `ImageConcanate`
- `WanVideoAnimateEmbeds`
- `VHS_LoadVideoPath`
- `INTConstant`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `Bjornulf_ShowInt`
- `VHS_VideoInfoLoaded`
- `GetNode`
- `GetNode`
- `GetNode`

## 知识

覆盖率 **51%**（44/86）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`GetImageSizeAndCount`、`INTConstant`、`WanVideoDecode`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTextEncodeCached`、`DrawViTPose`、`OnnxDetectionModelLoader`、`PoseAndFaceDetection`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`LoadImage`、`VHS_LoadVideo`、`ImageConcanate`、`WanVideoAnimateEmbeds`、`VHS_LoadVideoPath`、`MathExpression|pysssss`、`Bjornulf_ShowInt`、`VHS_VideoInfoLoaded`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoEncode
