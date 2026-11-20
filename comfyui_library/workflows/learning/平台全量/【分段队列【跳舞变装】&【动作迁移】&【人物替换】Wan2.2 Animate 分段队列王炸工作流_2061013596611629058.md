---
key: 平台全量/【分段队列【跳舞变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列王炸工作流_2061013596611629058.json
name: 【分段队列【跳舞变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列王炸工作流_2061013596611629058
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【分段队列【跳舞变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列王炸工作流_2061013596611629058.json
hash: f75c32c252c19001
coverage: 0.446809
learned_at: 2026-11-14 01:23:14
nodes: [GetNode, SetNode, WanVideoSetBlockSwap, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoUni3C_ControlnetLoader, GetNode, WanVideoClipVisionEncode, GetNode, GetNode, BlockifyMask, DrawMaskOnImage, GetNode, SetNode, WanVideoEncode, GetNode, Note, WanVideoUni3C_embeds, LayerUtility: PurgeVRAM V2, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, SetNode, ImageBlend, SetNode, WanVideoContextOptions, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, PoseAndFaceDetection, WanVideoSamplerSettings, WanVideoDecode, GetNode, SetNode, VHS_VideoCombine, CheckpointLoaderSimple, MaskToImage, SetNode, GetNode, OnnxDetectionModelLoader, SAM3_Detect, GetNode, GetNode, GetNode, GrowMaskWithBlur, WanVideoSamplerFromSettings, VHS_VideoCombine, SetNode, CheckpointLoaderSimple, Fast Groups Bypasser (rgthree), SDPoseKeypointExtractor, BodyRatioMapperSDPoseRender, BBoxYOLO, YOLOModelLoader, VHS_VideoCombine, ImageResizeKJv2, Fast Groups Bypasser (rgthree), LoadImage, Note, SetNode, WanVideoAnimateEmbeds, PreviewImage, Reroute, Reroute, ImageResizeKJv2, SetNode, GetNode, GetNode, WanVideoSetLoRAs, WanVideoBlockSwap, Note, CLIPVisionLoader, GetNode, SetNode, GetNode, VHS_VideoCombine, SetNode, SetNode, SetNode, SetNode, INTConstant, SetNode, INTConstant, MarkdownNote, Note, Note, VHS_VideoCombine, SegmentQueueRunner, PlaySound|pysssss, Label (rgthree), Fast Groups Bypasser (rgthree), GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy mathInt, easy mathInt, SetNode, VHS_LoadVideo, ImageResizeKJv2, VHS_VideoInfoLoaded, Note, Note, Seed (rgthree), WanVideoVAELoader, WanVideoModelLoader, WanVideoTorchCompileSettings, INTConstant, INTConstant, Label (rgthree), WanVideoTextEncodeCached, Reroute, Reroute, Note, SetNode, INTConstant, CLIPTextEncode, MuteSwitch, GetNode, GetNode, CR Text, Int, Fast Groups Bypasser (rgthree), CR Text, Fast Groups Bypasser (rgthree)]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/【分段队列【跳舞变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列王炸工作流_2061013596611629058.json

> 来源文件 `comfyui_library/workflows/平台全量/【分段队列【跳舞变装】&【动作迁移】&【人物替换】Wan2.2 Animate 分段队列王炸工作流_2061013596611629058.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（141 个）：
- `GetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoUni3C_ControlnetLoader`
- `GetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `BlockifyMask`
- `DrawMaskOnImage`
- `GetNode`
- `SetNode`
- `WanVideoEncode`
- `GetNode`
- `Note`
- `WanVideoUni3C_embeds`
- `LayerUtility: PurgeVRAM V2`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `ImageBlend`
- `SetNode`
- `WanVideoContextOptions`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `WanVideoSamplerSettings` ★核心
- `WanVideoDecode`
- `GetNode`
- `SetNode`
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
- `VHS_VideoCombine`
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `Fast Groups Bypasser (rgthree)`
- `SDPoseKeypointExtractor`
- `BodyRatioMapperSDPoseRender`
- `BBoxYOLO`
- `YOLOModelLoader`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `Note`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `PreviewImage`
- `Reroute`
- `Reroute`
- `ImageResizeKJv2`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `Note`
- `CLIPVisionLoader`
- `GetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `INTConstant`
- `SetNode`
- `INTConstant`
- `MarkdownNote`
- `Note`
- `Note`
- `VHS_VideoCombine`
- `SegmentQueueRunner`
- `PlaySound|pysssss`
- `Label (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy mathInt`
- `easy mathInt`
- `SetNode`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `VHS_VideoInfoLoaded`
- `Note`
- `Note`
- `Seed (rgthree)`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `INTConstant`
- `INTConstant`
- `Label (rgthree)`
- `WanVideoTextEncodeCached`
- `Reroute`
- `Reroute`
- `Note`
- `SetNode`
- `INTConstant`
- `CLIPTextEncode` ★核心
- `MuteSwitch`
- `GetNode`
- `GetNode`
- `CR Text`
- `Int`
- `Fast Groups Bypasser (rgthree)`
- `CR Text`
- `Fast Groups Bypasser (rgthree)`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **45%**（63/141）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoUni3C_ControlnetLoader`、`WanVideoClipVisionEncode`、`BlockifyMask`、`DrawMaskOnImage`、`WanVideoEncode`、`WanVideoUni3C_embeds`、`LayerUtility: PurgeVRAM V2`、`WanVideoLoraSelectMulti`、`ImageBlend`、`WanVideoContextOptions`、`VHS_VideoCombine`、`PoseAndFaceDetection`、`WanVideoSamplerSettings`、`WanVideoDecode`、`CheckpointLoaderSimple`、`MaskToImage`、`OnnxDetectionModelLoader`、`SAM3_Detect`、`GrowMaskWithBlur`、`WanVideoSamplerFromSettings`、`SDPoseKeypointExtractor`、`BodyRatioMapperSDPoseRender`、`BBoxYOLO`、`YOLOModelLoader`、`ImageResizeKJv2`、`LoadImage`、`WanVideoAnimateEmbeds`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`CLIPVisionLoader`、`INTConstant`、`SegmentQueueRunner`、`PlaySound|pysssss`、`Label (rgthree)`、`easy mathInt`、`VHS_LoadVideo`、`VHS_VideoInfoLoaded`、`Seed (rgthree)`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoTextEncodeCached`、`CLIPTextEncode`、`MuteSwitch`、`CR Text`、`Int`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、WanVideoUni3C_ControlnetLoader、Seed (rgthree)、WanVideoSamplerFromSettings、WanVideoSamplerSettings、WanVideoClipVisionEncode
