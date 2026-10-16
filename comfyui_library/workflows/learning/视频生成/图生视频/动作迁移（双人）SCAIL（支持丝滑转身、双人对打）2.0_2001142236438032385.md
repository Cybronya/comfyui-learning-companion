---
key: 视频生成/图生视频/动作迁移（双人）SCAIL（支持丝滑转身、双人对打）2.0_2001142236438032385.json
name: 动作迁移（双人）SCAIL（支持丝滑转身、双人对打）2.0_2001142236438032385.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2001142236438032385.json
hash: 94adaddb74f76a1d
coverage: 0.675676
learned_at: 2026-10-15 22:33:44
nodes: [SetNode, WanVideoSetBlockSwap, SetNode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoTorchCompileSettings, SetNode, SetNode, GetNode, GetNode, Reroute, Reroute, ImageResizeKJv2, WanVideoModelLoader, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoEncode, WanVideoVAELoader, NLFPredict, INTConstant, INTConstant, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, PoseDetectionVitPoseToDWPose, WanVideoUni3C_ControlnetLoader, WanVideoUni3C_embeds, SetNode, WanVideoTextEncode, WanVideoBlockSwap, VHS_LoadVideo, SetNode, CLIPVisionLoader, GetNode, GetNode, WanVideoEmptyEmbeds, WanVideoAddSCAILReferenceEmbeds, WanVideoAddSCAILPoseEmbeds, WanVideoSchedulerv2, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSamplerv2, WanVideoSamplerExtraArgs, FloatConstant, WanVideoClipVisionEncode, ImageConcatMulti, GetImageSizeAndCount, ImageConcatMulti, VHS_VideoCombine, VHS_VideoCombine, LoadImage, CR Text, VHS_VideoCombine, RenderNLFPoses, DownloadAndLoadNLFModel, Note, LayerUtility: ImageScaleByAspectRatio V2, ImageResizeKJv2, GetNode, SimpleMath+, GetNode, SimpleMath+, Int, MathExpression|pysssss, Note, Note, Int, Int, WanVideoDecode, WanVideoContextOptions, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/动作迁移（双人）SCAIL（支持丝滑转身、双人对打）2.0_2001142236438032385.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2001142236438032385.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（74 个）：
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `Reroute`
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEncode`
- `WanVideoVAELoader`
- `NLFPredict`
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
- `VHS_LoadVideo`
- `SetNode`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `WanVideoEmptyEmbeds`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoAddSCAILPoseEmbeds`
- `WanVideoSchedulerv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `WanVideoSamplerExtraArgs` ★核心
- `FloatConstant`
- `WanVideoClipVisionEncode`
- `ImageConcatMulti`
- `GetImageSizeAndCount`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `CR Text`
- `VHS_VideoCombine`
- `RenderNLFPoses`
- `DownloadAndLoadNLFModel`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageResizeKJv2`
- `GetNode`
- `SimpleMath+`
- `GetNode`
- `SimpleMath+`
- `Int`
- `MathExpression|pysssss`
- `Note`
- `Note`
- `Int`
- `Int`
- `WanVideoDecode`
- `WanVideoContextOptions`
- `LoadImage`

## 知识

覆盖率 **68%**（50/74）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoEncode`、`WanVideoVAELoader`、`NLFPredict`、`INTConstant`、`OnnxDetectionModelLoader`、`PoseDetectionVitPoseToDWPose`、`WanVideoUni3C_ControlnetLoader`、`WanVideoUni3C_embeds`、`WanVideoTextEncode`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`CLIPVisionLoader`、`WanVideoEmptyEmbeds`、`WanVideoAddSCAILReferenceEmbeds`、`WanVideoAddSCAILPoseEmbeds`、`WanVideoSchedulerv2`、`WanVideoSamplerv2`、`WanVideoSamplerExtraArgs`、`FloatConstant`、`WanVideoClipVisionEncode`、`ImageConcatMulti`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`LoadImage`、`CR Text`、`RenderNLFPoses`、`DownloadAndLoadNLFModel`、`LayerUtility: ImageScaleByAspectRatio V2`、`SimpleMath+`、`Int`、`MathExpression|pysssss`、`WanVideoDecode`、`WanVideoContextOptions`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSamplerv2、WanVideoSamplerExtraArgs、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
