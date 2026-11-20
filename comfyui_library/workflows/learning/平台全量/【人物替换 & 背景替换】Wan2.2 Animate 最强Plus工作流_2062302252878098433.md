---
key: 平台全量/【人物替换 & 背景替换】Wan2.2 Animate 最强Plus工作流_2062302252878098433.json
name: 【人物替换 & 背景替换】Wan2.2 Animate 最强Plus工作流_2062302252878098433
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【人物替换 & 背景替换】Wan2.2 Animate 最强Plus工作流_2062302252878098433.json
hash: 98ed4694fed2f625
coverage: 0.478469
learned_at: 2026-11-14 01:22:57
nodes: [Note, GetNode, SetNode, GetNode, SetNode, SetNode, GetNode, PreviewImage, BlockifyMask, DrawMaskOnImage, ImageResizeKJv2, PreviewAny, GetNode, GetNode, GetNode, SetNode, GetNode, Note, SetNode, SetNode, GetNode, GetNode, SetNode, ReverseImageBatch, ImageBatchMulti, SetNode, SetNode, SetNode, SimpleMath+, SimpleMath+, RepeatImageBatch, BatchCount+, SetNode, CheckpointLoaderSimple, SAM3_Detect, MaskToImage, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, ImageResizeKJv2, VHS_LoadVideo, GetNode, GetNode, ImageCompositeMasked, Any Switch (rgthree), ComfySwitchNode, SetNode, GetNode, SetNode, ImageBlend, GetNode, VHS_VideoCombine, INTConstant, PointsEditor, YOLOModelLoader, BBoxYOLO, PreviewImage, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, SDPoseKeypointExtractor, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, LoadImage, ImageResizeKJv2, RepeatImageBatch, PreviewAny, ImpactImageInfo, Image Blank, GetNode, VHS_VideoCombine, GetNode, ChangeImageBatchSize //Inspire, GetNode, VHS_VideoCombine, GetNode, VHS_VideoCombine, GetNode, GetNode, BBoxYOLO, PoseKeypointPreview, PoseJSONToPoseKeypoint, ChangeImageBatchSize //Inspire, Note, PreviewImage, SetNode, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, BodyRatioMapperSDPoseRender, INTConstant, GetNode, Fast Groups Bypasser (rgthree), PrimitiveBoolean, Fast Groups Bypasser (rgthree), CheckpointLoaderSimple, Note, ImpactConditionalBranch, BodyRatioMapperSDPoseRender, SDPoseKeypointExtractor, PoseKeypointPreview, CLIPTextEncode, PoseJSONToPoseKeypoint, GrowMaskWithBlur, Fast Groups Bypasser (rgthree), PrimitiveBoolean, YOLOModelLoader, PrimitiveBoolean, Fast Groups Bypasser (rgthree), SetNode, BodyRatioMapperProportionTransfer, ImageResizeKJv2, GetNode, GetNode, ImageResizeKJv2, SetNode, PreviewImage, ImageBatchMulti, LoadImage, LoadImage, LoadImage, LoadImage, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), GetNode, GetNode, SetNode, SetNode, GetNode, Note, CLIPVisionLoader, WanAnimatePlus VAELoader, WanAnimatePlus TorchCompileSettings, WanAnimatePlus SetBlockSwap, WanAnimatePlus SetLoRAs, WanAnimatePlus ClipVisionEncode, WanAnimatePlus BlockSwap, WanAnimatePlus LoraSelectMulti, WanAnimatePlus LoraSelectMulti, GetNode, GetNode, GetNode, GetNode, GetNode, Note, JjkText, Seed (rgthree), SetNode, PlaySound|pysssss, GetNode, GetNode, GetNode, WanAnimatePlus ContextOptions, WanAnimatePlus SamplerFromSettings, GetNode, SetNode, WanAnimatePlus SamplerSettings, WanAnimatePlus TextEncodeCached, GetNode, GetNode, GetNode, WanAnimatePlus AnimateEmbeds, Note, GetNode, INTConstant, SimpleMath+, GetNode, GetNode, GetImageRangeFromBatch, GetNode, VHS_VideoCombine, Fast Groups Bypasser (rgthree), SetNode, SetNode, VHS_VideoInfoLoaded, SimpleMath+, VHS_LoadVideo, Fast Groups Bypasser (rgthree), PoseAndFaceDetection, OnnxDetectionModelLoader, VHS_VideoCombine, GetNode, GetNode, GetNode, ComfySwitchNode, GetNode, INTConstant, Label (rgthree), Label (rgthree), VHS_LoadVideoFFmpeg, VHS_VideoInfo, Note, SimpleMath+, INTConstant, GetImageRangeFromBatch, SetNode, LoadImage, WanAnimatePlus Decode, WanAnimatePlus ModelLoader, MarkdownNote]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/【人物替换 & 背景替换】Wan2.2 Animate 最强Plus工作流_2062302252878098433.json

> 来源文件 `comfyui_library/workflows/平台全量/【人物替换 & 背景替换】Wan2.2 Animate 最强Plus工作流_2062302252878098433.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（209 个）：
- `Note`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `PreviewImage`
- `BlockifyMask`
- `DrawMaskOnImage`
- `ImageResizeKJv2`
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
- `SetNode`
- `SetNode`
- `SetNode`
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
- `INTConstant`
- `PointsEditor`
- `YOLOModelLoader`
- `BBoxYOLO`
- `PreviewImage`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SDPoseKeypointExtractor`
- `SetNode`
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
- `VHS_VideoCombine`
- `GetNode`
- `ChangeImageBatchSize //Inspire`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
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
- `INTConstant`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `CheckpointLoaderSimple` ★核心
- `Note`
- `ImpactConditionalBranch`
- `BodyRatioMapperSDPoseRender`
- `SDPoseKeypointExtractor`
- `PoseKeypointPreview`
- `CLIPTextEncode` ★核心
- `PoseJSONToPoseKeypoint`
- `GrowMaskWithBlur`
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `YOLOModelLoader`
- `PrimitiveBoolean`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `BodyRatioMapperProportionTransfer`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `ImageBatchMulti`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `Note`
- `CLIPVisionLoader`
- `WanAnimatePlus VAELoader`
- `WanAnimatePlus TorchCompileSettings`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus ClipVisionEncode`
- `WanAnimatePlus BlockSwap`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus LoraSelectMulti`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Note`
- `JjkText`
- `Seed (rgthree)`
- `SetNode`
- `PlaySound|pysssss`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus SamplerFromSettings` ★核心
- `GetNode`
- `SetNode`
- `WanAnimatePlus SamplerSettings` ★核心
- `WanAnimatePlus TextEncodeCached`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanAnimatePlus AnimateEmbeds`
- `Note`
- `GetNode`
- `INTConstant`
- `SimpleMath+`
- `GetNode`
- `GetNode`
- `GetImageRangeFromBatch`
- `GetNode`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `SimpleMath+`
- `VHS_LoadVideo`
- `Fast Groups Bypasser (rgthree)`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `ComfySwitchNode`
- `GetNode`
- `INTConstant`
- `Label (rgthree)`
- `Label (rgthree)`
- `VHS_LoadVideoFFmpeg`
- `VHS_VideoInfo`
- `Note`
- `SimpleMath+`
- `INTConstant`
- `GetImageRangeFromBatch`
- `SetNode`
- `LoadImage`
- `WanAnimatePlus Decode`
- `WanAnimatePlus ModelLoader`
- `MarkdownNote`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **48%**（100/209）

**有卡**：`BlockifyMask`、`DrawMaskOnImage`、`ImageResizeKJv2`、`ReverseImageBatch`、`ImageBatchMulti`、`SimpleMath+`、`RepeatImageBatch`、`BatchCount+`、`CheckpointLoaderSimple`、`SAM3_Detect`、`MaskToImage`、`VHS_LoadVideo`、`ImageCompositeMasked`、`ImageBlend`、`VHS_VideoCombine`、`INTConstant`、`PointsEditor`、`YOLOModelLoader`、`BBoxYOLO`、`SDPoseKeypointExtractor`、`LoadImage`、`ImpactImageInfo`、`Image Blank`、`ChangeImageBatchSize //Inspire`、`PoseKeypointPreview`、`PoseJSONToPoseKeypoint`、`BodyRatioMapperSDPoseRender`、`PrimitiveBoolean`、`ImpactConditionalBranch`、`CLIPTextEncode`、`GrowMaskWithBlur`、`BodyRatioMapperProportionTransfer`、`CLIPVisionLoader`、`WanAnimatePlus VAELoader`、`WanAnimatePlus TorchCompileSettings`、`WanAnimatePlus SetBlockSwap`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus ClipVisionEncode`、`WanAnimatePlus BlockSwap`、`WanAnimatePlus LoraSelectMulti`、`Seed (rgthree)`、`PlaySound|pysssss`、`WanAnimatePlus ContextOptions`、`WanAnimatePlus SamplerFromSettings`、`WanAnimatePlus SamplerSettings`、`WanAnimatePlus TextEncodeCached`、`WanAnimatePlus AnimateEmbeds`、`GetImageRangeFromBatch`、`VHS_VideoInfoLoaded`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`Label (rgthree)`、`VHS_LoadVideoFFmpeg`、`VHS_VideoInfo`、`WanAnimatePlus Decode`、`WanAnimatePlus ModelLoader`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、Seed (rgthree)、WanAnimatePlus SamplerFromSettings、WanAnimatePlus SamplerSettings、WanAnimatePlus ClipVisionEncode、WanAnimatePlus Decode
