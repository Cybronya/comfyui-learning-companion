---
key: 视频生成/图生视频/视频-视频生视频(动作)-wan2.1-SCAIL-KJ+_2046415072397893633.json
name: 视频-视频生视频(动作)-wan2.1-SCAIL-KJ+_2046415072397893633.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/视频-视频生视频(动作)-wan2.1-SCAIL-KJ+_2046415072397893633.json
hash: 0d3cead7bca404b8
coverage: 0.705882
learned_at: 2026-10-15 22:36:57
nodes: [easy showAnything, easy imageSize, GetImageSizeAndCount, GetNode, GetNode, GetImageSizeAndCount, SetNode, GetNode, VHS_VideoCombine, GetImageSizeAndCount, CreateVideo, ImpactInt, ImpactInt, CLIPLoader, SaveImage, ImpactFloat, SetNode, MemoryCleaner, VAEDecode, PreviewImage, GetNode, SetNode, ImageResizeKJv2, StringFunction|pysssss, LayerUtility: ImageScaleByAspectRatio V2, GetNode, GetNode, SetNode, easy showAnything, GetNode, GetImageSizeAndCount, ShowText|pysssss, GetImageSizeAndCount, AILab_MiniCPM_4_V, MemoryCleaner, MemoryCleaner, ShowText|pysssss, easy saveText, SetNode, ShowText|pysssss, GetNode, easy promptReplace, easy int, WanVideoSetBlockSwap, Note, WanVideoSetLoRAs, WanVideoAddSCAILPoseEmbeds, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoClipVisionEncode, OnnxDetectionModelLoader, WanVideoUni3C_ControlnetLoader, WanVideoTextEncode, WanVideoSamplerv2, DWPreprocessor, NLFPredict, DownloadAndLoadNLFModel, WanVideoEncode, SetNode, SetNode, SetNode, GetNode, GetNode, FloatConstant, CLIPVisionLoader, WanVideoSchedulerv2, WanVideoEmptyEmbeds, GetNode, WanVideoContextOptions, easy showAnything, WanVideoTorchCompileSettings, SimpleMath+, SimpleMath+, PoseDetectionVitPoseToDWPose, easy int, easy int, WanVideoAddSCAILReferenceEmbeds, ConvertOpenPoseKeypointsToDWPose, GetImageSizeAndCount, RenderNLFPoses, GetImageSizeAndCount, GetImageSizeAndCount, PoseDetectionVitPoseToDWPose, GetNode, PreviewImage, ImageFromBatch, ImageConcatMulti, WanVideoSamplerExtraArgs, WanVideoUni3C_embeds, WanVideoDecode, VHS_VideoInfoLoaded, GetNode, GetNode, ImageConcatMulti, GetImageSizeAndCount, SetNode, GetImageSizeAndCount, SetNode, GetNode, ImageFromBatch, GetImageSizeAndCount, GetImageSizeAndCount, SetNode, Reroute, VHS_VideoCombine, GetNode, VHS_VideoCombine, easy seed, PrimitiveFloat, VAELoader, AIO_Preprocessor, ModelPatchLoader, GetImageSizeAndCount, PreviewImage, ImageFromBatch+, ImageFromBatch+, Florence2ModelLoader, Florence2Run, INTConstant, KSamplerAdvanced, ConditioningZeroOut, CLIPTextEncode, GetNode, KSamplerAdvanced, UNETLoader, EmptyLatentImage, ZImageFunControlnet, INTConstant, LayerUtility: ImageScaleByAspectRatio V2, MathExpression|pysssss, WanVideoModelLoader, WanVideoBlockSwap, VHS_LoadVideo, RH_Captioner, easy positive]
patterns: []
missing: []
parameters: {"batch_size": 1, "cfg": 10, "denoise": "simple", "height": 1080, "sampler_name": 1, "scheduler": "euler", "seed": "enable", "steps": "randomize", "width": 1920}
---

# 视频生成/图生视频/视频-视频生视频(动作)-wan2.1-SCAIL-KJ+_2046415072397893633.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2046415072397893633.json`

## 结构

**生成流程**：Model → Condition → Latent → Control → Sampling → Decode → Process → Output → Other

**节点**（136 个）：
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
- `VAEDecode` ★核心
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
- `ConvertOpenPoseKeypointsToDWPose`
- `GetImageSizeAndCount`
- `RenderNLFPoses`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `PoseDetectionVitPoseToDWPose`
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
- `PrimitiveFloat`
- `VAELoader`
- `AIO_Preprocessor`
- `ModelPatchLoader`
- `GetImageSizeAndCount`
- `PreviewImage`
- `ImageFromBatch+`
- `ImageFromBatch+`
- `Florence2ModelLoader`
- `Florence2Run`
- `INTConstant`
- `KSamplerAdvanced` ★核心
- `ConditioningZeroOut`
- `CLIPTextEncode` ★核心
- `GetNode`
- `KSamplerAdvanced` ★核心
- `UNETLoader` ★核心
- `EmptyLatentImage` ★核心
- `ZImageFunControlnet`
- `INTConstant`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `MathExpression|pysssss`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `RH_Captioner`
- `easy positive`

## 关键参数

- `seed` = `enable`
- `steps` = `randomize`
- `cfg` = `10`
- `sampler_name` = `1`
- `scheduler` = `euler`
- `denoise` = `simple`
- `width` = `1920`
- `height` = `1080`
- `batch_size` = `1`

## 知识

覆盖率 **71%**（96/136）

**有卡**：`easy imageSize`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`CreateVideo`、`ImpactInt`、`CLIPLoader`、`SaveImage`、`ImpactFloat`、`MemoryCleaner`、`VAEDecode`、`ImageResizeKJv2`、`StringFunction|pysssss`、`LayerUtility: ImageScaleByAspectRatio V2`、`AILab_MiniCPM_4_V`、`easy saveText`、`easy promptReplace`、`easy int`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoAddSCAILPoseEmbeds`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`WanVideoUni3C_ControlnetLoader`、`WanVideoTextEncode`、`WanVideoSamplerv2`、`DWPreprocessor`、`NLFPredict`、`DownloadAndLoadNLFModel`、`WanVideoEncode`、`FloatConstant`、`CLIPVisionLoader`、`WanVideoSchedulerv2`、`WanVideoEmptyEmbeds`、`WanVideoContextOptions`、`WanVideoTorchCompileSettings`、`SimpleMath+`、`PoseDetectionVitPoseToDWPose`、`WanVideoAddSCAILReferenceEmbeds`、`ConvertOpenPoseKeypointsToDWPose`、`RenderNLFPoses`、`ImageFromBatch`、`ImageConcatMulti`、`WanVideoSamplerExtraArgs`、`WanVideoUni3C_embeds`、`WanVideoDecode`、`VHS_VideoInfoLoaded`、`easy seed`、`VAELoader`、`AIO_Preprocessor`、`ModelPatchLoader`、`ImageFromBatch+`、`Florence2ModelLoader`、`Florence2Run`、`INTConstant`、`KSamplerAdvanced`、`ConditioningZeroOut`、`CLIPTextEncode`、`UNETLoader`、`EmptyLatentImage`、`ZImageFunControlnet`、`MathExpression|pysssss`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`RH_Captioner`、`easy positive`

**用到的条目**：VAEDecode、VAELoader、CLIPTextEncode、CLIPLoader、ConditioningZeroOut、EmptyLatentImage、UNETLoader、LayerUtility: ImageScaleByAspectRatio V2
