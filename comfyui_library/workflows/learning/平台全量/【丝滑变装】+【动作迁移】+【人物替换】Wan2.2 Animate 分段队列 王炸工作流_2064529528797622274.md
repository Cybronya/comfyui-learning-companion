---
key: 平台全量/【丝滑变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列 王炸工作流_2064529528797622274.json
name: 【丝滑变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列 王炸工作流_2064529528797622274
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【丝滑变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列 王炸工作流_2064529528797622274.json
hash: 2ebafb54ac0fb8ce
coverage: 0.45
learned_at: 2026-11-14 01:22:47
nodes: [GetNode, WanVideoSetLoRAs, SetNode, GetNode, SetNode, SetNode, WanVideoSetBlockSwap, GetNode, GetNode, SetNode, WanVideoTorchCompileSettings, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, WanVideoBlockSwap, WanVideoUni3C_ControlnetLoader, GetNode, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, BlockifyMask, DrawMaskOnImage, ImageResizeKJv2, SetNode, GetNode, Note, GetNode, SetNode, SetNode, WanVideoEncode, GetNode, PlaySound|pysssss, Note, VHS_VideoCombine, Note, SetNode, SetNode, WanVideoUni3C_embeds, LayerUtility: PurgeVRAM V2, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoModelLoader, CLIPVisionLoader, SetNode, ImageBlend, SetNode, Note, WanVideoContextOptions, LoadImage, VHS_VideoInfoLoaded, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, PoseAndFaceDetection, SetNode, WanVideoSamplerSettings, WanVideoDecode, GetNode, GetNode, SetNode, ImageResizeKJv2, VHS_VideoCombine, CheckpointLoaderSimple, MaskToImage, SetNode, Label (rgthree), GetNode, OnnxDetectionModelLoader, SAM3_Detect, GetNode, GetNode, GetNode, GrowMaskWithBlur, WanVideoSamplerFromSettings, PreviewImage, WanVideoTextEncodeCached, VHS_VideoCombine, SetNode, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), SDPoseKeypointExtractor, BodyRatioMapperSDPoseRender, BBoxYOLO, YOLOModelLoader, VHS_VideoCombine, INTConstant, INTConstant, ImageResizeKJv2, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), Seed (rgthree), Note, Note, SegmentQueueRunner, Note, CLIPTextEncode, WanVideoAnimateEmbeds, Fast Groups Bypasser (rgthree), Label (rgthree), GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, VHS_LoadVideo, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/【丝滑变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列 王炸工作流_2064529528797622274.json

> 来源文件 `comfyui_library/workflows/平台全量/【丝滑变装】+【动作迁移】+【人物替换】Wan2.2 Animate 分段队列 王炸工作流_2064529528797622274.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（120 个）：
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
- `LoadImage`
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
- `Label (rgthree)`
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
- `BBoxYOLO`
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
- `Note`
- `SegmentQueueRunner`
- `Note`
- `CLIPTextEncode` ★核心
- `WanVideoAnimateEmbeds`
- `Fast Groups Bypasser (rgthree)`
- `Label (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_LoadVideo`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **45%**（54/120）

**有卡**：`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoUni3C_ControlnetLoader`、`WanVideoClipVisionEncode`、`BlockifyMask`、`DrawMaskOnImage`、`ImageResizeKJv2`、`WanVideoEncode`、`PlaySound|pysssss`、`VHS_VideoCombine`、`WanVideoUni3C_embeds`、`LayerUtility: PurgeVRAM V2`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`WanVideoModelLoader`、`CLIPVisionLoader`、`ImageBlend`、`WanVideoContextOptions`、`LoadImage`、`VHS_VideoInfoLoaded`、`PoseAndFaceDetection`、`WanVideoSamplerSettings`、`WanVideoDecode`、`CheckpointLoaderSimple`、`MaskToImage`、`Label (rgthree)`、`OnnxDetectionModelLoader`、`SAM3_Detect`、`GrowMaskWithBlur`、`WanVideoSamplerFromSettings`、`WanVideoTextEncodeCached`、`SDPoseKeypointExtractor`、`BodyRatioMapperSDPoseRender`、`BBoxYOLO`、`YOLOModelLoader`、`INTConstant`、`Seed (rgthree)`、`SegmentQueueRunner`、`CLIPTextEncode`、`WanVideoAnimateEmbeds`、`VHS_LoadVideo`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、WanVideoUni3C_ControlnetLoader、Seed (rgthree)、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoClipVisionEncode
