---
key: 数字人/数字人/视频-动作迁移单人-wan2.1-SCAIL-KJ_2011817884372180993.json
name: 视频-动作迁移单人-wan2.1-SCAIL-KJ_2011817884372180993
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/视频-动作迁移单人-wan2.1-SCAIL-KJ_2011817884372180993.json
hash: feebe889bf691ac1
coverage: 0.692308
learned_at: 2026-10-26 02:04:44
nodes: [WanVideoSetBlockSwap, Note, WanVideoSetLoRAs, WanVideoAddSCAILPoseEmbeds, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoClipVisionEncode, OnnxDetectionModelLoader, WanVideoUni3C_ControlnetLoader, WanVideoTextEncode, WanVideoSamplerv2, DWPreprocessor, VHS_VideoInfoLoaded, SetNode, easy showAnything, GetImageSizeAndCount, SetNode, easy seed, SetNode, SetNode, GetImageSizeAndCount, CM_IntToFloat, INTConstant, PreviewImage, SetNode, Florence2Run, PreviewImage, ShowText|pysssss, SetNode, ImageFromBatch, Florence2ModelLoader, SetNode, SetNode, GetImageSizeAndCount, NLFPredict, GetNode, Reroute, WanVideoEncode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, FloatConstant, CLIPVisionLoader, ImageConcatMulti, WanVideoSchedulerv2, WanVideoEmptyEmbeds, GetNode, WanVideoContextOptions, WanVideoBlockSwap, GetNode, GetNode, easy showAnything, WanVideoTorchCompileSettings, WanVideoModelLoader, SimpleMath+, SimpleMath+, PoseDetectionVitPoseToDWPose, easy int, easy int, WanVideoAddSCAILReferenceEmbeds, ImageFromBatch+, GetImageSizeAndCount, ImageResizeKJv2, PreviewImage, GetImageSizeAndCount, ImageResizeKJv2, GetNode, LayerUtility: ImageScaleByAspectRatio V2, easy int, ConvertOpenPoseKeypointsToDWPose, GetImageSizeAndCount, GetNode, GetImageSizeAndCount, RenderNLFPoses, VHS_VideoCombine, GetNode, GetImageSizeAndCount, GetImageSizeAndCount, SetNode, VHS_LoadVideo, PoseDetectionVitPoseToDWPose, LoadImage, GetNode, PreviewImage, VHS_VideoCombine, ImageFromBatch, easy anythingIndexSwitch, easy int, ImageConcatMulti, GetImageSizeAndCount, GetImageSizeAndCount, easy int, WanVideoSamplerExtraArgs, VHS_VideoCombine, MathExpression|pysssss, ImageFromBatch, easy positive, WanVideoUni3C_embeds, WanVideoDecode, DownloadAndLoadNLFModel]
patterns: []
missing: []
---

# 数字人/数字人/视频-动作迁移单人-wan2.1-SCAIL-KJ_2011817884372180993.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/视频-动作迁移单人-wan2.1-SCAIL-KJ_2011817884372180993.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（104 个）：
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
- `VHS_VideoInfoLoaded`
- `SetNode`
- `easy showAnything`
- `GetImageSizeAndCount`
- `SetNode`
- `easy seed`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `CM_IntToFloat`
- `INTConstant`
- `PreviewImage`
- `SetNode`
- `Florence2Run`
- `PreviewImage`
- `ShowText|pysssss`
- `SetNode`
- `ImageFromBatch`
- `Florence2ModelLoader`
- `SetNode`
- `SetNode`
- `GetImageSizeAndCount`
- `NLFPredict`
- `GetNode`
- `Reroute`
- `WanVideoEncode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `FloatConstant`
- `CLIPVisionLoader`
- `ImageConcatMulti`
- `WanVideoSchedulerv2`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `SimpleMath+`
- `SimpleMath+`
- `PoseDetectionVitPoseToDWPose`
- `easy int`
- `easy int`
- `WanVideoAddSCAILReferenceEmbeds`
- `ImageFromBatch+`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `PreviewImage`
- `GetImageSizeAndCount`
- `ImageResizeKJv2`
- `GetNode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy int`
- `ConvertOpenPoseKeypointsToDWPose`
- `GetImageSizeAndCount`
- `GetNode`
- `GetImageSizeAndCount`
- `RenderNLFPoses`
- `VHS_VideoCombine`
- `GetNode`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `SetNode`
- `VHS_LoadVideo`
- `PoseDetectionVitPoseToDWPose`
- `LoadImage`
- `GetNode`
- `PreviewImage`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `easy anythingIndexSwitch`
- `easy int`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `GetImageSizeAndCount`
- `easy int`
- `WanVideoSamplerExtraArgs` ★核心
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `ImageFromBatch`
- `easy positive`
- `WanVideoUni3C_embeds`
- `WanVideoDecode`
- `DownloadAndLoadNLFModel`

## 知识

覆盖率 **69%**（72/104）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoAddSCAILPoseEmbeds`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`WanVideoUni3C_ControlnetLoader`、`WanVideoTextEncode`、`WanVideoSamplerv2`、`DWPreprocessor`、`VHS_VideoInfoLoaded`、`GetImageSizeAndCount`、`easy seed`、`CM_IntToFloat`、`INTConstant`、`Florence2Run`、`ImageFromBatch`、`Florence2ModelLoader`、`NLFPredict`、`WanVideoEncode`、`FloatConstant`、`CLIPVisionLoader`、`ImageConcatMulti`、`WanVideoSchedulerv2`、`WanVideoEmptyEmbeds`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`SimpleMath+`、`PoseDetectionVitPoseToDWPose`、`easy int`、`WanVideoAddSCAILReferenceEmbeds`、`ImageFromBatch+`、`ImageResizeKJv2`、`LayerUtility: ImageScaleByAspectRatio V2`、`ConvertOpenPoseKeypointsToDWPose`、`RenderNLFPoses`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`、`easy anythingIndexSwitch`、`WanVideoSamplerExtraArgs`、`MathExpression|pysssss`、`easy positive`、`WanVideoUni3C_embeds`、`WanVideoDecode`、`DownloadAndLoadNLFModel`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、ConvertOpenPoseKeypointsToDWPose、WanVideoSamplerv2、WanVideoSamplerExtraArgs、easy seed、LoadWanVideoT5TextEncoder
