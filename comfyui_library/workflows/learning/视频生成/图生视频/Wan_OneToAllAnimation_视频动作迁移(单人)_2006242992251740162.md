---
key: 视频生成/图生视频/Wan_OneToAllAnimation_视频动作迁移(单人)_2006242992251740162.json
name: Wan_OneToAllAnimation_视频动作迁移(单人)_2006242992251740162.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan_OneToAllAnimation_视频动作迁移(单人)_2006242992251740162.json
hash: c258d25818da9afb
coverage: 0.535088
learned_at: 2026-10-15 22:34:01
nodes: [ImageBatchExtendWithOverlap, GetNode, GetNode, GetNode, WanVideoDecode, WanVideoSampler, VHS_VideoCombine, WanVideoAddOneToAllPoseEmbeds, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoEncode, GetNode, WanVideoAddOneToAllExtendEmbeds, GetImageSizeAndCount, ImageBatchExtendWithOverlap, Reroute, GetImageSizeAndCount, LayerUtility: PurgeVRAM V2, DownloadAndLoadGIMMVFIModel, GetNode, GetNode, ImageResizeKJv2, OnnxDetectionModelLoader, SetNode, SetNode, SetNode, SetNode, PreviewImage, PreviewImage, SetNode, WanVideoEmptyEmbeds, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAddOneToAllReferenceEmbeds, GetNode, SetNode, GetNode, WanVideoAddOneToAllPoseEmbeds, WanVideoSampler, GetNode, GetImageRangeFromBatch, VHS_VideoCombine, WanVideoDecode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoTextEncode, SetNode, SetNode, MaskPreview+, WanVideoScheduler, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAddOneToAllPoseEmbeds, WanVideoSampler, ImageBatchExtendWithOverlap, WanVideoEncode, WanVideoAddOneToAllExtendEmbeds, ImageBatchExtendWithOverlap, WanVideoDecode, GetNode, MathExpression|pysssss, easy forLoopStart, easy forLoopEnd, GetNode, VHS_VideoCombine, GetNode, ImageResizeKJv2, GIMMVFI_interpolate, DownloadAndLoadGIMMVFIModel, LayerUtility: PurgeVRAM V2, VHS_VideoCombine, SetNode, ImageConcatMulti, ImageConcatMulti, GetNode, GIMMVFI_interpolate, GetNode, SetNode, INTConstant, SetNode, SetNode, SetNode, SetNode, SetNode, INTConstant, INTConstant, INTConstant, Text Multiline, PoseDetectionOneToAllAnimation, VHS_VideoCombine, Note, LoadImage, WanVideoModelLoader, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, VHS_LoadVideo, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan_OneToAllAnimation_视频动作迁移(单人)_2006242992251740162.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2006242992251740162.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（114 个）：
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
- `GetNode`
- `WanVideoAddOneToAllExtendEmbeds`
- `GetImageSizeAndCount`
- `ImageBatchExtendWithOverlap`
- `Reroute`
- `GetImageSizeAndCount`
- `LayerUtility: PurgeVRAM V2`
- `DownloadAndLoadGIMMVFIModel`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `OnnxDetectionModelLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `PreviewImage`
- `SetNode`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAddOneToAllReferenceEmbeds`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoAddOneToAllPoseEmbeds`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetImageRangeFromBatch`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoTextEncode`
- `SetNode`
- `SetNode`
- `MaskPreview+`
- `WanVideoScheduler`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAddOneToAllPoseEmbeds`
- `WanVideoSampler` ★核心
- `ImageBatchExtendWithOverlap`
- `WanVideoEncode`
- `WanVideoAddOneToAllExtendEmbeds`
- `ImageBatchExtendWithOverlap`
- `WanVideoDecode`
- `GetNode`
- `MathExpression|pysssss`
- `easy forLoopStart`
- `easy forLoopEnd`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `ImageResizeKJv2`
- `GIMMVFI_interpolate`
- `DownloadAndLoadGIMMVFIModel`
- `LayerUtility: PurgeVRAM V2`
- `VHS_VideoCombine`
- `SetNode`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetNode`
- `GIMMVFI_interpolate`
- `GetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `Text Multiline`
- `PoseDetectionOneToAllAnimation`
- `VHS_VideoCombine`
- `Note`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `VHS_LoadVideo`
- `INTConstant`

## 知识

覆盖率 **54%**（61/114）

**有卡**：`ImageBatchExtendWithOverlap`、`WanVideoDecode`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoAddOneToAllPoseEmbeds`、`WanVideoEncode`、`WanVideoAddOneToAllExtendEmbeds`、`GetImageSizeAndCount`、`LayerUtility: PurgeVRAM V2`、`DownloadAndLoadGIMMVFIModel`、`ImageResizeKJv2`、`OnnxDetectionModelLoader`、`WanVideoEmptyEmbeds`、`WanVideoAddOneToAllReferenceEmbeds`、`GetImageRangeFromBatch`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`MaskPreview+`、`WanVideoScheduler`、`MathExpression|pysssss`、`easy forLoopStart`、`easy forLoopEnd`、`GIMMVFI_interpolate`、`ImageConcatMulti`、`INTConstant`、`Text Multiline`、`PoseDetectionOneToAllAnimation`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect
