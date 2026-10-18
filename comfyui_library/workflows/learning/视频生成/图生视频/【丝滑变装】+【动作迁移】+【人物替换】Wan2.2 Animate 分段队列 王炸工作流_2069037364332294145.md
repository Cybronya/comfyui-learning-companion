---
key: 视频生成/图生视频/【丝滑变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列 王炸工作流_2069037364332294145.json
name: 【丝滑变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列 王炸工作流_2069037364332294145.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【丝滑变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列 王炸工作流_2069037364332294145.json
hash: cd8133286a877a6b
coverage: 0.440678
learned_at: 2026-10-15 22:40:26
nodes: [GetNode, WanVideoSetLoRAs, SetNode, GetNode, SetNode, SetNode, WanVideoSetBlockSwap, GetNode, GetNode, SetNode, WanVideoTorchCompileSettings, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, WanVideoBlockSwap, WanVideoUni3C_ControlnetLoader, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, BlockifyMask, DrawMaskOnImage, ImageResizeKJv2, SetNode, GetNode, Note, GetNode, SetNode, SetNode, WanVideoEncode, GetNode, PlaySound|pysssss, Note, VHS_VideoCombine, Note, SetNode, SetNode, WanVideoUni3C_embeds, LayerUtility: PurgeVRAM V2, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoModelLoader, CLIPVisionLoader, SetNode, ImageBlend, SetNode, Note, WanVideoContextOptions, VHS_VideoInfoLoaded, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, PoseAndFaceDetection, SetNode, WanVideoSamplerSettings, WanVideoDecode, GetNode, GetNode, SetNode, ImageResizeKJv2, VHS_VideoCombine, CheckpointLoaderSimple, MaskToImage, SetNode, GetNode, OnnxDetectionModelLoader, SAM3_Detect, GetNode, GetNode, GetNode, GrowMaskWithBlur, WanVideoSamplerFromSettings, PreviewImage, WanVideoTextEncodeCached, VHS_VideoCombine, SetNode, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), SDPoseKeypointExtractor, BodyRatioMapperSDPoseRender, YOLOModelLoader, VHS_VideoCombine, INTConstant, INTConstant, ImageResizeKJv2, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Seed (rgthree), Note, SegmentQueueRunner, Note, CLIPTextEncode, WanVideoAnimateEmbeds, Fast Groups Bypasser (rgthree), GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, VHS_LoadVideo, VHS_VideoCombine, LoadImage, Note, BBoxYOLO]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/【丝滑变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列 王炸工作流_2069037364332294145.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2069037364332294145.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（118 个）：
- `GetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoUni3C_ControlnetLoader`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
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
- `GetNode`
- `PlaySound|pysssss`
- `Note`
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
- `CLIPVisionLoader`
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
- `Fast Groups Bypasser (rgthree)`
- `SDPoseKeypointExtractor`
- `BodyRatioMapperSDPoseRender`
- `YOLOModelLoader`
- `VHS_VideoCombine`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `Seed (rgthree)`
- `Note`
- `SegmentQueueRunner`
- `Note`
- `CLIPTextEncode` ★核心
- `WanVideoAnimateEmbeds`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `LoadImage`
- `Note`
- `BBoxYOLO`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **44%**（52/118）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoUni3C_ControlnetLoader`、`WanVideoClipVisionEncode`、`BlockifyMask`、`DrawMaskOnImage`、`ImageResizeKJv2`、`WanVideoEncode`、`PlaySound|pysssss`、`VHS_VideoCombine`、`WanVideoUni3C_embeds`、`LayerUtility: PurgeVRAM V2`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`、`CLIPVisionLoader`、`ImageBlend`、`WanVideoContextOptions`、`VHS_VideoInfoLoaded`、`PoseAndFaceDetection`、`WanVideoSamplerSettings`、`WanVideoDecode`、`CheckpointLoaderSimple`、`MaskToImage`、`OnnxDetectionModelLoader`、`SAM3_Detect`、`GrowMaskWithBlur`、`WanVideoSamplerFromSettings`、`WanVideoTextEncodeCached`、`SDPoseKeypointExtractor`、`BodyRatioMapperSDPoseRender`、`YOLOModelLoader`、`INTConstant`、`Seed (rgthree)`、`SegmentQueueRunner`、`CLIPTextEncode`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`、`LoadImage`、`BBoxYOLO`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、WanVideoUni3C_ControlnetLoader、WanVideoSamplerFromSettings、WanVideoSamplerSettings、Seed (rgthree)、WanVideoDecode
