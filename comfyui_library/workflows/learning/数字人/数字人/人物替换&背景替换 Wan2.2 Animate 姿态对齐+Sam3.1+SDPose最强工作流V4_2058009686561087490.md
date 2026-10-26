---
key: 数字人/数字人/人物替换&背景替换 Wan2.2 Animate 姿态对齐+Sam3.1+SDPose最强工作流V4_2058009686561087490.json
name: 人物替换&背景替换 Wan2.2 Animate 姿态对齐+Sam3.1+SDPose最强工作流V4_2058009686561087490
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/人物替换&背景替换 Wan2.2 Animate 姿态对齐+Sam3.1+SDPose最强工作流V4_2058009686561087490.json
hash: 7e6248268eae3d20
coverage: 0.431818
learned_at: 2026-10-26 02:00:17
nodes: [WanVideoSetLoRAs, SetNode, SetNode, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, GetNode, WanVideoBlockSwap, WanVideoClipVisionEncode, Note, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoModelLoader, CLIPVisionLoader, SetNode, GetNode, SetNode, SetNode, GetNode, SetNode, GetNode, BlockifyMask, DrawMaskOnImage, VHS_VideoInfoLoaded, PreviewAny, GetNode, GetNode, GetNode, SetNode, GetNode, Note, SetNode, SetNode, GetNode, GetNode, SetNode, ReverseImageBatch, ImageBatchMulti, SimpleMath+, SimpleMath+, RepeatImageBatch, BatchCount+, SetNode, CheckpointLoaderSimple, SAM3_Detect, MaskToImage, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ImageResizeKJv2, VHS_LoadVideo, GetNode, GetNode, ImageCompositeMasked, Any Switch (rgthree), ComfySwitchNode, SetNode, GetNode, SetNode, ImageBlend, GetNode, VHS_VideoCombine, PointsEditor, YOLOModelLoader, BBoxYOLO, PreviewImage, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, SDPoseKeypointExtractor, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, LoadImage, ImageResizeKJv2, RepeatImageBatch, PreviewAny, ImpactImageInfo, Image Blank, GetNode, GetNode, ChangeImageBatchSize //Inspire, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, BBoxYOLO, PoseKeypointPreview, PoseJSONToPoseKeypoint, ChangeImageBatchSize //Inspire, Note, PreviewImage, SetNode, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, GetNode, PoseAndFaceDetection, Fast Groups Bypasser (rgthree), Note, ImpactConditionalBranch, BodyRatioMapperSDPoseRender, SDPoseKeypointExtractor, PoseKeypointPreview, CLIPTextEncode, PoseJSONToPoseKeypoint, GrowMaskWithBlur, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, SetNode, WanVideoDecode, YOLOModelLoader, Fast Groups Bypasser (rgthree), SetNode, SetNode, SetNode, INTConstant, INTConstant, GetNode, SetNode, SetNode, easy int, SetNode, easy int, easy int, GetNode, SetNode, VHS_VideoCombine, WanVideoLoraSelectMulti, Note, VHS_VideoCombine, BodyRatioMapperProportionTransfer, SetNode, MarkdownNote, VHS_VideoCombine, WanVideoContextOptions, Seed (rgthree), GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoTextEncodeCached, WanVideoSamplerSettings, GetNode, GetNode, ImageResizeKJv2, SetNode, Note, ImageResizeKJv2, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, WanVideoUni3C_ControlnetLoader, WanVideoEncode, WanVideoUni3C_embeds, SetNode, LayerUtility: PurgeVRAM V2, easy mathInt, easy mathInt, GetNode, GetNode, GetNode, WanVideoSamplerFromSettings, PlaySound|pysssss, CR Text, Label (rgthree), CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), PrimitiveBoolean, Fast Groups Bypasser (rgthree), PrimitiveBoolean, PrimitiveBoolean, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), VHS_VideoCombine, PreviewImage, Label (rgthree), WanVideoAnimateEmbeds, WanVideoAnimateEmbeds, VHS_LoadVideo, LoadImage, Fast Groups Bypasser (rgthree), Note, Fast Groups Bypasser (rgthree), Note, Note, PrimitiveNode, ImpactSwitch]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 数字人/数字人/人物替换&背景替换 Wan2.2 Animate 姿态对齐+Sam3.1+SDPose最强工作流V4_2058009686561087490.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/人物替换&背景替换 Wan2.2 Animate 姿态对齐+Sam3.1+SDPose最强工作流V4_2058009686561087490.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（220 个）：
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoClipVisionEncode`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `BlockifyMask`
- `DrawMaskOnImage`
- `VHS_VideoInfoLoaded`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `Note`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ReverseImageBatch`
- `ImageBatchMulti`
- `SimpleMath+`
- `SimpleMath+`
- `RepeatImageBatch`
- `BatchCount+`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `SAM3_Detect`
- `MaskToImage`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `ImageResizeKJv2`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `ImageCompositeMasked`
- `Any Switch (rgthree)`
- `ComfySwitchNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `ImageBlend`
- `GetNode`
- `VHS_VideoCombine`
- `PointsEditor`
- `YOLOModelLoader`
- `BBoxYOLO`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SDPoseKeypointExtractor`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RepeatImageBatch`
- `LoadImage`
- `ImageResizeKJv2`
- `RepeatImageBatch`
- `PreviewAny`
- `ImpactImageInfo`
- `Image Blank`
- `GetNode`
- `GetNode`
- `ChangeImageBatchSize //Inspire`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BBoxYOLO`
- `PoseKeypointPreview`
- `PoseJSONToPoseKeypoint`
- `ChangeImageBatchSize //Inspire`
- `Note`
- `PreviewImage`
- `SetNode`
- `BodyRatioMapperSDPoseRender`
- `BodyRatioMapperSDPoseRender`
- `BodyRatioMapperSDPoseRender`
- `GetNode`
- `PoseAndFaceDetection`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `ImpactConditionalBranch`
- `BodyRatioMapperSDPoseRender`
- `SDPoseKeypointExtractor`
- `PoseKeypointPreview`
- `CLIPTextEncode` ★核心
- `PoseJSONToPoseKeypoint`
- `GrowMaskWithBlur`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `SetNode`
- `WanVideoDecode`
- `YOLOModelLoader`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy int`
- `SetNode`
- `easy int`
- `easy int`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`
- `Note`
- `VHS_VideoCombine`
- `BodyRatioMapperProportionTransfer`
- `SetNode`
- `MarkdownNote`
- `VHS_VideoCombine`
- `WanVideoContextOptions`
- `Seed (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoSamplerSettings` ★核心
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `Note`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `WanVideoUni3C_ControlnetLoader`
- `WanVideoEncode`
- `WanVideoUni3C_embeds`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `easy mathInt`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSamplerFromSettings` ★核心
- `PlaySound|pysssss`
- `CR Text`
- `Label (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `PreviewImage`
- `Label (rgthree)`
- `WanVideoAnimateEmbeds`
- `WanVideoAnimateEmbeds`
- `VHS_LoadVideo`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Note`
- `PrimitiveNode`
- `ImpactSwitch`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **43%**（95/220）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoClipVisionEncode`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`、`CLIPVisionLoader`、`BlockifyMask`、`DrawMaskOnImage`、`VHS_VideoInfoLoaded`、`ReverseImageBatch`、`ImageBatchMulti`、`SimpleMath+`、`RepeatImageBatch`、`BatchCount+`、`CheckpointLoaderSimple`、`SAM3_Detect`、`MaskToImage`、`ImageResizeKJv2`、`VHS_LoadVideo`、`ImageCompositeMasked`、`ImageBlend`、`VHS_VideoCombine`、`PointsEditor`、`YOLOModelLoader`、`BBoxYOLO`、`SDPoseKeypointExtractor`、`OnnxDetectionModelLoader`、`LoadImage`、`ImpactImageInfo`、`Image Blank`、`ChangeImageBatchSize //Inspire`、`PoseKeypointPreview`、`PoseJSONToPoseKeypoint`、`BodyRatioMapperSDPoseRender`、`PoseAndFaceDetection`、`ImpactConditionalBranch`、`CLIPTextEncode`、`GrowMaskWithBlur`、`WanVideoDecode`、`INTConstant`、`easy int`、`BodyRatioMapperProportionTransfer`、`WanVideoContextOptions`、`Seed (rgthree)`、`WanVideoTextEncodeCached`、`WanVideoSamplerSettings`、`WanVideoUni3C_ControlnetLoader`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`LayerUtility: PurgeVRAM V2`、`easy mathInt`、`WanVideoSamplerFromSettings`、`PlaySound|pysssss`、`CR Text`、`Label (rgthree)`、`PrimitiveBoolean`、`WanVideoAnimateEmbeds`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSamplerFromSettings、WanVideoSamplerSettings、Seed (rgthree)、WanVideoDecode
