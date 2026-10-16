---
key: 视频生成/图生视频/【动作迁移】Wan2.2 Animate Plus工作流可多人版_2084663749063045122.json
name: 【动作迁移】Wan2.2 Animate Plus工作流可多人版_2084663749063045122
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【动作迁移】Wan2.2 Animate Plus工作流可多人版_2084663749063045122.json
hash: 57f805f60052e5ed
coverage: 0.51049
learned_at: 2026-10-16 20:35:47
nodes: [SetNode, SetNode, GetNode, Note, CLIPVisionLoader, GetNode, SetNode, SetNode, LayerUtility: PurgeVRAM V2, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoUni3C_ControlnetLoader, SetNode, WanVideoEncode, ImageResizeKJv2, WanVideoUni3C_embeds, ImageResizeKJv2, PreviewImage, YOLOModelLoader, BBoxYOLO, PreviewImage, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, SDPoseKeypointExtractor, SDPoseKeypointExtractor, OnnxDetectionModelLoader, VHS_VideoCombine, SetNode, GetNode, GetNode, GetNode, BBoxYOLO, PoseJSONToPoseKeypoint, PoseKeypointPreview, PoseKeypointPreview, PoseJSONToPoseKeypoint, SetNode, Note, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, GetNode, GetNode, ImpactConditionalBranch, PoseAndFaceDetection, YOLOModelLoader, WanAnimatePlus VAELoader, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus ClipVisionEncode, WanAnimatePlus BlockSwap, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, JjkText, GetNode, Seed (rgthree), WanAnimatePlus TextEncodeCached, WanAnimatePlus SamplerSettings, WanAnimatePlus Decode, SetNode, PlaySound|pysssss, GetNode, GetNode, GetNode, WanAnimatePlus ContextOptions, WanAnimatePlus SamplerFromSettings, WanAnimatePlus AnimateEmbeds, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, PreviewImage, SimpleMath+, VHS_VideoInfo, INTConstant, Note, GetImageRangeFromBatch, VHS_LoadVideoFFmpeg, INTConstant, INTConstant, Fast Groups Bypasser (rgthree), SetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, VHS_VideoCombine, ImageResizeKJv2, GetNode, GetNode, GetNode, GetImageRangeFromBatch, GetNode, GetNode, BodyRatioMapperProportionTransfer, Fast Groups Bypasser (rgthree), GetNode, GetNode, SetNode, GetNode, INTConstant, VHS_VideoInfoLoaded, SetNode, SetNode, SetNode, SimpleMath+, SetNode, SetNode, WanAnimatePlus TorchCompileSettings, SetNode, ComfyMathExpression, WanAnimatePlus ModelLoader, VHS_VideoCombine, INTConstant, Note, WanAnimatePlus LoraSelectMulti, WanAnimatePlus LoraSelectMulti, CheckpointLoaderSimple, ImageBatchMulti, Fast Groups Bypasser (rgthree), PrimitiveBoolean, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Note, Float, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/【动作迁移】Wan2.2 Animate Plus工作流可多人版_2084663749063045122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/【动作迁移】Wan2.2 Animate Plus工作流可多人版_2084663749063045122.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（143 个）：
- `SetNode`
- `SetNode`
- `GetNode`
- `Note`
- `CLIPVisionLoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `LayerUtility: PurgeVRAM V2`
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
- `YOLOModelLoader`
- `WanAnimatePlus VAELoader`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus ClipVisionEncode`
- `WanAnimatePlus BlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `JjkText`
- `GetNode`
- `Seed (rgthree)`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus SamplerSettings` ★核心
- `WanAnimatePlus Decode`
- `SetNode`
- `PlaySound|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus SamplerFromSettings` ★核心
- `WanAnimatePlus AnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `SimpleMath+`
- `VHS_VideoInfo`
- `INTConstant`
- `Note`
- `GetImageRangeFromBatch`
- `VHS_LoadVideoFFmpeg`
- `INTConstant`
- `INTConstant`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `SetNode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `BodyRatioMapperProportionTransfer`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `INTConstant`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `SetNode`
- `SetNode`
- `WanAnimatePlus TorchCompileSettings`
- `SetNode`
- `ComfyMathExpression`
- `WanAnimatePlus ModelLoader`
- `VHS_VideoCombine`
- `INTConstant`
- `Note`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus LoraSelectMulti`
- `CheckpointLoaderSimple` ★核心
- `ImageBatchMulti`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Float`
- `VHS_LoadVideo`
- `LoadImage`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **51%**（73/143）

**有卡**：`CLIPVisionLoader`、`LayerUtility: PurgeVRAM V2`、`WanVideoUni3C_ControlnetLoader`、`WanVideoEncode`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`YOLOModelLoader`、`BBoxYOLO`、`VHS_VideoCombine`、`SDPoseKeypointExtractor`、`OnnxDetectionModelLoader`、`PoseJSONToPoseKeypoint`、`PoseKeypointPreview`、`BodyRatioMapperSDPoseRender`、`ImpactConditionalBranch`、`PoseAndFaceDetection`、`WanAnimatePlus VAELoader`、`WanAnimatePlus SetBlockSwap`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus ClipVisionEncode`、`WanAnimatePlus BlockSwap`、`Seed (rgthree)`、`WanAnimatePlus TextEncodeCached`、`WanAnimatePlus SamplerSettings`、`WanAnimatePlus Decode`、`PlaySound|pysssss`、`WanAnimatePlus ContextOptions`、`WanAnimatePlus SamplerFromSettings`、`WanAnimatePlus AnimateEmbeds`、`SimpleMath+`、`VHS_VideoInfo`、`INTConstant`、`GetImageRangeFromBatch`、`VHS_LoadVideoFFmpeg`、`LoadImage`、`BodyRatioMapperProportionTransfer`、`VHS_VideoInfoLoaded`、`WanAnimatePlus TorchCompileSettings`、`ComfyMathExpression`、`WanAnimatePlus ModelLoader`、`WanAnimatePlus LoraSelectMulti`、`CheckpointLoaderSimple`、`ImageBatchMulti`、`PrimitiveBoolean`、`Float`、`VHS_LoadVideo`

**用到的条目**：CheckpointLoaderSimple、LoadImage、WanVideoUni3C_ControlnetLoader、Seed (rgthree)、WanAnimatePlus SamplerFromSettings、WanAnimatePlus SamplerSettings、WanVideoEncode、WanAnimatePlus ClipVisionEncode
