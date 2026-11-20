---
key: 平台全量/【视频变装】+【动作迁移】+【人物替换】Wan2.2+Animate+分段队列+_2062724836660699138.json
name: 【视频变装】+【动作迁移】+【人物替换】Wan2.2+Animate+分段队列+_2062724836660699138
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【视频变装】+【动作迁移】+【人物替换】Wan2.2+Animate+分段队列+_2062724836660699138.json
hash: d367decb127e4537
coverage: 0.455285
learned_at: 2026-11-14 01:25:08
nodes: [GetNode, WanVideoSetLoRAs, SetNode, GetNode, SetNode, SetNode, SetNode, WanVideoSetBlockSwap, GetNode, GetNode, SetNode, WanVideoTorchCompileSettings, GetNode, SetNode, GetNode, WanVideoUni3C_ControlnetLoader, GetNode, GetNode, BlockifyMask, DrawMaskOnImage, ImageResizeKJv2, GetNode, SetNode, SetNode, WanVideoEncode, Note, SetNode, SetNode, WanVideoUni3C_embeds, LayerUtility: PurgeVRAM V2, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoModelLoader, SetNode, ImageBlend, SetNode, WanVideoContextOptions, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, PoseAndFaceDetection, SetNode, WanVideoSamplerSettings, WanVideoDecode, GetNode, GetNode, SetNode, GetNode, OnnxDetectionModelLoader, SAM3_Detect, GetNode, GrowMaskWithBlur, WanVideoTextEncodeCached, VHS_VideoCombine, SetNode, CheckpointLoaderSimple, SDPoseKeypointExtractor, BodyRatioMapperSDPoseRender, BBoxYOLO, YOLOModelLoader, ImageResizeKJv2, Note, CLIPTextEncode, GetNode, VHS_VideoCombine, CLIPVisionLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, INTConstant, INTConstant, Fast Groups Bypasser (rgthree), GetNode, Note, GetNode, GetNode, GetNode, WanVideoBlockSwap, CheckpointLoaderSimple, GetNode, VHS_VideoCombine, MaskToImage, GetNode, VHS_VideoCombine, Note, VHS_VideoCombine, LoadImage, Note, PreviewImage, Note, GetNode, WanVideoSamplerFromSettings, PlaySound|pysssss, VHS_VideoInfoLoaded, SetNode, SetNode, Fast Groups Bypasser (rgthree), SetNode, GetNode, LoadImage, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Seed (rgthree), WanVideoClipVisionEncode, Primitive integer [Crystools], Note, VHS_LoadVideo, SimpleMath+, Primitive integer [Crystools], GetNode, ImageResizeKJv2, Fast Groups Bypasser (rgthree), SegmentQueueRunner, WanVideoAnimateEmbeds, GetNode, GetNode, Note]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/【视频变装】+【动作迁移】+【人物替换】Wan2.2+Animate+分段队列+_2062724836660699138.json

> 来源文件 `comfyui_library/workflows/平台全量/【视频变装】+【动作迁移】+【人物替换】Wan2.2+Animate+分段队列+_2062724836660699138.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（123 个）：
- `GetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoUni3C_ControlnetLoader`
- `GetNode`
- `GetNode`
- `BlockifyMask`
- `DrawMaskOnImage`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoEncode`
- `Note`
- `SetNode`
- `SetNode`
- `WanVideoUni3C_embeds`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `SetNode`
- `ImageBlend`
- `SetNode`
- `WanVideoContextOptions`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `SetNode`
- `WanVideoSamplerSettings` ★核心
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `SAM3_Detect`
- `GetNode`
- `GrowMaskWithBlur`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `BodyRatioMapperSDPoseRender`
- `BBoxYOLO`
- `YOLOModelLoader`
- `ImageResizeKJv2`
- `Note`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `CLIPVisionLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `MaskToImage`
- `GetNode`
- `VHS_VideoCombine`
- `Note`
- `VHS_VideoCombine`
- `LoadImage`
- `Note`
- `PreviewImage`
- `Note`
- `GetNode`
- `WanVideoSamplerFromSettings` ★核心
- `PlaySound|pysssss`
- `VHS_VideoInfoLoaded`
- `SetNode`
- `SetNode`
- `Fast Groups Bypasser (rgthree)`
- `SetNode`
- `GetNode`
- `LoadImage`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Seed (rgthree)`
- `WanVideoClipVisionEncode`
- `Primitive integer [Crystools]`
- `Note`
- `VHS_LoadVideo`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `GetNode`
- `ImageResizeKJv2`
- `Fast Groups Bypasser (rgthree)`
- `SegmentQueueRunner`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `Note`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **46%**（56/123）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoUni3C_ControlnetLoader`、`BlockifyMask`、`DrawMaskOnImage`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`LayerUtility: PurgeVRAM V2`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`、`ImageBlend`、`WanVideoContextOptions`、`VHS_VideoCombine`、`PoseAndFaceDetection`、`WanVideoSamplerSettings`、`WanVideoDecode`、`OnnxDetectionModelLoader`、`SAM3_Detect`、`GrowMaskWithBlur`、`WanVideoTextEncodeCached`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`BodyRatioMapperSDPoseRender`、`BBoxYOLO`、`YOLOModelLoader`、`CLIPTextEncode`、`CLIPVisionLoader`、`INTConstant`、`WanVideoBlockSwap`、`MaskToImage`、`LoadImage`、`WanVideoSamplerFromSettings`、`PlaySound|pysssss`、`VHS_VideoInfoLoaded`、`Seed (rgthree)`、`WanVideoClipVisionEncode`、`Primitive integer [Crystools]`、`VHS_LoadVideo`、`SimpleMath+`、`SegmentQueueRunner`、`WanVideoAnimateEmbeds`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、WanVideoUni3C_ControlnetLoader、Seed (rgthree)、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoClipVisionEncode
