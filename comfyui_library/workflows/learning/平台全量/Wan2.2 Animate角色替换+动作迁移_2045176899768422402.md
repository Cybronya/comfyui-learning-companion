---
key: 平台全量/Wan2.2 Animate角色替换+动作迁移_2045176899768422402.json
name: Wan2.2 Animate角色替换+动作迁移_2045176899768422402
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate角色替换+动作迁移_2045176899768422402.json
hash: 42509b03f47cd2e0
coverage: 0.502825
learned_at: 2026-11-14 01:05:26
nodes: [GetNode, GetNode, GetNode, GetNode, CLIPVisionLoader, ImageFromBatch, GetNode, GetNode, GetNode, WanVideoClipVisionEncode, RepeatImageBatch, GetNode, GetNode, GetNode, GetNode, GetNode, PreviewImage, Note, SetNode, SetNode, SetNode, SetNode, Note, GetNode, OnnxDetectionModelLoader, PoseDetectionVitPoseToDWPose, PoseDetectionVitPoseToDWPose, Note, WanVideoDecode, WanVideoLoraSelectMulti, SetNode, DownloadAndLoadNLFModel, Note, easy float, easy boolean, SetNode, Note, WanVideoLoraSelectMulti, RenderNLFPoses, MemoryCleaner, WanVideoModelLoader, WanVideoSetLoRAs, easy int, WanVideoAnimateEmbeds, easy float, Note, ImageFromBatch, ImageBatch, easy mathInt, BatchCount+, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, BatchCount+, LazySwitch2way, easy int, Note, Note, Reroute, YOLOModelLoader, easy anythingIndexSwitch, CheckpointLoaderSimple, SDPoseKeypointExtractor, WanVideoBlockSwap, PreviewAny, Note, easy sam3GetObjectIds, MaskToImage, MaskToImage, easy sam3Visualization, easy sam3VideoModelExtraConfig, MaskToImage, Note, Note, easy sam3GetObjectMask, easy sam3GetObjectMask, VHS_VideoCombine, VHS_VideoCombine, MemoryCleaner, SetNode, GetNode, SetNode, SetNode, VHS_VideoCombine, easy sam3ModelLoader, PreviewAny, Note, easy framesEditor, GetNode, SetNode, easy int, easy float, BlockifyMask, GrowMaskWithBlur, GetNode, ImageResizeKJv2, ImpactSwitch, SetNode, SetNode, SetNode, DrawMaskOnImage, VHS_VideoInfo, easy mathInt, GetNode, GetNode, MemoryCleaner, GetNode, GetNode, SetNode, SetNode, WanVideoVAELoader, GetNode, easy int, LayerUtility: PurgeVRAM, GetNode, WanVideoSampler, SetNode, WanVideoTextEncodeCached, WanVideoContextOptions, WanVideoSetBlockSwap, ImageBlend, GetNode, GetNode, GetNode, GetNode, GetNode, PoseAndFaceDetection, DrawViTPose, NLFPredict, PoseAndFaceDetection, BBoxYOLO, LazySwitch1way, GetNode, OnnxDetectionModelLoader, SetNode, SetNode, VHS_VideoCombine, VHS_VideoCombine, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, CR Text, CR Text, LayerUtility: ImageScaleByAspectRatio V2, LazySwitch1way, easy compare, easy imageSize, SetNode, easy sam3VideoSegmentation, GetNode, GetNode, Note, Note, Note, GetNode, easy int, Note, Note, GetNode, GetNode, Fast Groups Bypasser (rgthree), Fast Groups Bypasser (rgthree), SDPoseDrawKeypoints, LoadImage, easy int, easy boolean, VHS_LoadVideo, ImageResizeKJv2, VHS_VideoCombine]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 平台全量/Wan2.2 Animate角色替换+动作迁移_2045176899768422402.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate角色替换+动作迁移_2045176899768422402.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（177 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoClipVisionEncode`
- `RepeatImageBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `Note`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Note`
- `GetNode`
- `OnnxDetectionModelLoader`
- `PoseDetectionVitPoseToDWPose`
- `PoseDetectionVitPoseToDWPose`
- `Note`
- `WanVideoDecode`
- `WanVideoLoraSelectMulti`
- `SetNode`
- `DownloadAndLoadNLFModel`
- `Note`
- `easy float`
- `easy boolean`
- `SetNode`
- `Note`
- `WanVideoLoraSelectMulti`
- `RenderNLFPoses`
- `MemoryCleaner`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `easy int`
- `WanVideoAnimateEmbeds`
- `easy float`
- `Note`
- `ImageFromBatch`
- `ImageBatch`
- `easy mathInt`
- `BatchCount+`
- `SetNode`
- `RepeatImageBatch`
- `SetNode`
- `SetNode`
- `RHHiddenNodes`
- `BatchCount+`
- `LazySwitch2way`
- `easy int`
- `Note`
- `Note`
- `Reroute`
- `YOLOModelLoader`
- `easy anythingIndexSwitch`
- `CheckpointLoaderSimple` ★核心
- `SDPoseKeypointExtractor`
- `WanVideoBlockSwap`
- `PreviewAny`
- `Note`
- `easy sam3GetObjectIds`
- `MaskToImage`
- `MaskToImage`
- `easy sam3Visualization`
- `easy sam3VideoModelExtraConfig`
- `MaskToImage`
- `Note`
- `Note`
- `easy sam3GetObjectMask`
- `easy sam3GetObjectMask`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MemoryCleaner`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `easy sam3ModelLoader`
- `PreviewAny`
- `Note`
- `easy framesEditor`
- `GetNode`
- `SetNode`
- `easy int`
- `easy float`
- `BlockifyMask`
- `GrowMaskWithBlur`
- `GetNode`
- `ImageResizeKJv2`
- `ImpactSwitch`
- `SetNode`
- `SetNode`
- `SetNode`
- `DrawMaskOnImage`
- `VHS_VideoInfo`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `MemoryCleaner`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `GetNode`
- `easy int`
- `LayerUtility: PurgeVRAM`
- `GetNode`
- `WanVideoSampler` ★核心
- `SetNode`
- `WanVideoTextEncodeCached`
- `WanVideoContextOptions`
- `WanVideoSetBlockSwap`
- `ImageBlend`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `NLFPredict`
- `PoseAndFaceDetection`
- `BBoxYOLO`
- `LazySwitch1way`
- `GetNode`
- `OnnxDetectionModelLoader`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CR Text`
- `CR Text`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LazySwitch1way`
- `easy compare`
- `easy imageSize`
- `SetNode`
- `easy sam3VideoSegmentation`
- `GetNode`
- `GetNode`
- `Note`
- `Note`
- `Note`
- `GetNode`
- `easy int`
- `Note`
- `Note`
- `GetNode`
- `GetNode`
- `Fast Groups Bypasser (rgthree)`
- `Fast Groups Bypasser (rgthree)`
- `SDPoseDrawKeypoints`
- `LoadImage`
- `easy int`
- `easy boolean`
- `VHS_LoadVideo`
- `ImageResizeKJv2`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **50%**（89/177）

**有卡**：`CLIPVisionLoader`、`ImageFromBatch`、`WanVideoClipVisionEncode`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`PoseDetectionVitPoseToDWPose`、`WanVideoDecode`、`WanVideoLoraSelectMulti`、`DownloadAndLoadNLFModel`、`easy float`、`easy boolean`、`RenderNLFPoses`、`MemoryCleaner`、`WanVideoModelLoader`、`WanVideoSetLoRAs`、`easy int`、`WanVideoAnimateEmbeds`、`ImageBatch`、`easy mathInt`、`BatchCount+`、`RHHiddenNodes`、`LazySwitch2way`、`YOLOModelLoader`、`easy anythingIndexSwitch`、`CheckpointLoaderSimple`、`SDPoseKeypointExtractor`、`WanVideoBlockSwap`、`easy sam3GetObjectIds`、`MaskToImage`、`easy sam3Visualization`、`easy sam3VideoModelExtraConfig`、`easy sam3GetObjectMask`、`VHS_VideoCombine`、`easy sam3ModelLoader`、`easy framesEditor`、`BlockifyMask`、`GrowMaskWithBlur`、`ImageResizeKJv2`、`DrawMaskOnImage`、`VHS_VideoInfo`、`WanVideoVAELoader`、`LayerUtility: PurgeVRAM`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoContextOptions`、`WanVideoSetBlockSwap`、`ImageBlend`、`PoseAndFaceDetection`、`DrawViTPose`、`NLFPredict`、`BBoxYOLO`、`LazySwitch1way`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy compare`、`easy imageSize`、`easy sam3VideoSegmentation`、`SDPoseDrawKeypoints`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：CheckpointLoaderSimple、LayerUtility: ImageScaleByAspectRatio V2、LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader
