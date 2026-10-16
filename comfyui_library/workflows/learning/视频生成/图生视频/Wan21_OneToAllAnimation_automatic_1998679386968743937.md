---
key: 视频生成/图生视频/Wan21_OneToAllAnimation_automatic_1998679386968743937.json
name: Wan21_OneToAllAnimation_automatic_1998679386968743937.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1998679386968743937.json
hash: e4b836791729e0bc
coverage: 0.485714
learned_at: 2026-10-15 22:33:33
nodes: [ImageBatchExtendWithOverlap, GetNode, GetNode, GetNode, WanVideoDecode, WanVideoSampler, VHS_VideoCombine, WanVideoAddOneToAllPoseEmbeds, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoEncode, SetNode, SetNode, GetNode, WanVideoAddOneToAllExtendEmbeds, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetNode, GetNode, ImageBatchExtendWithOverlap, Reroute, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, WanVideoEncode, WanVideoAddOneToAllPoseEmbeds, WanVideoSampler, MarkdownNote, SetNode, SetNode, WanVideoBlockSwap, WanVideoModelLoader, Note, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, WanVideoTextEncode, SetNode, SetNode, WanVideoVAELoader, SetNode, INTConstant, INTConstant, INTConstant, FloatConstant, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, OnnxDetectionModelLoader, PoseDetectionOneToAllAnimation, SetNode, PreviewImage, MaskPreview+, WanVideoEmptyEmbeds, SetNode, WanVideoScheduler, WanVideoAddOneToAllReferenceEmbeds, GetImageRangeFromBatch, WanVideoAddOneToAllPoseEmbeds, WanVideoDecode, VHS_VideoCombine, GetNode, GetImageSizeAndCount, PreviewImage, SetNode, ImageResizeKJv2, ImageResizeKJv2, GetNode, GetNode, SetNode, SetNode, SetNode, INTConstant, SetNode, GetNode, ImageBatchExtendWithOverlap, ImageBatchExtendWithOverlap, easy forLoopEnd, easy forLoopStart, VHS_VideoCombine, GetNode, GetNode, GetNode, WanVideoDecode, LoadImage, MathExpression|pysssss, VHS_LoadVideo, WanVideoAddOneToAllExtendEmbeds]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan21_OneToAllAnimation_automatic_1998679386968743937.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998679386968743937.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（105 个）：
- `ImageBatchExtendWithOverlap`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `WanVideoAddOneToAllPoseEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoAddOneToAllExtendEmbeds`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `Reroute`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoEncode`
- `WanVideoAddOneToAllPoseEmbeds`
- `WanVideoSampler` ★核心
- `MarkdownNote`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `Note`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncode`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `FloatConstant`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `PoseDetectionOneToAllAnimation`
- `SetNode`
- `PreviewImage`
- `MaskPreview+`
- `WanVideoEmptyEmbeds`
- `SetNode`
- `WanVideoScheduler`
- `WanVideoAddOneToAllReferenceEmbeds`
- `GetImageRangeFromBatch`
- `WanVideoAddOneToAllPoseEmbeds`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `GetNode`
- `GetImageSizeAndCount`
- `PreviewImage`
- `SetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `ImageBatchExtendWithOverlap`
- `easy forLoopEnd`
- `easy forLoopStart`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `LoadImage`
- `MathExpression|pysssss`
- `VHS_LoadVideo`
- `WanVideoAddOneToAllExtendEmbeds`

## 知识

覆盖率 **49%**（51/105）

**有卡**：`ImageBatchExtendWithOverlap`、`WanVideoDecode`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoAddOneToAllPoseEmbeds`、`WanVideoEncode`、`WanVideoAddOneToAllExtendEmbeds`、`GetImageSizeAndCount`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncode`、`WanVideoVAELoader`、`INTConstant`、`FloatConstant`、`OnnxDetectionModelLoader`、`PoseDetectionOneToAllAnimation`、`MaskPreview+`、`WanVideoEmptyEmbeds`、`WanVideoScheduler`、`WanVideoAddOneToAllReferenceEmbeds`、`GetImageRangeFromBatch`、`ImageResizeKJv2`、`easy forLoopEnd`、`easy forLoopStart`、`LoadImage`、`MathExpression|pysssss`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect
