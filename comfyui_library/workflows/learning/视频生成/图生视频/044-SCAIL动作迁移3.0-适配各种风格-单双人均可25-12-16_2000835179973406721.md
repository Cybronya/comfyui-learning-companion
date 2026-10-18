---
key: 视频生成/图生视频/044-SCAIL动作迁移3.0-适配各种风格-单双人均可25-12-16_2000835179973406721.json
name: 044-SCAIL动作迁移3.0-适配各种风格-单双人均可25-12-16_2000835179973406721.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/044-SCAIL动作迁移3.0-适配各种风格-单双人均可25-12-16_2000835179973406721.json
hash: 0e5a085c2fabe917
coverage: 0.618421
learned_at: 2026-10-15 22:33:43
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAddSCAILReferenceEmbeds, WanVideoEmptyEmbeds, GetNode, WanVideoDecode, SetNode, WanVideoUni3C_ControlnetLoader, SimpleMath+, SetNode, SetNode, SetNode, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, PoseDetectionVitPoseToDWPose, Mute / Bypass Repeater (rgthree), SetNode, DownloadAndLoadNLFModel, NLFPredict, GetNode, GetNode, Reroute, SetNode, WanVideoSchedulerv2, WanVideoSamplerExtraArgs, GetImageSizeAndCount, GetNode, FloatConstant, WanVideoAddSCAILPoseEmbeds, Reroute, ImageConcatMulti, ImageConcatMulti, SetNode, GetNode, GetNode, VHS_VideoCombine, WanVideoVAELoader, WanVideoContextOptions, CR Text, WanVideoEncode, WanVideoUni3C_embeds, SimpleMath+, GetNode, SimpleMath+, RenderNLFPoses, GetNode, ImageResizeKJv2, ImageResizeKJv2, SetNode, SetNode, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetLoRAs, SetNode, WanVideoBlockSwap, WanVideoSetBlockSwap, GetNode, WanVideoTextEncode, LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, CLIPVisionLoader, WanVideoSamplerv2, SetNode, VHS_VideoCombine, SetNode, VHS_VideoCombine, Fast Bypasser (rgthree), easy int, easy int, VHS_LoadVideo, easy int, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/044-SCAIL动作迁移3.0-适配各种风格-单双人均可25-12-16_2000835179973406721.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2000835179973406721.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（76 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoEmptyEmbeds`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `WanVideoUni3C_ControlnetLoader`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `PoseDetectionVitPoseToDWPose`
- `Mute / Bypass Repeater (rgthree)`
- `SetNode`
- `DownloadAndLoadNLFModel`
- `NLFPredict`
- `GetNode`
- `GetNode`
- `Reroute`
- `SetNode`
- `WanVideoSchedulerv2`
- `WanVideoSamplerExtraArgs` ★核心
- `GetImageSizeAndCount`
- `GetNode`
- `FloatConstant`
- `WanVideoAddSCAILPoseEmbeds`
- `Reroute`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoContextOptions`
- `CR Text`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `SimpleMath+`
- `GetNode`
- `SimpleMath+`
- `RenderNLFPoses`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `GetNode`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `CLIPVisionLoader`
- `WanVideoSamplerv2` ★核心
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `VHS_VideoCombine`
- `Fast Bypasser (rgthree)`
- `easy int`
- `easy int`
- `VHS_LoadVideo`
- `easy int`
- `LoadImage`

## 知识

覆盖率 **62%**（47/76）

**有卡**：`WanVideoAddSCAILReferenceEmbeds`、`WanVideoEmptyEmbeds`、`WanVideoDecode`、`WanVideoUni3C_ControlnetLoader`、`SimpleMath+`、`OnnxDetectionModelLoader`、`PoseDetectionVitPoseToDWPose`、`Mute / Bypass Repeater (rgthree)`、`DownloadAndLoadNLFModel`、`NLFPredict`、`WanVideoSchedulerv2`、`WanVideoSamplerExtraArgs`、`GetImageSizeAndCount`、`FloatConstant`、`WanVideoAddSCAILPoseEmbeds`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoContextOptions`、`CR Text`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`RenderNLFPoses`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`WanVideoSamplerv2`、`Fast Bypasser (rgthree)`、`easy int`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSamplerv2、WanVideoSamplerExtraArgs、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
