---
key: 视频生成/图生视频/wan2.1-scail+FOR循环适合小显存配置_2050481432279175169.json
name: wan2.1-scail+FOR循环适合小显存配置_2050481432279175169.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2050481432279175169.json
hash: 5f0b3bf6fd9e0c77
coverage: 0.926471
learned_at: 2026-10-15 22:37:18
nodes: [WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, SimpleMath+, Note, Note, SimpleMath+, easy clearCacheAll, INTConstant, INTConstant, easy cleanGpuUsed, easy clearCacheAll, LoadNLFModel, WanVideoSamplerv2, WanVideoVAELoader, CLIPVisionLoader, ImageResizeKJv2, PreviewImage, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, PoseDetectionVitPoseToDWPose, NLFPredict, RenderNLFPoses, WanVideoSchedulerv2, WanVideoTextEncode, WanVideoContextOptions, PreviewAnimation, easy cleanGpuUsed, easy clearCacheAll, WanVideoEmptyEmbeds, WanVideoSamplerExtraArgs, WanVideoBlockSwap, SimpleMath+, WanVideoAddSCAILPoseEmbeds, ImageFromBatch, easy ifElse, GetImageSizeAndCount, ImageFromBatch, WanVideoClipVisionEncode, WanVideoAddSCAILReferenceEmbeds, MathExpression|pysssss, GetImageSizeAndCount, ImageFromBatch, easy forLoopStart, ImpactCompare, Display Int (rgthree), Display Int (rgthree), ImageResizeKJv2, WanVideoDecode, ImpactInt, MathExpression|pysssss, SimpleMath+, MathExpression|pysssss, ImpactInt, easy forLoopEnd, easy ifElse, ImageBatchExtendWithOverlap, LoadImage, INTConstant, PreviewAnimation, GetImageSizeAndCount, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoLoraSelect, VHS_LoadVideo, VHS_VideoCombine, CM_FloatToInt, FloatConstant]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1-scail+FOR循环适合小显存配置_2050481432279175169.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2050481432279175169.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（68 个）：
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `SimpleMath+`
- `Note`
- `Note`
- `SimpleMath+`
- `easy clearCacheAll`
- `INTConstant`
- `INTConstant`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `LoadNLFModel`
- `WanVideoSamplerv2` ★核心
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `ImageResizeKJv2`
- `PreviewImage`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `PoseDetectionVitPoseToDWPose`
- `NLFPredict`
- `RenderNLFPoses`
- `WanVideoSchedulerv2`
- `WanVideoTextEncode`
- `WanVideoContextOptions`
- `PreviewAnimation`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `WanVideoEmptyEmbeds`
- `WanVideoSamplerExtraArgs` ★核心
- `WanVideoBlockSwap`
- `SimpleMath+`
- `WanVideoAddSCAILPoseEmbeds`
- `ImageFromBatch`
- `easy ifElse`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `WanVideoClipVisionEncode`
- `WanVideoAddSCAILReferenceEmbeds`
- `MathExpression|pysssss`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `easy forLoopStart`
- `ImpactCompare`
- `Display Int (rgthree)`
- `Display Int (rgthree)`
- `ImageResizeKJv2`
- `WanVideoDecode`
- `ImpactInt`
- `MathExpression|pysssss`
- `SimpleMath+`
- `MathExpression|pysssss`
- `ImpactInt`
- `easy forLoopEnd`
- `easy ifElse`
- `ImageBatchExtendWithOverlap`
- `LoadImage`
- `INTConstant`
- `PreviewAnimation`
- `GetImageSizeAndCount`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoLoraSelect`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `CM_FloatToInt`
- `FloatConstant`

## 知识

覆盖率 **93%**（63/68）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`SimpleMath+`、`easy clearCacheAll`、`INTConstant`、`easy cleanGpuUsed`、`LoadNLFModel`、`WanVideoSamplerv2`、`WanVideoVAELoader`、`CLIPVisionLoader`、`ImageResizeKJv2`、`OnnxDetectionModelLoader`、`PoseDetectionVitPoseToDWPose`、`NLFPredict`、`RenderNLFPoses`、`WanVideoSchedulerv2`、`WanVideoTextEncode`、`WanVideoContextOptions`、`PreviewAnimation`、`WanVideoEmptyEmbeds`、`WanVideoSamplerExtraArgs`、`WanVideoBlockSwap`、`WanVideoAddSCAILPoseEmbeds`、`ImageFromBatch`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`WanVideoAddSCAILReferenceEmbeds`、`MathExpression|pysssss`、`easy forLoopStart`、`ImpactCompare`、`Display Int (rgthree)`、`WanVideoDecode`、`ImpactInt`、`easy forLoopEnd`、`ImageBatchExtendWithOverlap`、`LoadImage`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`VHS_LoadVideo`、`VHS_VideoCombine`、`CM_FloatToInt`、`FloatConstant`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoSamplerExtraArgs、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
