---
key: 平台全量/视频-视频生视频动作参考图(分割)-wan2.1-SCAIL-KJ_2019670989998657537.json
name: 视频-视频生视频动作参考图(分割)-wan2.1-SCAIL-KJ_2019670989998657537
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-视频生视频动作参考图(分割)-wan2.1-SCAIL-KJ_2019670989998657537.json
hash: ccde3f059ee799e3
coverage: 0.647059
learned_at: 2026-11-14 02:34:38
nodes: [PreviewImage, ImageFromBatch, SetNode, GetImageSizeAndCount, CreateVideo, VHS_VideoInfoLoaded, SetNode, LayerUtility: ImageScaleByAspectRatio V2, GetImageSizeAndCount, ShowText|pysssss, AILab_MiniCPM_4_V, ShowText|pysssss, GetNode, easy promptReplace, easy seed, easy positive, Florence2ModelLoader, Florence2Run, easy showAnything, GetImageSizeAndCount, GetNode, KSamplerSelect, CFGGuider, CLIPTextEncode, VAELoader, UNETLoader, CLIPTextEncode, ReferenceLatent, CLIPLoader, Reroute, VAEEncode, Reroute, Reroute, ReferenceLatent, RandomNoise, GetNode, StringFunction|pysssss, GetImageSizeAndCount, GetNode, MemoryCleaner, SamplerCustomAdvanced, Reroute, Reroute, PreviewImage, SetNode, GetNode, ImageConcanate, ImageFromBatch+, PreviewImage, GetNode, Reroute, VHS_VideoCombine, easy showAnything, easy imageSize, SetNode, CR String To Number, GetImageSizeAndCount, Reroute, Reroute, GetImageSizeAndCount, GetNode, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, PreviewImage, VHS_VideoCombine, WanVideoSetBlockSwap, Note, WanVideoSetLoRAs, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoClipVisionEncode, OnnxDetectionModelLoader, WanVideoUni3C_ControlnetLoader, DWPreprocessor, NLFPredict, SetNode, SetNode, SetNode, GetNode, CLIPVisionLoader, WanVideoEmptyEmbeds, GetNode, easy showAnything, WanVideoTorchCompileSettings, SimpleMath+, SimpleMath+, PoseDetectionVitPoseToDWPose, easy int, easy int, WanVideoAddSCAILReferenceEmbeds, RenderNLFPoses, GetImageSizeAndCount, PreviewImage, GetImageSizeAndCount, SetNode, GetImageSizeAndCount, SetNode, VHS_VideoCombine, DownloadAndLoadNLFModel, Reroute, GetNode, GetImageSizeAndCount, ImageResizeKJv2, VHS_VideoCombine, ImageFromBatch, GetNode, SetNode, TextSplitByDelimiter, easy showAnything, easy lengthAnything, GODMT_ListToBatch, FL_VideoCadence, easy showAnything, easy showAnything, easy showAnything, easy showAnything, AnyBatchSliceNode, easy showAnything, SetNode, easy showAnything, Text List to Text, ImageFromBatch+, Int, easy batchAnything, VAEDecode, VHS_VideoCombine, easy mathInt, easy showAnything, GetNode, GetNode, RH_Captioner, WanVideoTextEncode, ShowText|pysssss, FloatConstant, GetNode, WanVideoAddSCAILPoseEmbeds, WanVideoEncode, WanVideoUni3C_embeds, GetNode, GetNode, WanVideoSchedulerv2, WanVideoSamplerv2, ImpactFloat, SetNode, GetNode, SetNode, MathExpression|pysssss, Float, VHS_VideoInfoLoaded, GetImageSizeAndCount, SegmentFrameAdjuster, Flux2Scheduler, WanVideoBlockSwap, GetNode, CM_IntToBool, easy showAnything, CR Float To Integer, CM_IntUnaryOperation, MemoryCleaner, CM_BoolToInt, WanVideoContextOptions, WanVideoSamplerExtraArgs, WanVideoDecode, ImageToDevice+, GetImageSizeAndCount, PreviewImage, easy imageRemBg, EmptyFlux2LatentImage, GetImageSizeAndCount, SetNode, GetNode, Reroute, StringFunction|pysssss, GetNode, AutoCropFaces, LayerUtility: ImageScaleByAspectRatio V2, ImageFromBatch+, GetNode, Switch any [Crystools], GetImageSizeAndCount, ImageFromBatch, GetImageSizeAndCount, ImageConcatMulti, MemoryCleaner, VHS_LoadVideo, LoadImage, easy int, PrimitiveFloat, WanVideoModelLoader, Note, PoseDetectionVitPoseToDWPose, ConvertOpenPoseKeypointsToDWPose, PrimitiveBoolean, Switch any [Crystools], easy forLoopEnd, easy forLoopStart, GetImageSizeAndCount, PreviewImage, SaveImage, SetNode, easy saveText, LayerUtility: ImageScaleByAspectRatio V2]
patterns: []
missing: []
---

# 平台全量/视频-视频生视频动作参考图(分割)-wan2.1-SCAIL-KJ_2019670989998657537.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-视频生视频动作参考图(分割)-wan2.1-SCAIL-KJ_2019670989998657537.json`

## 结构

**生成流程**：Model → Encode → Condition → Sampling → Decode → Process → Output → Other

**节点**（204 个）：
- `PreviewImage`
- `ImageFromBatch`
- `SetNode`
- `GetImageSizeAndCount`
- `CreateVideo`
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
- `easy positive`
- `Florence2ModelLoader`
- `Florence2Run`
- `easy showAnything`
- `GetImageSizeAndCount`
- `GetNode`
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
- `Reroute`
- `Reroute`
- `ReferenceLatent`
- `RandomNoise`
- `GetNode`
- `StringFunction|pysssss`
- `GetImageSizeAndCount`
- `GetNode`
- `MemoryCleaner`
- `SamplerCustomAdvanced` ★核心
- `Reroute`
- `Reroute`
- `PreviewImage`
- `SetNode`
- `GetNode`
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
- `RenderNLFPoses`
- `GetImageSizeAndCount`
- `PreviewImage`
- `GetImageSizeAndCount`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `VHS_VideoCombine`
- `DownloadAndLoadNLFModel`
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
- `easy mathInt`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `RH_Captioner`
- `WanVideoTextEncode`
- `ShowText|pysssss`
- `FloatConstant`
- `GetNode`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `GetNode`
- `GetNode`
- `WanVideoSchedulerv2`
- `WanVideoSamplerv2` ★核心
- `ImpactFloat`
- `SetNode`
- `GetNode`
- `SetNode`
- `MathExpression|pysssss`
- `Float`
- `VHS_VideoInfoLoaded`
- `GetImageSizeAndCount`
- `SegmentFrameAdjuster`
- `Flux2Scheduler`
- `WanVideoBlockSwap`
- `GetNode`
- `CM_IntToBool`
- `easy showAnything`
- `CR Float To Integer`
- `CM_IntUnaryOperation`
- `MemoryCleaner`
- `CM_BoolToInt`
- `WanVideoContextOptions`
- `WanVideoSamplerExtraArgs` ★核心
- `WanVideoDecode`
- `ImageToDevice+`
- `GetImageSizeAndCount`
- `PreviewImage`
- `easy imageRemBg`
- `EmptyFlux2LatentImage`
- `GetImageSizeAndCount`
- `SetNode`
- `GetNode`
- `Reroute`
- `StringFunction|pysssss`
- `GetNode`
- `AutoCropFaces`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageFromBatch+`
- `GetNode`
- `Switch any [Crystools]`
- `GetImageSizeAndCount`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `MemoryCleaner`
- `VHS_LoadVideo`
- `LoadImage`
- `easy int`
- `PrimitiveFloat`
- `WanVideoModelLoader`
- `Note`
- `PoseDetectionVitPoseToDWPose`
- `ConvertOpenPoseKeypointsToDWPose`
- `PrimitiveBoolean`
- `Switch any [Crystools]`
- `easy forLoopEnd`
- `easy forLoopStart`
- `GetImageSizeAndCount`
- `PreviewImage`
- `SaveImage`
- `SetNode`
- `easy saveText`
- `LayerUtility: ImageScaleByAspectRatio V2`

## 知识

覆盖率 **65%**（132/204）

**有卡**：`ImageFromBatch`、`GetImageSizeAndCount`、`CreateVideo`、`VHS_VideoInfoLoaded`、`LayerUtility: ImageScaleByAspectRatio V2`、`AILab_MiniCPM_4_V`、`easy promptReplace`、`easy seed`、`easy positive`、`Florence2ModelLoader`、`Florence2Run`、`KSamplerSelect`、`CFGGuider`、`CLIPTextEncode`、`VAELoader`、`UNETLoader`、`ReferenceLatent`、`CLIPLoader`、`VAEEncode`、`RandomNoise`、`StringFunction|pysssss`、`MemoryCleaner`、`SamplerCustomAdvanced`、`ImageConcanate`、`ImageFromBatch+`、`VHS_VideoCombine`、`easy imageSize`、`CR String To Number`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`WanVideoUni3C_ControlnetLoader`、`DWPreprocessor`、`NLFPredict`、`CLIPVisionLoader`、`WanVideoEmptyEmbeds`、`WanVideoTorchCompileSettings`、`SimpleMath+`、`PoseDetectionVitPoseToDWPose`、`easy int`、`WanVideoAddSCAILReferenceEmbeds`、`RenderNLFPoses`、`DownloadAndLoadNLFModel`、`ImageResizeKJv2`、`TextSplitByDelimiter`、`easy lengthAnything`、`GODMT_ListToBatch`、`FL_VideoCadence`、`AnyBatchSliceNode`、`Text List to Text`、`Int`、`easy batchAnything`、`VAEDecode`、`easy mathInt`、`RH_Captioner`、`WanVideoTextEncode`、`FloatConstant`、`WanVideoAddSCAILPoseEmbeds`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`WanVideoSchedulerv2`、`WanVideoSamplerv2`、`ImpactFloat`、`MathExpression|pysssss`、`Float`、`SegmentFrameAdjuster`、`Flux2Scheduler`、`WanVideoBlockSwap`、`CM_IntToBool`、`CR Float To Integer`、`CM_IntUnaryOperation`、`CM_BoolToInt`、`WanVideoContextOptions`、`WanVideoSamplerExtraArgs`、`WanVideoDecode`、`ImageToDevice+`、`easy imageRemBg`、`EmptyFlux2LatentImage`、`AutoCropFaces`、`Switch any [Crystools]`、`ImageConcatMulti`、`VHS_LoadVideo`、`LoadImage`、`WanVideoModelLoader`、`ConvertOpenPoseKeypointsToDWPose`、`PrimitiveBoolean`、`easy forLoopEnd`、`easy forLoopStart`、`SaveImage`、`easy saveText`

**用到的条目**：VAEDecode、VAELoader、UNETLoader、CLIPLoader、CLIPTextEncode、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、ConvertOpenPoseKeypointsToDWPose
