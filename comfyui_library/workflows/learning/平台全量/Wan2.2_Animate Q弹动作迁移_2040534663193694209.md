---
key: 平台全量/Wan2.2_Animate Q弹动作迁移_2040534663193694209.json
name: Wan2.2_Animate Q弹动作迁移_2040534663193694209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2_Animate Q弹动作迁移_2040534663193694209.json
hash: b4f0c7e76a9b96d6
coverage: 0.577778
learned_at: 2026-11-14 01:06:13
nodes: [Int, SetNode, easy cleanGpuUsed, OnnxDetectionModelLoader, SetNode, SetNode, GetImageSizeAndCount, WanVideoContextOptions, easy cleanGpuUsed, GetNode, GetNode, VHS_VideoCombine, INTConstant, SetNode, WanVideoAnimateEmbeds, PoseAndFaceDetection, PoseAndFaceDetection, DrawViTPose, GetNode, SetNode, GetNode, VHS_VideoInfo, SetNode, WanVideoSampler, GetNode, INTConstant, ImageResizeKJv2, SetNode, GetNode, GetNode, SetNode, GetNode, SetNode, WanVideoTextEncodeCached, WanVideoDecode, VHS_LoadVideo, LoadImage, WanVideoBlockSwap, CLIPVisionLoader, SetNode, WanVideoVAELoader, WanVideoClipVisionEncode, WanVideoSetBlockSwap, GetNode, RHHiddenNodes]
patterns: []
missing: []
---

# 平台全量/Wan2.2_Animate Q弹动作迁移_2040534663193694209.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2_Animate Q弹动作迁移_2040534663193694209.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `Int`
- `SetNode`
- `easy cleanGpuUsed`
- `OnnxDetectionModelLoader`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `WanVideoContextOptions`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `INTConstant`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `PoseAndFaceDetection`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoInfo`
- `SetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `INTConstant`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `WanVideoTextEncodeCached`
- `WanVideoDecode`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoBlockSwap`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `WanVideoSetBlockSwap`
- `GetNode`
- `RHHiddenNodes`

## 知识

覆盖率 **58%**（26/45）

**有卡**：`Int`、`easy cleanGpuUsed`、`OnnxDetectionModelLoader`、`GetImageSizeAndCount`、`WanVideoContextOptions`、`VHS_VideoCombine`、`INTConstant`、`WanVideoAnimateEmbeds`、`PoseAndFaceDetection`、`DrawViTPose`、`VHS_VideoInfo`、`WanVideoSampler`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`VHS_LoadVideo`、`LoadImage`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`RHHiddenNodes`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、CLIPVisionLoader、GetImageSizeAndCount
