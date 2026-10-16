---
key: 视频生成/图生视频/Wan2.2+Animate+动作迁移天花板级工作流（加强版）_2069239719984189441.json
name: Wan2.2+Animate+动作迁移天花板级工作流（加强版）_2069239719984189441.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2069239719984189441.json
hash: 293fe1333d37b71f
coverage: 0.482456
learned_at: 2026-10-15 22:40:26
nodes: [WanVideoSetLoRAs, SetNode, SetNode, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, GetNode, WanVideoBlockSwap, Note, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoVAELoader, CLIPVisionLoader, SetNode, WanVideoClipVisionEncode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoCombine, SetNode, SetNode, LayerUtility: PurgeVRAM V2, GetNode, Note, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoUni3C_ControlnetLoader, SetNode, WanVideoEncode, ImageResizeKJv2, WanVideoUni3C_embeds, ImageResizeKJv2, PreviewImage, ImageResizeKJv2, VHS_VideoInfoLoaded, YOLOModelLoader, BBoxYOLO, PreviewImage, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, SDPoseKeypointExtractor, SDPoseKeypointExtractor, OnnxDetectionModelLoader, VHS_VideoCombine, SetNode, GetNode, GetNode, GetNode, GetNode, BBoxYOLO, PoseJSONToPoseKeypoint, PoseKeypointPreview, PoseKeypointPreview, PoseJSONToPoseKeypoint, SetNode, Note, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, GetNode, GetNode, ImpactConditionalBranch, PoseAndFaceDetection, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), CheckpointLoaderSimple, SetNode, Fast Groups Bypasser (rgthree), WanVideoSamplerFromSettings, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoContextOptions, GetNode, PlaySound|pysssss, GetNode, WanVideoSamplerSettings, Note, WanVideoDecode, GetNode, WanVideoAnimateEmbeds, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, YOLOModelLoader, VHS_LoadVideo, WanVideoTextEncodeCached, JjkText, Seed (rgthree), PrimitiveBoolean, BodyRatioMapperProportionTransfer, WanVideoModelLoader, LoadImage, MarkdownNote, Note, INTConstant, INTConstant]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2+Animate+动作迁移天花板级工作流（加强版）_2069239719984189441.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2069239719984189441.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（114 个）：
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `WanVideoBlockSwap`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoUni3C_ControlnetLoader`
- `SetNode`
- `WanVideoEncode`
- `ImageResizeKJv2`
- `WanVideoUni3C_embeds`
- `ImageResizeKJv2`
- `PreviewImage`
- `ImageResizeKJv2`
- `VHS_VideoInfoLoaded`
- `YOLOModelLoader`
- `BBoxYOLO`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SDPoseKeypointExtractor`
- `SDPoseKeypointExtractor`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BBoxYOLO`
- `PoseJSONToPoseKeypoint`
- `PoseKeypointPreview`
- `PoseKeypointPreview`
- `PoseJSONToPoseKeypoint`
- `SetNode`
- `Note`
- `BodyRatioMapperSDPoseRender`
- `BodyRatioMapperSDPoseRender`
- `BodyRatioMapperSDPoseRender`
- `BodyRatioMapperSDPoseRender`
- `GetNode`
- `GetNode`
- `ImpactConditionalBranch`
- `PoseAndFaceDetection`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoSamplerFromSettings` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoContextOptions`
- `GetNode`
- `PlaySound|pysssss`
- `GetNode`
- `WanVideoSamplerSettings` ★核心
- `Note`
- `WanVideoDecode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `YOLOModelLoader`
- `VHS_LoadVideo`
- `WanVideoTextEncodeCached`
- `JjkText`
- `Seed (rgthree)`
- `PrimitiveBoolean`
- `BodyRatioMapperProportionTransfer`
- `WanVideoModelLoader`
- `LoadImage`
- `MarkdownNote`
- `Note`
- `INTConstant`
- `INTConstant`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **48%**（55/114）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`WanVideoUni3C_ControlnetLoader`、`WanVideoEncode`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`VHS_VideoInfoLoaded`、`YOLOModelLoader`、`BBoxYOLO`、`SDPoseKeypointExtractor`、`OnnxDetectionModelLoader`、`PoseJSONToPoseKeypoint`、`PoseKeypointPreview`、`BodyRatioMapperSDPoseRender`、`ImpactConditionalBranch`、`PoseAndFaceDetection`、`CheckpointLoaderSimple`、`WanVideoSamplerFromSettings`、`WanVideoContextOptions`、`PlaySound|pysssss`、`WanVideoSamplerSettings`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`WanVideoTextEncodeCached`、`Seed (rgthree)`、`PrimitiveBoolean`、`BodyRatioMapperProportionTransfer`、`WanVideoModelLoader`、`LoadImage`、`INTConstant`

**用到的条目**：CheckpointLoaderSimple、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSamplerFromSettings、WanVideoSamplerSettings、Seed (rgthree)、WanVideoDecode、WanVideoVAELoader
