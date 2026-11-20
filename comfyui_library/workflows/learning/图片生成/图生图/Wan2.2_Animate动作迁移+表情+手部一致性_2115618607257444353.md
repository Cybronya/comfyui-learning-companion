---
key: 图片生成/图生图/Wan2.2_Animate动作迁移+表情+手部一致性_2115618607257444353.json
name: Wan2.2_Animate动作迁移+表情+手部一致性_2115618607257444353
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/Wan2.2_Animate动作迁移+表情+手部一致性_2115618607257444353.json
hash: 04c46978303c41d4
coverage: 0.547619
learned_at: 2026-10-30 17:51:27
nodes: [GetNode, GetNode, GetNode, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, RepeatImageBatch, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, LazySwitch1way, GetNode, PreviewImage, SetNode, SetNode, ImageResizeKJv2, PoseAndFaceDetection, SetNode, GetNode, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, GetNode, PoseDetectionVitPoseToDWPose, PoseAndFaceDetection, SetNode, SetNode, WanVideoLoraSelectMulti, GetNode, MemoryCleaner, SetNode, easy int, ImageFromBatch, ImageBatch, GetNode, easy mathInt, SetNode, RepeatImageBatch, SetNode, SetNode, RHHiddenNodes, Reroute, YOLOModelLoader, BBoxYOLO, WanVideoContextOptions, CheckpointLoaderSimple, easy float, SetNode, WanVideoLoraSelectMulti, easy float, easy mathInt, RenderNLFPoses, DrawViTPose, DownloadAndLoadNLFModel, easy anythingIndexSwitch, SDPoseDrawKeypoints, BatchCount+, GetNode, BatchCount+, SDPoseKeypointExtractor, SetNode, WanVideoAnimateEmbeds, GetNode, GetNode, GetNode, MemoryCleaner, MemoryCleaner, WanVideoDecode, GetNode, GetNode, CLIPVisionLoader, SetNode, SetNode, WanVideoClipVisionEncode, SetNode, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoTextEncodeCached, SetNode, WanVideoSampler, VHS_VideoCombine, easy int, easy int, easy int, easy int, WanVideoBlockSwap, easy boolean, easy int, ImpactSwitch, easy boolean, easy float, LoadImage, easy compare, VHS_VideoInfo, SetNode, SetNode, SetNode, SetNode, SimpleMath+, LazySwitch2way, CR Text, CR Text, LazySwitch1way, LayerUtility: ImageScaleByAspectRatio V2, easy imageSize, SetNode, VHS_LoadVideo, LoadImage, 孤海注释]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 图片生成/图生图/Wan2.2_Animate动作迁移+表情+手部一致性_2115618607257444353.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/Wan2.2_Animate动作迁移+表情+手部一致性_2115618607257444353.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（126 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
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
- `GetNode`
- `GetNode`
- `RepeatImageBatch`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LazySwitch1way`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `PoseAndFaceDetection`
- `SetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `NLFPredict`
- `PoseDetectionVitPoseToDWPose`
- `GetNode`
- `PoseDetectionVitPoseToDWPose`
- `PoseAndFaceDetection`
- `SetNode`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `GetNode`
- `MemoryCleaner`
- `SetNode`
- `easy int`
- `ImageFromBatch`
- `ImageBatch`
- `GetNode`
- `easy mathInt`
- `SetNode`
- `RepeatImageBatch`
- `SetNode`
- `SetNode`
- `RHHiddenNodes`
- `Reroute`
- `YOLOModelLoader`
- `BBoxYOLO`
- `WanVideoContextOptions`
- `CheckpointLoaderSimple` ★核心
- `easy float`
- `SetNode`
- `WanVideoLoraSelectMulti`
- `easy float`
- `easy mathInt`
- `RenderNLFPoses`
- `DrawViTPose`
- `DownloadAndLoadNLFModel`
- `easy anythingIndexSwitch`
- `SDPoseDrawKeypoints`
- `BatchCount+`
- `GetNode`
- `BatchCount+`
- `SDPoseKeypointExtractor`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `MemoryCleaner`
- `MemoryCleaner`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `SetNode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `easy int`
- `easy int`
- `easy int`
- `easy int`
- `WanVideoBlockSwap`
- `easy boolean`
- `easy int`
- `ImpactSwitch`
- `easy boolean`
- `easy float`
- `LoadImage`
- `easy compare`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `LazySwitch2way`
- `CR Text`
- `CR Text`
- `LazySwitch1way`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy imageSize`
- `SetNode`
- `VHS_LoadVideo`
- `LoadImage`
- `孤海注释`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **55%**（69/126）

**有卡**：`ImageFromBatch`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`LazySwitch1way`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`WanVideoLoraSelectMulti`、`MemoryCleaner`、`easy int`、`ImageBatch`、`easy mathInt`、`RHHiddenNodes`、`YOLOModelLoader`、`BBoxYOLO`、`WanVideoContextOptions`、`CheckpointLoaderSimple`、`easy float`、`RenderNLFPoses`、`DrawViTPose`、`DownloadAndLoadNLFModel`、`easy anythingIndexSwitch`、`SDPoseDrawKeypoints`、`BatchCount+`、`SDPoseKeypointExtractor`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`easy boolean`、`LoadImage`、`easy compare`、`VHS_VideoInfo`、`SimpleMath+`、`LazySwitch2way`、`CR Text`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy imageSize`、`VHS_LoadVideo`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
