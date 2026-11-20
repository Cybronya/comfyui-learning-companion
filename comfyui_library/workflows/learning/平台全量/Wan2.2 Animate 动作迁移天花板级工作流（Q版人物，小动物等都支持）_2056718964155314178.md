---
key: 平台全量/Wan2.2 Animate 动作迁移天花板级工作流（Q版人物，小动物等都支持）_2056718964155314178.json
name: Wan2.2 Animate 动作迁移天花板级工作流（Q版人物，小动物等都支持）_2056718964155314178
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate 动作迁移天花板级工作流（Q版人物，小动物等都支持）_2056718964155314178.json
hash: 2ca1c496a2f1930e
coverage: 0.486957
learned_at: 2026-11-14 01:04:58
nodes: [MarkdownNote, Note, WanVideoSetLoRAs, SetNode, SetNode, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, GetNode, WanVideoBlockSwap, Note, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoModelLoader, CLIPVisionLoader, SetNode, WanVideoClipVisionEncode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoCombine, SetNode, SetNode, LayerUtility: PurgeVRAM V2, GetNode, Note, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoUni3C_ControlnetLoader, SetNode, WanVideoEncode, ImageResizeKJv2, MarkdownNote, WanVideoUni3C_embeds, ImageResizeKJv2, ImageResizeKJv2, INTConstant, INTConstant, VHS_VideoInfoLoaded, YOLOModelLoader, BBoxYOLO, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, SDPoseKeypointExtractor, SDPoseKeypointExtractor, OnnxDetectionModelLoader, VHS_VideoCombine, SetNode, GetNode, GetNode, GetNode, GetNode, BBoxYOLO, PoseJSONToPoseKeypoint, PoseKeypointPreview, PoseKeypointPreview, PoseJSONToPoseKeypoint, SetNode, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, GetNode, GetNode, ImpactConditionalBranch, PoseAndFaceDetection, CheckpointLoaderSimple, SetNode, Fast Groups Bypasser (rgthree), PrimitiveBoolean, Label (rgthree), WanVideoSamplerFromSettings, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoContextOptions, GetNode, PlaySound|pysssss, GetNode, WanVideoSamplerSettings, Note, WanVideoDecode, GetNode, WanVideoAnimateEmbeds, Seed (rgthree), SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, YOLOModelLoader, WanVideoTextEncodeCached, PreviewImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Note, BodyRatioMapperProportionTransfer, LoadImage, PreviewImage, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/Wan2.2 Animate 动作迁移天花板级工作流（Q版人物，小动物等都支持）_2056718964155314178.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate 动作迁移天花板级工作流（Q版人物，小动物等都支持）_2056718964155314178.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（115 个）：
- `MarkdownNote`
- `Note`
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
- `WanVideoModelLoader`
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
- `MarkdownNote`
- `WanVideoUni3C_embeds`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `VHS_VideoInfoLoaded`
- `YOLOModelLoader`
- `BBoxYOLO`
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
- `BodyRatioMapperSDPoseRender`
- `BodyRatioMapperSDPoseRender`
- `BodyRatioMapperSDPoseRender`
- `BodyRatioMapperSDPoseRender`
- `GetNode`
- `GetNode`
- `ImpactConditionalBranch`
- `PoseAndFaceDetection`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `Label (rgthree)`
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
- `Seed (rgthree)`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `YOLOModelLoader`
- `WanVideoTextEncodeCached`
- `PreviewImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `BodyRatioMapperProportionTransfer`
- `LoadImage`
- `PreviewImage`
- `VHS_LoadVideo`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **49%**（56/115）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`WanVideoUni3C_ControlnetLoader`、`WanVideoEncode`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`INTConstant`、`VHS_VideoInfoLoaded`、`YOLOModelLoader`、`BBoxYOLO`、`SDPoseKeypointExtractor`、`OnnxDetectionModelLoader`、`PoseJSONToPoseKeypoint`、`PoseKeypointPreview`、`BodyRatioMapperSDPoseRender`、`ImpactConditionalBranch`、`PoseAndFaceDetection`、`CheckpointLoaderSimple`、`PrimitiveBoolean`、`Label (rgthree)`、`WanVideoSamplerFromSettings`、`WanVideoContextOptions`、`PlaySound|pysssss`、`WanVideoSamplerSettings`、`WanVideoDecode`、`WanVideoAnimateEmbeds`、`Seed (rgthree)`、`WanVideoTextEncodeCached`、`BodyRatioMapperProportionTransfer`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：CheckpointLoaderSimple、LoadImage、WanVideoUni3C_ControlnetLoader、Seed (rgthree)、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoClipVisionEncode、WanVideoDecode
