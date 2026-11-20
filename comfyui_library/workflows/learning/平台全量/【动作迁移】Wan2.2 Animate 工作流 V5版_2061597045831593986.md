---
key: 平台全量/【动作迁移】Wan2.2 Animate 工作流 V5版_2061597045831593986.json
name: 【动作迁移】Wan2.2 Animate 工作流 V5版_2061597045831593986
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【动作迁移】Wan2.2 Animate 工作流 V5版_2061597045831593986.json
hash: a3665e8c2a779b09
coverage: 0.506849
learned_at: 2026-11-14 01:23:28
nodes: [MarkdownNote, SetNode, SetNode, GetNode, Note, CLIPVisionLoader, GetNode, SetNode, SetNode, LayerUtility: PurgeVRAM V2, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoUni3C_ControlnetLoader, SetNode, WanVideoEncode, ImageResizeKJv2, MarkdownNote, WanVideoUni3C_embeds, ImageResizeKJv2, PreviewImage, YOLOModelLoader, BBoxYOLO, PreviewImage, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, SDPoseKeypointExtractor, SDPoseKeypointExtractor, OnnxDetectionModelLoader, VHS_VideoCombine, SetNode, GetNode, GetNode, GetNode, BBoxYOLO, PoseJSONToPoseKeypoint, PoseKeypointPreview, PoseKeypointPreview, PoseJSONToPoseKeypoint, SetNode, Note, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, GetNode, GetNode, ImpactConditionalBranch, PoseAndFaceDetection, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), CheckpointLoaderSimple, YOLOModelLoader, WanAnimatePlus VAELoader, WanAnimatePlus ModelLoader, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus ClipVisionEncode, WanAnimatePlus BlockSwap, WanAnimatePlus LoraSelectMulti, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, Note, JjkText, GetNode, Seed (rgthree), WanAnimatePlus TextEncodeCached, WanAnimatePlus SamplerSettings, WanAnimatePlus Decode, SetNode, PlaySound|pysssss, GetNode, GetNode, GetNode, WanAnimatePlus ContextOptions, WanAnimatePlus SamplerFromSettings, WanAnimatePlus AnimateEmbeds, GetNode, GetNode, GetNode, GetNode, ImageResizeKJv2, SetNode, PreviewImage, ImageBatchMulti, SimpleMath+, VHS_VideoInfo, INTConstant, Note, GetImageRangeFromBatch, VHS_LoadVideoFFmpeg, INTConstant, INTConstant, Fast Groups Bypasser (rgthree), SetNode, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, SetNode, VHS_VideoCombine, ImageResizeKJv2, GetNode, VHS_LoadVideo, GetNode, GetNode, VHS_VideoCombine, GetImageRangeFromBatch, GetNode, GetNode, BodyRatioMapperProportionTransfer, Fast Groups Bypasser (rgthree), GetNode, GetNode, Fast Groups Bypasser (rgthree), SimpleMath+, Note, GetNode, INTConstant, VHS_VideoInfoLoaded, SetNode, SetNode, SetNode, SimpleMath+, SetNode, SetNode, WanAnimatePlus TorchCompileSettings, SetNode, PrimitiveBoolean, Fast Groups Bypasser (rgthree), SetNode, Note, WanAnimatePlus LoraSelectMulti, LoadImage, Label (rgthree), Label (rgthree), INTConstant]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/【动作迁移】Wan2.2 Animate 工作流 V5版_2061597045831593986.json

> 来源文件 `comfyui_library/workflows/平台全量/【动作迁移】Wan2.2 Animate 工作流 V5版_2061597045831593986.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（146 个）：
- `MarkdownNote`
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
- `MarkdownNote`
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
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `YOLOModelLoader`
- `WanAnimatePlus VAELoader`
- `WanAnimatePlus ModelLoader`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus ClipVisionEncode`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus LoraSelectMulti`
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
- `ImageBatchMulti`
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
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `BodyRatioMapperProportionTransfer`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `SimpleMath+`
- `Note`
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
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `Note`
- `WanAnimatePlus LoraSelectMulti`
- `LoadImage`
- `Label (rgthree)`
- `Label (rgthree)`
- `INTConstant`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **51%**（74/146）

**有卡**：`CLIPVisionLoader`、`LayerUtility: PurgeVRAM V2`、`WanVideoUni3C_ControlnetLoader`、`WanVideoEncode`、`ImageResizeKJv2`、`WanVideoUni3C_embeds`、`YOLOModelLoader`、`BBoxYOLO`、`VHS_VideoCombine`、`SDPoseKeypointExtractor`、`OnnxDetectionModelLoader`、`PoseJSONToPoseKeypoint`、`PoseKeypointPreview`、`BodyRatioMapperSDPoseRender`、`ImpactConditionalBranch`、`PoseAndFaceDetection`、`CheckpointLoaderSimple`、`WanAnimatePlus VAELoader`、`WanAnimatePlus ModelLoader`、`WanAnimatePlus SetBlockSwap`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus ClipVisionEncode`、`WanAnimatePlus BlockSwap`、`WanAnimatePlus LoraSelectMulti`、`Seed (rgthree)`、`WanAnimatePlus TextEncodeCached`、`WanAnimatePlus SamplerSettings`、`WanAnimatePlus Decode`、`PlaySound|pysssss`、`WanAnimatePlus ContextOptions`、`WanAnimatePlus SamplerFromSettings`、`WanAnimatePlus AnimateEmbeds`、`ImageBatchMulti`、`SimpleMath+`、`VHS_VideoInfo`、`INTConstant`、`GetImageRangeFromBatch`、`VHS_LoadVideoFFmpeg`、`LoadImage`、`VHS_LoadVideo`、`BodyRatioMapperProportionTransfer`、`VHS_VideoInfoLoaded`、`WanAnimatePlus TorchCompileSettings`、`PrimitiveBoolean`、`Label (rgthree)`

**用到的条目**：CheckpointLoaderSimple、LoadImage、WanVideoUni3C_ControlnetLoader、Seed (rgthree)、WanAnimatePlus SamplerFromSettings、WanAnimatePlus SamplerSettings、WanAnimatePlus ClipVisionEncode、WanAnimatePlus Decode
