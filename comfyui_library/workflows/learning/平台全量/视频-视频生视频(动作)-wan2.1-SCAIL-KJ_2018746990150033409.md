---
key: 平台全量/视频-视频生视频(动作)-wan2.1-SCAIL-KJ_2018746990150033409.json
name: 视频-视频生视频(动作)-wan2.1-SCAIL-KJ_2018746990150033409
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/视频-视频生视频(动作)-wan2.1-SCAIL-KJ_2018746990150033409.json
hash: 3aa105e31372ffb7
coverage: 0.705036
learned_at: 2026-11-14 02:34:33
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetNode, GetNode, GetImageSizeAndCount, SetNode, GetNode, VHS_VideoCombine, GetImageSizeAndCount, CreateVideo, ImpactInt, ImpactInt, CLIPLoader, SaveImage, ImpactFloat, SetNode, MemoryCleaner, PreviewImage, GetNode, SetNode, ImageResizeKJv2, StringFunction|pysssss, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, SetNode, easy showAnything, GetNode, GetImageSizeAndCount, ShowText|pysssss, GetImageSizeAndCount, AILab_MiniCPM_4_V, MemoryCleaner, MemoryCleaner, ShowText|pysssss, easy saveText, SetNode, ShowText|pysssss, GetNode, easy promptReplace, easy int, WanVideoSetBlockSwap, Note, WanVideoSetLoRAs, WanVideoAddSCAILPoseEmbeds, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoClipVisionEncode, OnnxDetectionModelLoader, WanVideoUni3C_ControlnetLoader, WanVideoTextEncode, WanVideoSamplerv2, DWPreprocessor, NLFPredict, DownloadAndLoadNLFModel, WanVideoEncode, SetNode, SetNode, SetNode, GetNode, GetNode, FloatConstant, CLIPVisionLoader, WanVideoSchedulerv2, WanVideoEmptyEmbeds, GetNode, WanVideoContextOptions, easy showAnything, WanVideoTorchCompileSettings, SimpleMath+, SimpleMath+, PoseDetectionVitPoseToDWPose, easy int, easy int, WanVideoAddSCAILReferenceEmbeds, GetImageSizeAndCount, RenderNLFPoses, GetImageSizeAndCount, GetImageSizeAndCount, GetNode, PreviewImage, ImageFromBatch, ImageConcatMulti, WanVideoSamplerExtraArgs, WanVideoUni3C_embeds, WanVideoDecode, VHS_VideoInfoLoaded, GetNode, GetNode, ImageConcatMulti, GetImageSizeAndCount, SetNode, GetImageSizeAndCount, SetNode, GetNode, ImageFromBatch, GetImageSizeAndCount, GetImageSizeAndCount, SetNode, Reroute, VHS_VideoCombine, GetNode, VHS_VideoCombine, easy seed, VAELoader, AIO_Preprocessor, GetImageSizeAndCount, PreviewImage, ImageFromBatch+, ImageFromBatch+, Florence2ModelLoader, Florence2Run, RH_Captioner, easy positive, PrimitiveFloat, ModelPatchLoader, INTConstant, ZImageFunControlnet, EmptyLatentImage, ConditioningZeroOut, CLIPTextEncode, GetNode, INTConstant, UNETLoader, VAEDecode, KSamplerAdvanced, KSamplerAdvanced, VHS_LoadVideo, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, WanVideoBlockSwap, WanVideoModelLoader, Note, PoseDetectionVitPoseToDWPose, ConvertOpenPoseKeypointsToDWPose, Switch any [Crystools], PrimitiveBoolean]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 1080, "sampler_name": 1, "scheduler": "euler", "seed": "disable", "steps": "randomize", "width": 1920}
---

# 平台全量/视频-视频生视频(动作)-wan2.1-SCAIL-KJ_2018746990150033409.json

> 来源文件 `comfyui_library/workflows/平台全量/视频-视频生视频(动作)-wan2.1-SCAIL-KJ_2018746990150033409.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（139 个）：
- `easy showAnything`
- `easy imageSize`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `CreateVideo`
- `ImpactInt`
- `ImpactInt`
- `CLIPLoader`
- `SaveImage`
- `ImpactFloat`
- `SetNode`
- `MemoryCleaner`
- `PreviewImage`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `StringFunction|pysssss`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy showAnything`
- `GetNode`
- `GetImageSizeAndCount`
- `ShowText|pysssss`
- `GetImageSizeAndCount`
- `AILab_MiniCPM_4_V`
- `MemoryCleaner`
- `MemoryCleaner`
- `ShowText|pysssss`
- `easy saveText`
- `SetNode`
- `ShowText|pysssss`
- `GetNode`
- `easy promptReplace`
- `easy int`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoSetLoRAs`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoClipVisionEncode`
- `OnnxDetectionModelLoader`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoTextEncode`
- `WanVideoSamplerv2` ★核心
- `DWPreprocessor`
- `NLFPredict`
- `DownloadAndLoadNLFModel`
- `WanVideoEncode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `FloatConstant`
- `CLIPVisionLoader`
- `WanVideoSchedulerv2`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `WanVideoContextOptions`
- `easy showAnything`
- `WanVideoTorchCompileSettings`
- `SimpleMath+`
- `SimpleMath+`
- `PoseDetectionVitPoseToDWPose`
- `easy int`
- `easy int`
- `WanVideoAddSCAILReferenceEmbeds`
- `GetImageSizeAndCount`
- `RenderNLFPoses`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `GetNode`
- `PreviewImage`
- `ImageFromBatch`
- `ImageConcatMulti`
- `WanVideoSamplerExtraArgs` ★核心
- `WanVideoUni3C_embeds`
- `WanVideoDecode`
- `VHS_VideoInfoLoaded`
- `GetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `SetNode`
- `GetImageSizeAndCount`
- `SetNode`
- `GetNode`
- `ImageFromBatch`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `SetNode`
- `Reroute`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `easy seed`
- `VAELoader`
- `AIO_Preprocessor`
- `GetImageSizeAndCount`
- `PreviewImage`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `Florence2ModelLoader`
- `Florence2Run`
- `RH_Captioner`
- `easy positive`
- `PrimitiveFloat`
- `ModelPatchLoader`
- `INTConstant`
- `ZImageFunControlnet`
- `EmptyLatentImage` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `GetNode`
- `INTConstant`
- `UNETLoader` ★核心
- `VAEDecode` ★核心
- `KSamplerAdvanced` ★核心
- `KSamplerAdvanced` ★核心
- `VHS_LoadVideo`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `Note`
- `PoseDetectionVitPoseToDWPose`
- `ConvertOpenPoseKeypointsToDWPose`
- `Switch any [Crystools]`
- `PrimitiveBoolean`

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

覆盖率 **71%**（98/139）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`CreateVideo`、`ImpactInt`、`CLIPLoader`、`SaveImage`、`ImpactFloat`、`MemoryCleaner`、`ImageResizeKJv2`、`StringFunction|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`AILab_MiniCPM_4_V`、`easy saveText`、`easy promptReplace`、`easy int`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoAddSCAILPoseEmbeds`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`WanVideoUni3C_ControlnetLoader`、`WanVideoTextEncode`、`WanVideoSamplerv2`、`DWPreprocessor`、`NLFPredict`、`DownloadAndLoadNLFModel`、`WanVideoEncode`、`FloatConstant`、`CLIPVisionLoader`、`WanVideoSchedulerv2`、`WanVideoEmptyEmbeds`、`WanVideoContextOptions`、`WanVideoTorchCompileSettings`、`SimpleMath+`、`PoseDetectionVitPoseToDWPose`、`WanVideoAddSCAILReferenceEmbeds`、`RenderNLFPoses`、`ImageFromBatch`、`ImageConcatMulti`、`WanVideoSamplerExtraArgs`、`WanVideoUni3C_embeds`、`WanVideoDecode`、`VHS_VideoInfoLoaded`、`easy seed`、`VAELoader`、`AIO_Preprocessor`、`ImageFromBatch+`、`Florence2ModelLoader`、`Florence2Run`、`RH_Captioner`、`easy positive`、`ModelPatchLoader`、`INTConstant`、`ZImageFunControlnet`、`EmptyLatentImage`、`ConditioningZeroOut`、`CLIPTextEncode`、`UNETLoader`、`VAEDecode`、`KSamplerAdvanced`、`VHS_LoadVideo`、`MathExpression|pysssss`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`ConvertOpenPoseKeypointsToDWPose`、`Switch any [Crystools]`、`PrimitiveBoolean`

**用到的条目**：VAEDecode、VAELoader、CLIPLoader、CLIPTextEncode、ConditioningZeroOut、EmptyLatentImage、LayerUtility: ImageScaleByAspectRatio V2、UNETLoader
