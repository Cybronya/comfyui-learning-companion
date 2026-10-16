---
key: 视频生成/图生视频/【丝滑变装】&【动作迁移】&【人物替换】Wan2.2+Animate+分段队列+ (1)_2064236484089171969.json
name: 【丝滑变装】&【动作迁移】&【人物替换】Wan2.2+Animate+分段队列+ (1)_2064236484089171969.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064236484089171969.json
hash: 161c771a883f9bf0
coverage: 0.440678
learned_at: 2026-10-15 22:39:21
nodes: [GetNode, WanVideoSetLoRAs, SetNode, GetNode, SetNode, SetNode, SetNode, WanVideoSetBlockSwap, GetNode, GetNode, SetNode, WanVideoTorchCompileSettings, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoBlockSwap, WanVideoUni3C_ControlnetLoader, GetNode, GetNode, BlockifyMask, DrawMaskOnImage, ImageResizeKJv2, SetNode, GetNode, Note, GetNode, SetNode, SetNode, WanVideoEncode, PlaySound|pysssss, VHS_VideoCombine, Note, SetNode, SetNode, WanVideoUni3C_embeds, LayerUtility: PurgeVRAM V2, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoModelLoader, SetNode, ImageBlend, SetNode, Note, WanVideoContextOptions, VHS_VideoInfoLoaded, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, PoseAndFaceDetection, SetNode, WanVideoSamplerSettings, WanVideoDecode, GetNode, GetNode, SetNode, ImageResizeKJv2, VHS_VideoCombine, CheckpointLoaderSimple, MaskToImage, SetNode, GetNode, OnnxDetectionModelLoader, SAM3_Detect, GetNode, GetNode, GetNode, GrowMaskWithBlur, WanVideoSamplerFromSettings, PreviewImage, WanVideoTextEncodeCached, VHS_VideoCombine, SetNode, CheckpointLoaderSimple, SDPoseKeypointExtractor, BodyRatioMapperSDPoseRender, BBoxYOLO, YOLOModelLoader, VHS_VideoCombine, ImageResizeKJv2, Seed (rgthree), Note, Note, Note, CLIPTextEncode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), GetNode, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoClipVisionEncode, GetNode, CLIPVisionLoader, Note, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, INTConstant, INTConstant, VHS_LoadVideo, SegmentQueueRunner, LoadImage]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/【丝滑变装】&【动作迁移】&【人物替换】Wan2.2+Animate+分段队列+ (1)_2064236484089171969.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064236484089171969.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（118 个）：
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
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoUni3C_ControlnetLoader`
- `GetNode`
- `GetNode`
- `BlockifyMask`
- `DrawMaskOnImage`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `Note`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoEncode`
- `PlaySound|pysssss`
- `VHS_VideoCombine`
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
- `Note`
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
- `VHS_VideoCombine`
- `CheckpointLoaderSimple` ★核心
- `MaskToImage`
- `SetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `SAM3_Detect`
- `GetNode`
- `GetNode`
- `GetNode`
- `GrowMaskWithBlur`
- `WanVideoSamplerFromSettings` ★核心
- `PreviewImage`
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `BodyRatioMapperSDPoseRender`
- `BBoxYOLO`
- `YOLOModelLoader`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `Seed (rgthree)`
- `Note`
- `Note`
- `Note`
- `CLIPTextEncode` ★核心
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoClipVisionEncode`
- `GetNode`
- `CLIPVisionLoader`
- `Note`
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
- `INTConstant`
- `INTConstant`
- `VHS_LoadVideo`
- `SegmentQueueRunner`
- `LoadImage`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **44%**（52/118）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoUni3C_ControlnetLoader`、`BlockifyMask`、`DrawMaskOnImage`、`ImageResizeKJv2`、`WanVideoEncode`、`PlaySound|pysssss`、`VHS_VideoCombine`、`WanVideoUni3C_embeds`、`LayerUtility: PurgeVRAM V2`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`、`ImageBlend`、`WanVideoContextOptions`、`VHS_VideoInfoLoaded`、`PoseAndFaceDetection`、`WanVideoSamplerSettings`、`WanVideoDecode`、`CheckpointLoaderSimple`、`MaskToImage`、`OnnxDetectionModelLoader`、`SAM3_Detect`、`GrowMaskWithBlur`、`WanVideoSamplerFromSettings`、`WanVideoTextEncodeCached`、`SDPoseKeypointExtractor`、`BodyRatioMapperSDPoseRender`、`BBoxYOLO`、`YOLOModelLoader`、`Seed (rgthree)`、`CLIPTextEncode`、`WanVideoAnimateEmbeds`、`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`INTConstant`、`VHS_LoadVideo`、`SegmentQueueRunner`、`LoadImage`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSamplerFromSettings、WanVideoSamplerSettings、Seed (rgthree)、WanVideoDecode
