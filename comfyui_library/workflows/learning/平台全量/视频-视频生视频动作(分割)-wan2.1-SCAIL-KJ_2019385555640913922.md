---
key: 平台全量/视频-视频生视频动作(分割)-wan2.1-SCAIL-KJ_2019385555640913922.json
name: 视频-视频生视频动作(分割)-wan2.1-SCAIL-KJ_2019385555640913922
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-视频生视频动作(分割)-wan2.1-SCAIL-KJ_2019385555640913922.json
hash: b72df187d6e07368
coverage: 0.668161
learned_at: 2026-11-14 02:34:36
nodes: [PreviewImage, ImageFromBatch, SetNode, GetImageSizeAndCount, CreateVideo, ImpactInt, ImpactInt, CLIPLoader, VHS_VideoInfoLoaded, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, ShowText|pysssss, AILab_MiniCPM_4_V, ShowText|pysssss, GetNode, easy promptReplace, easy seed, EmptyLatentImage, VAELoader, AIO_Preprocessor, ModelPatchLoader, GetImageSizeAndCount, easy positive, Florence2ModelLoader, Florence2Run, ConditioningZeroOut, KSamplerAdvanced, KSamplerAdvanced, INTConstant, ZImageFunControlnet, UNETLoader, easy showAnything, GetImageSizeAndCount, GetNode, GetNode, INTConstant, KSamplerSelect, CFGGuider, CLIPTextEncode, VAELoader, UNETLoader, CLIPTextEncode, ReferenceLatent, CLIPLoader, Reroute, VAEEncode, EmptyFlux2LatentImage, Reroute, Reroute, ReferenceLatent, RandomNoise, GetNode, StringFunction|pysssss, Reroute, GetImageSizeAndCount, GetNode, MemoryCleaner, GetNode, SamplerCustomAdvanced, Reroute, Reroute, PreviewImage, VAEDecode, SetNode, GetNode, PreviewImage, ImageConcanate, ImageFromBatch+, PreviewImage, GetNode, Reroute, VHS_VideoCombine, easy showAnything, easy imageSize, SetNode, CR String To Number, GetImageSizeAndCount, Reroute, Reroute, GetImageSizeAndCount, GetNode, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, PreviewImage, PreviewImage, VHS_VideoCombine, WanVideoSetBlockSwap, Note, WanVideoSetLoRAs, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoClipVisionEncode, OnnxDetectionModelLoader, WanVideoUni3C_ControlnetLoader, DWPreprocessor, NLFPredict, SetNode, SetNode, SetNode, GetNode, CLIPVisionLoader, WanVideoEmptyEmbeds, GetNode, easy showAnything, WanVideoTorchCompileSettings, SimpleMath+, SimpleMath+, PoseDetectionVitPoseToDWPose, easy int, easy int, WanVideoAddSCAILReferenceEmbeds, GetImageSizeAndCount, PreviewImage, ImageConcatMulti, ImageConcatMulti, GetImageSizeAndCount, SetNode, GetImageSizeAndCount, SetNode, VHS_VideoCombine, DownloadAndLoadNLFModel, GetImageSizeAndCount, Reroute, GetNode, GetImageSizeAndCount, ImageResizeKJv2, VHS_VideoCombine, ImageFromBatch, GetNode, SetNode, TextSplitByDelimiter, easy showAnything, easy lengthAnything, GODMT_ListToBatch, FL_VideoCadence, easy showAnything, easy showAnything, easy showAnything, easy showAnything, AnyBatchSliceNode, easy showAnything, SetNode, easy showAnything, Text List to Text, ImageFromBatch+, Int, easy batchAnything, VAEDecode, VHS_VideoCombine, GetNode, CLIPTextEncode, easy mathInt, easy showAnything, GetNode, GetNode, RH_Captioner, WanVideoTextEncode, ShowText|pysssss, RH_Captioner, ShowText|pysssss, FloatConstant, GetNode, WanVideoAddSCAILPoseEmbeds, WanVideoEncode, WanVideoUni3C_embeds, GetNode, GetNode, WanVideoSchedulerv2, GetImageSizeAndCount, WanVideoSamplerv2, SetNode, GetNode, SetNode, MathExpression|pysssss, Float, VHS_VideoInfoLoaded, GetImageSizeAndCount, SegmentFrameAdjuster, LayerUtility: ImageScaleByAspectRatio V2, Flux2Scheduler, WanVideoBlockSwap, GetNode, CM_IntToBool, easy showAnything, CR Float To Integer, CM_IntUnaryOperation, CM_BoolToInt, WanVideoContextOptions, WanVideoSamplerExtraArgs, easy anythingInversedSwitch, ImageFromBatch+, ImageFromBatch, WanVideoDecode, MemoryCleaner, ImageToDevice+, GetImageSizeAndCount, easy anythingIndexSwitch, VHS_LoadVideo, PrimitiveFloat, WanVideoModelLoader, ConvertOpenPoseKeypointsToDWPose, MemoryCleaner, MemoryCleaner, ImpactFloat, easy int, PrimitiveBoolean, Note, Note, Switch any [Crystools], RenderNLFPoses, PoseDetectionVitPoseToDWPose, Switch any [Crystools], PrimitiveBoolean, easy forLoopEnd, easy forLoopStart, GetImageSizeAndCount, PreviewImage, SaveImage, SetNode, easy saveText]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 1080, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "width": 1920}
---

# 平台全量/视频-视频生视频动作(分割)-wan2.1-SCAIL-KJ_2019385555640913922.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-视频生视频动作(分割)-wan2.1-SCAIL-KJ_2019385555640913922.json`

## 结构

**生成流程**：Model → Encode → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（223 个）：
- `PreviewImage`
- `ImageFromBatch`
- `SetNode`
- `GetImageSizeAndCount`
- `CreateVideo`
- `ImpactInt`
- `ImpactInt`
- `CLIPLoader`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetImageSizeAndCount`
- `ShowText|pysssss`
- `AILab_MiniCPM_4_V`
- `ShowText|pysssss`
- `GetNode`
- `easy promptReplace`
- `easy seed`
- `EmptyLatentImage` ★核心
- `VAELoader`
- `AIO_Preprocessor`
- `ModelPatchLoader`
- `GetImageSizeAndCount`
- `easy positive`
- `Florence2ModelLoader`
- `Florence2Run`
- `ConditioningZeroOut`
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `INTConstant`
- `ZImageFunControlnet`
- `UNETLoader` ★核心
- `easy showAnything`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `INTConstant`
- `KSamplerSelect` ★核心
- `CFGGuider`
- `CLIPTextEncode` ★核心
- `VAELoader`
- `UNETLoader` ★核心
- `CLIPTextEncode` ★核心
- `ReferenceLatent`
- `CLIPLoader`
- `Reroute`
- `VAEEncode` ★核心
- `EmptyFlux2LatentImage`
- `Reroute`
- `Reroute`
- `ReferenceLatent`
- `RandomNoise`
- `GetNode`
- `StringFunction|pysssss`
- `Reroute`
- `GetImageSizeAndCount`
- `GetNode`
- `MemoryCleaner`
- `GetNode`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `Reroute`
- `PreviewImage`
- `VAEDecode` ★核心
- `SetNode`
- `GetNode`
- `PreviewImage`
- `ImageConcanate`
- `ImageFromBatch+`
- `PreviewImage`
- `GetNode`
- `Reroute`
- `VHS_VideoCombine`
- `easy showAnything`
- `easy imageSize`
- `SetNode`
- `CR String To Number`
- `GetImageSizeAndCount`
- `Reroute`
- `Reroute`
- `GetImageSizeAndCount`
- `GetNode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `OnnxDetectionModelLoader`
- `WanVideoUni3C_ControlnetLoader`
- `DWPreprocessor`
- `NLFPredict`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `easy showAnything`
- `WanVideoTorchCompileSettings`
- `SimpleMath+`
- `SimpleMath+`
- `PoseDetectionVitPoseToDWPose`
- `easy int`
- `easy int`
- `WanVideoAddSCAILReferenceEmbeds`
- `GetImageSizeAndCount`
- `PreviewImage`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `VHS_VideoCombine`
- `DownloadAndLoadNLFModel`
- `GetImageSizeAndCount`
- `Reroute`
- `GetNode`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `GetNode`
- `SetNode`
- `TextSplitByDelimiter`
- `easy showAnything`
- `easy lengthAnything`
- `GODMT_ListToBatch`
- `FL_VideoCadence`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `AnyBatchSliceNode`
- `easy showAnything`
- `SetNode`
- `easy showAnything`
- `Text List to Text`
- `ImageFromBatch+`
- `Int`
- `easy batchAnything`
- `VAEDecode` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `CLIPTextEncode` ★核心
- `easy mathInt`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `RH_Captioner`
- `WanVideoTextEncode`
- `ShowText|pysssss`
- `RH_Captioner`
- `ShowText|pysssss`
- `FloatConstant`
- `GetNode`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `GetNode`
- `GetNode`
- `WanVideoSchedulerv2`
- `GetImageSizeAndCount`
- `WanVideoSamplerv2` ★核心
- `SetNode`
- `GetNode`
- `SetNode`
- `MathExpression|pysssss`
- `Float`
- `VHS_VideoInfoLoaded`
- `GetImageSizeAndCount`
- `SegmentFrameAdjuster`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Flux2Scheduler`
- `WanVideoBlockSwap`
- `GetNode`
- `CM_IntToBool`
- `easy showAnything`
- `CR Float To Integer`
- `CM_IntUnaryOperation`
- `CM_BoolToInt`
- `WanVideoContextOptions`
- `WanVideoSamplerExtraArgs` ★核心
- `easy anythingInversedSwitch`
- `ImageFromBatch+`
- `ImageFromBatch`
- `WanVideoDecode`
- `MemoryCleaner`
- `ImageToDevice+`
- `GetImageSizeAndCount`
- `easy anythingIndexSwitch`
- `VHS_LoadVideo`
- `PrimitiveFloat`
- `WanVideoModelLoader`
- `ConvertOpenPoseKeypointsToDWPose`
- `MemoryCleaner`
- `MemoryCleaner`
- `ImpactFloat`
- `easy int`
- `PrimitiveBoolean`
- `Note`
- `Note`
- `Switch any [Crystools]`
- `RenderNLFPoses`
- `PoseDetectionVitPoseToDWPose`
- `Switch any [Crystools]`
- `PrimitiveBoolean`
- `easy forLoopEnd`
- `easy forLoopStart`
- `GetImageSizeAndCount`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `easy saveText`

## 关键参数

- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`
- `seed` = `disable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`

## 知识

覆盖率 **67%**（149/223）

**有卡**：`ImageFromBatch`、`GetImageSizeAndCount`、`CreateVideo`、`ImpactInt`、`CLIPLoader`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageScaleByAspectRatio V2`、`AILab_MiniCPM_4_V`、`easy promptReplace`、`easy seed`、`EmptyLatentImage`、`VAELoader`、`AIO_Preprocessor`、`ModelPatchLoader`、`easy positive`、`Florence2ModelLoader`、`Florence2Run`、`ConditioningZeroOut`、`KSamplerAdvanced`、`INTConstant`、`ZImageFunControlnet`、`UNETLoader`、`KSamplerSelect`、`CFGGuider`、`CLIPTextEncode`、`ReferenceLatent`、`VAEEncode`、`EmptyFlux2LatentImage`、`RandomNoise`、`StringFunction|pysssss`、`MemoryCleaner`、`SamplerCustomAdvanced`、`VAEDecode`、`ImageConcanate`、`ImageFromBatch+`、`VHS_VideoCombine`、`easy imageSize`、`CR String To Number`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`WanVideoUni3C_ControlnetLoader`、`DWPreprocessor`、`NLFPredict`、`CLIPVisionLoader`、`WanVideoEmptyEmbeds`、`WanVideoTorchCompileSettings`、`SimpleMath+`、`PoseDetectionVitPoseToDWPose`、`easy int`、`WanVideoAddSCAILReferenceEmbeds`、`ImageConcatMulti`、`DownloadAndLoadNLFModel`、`ImageResizeKJv2`、`TextSplitByDelimiter`、`easy lengthAnything`、`GODMT_ListToBatch`、`FL_VideoCadence`、`AnyBatchSliceNode`、`Text List to Text`、`Int`、`easy batchAnything`、`easy mathInt`、`RH_Captioner`、`WanVideoTextEncode`、`FloatConstant`、`WanVideoAddSCAILPoseEmbeds`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`WanVideoSchedulerv2`、`WanVideoSamplerv2`、`MathExpression|pysssss`、`Float`、`SegmentFrameAdjuster`、`Flux2Scheduler`、`WanVideoBlockSwap`、`CM_IntToBool`、`CR Float To Integer`、`CM_IntUnaryOperation`、`CM_BoolToInt`、`WanVideoContextOptions`、`WanVideoSamplerExtraArgs`、`easy anythingInversedSwitch`、`WanVideoDecode`、`ImageToDevice+`、`easy anythingIndexSwitch`、`VHS_LoadVideo`、`WanVideoModelLoader`、`ConvertOpenPoseKeypointsToDWPose`、`ImpactFloat`、`PrimitiveBoolean`、`Switch any [Crystools]`、`RenderNLFPoses`、`easy forLoopEnd`、`easy forLoopStart`、`SaveImage`、`easy saveText`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LayerUtility: ImageScaleByAspectRatio V2
