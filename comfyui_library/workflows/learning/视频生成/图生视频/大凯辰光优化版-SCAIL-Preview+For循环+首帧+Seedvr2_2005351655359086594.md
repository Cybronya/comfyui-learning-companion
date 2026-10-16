---
key: 视频生成/图生视频/大凯辰光优化版-SCAIL-Preview+For循环+首帧+Seedvr2_2005351655359086594.json
name: 大凯辰光优化版-SCAIL-Preview+For循环+首帧+Seedvr2_2005351655359086594.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2005351655359086594.json
hash: d279d5a58c6ca1e3
coverage: 0.5
learned_at: 2026-10-15 22:33:56
nodes: [SetNode, WanVideoSetLoRAs, WanVideoVAELoader, GetNode, WanVideoTorchCompileSettings, GetNode, GetNode, GetNode, GetNode, SetNode, CLIPVisionLoader, GetNode, GetNode, NLFPredict, DownloadAndLoadNLFModel, PreviewAnimation, SetNode, GetNode, GetNode, GetNode, GetNode, GetImageRangeFromBatch, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetImageSizeAndCount, GetNode, SetNode, INTConstant, INTConstant, RenderNLFPoses, Fast Groups Bypasser (rgthree), MarkdownNote, LoadWanVideoT5TextEncoder, MathExpression|pysssss, WanVideoModelLoader, SetNode, FloatConstant, GetNode, SetNode, WanVideoBlockSwap, SetNode, SetNode, SDVN Boolean, MathExpression|pysssss, GetImageRangeFromBatch, easy forLoopEnd, MathExpression|pysssss, SetNode, MathExpression|pysssss, SetNode, GetNode, GetNode, MathExpression|pysssss, easy forLoopStart, SetNode, SetNode, GetNode, Display Any (rgthree), Display Any (rgthree), GetNode, SetNode, MathExpression|pysssss, PoseDetectionVitPoseToDWPose, ConvertOpenPoseKeypointsToDWPose, DWPreprocessor, GetNode, WanVideoDecode, INTConstant, ToInt, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoImageToVideoEncode, WanVideoEmptyEmbeds, WanVideoClipVisionEncode, GetNode, Int, WanVideoAddSCAILPoseEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoSamplerv2, GetNode, GetNode, GetNode, WanVideoContextOptions, WanVideoUni3C_embeds, WanVideoSamplerExtraArgs, GetNode, GetNode, WanVideoUni3C_ControlnetLoader, WanVideoTextEncode, SetNode, easy cleanGpuUsed, easy clearCacheAll, Any To String (mtb), WanVideoLoraSelect, WanVideoLoraSelect, SetNode, SetNode, OnnxDetectionModelLoader, WanVideoSetBlockSwap, SetNode, easy compare, ImageResizeKJv2, ImageResizeKJv2, LoadImage, SetNode, SetNode, easy ifElse, SetNode, SetNode, GetNode, SetNode, ShowText|pysssss, Qwen3_VQA, GetNode, WanVideoEncode, ImageBatchExtendWithOverlap, LayerUtility: PurgeVRAM, PreviewAnimation, INTConstant, GetNode, SetNode, easy ifElse, GetNode, GetNode, easy ifElse, WanVideoSchedulerv2, GetNode, easy clearCacheAll, GetNode, VHS_VideoCombine, easy cleanGpuUsed, SeedVR2, GetNode, SeedVR2BlockSwap, SeedVR2ExtraArgs, easy clearCacheAll, easy cleanGpuUsed, SetNode, LayerUtility: PurgeVRAM, Note, RIFE VFI, VHS_VideoCombine, VHS_LoadVideo, INTConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/大凯辰光优化版-SCAIL-Preview+For循环+首帧+Seedvr2_2005351655359086594.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2005351655359086594.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（154 个）：
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoVAELoader`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `NLFPredict`
- `DownloadAndLoadNLFModel`
- `PreviewAnimation`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `RenderNLFPoses`
- `Fast Groups Bypasser (rgthree)`
- `MarkdownNote`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `WanVideoModelLoader`
- `SetNode`
- `FloatConstant`
- `GetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `SetNode`
- `SetNode`
- `SDVN Boolean`
- `MathExpression|pysssss`
- `GetImageRangeFromBatch`
- `easy forLoopEnd`
- `MathExpression|pysssss`
- `SetNode`
- `MathExpression|pysssss`
- `SetNode`
- `GetNode`
- `GetNode`
- `MathExpression|pysssss`
- `easy forLoopStart`
- `SetNode`
- `SetNode`
- `GetNode`
- `Display Any (rgthree)`
- `Display Any (rgthree)`
- `GetNode`
- `SetNode`
- `MathExpression|pysssss`
- `PoseDetectionVitPoseToDWPose`
- `ConvertOpenPoseKeypointsToDWPose`
- `DWPreprocessor`
- `GetNode`
- `WanVideoDecode`
- `INTConstant`
- `ToInt`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoEmptyEmbeds`
- `WanVideoClipVisionEncode`
- `GetNode`
- `Int`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoSamplerv2` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoContextOptions`
- `WanVideoUni3C_embeds`
- `WanVideoSamplerExtraArgs` ★核心
- `GetNode`
- `GetNode`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoTextEncode`
- `SetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `Any To String (mtb)`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `SetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `WanVideoSetBlockSwap`
- `SetNode`
- `easy compare`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `SetNode`
- `SetNode`
- `easy ifElse`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `ShowText|pysssss`
- `Qwen3_VQA`
- `GetNode`
- `WanVideoEncode`
- `ImageBatchExtendWithOverlap`
- `LayerUtility: PurgeVRAM`
- `PreviewAnimation`
- `INTConstant`
- `GetNode`
- `SetNode`
- `easy ifElse`
- `GetNode`
- `GetNode`
- `easy ifElse`
- `WanVideoSchedulerv2`
- `GetNode`
- `easy clearCacheAll`
- `GetNode`
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `SeedVR2`
- `GetNode`
- `SeedVR2BlockSwap`
- `SeedVR2ExtraArgs`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `SetNode`
- `LayerUtility: PurgeVRAM`
- `Note`
- `RIFE VFI`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `INTConstant`

## 知识

覆盖率 **50%**（77/154）

**有卡**：`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`CLIPVisionLoader`、`NLFPredict`、`DownloadAndLoadNLFModel`、`PreviewAnimation`、`GetImageRangeFromBatch`、`GetImageSizeAndCount`、`INTConstant`、`RenderNLFPoses`、`LoadWanVideoT5TextEncoder`、`MathExpression|pysssss`、`WanVideoModelLoader`、`FloatConstant`、`WanVideoBlockSwap`、`SDVN Boolean`、`easy forLoopEnd`、`easy forLoopStart`、`Display Any (rgthree)`、`PoseDetectionVitPoseToDWPose`、`ConvertOpenPoseKeypointsToDWPose`、`DWPreprocessor`、`WanVideoDecode`、`ToInt`、`WanVideoImageToVideoEncode`、`WanVideoEmptyEmbeds`、`WanVideoClipVisionEncode`、`Int`、`WanVideoAddSCAILPoseEmbeds`、`WanVideoAddSCAILReferenceEmbeds`、`WanVideoSamplerv2`、`WanVideoContextOptions`、`WanVideoUni3C_embeds`、`WanVideoSamplerExtraArgs`、`WanVideoUni3C_ControlnetLoader`、`WanVideoTextEncode`、`easy cleanGpuUsed`、`easy clearCacheAll`、`Any To String (mtb)`、`WanVideoLoraSelect`、`OnnxDetectionModelLoader`、`WanVideoSetBlockSwap`、`easy compare`、`ImageResizeKJv2`、`LoadImage`、`Qwen3_VQA`、`WanVideoEncode`、`ImageBatchExtendWithOverlap`、`LayerUtility: PurgeVRAM`、`WanVideoSchedulerv2`、`VHS_VideoCombine`、`SeedVR2`、`SeedVR2BlockSwap`、`SeedVR2ExtraArgs`、`RIFE VFI`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、ConvertOpenPoseKeypointsToDWPose、SeedVR2、SeedVR2BlockSwap、SeedVR2ExtraArgs、WanVideoSamplerv2、WanVideoSamplerExtraArgs
