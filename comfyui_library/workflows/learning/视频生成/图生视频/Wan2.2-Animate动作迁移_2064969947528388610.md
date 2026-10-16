---
key: 视频生成/图生视频/Wan2.2-Animate动作迁移_2064969947528388610.json
name: Wan2.2-Animate动作迁移_2064969947528388610.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2064969947528388610.json
hash: eaff437689b968a8
coverage: 0.559633
learned_at: 2026-10-15 22:39:32
nodes: [SetNode, ImageFromBatch, BatchCount+, ImageBatch, RepeatImageBatch, easy mathInt, GetNode, easy mathInt, SetNode, SetNode, SetNode, SetNode, GetNode, WanAnimatePlus SetLoRAs, WanAnimatePlus SetBlockSwap, WanAnimatePlus ClipVisionEncode, SetNode, SetNode, WanAnimatePlus Uni3C Embeds, WanAnimatePlus Encode, SetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, SetNode, WanAnimatePlus Decode, GetNode, VHS_VideoCombine, GetNode, GetNode, GetNode, GetNode, SDPoseDrawKeypoints, easy float, WanAnimatePlus LoraSelectMulti, WanAnimatePlus LoraSelectMulti, WanAnimatePlus Uni3C ControlnetLoader, easy cleanGpuUsed, SetNode, SetNode, OnnxDetectionModelLoader, VHS_VideoInfo, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SDPoseKeypointExtractor, PoseAndFaceDetection, LazySwitch1way, RepeatImageBatch, LazySwitch1way, SetNode, GetNode, GetNode, WanAnimatePlus Sampler, SetNode, GetNode, GetNode, ImageFromBatch, PreviewImage, LazySwitch1way, easy compare, LazySwitch2way, GetImageSize+, LayerUtility: ImageScaleByAspectRatio V2, VHS_LoadVideo, WanAnimatePlus ModelLoader, GetNode, WanAnimatePlus ContextOptions, WanAnimatePlus AnimateEmbeds, SetNode, WanAnimatePlus TextEncodeCached, WanAnimatePlus VAELoader, WanAnimatePlus BlockSwap, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, GetNode, CLIPVisionLoader, GetNode, LoadImage, BatchCount+, RHHiddenNodes, BBoxYOLO, easy int, easy int, easy int, easy int, easy boolean, easy int, CR Text, CR Text, SetNode, easy boolean, YOLOModelLoader, CheckpointLoaderSimple, easy float, easy float, Fast Groups Bypasser (rgthree), ImageResizeKJv2]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2-Animate动作迁移_2064969947528388610.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2064969947528388610.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（109 个）：
- `SetNode`
- `ImageFromBatch`
- `BatchCount+`
- `ImageBatch`
- `RepeatImageBatch`
- `easy mathInt`
- `GetNode`
- `easy mathInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanAnimatePlus SetLoRAs`
- `WanAnimatePlus SetBlockSwap`
- `WanAnimatePlus ClipVisionEncode`
- `SetNode`
- `SetNode`
- `WanAnimatePlus Uni3C Embeds`
- `WanAnimatePlus Encode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanAnimatePlus Decode`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SDPoseDrawKeypoints`
- `easy float`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus LoraSelectMulti`
- `WanAnimatePlus Uni3C ControlnetLoader`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SDPoseKeypointExtractor`
- `PoseAndFaceDetection`
- `LazySwitch1way`
- `RepeatImageBatch`
- `LazySwitch1way`
- `SetNode`
- `GetNode`
- `GetNode`
- `WanAnimatePlus Sampler` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `PreviewImage`
- `LazySwitch1way`
- `easy compare`
- `LazySwitch2way`
- `GetImageSize+`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `VHS_LoadVideo`
- `WanAnimatePlus ModelLoader`
- `GetNode`
- `WanAnimatePlus ContextOptions`
- `WanAnimatePlus AnimateEmbeds`
- `SetNode`
- `WanAnimatePlus TextEncodeCached`
- `WanAnimatePlus VAELoader`
- `WanAnimatePlus BlockSwap`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `GetNode`
- `CLIPVisionLoader`
- `GetNode`
- `LoadImage`
- `BatchCount+`
- `RHHiddenNodes`
- `BBoxYOLO`
- `easy int`
- `easy int`
- `easy int`
- `easy int`
- `easy boolean`
- `easy int`
- `CR Text`
- `CR Text`
- `SetNode`
- `easy boolean`
- `YOLOModelLoader`
- `CheckpointLoaderSimple` ★核心
- `easy float`
- `easy float`
- `Fast Groups Bypasser (rgthree)`
- `ImageResizeKJv2`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **56%**（61/109）

**有卡**：`ImageFromBatch`、`BatchCount+`、`ImageBatch`、`RepeatImageBatch`、`easy mathInt`、`WanAnimatePlus SetLoRAs`、`WanAnimatePlus SetBlockSwap`、`WanAnimatePlus ClipVisionEncode`、`WanAnimatePlus Uni3C Embeds`、`WanAnimatePlus Encode`、`WanAnimatePlus Decode`、`VHS_VideoCombine`、`SDPoseDrawKeypoints`、`easy float`、`WanAnimatePlus LoraSelectMulti`、`WanAnimatePlus Uni3C ControlnetLoader`、`easy cleanGpuUsed`、`OnnxDetectionModelLoader`、`VHS_VideoInfo`、`SDPoseKeypointExtractor`、`PoseAndFaceDetection`、`LazySwitch1way`、`WanAnimatePlus Sampler`、`easy compare`、`LazySwitch2way`、`GetImageSize+`、`LayerUtility: ImageScaleByAspectRatio V2`、`VHS_LoadVideo`、`WanAnimatePlus ModelLoader`、`WanAnimatePlus ContextOptions`、`WanAnimatePlus AnimateEmbeds`、`WanAnimatePlus TextEncodeCached`、`WanAnimatePlus VAELoader`、`WanAnimatePlus BlockSwap`、`CLIPVisionLoader`、`LoadImage`、`RHHiddenNodes`、`BBoxYOLO`、`easy int`、`easy boolean`、`CR Text`、`YOLOModelLoader`、`CheckpointLoaderSimple`、`ImageResizeKJv2`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanAnimatePlus Uni3C ControlnetLoader、WanAnimatePlus Sampler、WanAnimatePlus ClipVisionEncode、WanAnimatePlus Decode、WanAnimatePlus Encode
