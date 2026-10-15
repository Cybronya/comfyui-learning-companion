---
key: 视频生成/文生视频/OneToAllAnimation_动作迁移长视频for循环流 课程同步免费升级_1999868233400414209.json
name: OneToAllAnimation_动作迁移长视频for循环流 课程同步免费升级_1999868233400414209
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/OneToAllAnimation_动作迁移长视频for循环流 课程同步免费升级_1999868233400414209.json
hash: 8f670d2e2b244a80
coverage: 0.5
learned_at: 2026-10-15 22:46:50
nodes: [LoadWanVideoT5TextEncoder, WanVideoTextEncode, WanVideoSampler, WanVideoDecode, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoAddOneToAllPoseEmbeds, WanVideoEmptyEmbeds, WanVideoAddOneToAllReferenceEmbeds, ImageResizeKJv2, OnnxDetectionModelLoader, ImageResizeKJv2, VHS_VideoCombine, VHS_VideoCombine, PoseDetectionOneToAllAnimation, PreviewImage, INTConstant, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetImageRangeFromBatch, SetNode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, WanVideoScheduler, GetNode, FloatConstant, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAddOneToAllExtendEmbeds, WanVideoDecode, ImageBatchExtendWithOverlap, WanVideoAddOneToAllPoseEmbeds, WanVideoSampler, WanVideoEncode, ImageBatchExtendWithOverlap, GetImageSizeAndCount, easy forLoopStart, easy forLoopEnd, SetNode, GetNode, SetNode, INTConstant, GetNode, GetNode, LoadImage, INTConstant, INTConstant, SetNode, WanVideoBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, MathExpression|pysssss, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/文生视频/OneToAllAnimation_动作迁移长视频for循环流 课程同步免费升级_1999868233400414209.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/OneToAllAnimation_动作迁移长视频for循环流 课程同步免费升级_1999868233400414209.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（80 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoAddOneToAllPoseEmbeds`
- `WanVideoEmptyEmbeds`
- `WanVideoAddOneToAllReferenceEmbeds`
- `ImageResizeKJv2`
- `OnnxDetectionModelLoader`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PoseDetectionOneToAllAnimation`
- `PreviewImage`
- `INTConstant`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoScheduler`
- `GetNode`
- `FloatConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAddOneToAllExtendEmbeds`
- `WanVideoDecode`
- `ImageBatchExtendWithOverlap`
- `WanVideoAddOneToAllPoseEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `ImageBatchExtendWithOverlap`
- `GetImageSizeAndCount`
- `easy forLoopStart`
- `easy forLoopEnd`
- `SetNode`
- `GetNode`
- `SetNode`
- `INTConstant`
- `GetNode`
- `GetNode`
- `LoadImage`
- `INTConstant`
- `INTConstant`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `MathExpression|pysssss`
- `VHS_LoadVideo`

## 知识

覆盖率 **50%**（40/80）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoAddOneToAllPoseEmbeds`、`WanVideoEmptyEmbeds`、`WanVideoAddOneToAllReferenceEmbeds`、`ImageResizeKJv2`、`OnnxDetectionModelLoader`、`VHS_VideoCombine`、`PoseDetectionOneToAllAnimation`、`INTConstant`、`GetImageRangeFromBatch`、`WanVideoScheduler`、`FloatConstant`、`WanVideoAddOneToAllExtendEmbeds`、`ImageBatchExtendWithOverlap`、`WanVideoEncode`、`GetImageSizeAndCount`、`easy forLoopStart`、`easy forLoopEnd`、`LoadImage`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`MathExpression|pysssss`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect
