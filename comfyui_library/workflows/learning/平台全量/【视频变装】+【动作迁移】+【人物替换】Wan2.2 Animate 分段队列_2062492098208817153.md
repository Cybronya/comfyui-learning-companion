---
key: 平台全量/【视频变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列_2062492098208817153.json
name: 【视频变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列_2062492098208817153
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【视频变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列_2062492098208817153.json
hash: ada98b190197c8fa
coverage: 0.455285
learned_at: 2026-11-14 01:25:08
nodes: [GetNode, WanVideoSetLoRAs, SetNode, GetNode, SetNode, SetNode, SetNode, WanVideoSetBlockSwap, GetNode, GetNode, SetNode, WanVideoTorchCompileSettings, GetNode, SetNode, SetNode, GetNode, WanVideoUni3C_ControlnetLoader, GetNode, GetNode, BlockifyMask, DrawMaskOnImage, ImageResizeKJv2, GetNode, SetNode, SetNode, WanVideoEncode, PlaySound|pysssss, Note, SetNode, SetNode, WanVideoUni3C_embeds, LayerUtility: PurgeVRAM V2, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoModelLoader, SetNode, ImageBlend, SetNode, WanVideoContextOptions, VHS_VideoInfoLoaded, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, PoseAndFaceDetection, SetNode, WanVideoSamplerSettings, WanVideoDecode, GetNode, GetNode, SetNode, ImageResizeKJv2, SetNode, GetNode, OnnxDetectionModelLoader, SAM3_Detect, GetNode, GrowMaskWithBlur, PreviewImage, WanVideoTextEncodeCached, VHS_VideoCombine, SetNode, CheckpointLoaderSimple, SDPoseKeypointExtractor, BodyRatioMapperSDPoseRender, BBoxYOLO, YOLOModelLoader, ImageResizeKJv2, Seed (rgthree), Note, Note, CLIPTextEncode, GetNode, VHS_VideoCombine, WanVideoAnimateEmbeds, CLIPVisionLoader, Note, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, INTConstant, INTConstant, WanVideoClipVisionEncode, Fast Groups Bypasser (rgthree), GetNode, Fast Groups Bypasser (rgthree), Note, Fast Groups Bypasser (rgthree), GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Note, GetNode, GetNode, WanVideoSamplerFromSettings, WanVideoBlockSwap, CheckpointLoaderSimple, GetNode, GetNode, VHS_VideoCombine, MaskToImage, GetNode, VHS_VideoCombine, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Primitive integer [Crystools], SimpleMath+, Primitive integer [Crystools], VHS_LoadVideo, Note, LoadImage, VHS_VideoCombine, LoadImage, Note, SegmentQueueRunner]
patterns: []
missing: []
parameters: {"checkpoint": "sam3.1_multiplex_fp16.safetensors"}
---

# 平台全量/【视频变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列_2062492098208817153.json

> 来源文件 `comfyui_library/workflows/平台全量/【视频变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列_2062492098208817153.json`

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
- `PlaySound|pysssss`
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
- `VHS_VideoInfoLoaded`
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
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `SAM3_Detect`
- `GetNode`
- `GrowMaskWithBlur`
- `PreviewImage`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `BodyRatioMapperSDPoseRender`
- `BBoxYOLO`
- `YOLOModelLoader`
- `ImageResizeKJv2`
- `Seed (rgthree)`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `CLIPVisionLoader`
- `Note`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `WanVideoClipVisionEncode`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Note`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Note`
- `GetNode`
- `GetNode`
- `WanVideoSamplerFromSettings` ★核心
- `WanVideoBlockSwap`
- `CheckpointLoaderSimple` ★核心
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `MaskToImage`
- `GetNode`
- `VHS_VideoCombine`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Primitive integer [Crystools]`
- `SimpleMath+`
- `Primitive integer [Crystools]`
- `VHS_LoadVideo`
- `Note`
- `LoadImage`
- `VHS_VideoCombine`
- `LoadImage`
- `Note`
- `SegmentQueueRunner`

## 关键参数

- `checkpoint` = `sam3.1_multiplex_fp16.safetensors`

## 知识

覆盖率 **46%**（56/123）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoUni3C_ControlnetLoader`、`BlockifyMask`、`DrawMaskOnImage`、`ImageResizeKJv2`、`WanVideoEncode`、`PlaySound|pysssss`、`WanVideoUni3C_embeds`、`LayerUtility: PurgeVRAM V2`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`、`ImageBlend`、`WanVideoContextOptions`、`VHS_VideoInfoLoaded`、`VHS_VideoCombine`、`PoseAndFaceDetection`、`WanVideoSamplerSettings`、`WanVideoDecode`、`OnnxDetectionModelLoader`、`SAM3_Detect`、`GrowMaskWithBlur`、`WanVideoTextEncodeCached`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`BodyRatioMapperSDPoseRender`、`BBoxYOLO`、`YOLOModelLoader`、`Seed (rgthree)`、`CLIPTextEncode`、`WanVideoAnimateEmbeds`、`CLIPVisionLoader`、`INTConstant`、`WanVideoClipVisionEncode`、`WanVideoSamplerFromSettings`、`WanVideoBlockSwap`、`MaskToImage`、`Primitive integer [Crystools]`、`SimpleMath+`、`VHS_LoadVideo`、`LoadImage`、`SegmentQueueRunner`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、WanVideoUni3C_ControlnetLoader、Seed (rgthree)、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoClipVisionEncode
