---
key: 视频生成/图生视频/动作迁移（单人）SCAIL（支持丝滑转身）2.0_2001144706195222530.json
name: 动作迁移（单人）SCAIL（支持丝滑转身）2.0_2001144706195222530.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/动作迁移（单人）SCAIL（支持丝滑转身）2.0_2001144706195222530.json
hash: 50d1550a29adacda
coverage: 0.671053
learned_at: 2026-10-15 22:33:44
nodes: [SetNode, WanVideoSetBlockSwap, SetNode, SetNode, SetNode, Note, WanVideoSetLoRAs, WanVideoTorchCompileSettings, SetNode, SetNode, WanVideoModelLoader, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoEncode, WanVideoVAELoader, SetNode, INTConstant, INTConstant, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, PoseDetectionVitPoseToDWPose, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, SetNode, WanVideoTextEncode, WanVideoBlockSwap, RenderNLFPoses, LoadImage, ImageResizeKJv2, VHS_VideoCombine, LoadImage, VHS_VideoCombine, DownloadAndLoadNLFModel, NLFPredict, SimpleMath+, SimpleMath+, GetNode, GetNode, ImageResizeKJv2, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, GetNode, GetNode, PreviewImage, WanVideoSamplerExtraArgs, GetNode, GetNode, WanVideoSamplerv2, WanVideoDecode, GetNode, GetImageSizeAndCount, WanVideoClipVisionEncode, CLIPVisionLoader, GetNode, GetNode, WanVideoAddSCAILReferenceEmbeds, WanVideoAddSCAILPoseEmbeds, WanVideoEmptyEmbeds, GetNode, WanVideoSchedulerv2, WanVideoContextOptions, FloatConstant, GetNode, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, Reroute, Reroute, Int, CR Text, MathExpression|pysssss, Note, Int, Int, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移（单人）SCAIL（支持丝滑转身）2.0_2001144706195222530.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001144706195222530.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（76 个）：
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `PoseDetectionVitPoseToDWPose`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoUni3C_embeds`
- `SetNode`
- `WanVideoTextEncode`
- `WanVideoBlockSwap`
- `RenderNLFPoses`
- `LoadImage`
- `ImageResizeKJv2`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_VideoCombine`
- `DownloadAndLoadNLFModel`
- `NLFPredict`
- `SimpleMath+`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `WanVideoSamplerExtraArgs` ★核心
- `GetNode`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `WanVideoDecode`
- `GetNode`
- `GetImageSizeAndCount`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `WanVideoSchedulerv2`
- `WanVideoContextOptions`
- `FloatConstant`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `Reroute`
- `Reroute`
- `Int`
- `CR Text`
- `MathExpression|pysssss`
- `Note`
- `Int`
- `Int`
- `Note`

## 知识

覆盖率 **67%**（51/76）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoEncode`、`WanVideoVAELoader`、`INTConstant`、`OnnxDetectionModelLoader`、`PoseDetectionVitPoseToDWPose`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`RenderNLFPoses`、`LoadImage`、`ImageResizeKJv2`、`VHS_VideoCombine`、`DownloadAndLoadNLFModel`、`NLFPredict`、`SimpleMath+`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`WanVideoSamplerExtraArgs`、`WanVideoSamplerv2`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoAddSCAILReferenceEmbeds`、`WanVideoAddSCAILPoseEmbeds`、`WanVideoEmptyEmbeds`、`WanVideoSchedulerv2`、`WanVideoContextOptions`、`FloatConstant`、`ImageConcatMulti`、`Int`、`CR Text`、`MathExpression|pysssss`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSamplerv2、WanVideoSamplerExtraArgs、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
