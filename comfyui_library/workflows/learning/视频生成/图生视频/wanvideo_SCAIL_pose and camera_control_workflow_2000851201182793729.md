---
key: 视频生成/图生视频/wanvideo_SCAIL_pose and camera_control_workflow_2000851201182793729.json
name: wanvideo_SCAIL_pose and camera_control_workflow_2000851201182793729.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wanvideo_SCAIL_pose and camera_control_workflow_2000851201182793729.json
hash: 80648161de97f9b1
coverage: 0.620253
learned_at: 2026-10-15 22:33:43
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, INTConstant, INTConstant, GetNode, FloatConstant, Note, GetNode, GetNode, OnnxDetectionModelLoader, DownloadAndLoadNLFModel, PoseDetectionVitPoseToDWPose, PoseDetectionVitPoseToDWPose, SetNode, GetNode, GetNode, SimpleCalculatorKJ, SimpleCalculatorKJ, ImageResizeKJv2, SetNode, SetNode, RenderNLFPoses, MarkdownNote, VHS_VideoCombine, Reroute, WanVideoLoraSelect, MarkdownNote, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoVAELoader, WanVideoTextEncodeCached, SetNode, CLIPVisionLoader, SetNode, WanVideoClipVisionEncode, WanVideoAddSCAILReferenceEmbeds, WanVideoEmptyEmbeds, WanVideoAddSCAILPoseEmbeds, GetNode, GetNode, GetNode, Reroute, WanVideoSchedulerv2, GetNode, WanVideoContextOptions, GetNode, WanVideoDecode, GetImageSizeAndCount, WanVideoSamplerv2, ImageConcatMulti, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, MarkdownNote, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), LoadImage, VHS_LoadVideo, WanVideoSamplerExtraArgs, NLFPredict, ImageResizeKJv2, SetNode, WanVideoUni3C_embeds, GetNode, GetNode, WanVideoEncode, WanVideoUni3C_ControlnetLoader]
patterns: []
missing: []
---

# 视频生成/图生视频/wanvideo_SCAIL_pose and camera_control_workflow_2000851201182793729.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2000851201182793729.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（79 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `FloatConstant`
- `Note`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `DownloadAndLoadNLFModel`
- `PoseDetectionVitPoseToDWPose`
- `PoseDetectionVitPoseToDWPose`
- `SetNode`
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `ImageResizeKJv2`
- `SetNode`
- `SetNode`
- `RenderNLFPoses`
- `MarkdownNote`
- `VHS_VideoCombine`
- `Reroute`
- `WanVideoLoraSelect`
- `MarkdownNote`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoClipVisionEncode`
- `WanVideoAddSCAILReferenceEmbeds`
- `WanVideoEmptyEmbeds`
- `WanVideoAddSCAILPoseEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `Reroute`
- `WanVideoSchedulerv2`
- `GetNode`
- `WanVideoContextOptions`
- `GetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `WanVideoSamplerv2` ★核心
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `MarkdownNote`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `Label (rgthree)`
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoSamplerExtraArgs` ★核心
- `NLFPredict`
- `ImageResizeKJv2`
- `SetNode`
- `WanVideoUni3C_embeds`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`

## 知识

覆盖率 **62%**（49/79）

**有卡**：`INTConstant`、`FloatConstant`、`OnnxDetectionModelLoader`、`DownloadAndLoadNLFModel`、`PoseDetectionVitPoseToDWPose`、`SimpleCalculatorKJ`、`ImageResizeKJv2`、`RenderNLFPoses`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAddSCAILReferenceEmbeds`、`WanVideoEmptyEmbeds`、`WanVideoAddSCAILPoseEmbeds`、`WanVideoSchedulerv2`、`WanVideoContextOptions`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoSamplerv2`、`ImageConcatMulti`、`Label (rgthree)`、`LoadImage`、`VHS_LoadVideo`、`WanVideoSamplerExtraArgs`、`NLFPredict`、`WanVideoUni3C_embeds`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`

**用到的条目**：LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSamplerv2、WanVideoSamplerExtraArgs、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
