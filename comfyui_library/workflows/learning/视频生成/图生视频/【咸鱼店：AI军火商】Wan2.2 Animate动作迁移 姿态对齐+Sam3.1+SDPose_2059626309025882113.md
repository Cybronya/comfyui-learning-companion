---
key: 视频生成/图生视频/【咸鱼店：AI军火商】Wan2.2 Animate动作迁移 姿态对齐+Sam3.1+SDPose_2059626309025882113.json
name: 【咸鱼店：AI军火商】Wan2.2 Animate动作迁移 姿态对齐+Sam3.1+SDPose_2059626309025882113.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2059626309025882113.json
hash: 23ff978b559c2708
coverage: 0.5
learned_at: 2026-10-15 22:38:41
nodes: [GetNode, SetNode, GetNode, VHS_VideoCombine, SetNode, SetNode, LayerUtility: PurgeVRAM V2, MarkdownNote, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoUni3C_ControlnetLoader, SetNode, WanVideoEncode, Note, ImageResizeKJv2, WanVideoUni3C_embeds, ImageResizeKJv2, ImageResizeKJv2, BBoxYOLO, YOLOModelLoader, PreviewImage, PreviewImage, VHS_VideoCombine, SDPoseKeypointExtractor, SDPoseKeypointExtractor, SetNode, GetNode, GetNode, GetNode, GetNode, BBoxYOLO, PoseKeypointPreview, PoseKeypointPreview, PoseJSONToPoseKeypoint, GetNode, GetNode, PoseAndFaceDetection, CheckpointLoaderSimple, SetNode, GetNode, GetNode, Note, PoseJSONToPoseKeypoint, YOLOModelLoader, SetNode, ImpactConditionalBranch, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, VHS_VideoCombine, VHS_VideoCombine, PrimitiveBoolean, Fast Groups Bypasser (rgthree), VHS_VideoInfoLoaded, SetNode, SetNode, Fast Groups Bypasser (rgthree), VHS_VideoCombine, OnnxDetectionModelLoader, VHS_LoadVideo, Fast Groups Bypasser (rgthree), PreviewImage, Note, GetNode, SetNode, GetNode, GetNode, SetNode, Note, WanVideoContextOptions, WanAnimatePlus SetLoRAs, WanAnimatePlus ClipVisionEncode, SetNode, WanAnimatePlus VAELoader, SetNode, WanAnimatePlus SetBlockSwap, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanAnimatePlus SamplerSettings, WanAnimatePlus SamplerFromSettings, PlaySound|pysssss, WanAnimatePlus AnimateEmbeds, SetNode, CLIPVisionLoader, Note, Seed (rgthree), WanAnimatePlus LoraSelectMulti, SimpleMath+, VHS_VideoInfo, INTConstant, GetImageRangeFromBatch, SetNode, Note, Note, GetImageRangeFromBatch, GetNode, SetNode, SimpleMath+, Int, MarkdownNote, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), WanVideoTextEncodeCached, INTConstant, INTConstant, WanAnimatePlus Decode, WanAnimatePlus LoraSelectMulti, WanAnimatePlus ModelLoader, WanAnimatePlus TorchCompileSettings, WanAnimatePlus BlockSwap, BodyRatioMapperProportionTransfer, VHS_LoadImagesPath, VHS_LoadVideo, LoadImage, Label (rgthree), Label (rgthree), ImageResizeKJv2, SetNode, PreviewImage, Label (rgthree)]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/【咸鱼店：AI军火商】Wan2.2 Animate动作迁移 姿态对齐+Sam3.1+SDPose_2059626309025882113.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2059626309025882113.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（136 个）：
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
- `MarkdownNote`
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
- `Note`
- `ImageResizeKJv2`
- `WanVideoUni3C_embeds`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `BBoxYOLO`
- `YOLOModelLoader`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `SDPoseKeypointExtractor`
- `SDPoseKeypointExtractor`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BBoxYOLO`
- `PoseKeypointPreview`
- `PoseKeypointPreview`
- `PoseJSONToPoseKeypoint`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `CheckpointLoaderSimple` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `PoseJSONToPoseKeypoint`
- `YOLOModelLoader`
- `SetNode`
- `ImpactConditionalBranch`
- `BodyRatioMapperSDPoseRender`
- `BodyRatioMapperSDPoseRender`
- `BodyRatioMapperSDPoseRender`
- `BodyRatioMapperSDPoseRender`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `VHS_VideoCombine`
- `OnnxDetectionModelLoader`
- `VHS_LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `PreviewImage`
- `Note`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Note`
- `WanVideoContextOptions`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus ClipVisionEncode`
- `SetNode`
- `WanAnimatePlus VAELoader`
- `SetNode`
- `WanAnimatePlus SetBlockSwap`
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
- `WanAnimatePlus SamplerSettings` ★核心
- `WanAnimatePlus SamplerFromSettings` ★核心
- `PlaySound|pysssss`
- `WanAnimatePlus AnimateEmbeds`
- `SetNode`
- `CLIPVisionLoader`
- `Note`
- `Seed (rgthree)`
- `WanAnimatePlus LoraSelectMulti`
- `SimpleMath+`
- `VHS_VideoInfo`
- `INTConstant`
- `GetImageRangeFromBatch`
- `SetNode`
- `Note`
- `Note`
- `GetImageRangeFromBatch`
- `GetNode`
- `SetNode`
- `SimpleMath+`
- `Int`
- `MarkdownNote`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `WanVideoTextEncodeCached`
- `INTConstant`
- `INTConstant`
- `WanAnimatePlus Decode`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus TorchCompileSettings`
- `WanAnimatePlus BlockSwap`
- `BodyRatioMapperProportionTransfer`
- `VHS_LoadImagesPath`
- `VHS_LoadVideo`
- `LoadImage`
- `Label (rgthree)`
- `Label (rgthree)`
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `Label (rgthree)`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **50%**（68/136）

**有卡**：`VHS_VideoCombine`、`LayerUtility: PurgeVRAM V2`、`WanVideoUni3C_ControlnetLoader`、`WanVideoEncode`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`BBoxYOLO`、`YOLOModelLoader`、`SDPoseKeypointExtractor`、`PoseKeypointPreview`、`PoseJSONToPoseKeypoint`、`PoseAndFaceDetection`、`CheckpointLoaderSimple`、`ImpactConditionalBranch`、`BodyRatioMapperSDPoseRender`、`PrimitiveBoolean`、`VHS_VideoInfoLoaded`、`OnnxDetectionModelLoader`、`VHS_LoadVideo`、`WanVideoContextOptions`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus ClipVisionEncode`、`WanAnimatePlus VAELoader`、`WanAnimatePlus SetBlockSwap`、`WanAnimatePlus SamplerSettings`、`WanAnimatePlus SamplerFromSettings`、`PlaySound|pysssss`、`WanAnimatePlus AnimateEmbeds`、`CLIPVisionLoader`、`Seed (rgthree)`、`WanAnimatePlus LoraSelectMulti`、`SimpleMath+`、`VHS_VideoInfo`、`INTConstant`、`GetImageRangeFromBatch`、`Int`、`WanVideoTextEncodeCached`、`WanAnimatePlus Decode`、`WanAnimatePlus ModelLoader`、`WanAnimatePlus TorchCompileSettings`、`WanAnimatePlus BlockSwap`、`BodyRatioMapperProportionTransfer`、`VHS_LoadImagesPath`、`LoadImage`、`Label (rgthree)`

**用到的条目**：CheckpointLoaderSimple、LoadImage、WanVideoUni3C_ControlnetLoader、Seed (rgthree)、WanAnimatePlus SamplerFromSettings、WanAnimatePlus SamplerSettings、WanVideoTextEncodeCached、WanVideoEncode
