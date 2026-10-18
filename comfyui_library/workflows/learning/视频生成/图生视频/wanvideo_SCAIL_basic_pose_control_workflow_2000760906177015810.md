---
key: 视频生成/图生视频/wanvideo_SCAIL_basic_pose_control_workflow_2000760906177015810.json
name: wanvideo_SCAIL_basic_pose_control_workflow_2000760906177015810.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wanvideo_SCAIL_basic_pose_control_workflow_2000760906177015810.json
hash: 633a362cb224db4f
coverage: 0.630137
learned_at: 2026-10-15 22:33:42
nodes: [SetNode, SetNode, SetNode, GetNode, GetNode, INTConstant, INTConstant, GetNode, FloatConstant, Note, GetNode, GetNode, ImageResizeKJv2, OnnxDetectionModelLoader, DownloadAndLoadNLFModel, NLFPredict, PoseDetectionVitPoseToDWPose, PoseDetectionVitPoseToDWPose, SetNode, GetNode, GetNode, SimpleCalculatorKJ, SimpleCalculatorKJ, VHS_LoadVideo, ImageResizeKJv2, SetNode, SetNode, RenderNLFPoses, MarkdownNote, VHS_VideoCombine, Reroute, WanVideoLoraSelect, MarkdownNote, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoVAELoader, WanVideoTextEncodeCached, SetNode, CLIPVisionLoader, SetNode, WanVideoClipVisionEncode, WanVideoAddSCAILReferenceEmbeds, WanVideoEmptyEmbeds, WanVideoAddSCAILPoseEmbeds, GetNode, GetNode, GetNode, Reroute, WanVideoSchedulerv2, GetNode, WanVideoContextOptions, GetNode, WanVideoDecode, GetImageSizeAndCount, WanVideoSamplerv2, WanVideoSamplerExtraArgs, ImageConcatMulti, VHS_VideoCombine, ImageConcatMulti, VHS_VideoCombine, MarkdownNote, Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), Label (rgthree), LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wanvideo_SCAIL_basic_pose_control_workflow_2000760906177015810.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2000760906177015810.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（73 个）：
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
- `ImageResizeKJv2`
- `OnnxDetectionModelLoader`
- `DownloadAndLoadNLFModel`
- `NLFPredict`
- `PoseDetectionVitPoseToDWPose`
- `PoseDetectionVitPoseToDWPose`
- `SetNode`
- `GetNode`
- `GetNode`
- `SimpleCalculatorKJ`
- `SimpleCalculatorKJ`
- `VHS_LoadVideo`
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
- `WanVideoSamplerExtraArgs` ★核心
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

## 知识

覆盖率 **63%**（46/73）

**有卡**：`INTConstant`、`FloatConstant`、`ImageResizeKJv2`、`OnnxDetectionModelLoader`、`DownloadAndLoadNLFModel`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`SimpleCalculatorKJ`、`VHS_LoadVideo`、`RenderNLFPoses`、`VHS_VideoCombine`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoAddSCAILReferenceEmbeds`、`WanVideoEmptyEmbeds`、`WanVideoAddSCAILPoseEmbeds`、`WanVideoSchedulerv2`、`WanVideoContextOptions`、`WanVideoDecode`、`GetImageSizeAndCount`、`WanVideoSamplerv2`、`WanVideoSamplerExtraArgs`、`ImageConcatMulti`、`Label (rgthree)`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSamplerv2、WanVideoSamplerExtraArgs、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect
