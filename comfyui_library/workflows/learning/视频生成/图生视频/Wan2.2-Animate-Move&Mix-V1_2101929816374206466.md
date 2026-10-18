---
key: 视频生成/图生视频/Wan2.2-Animate-Move&Mix-V1_2101929816374206466.json
name: Wan2.2-Animate-Move&Mix-V1_2101929816374206466
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-Animate-Move&Mix-V1_2101929816374206466.json
hash: 0207821c7425215c
coverage: 0.802198
learned_at: 2026-10-17 02:29:29
nodes: [WanVideoClipVisionEncode, WanVideoVAELoader, WanVideoTextEncodeCached, easy int, easy int, Note, Note, Note, Note, easy int, easy boolean, easy int, ImpactSwitch, easy int, easy int, WanVideoSetLoRAs, WanVideoSetBlockSwap, SDPoseKeypointExtractor, BBoxYOLO, YOLOModelLoader, BatchCount+, ImageFromBatch, CLIPVisionLoader, DownloadAndLoadNLFModel, RenderNLFPoses, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, PoseDetectionVitPoseToDWPose, SDPoseDrawKeypoints, CheckpointLoaderSimple, Reroute, Note, DrawViTPose, OnnxDetectionModelLoader, LazySwitch1way, easy anythingIndexSwitch, WanVideoBlockSwap, PoseAndFaceDetection, ImageBatch, MemoryCleaner, easy float, easy float, Note, Note, easy mathInt, RepeatImageBatch, PoseAndFaceDetection, WanVideoContextOptions, VHS_VideoCombine, ImageFromBatch, WanVideoSampler, Note, Note, WanVideoLoraSelectMulti, LazySwitch2way, easy boolean, Note, Note, Note, WanVideoModelLoader, WanVideoLoraSelectMulti, ImageResizeKJv2, PreviewImage, VHS_VideoCombine, WanVideoAnimateEmbeds, Fast Groups Bypasser (rgthree), easy imageSize, CR Text, easy compare, LazySwitch1way, LayerUtility: ImageScaleByAspectRatio V2, easy float, Note, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMaskWithBlur, BlockifyMask, DrawMaskOnImage, WanVideoAnimateEmbeds, RepeatImageBatch, RHHiddenNodes, BatchCount+, MemoryCleaner, WanVideoDecode, Any Switch (rgthree), CR Text, VHS_VideoInfo, VHS_VideoCombine, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 视频生成/图生视频/Wan2.2-Animate-Move&Mix-V1_2101929816374206466.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/Wan2.2-Animate-Move&Mix-V1_2101929816374206466.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（91 个）：
- `WanVideoClipVisionEncode`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `easy int`
- `easy int`
- `Note`
- `Note`
- `Note`
- `Note`
- `easy int`
- `easy boolean`
- `easy int`
- `ImpactSwitch`
- `easy int`
- `easy int`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `SDPoseKeypointExtractor`
- `BBoxYOLO`
- `YOLOModelLoader`
- `BatchCount+`
- `ImageFromBatch`
- `CLIPVisionLoader`
- `DownloadAndLoadNLFModel`
- `RenderNLFPoses`
- `OnnxDetectionModelLoader`
- `NLFPredict`
- `PoseDetectionVitPoseToDWPose`
- `PoseDetectionVitPoseToDWPose`
- `SDPoseDrawKeypoints`
- `CheckpointLoaderSimple` ★核心
- `Reroute`
- `Note`
- `DrawViTPose`
- `OnnxDetectionModelLoader`
- `LazySwitch1way`
- `easy anythingIndexSwitch`
- `WanVideoBlockSwap`
- `PoseAndFaceDetection`
- `ImageBatch`
- `MemoryCleaner`
- `easy float`
- `easy float`
- `Note`
- `Note`
- `easy mathInt`
- `RepeatImageBatch`
- `PoseAndFaceDetection`
- `WanVideoContextOptions`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `WanVideoSampler` ★核心
- `Note`
- `Note`
- `WanVideoLoraSelectMulti`
- `LazySwitch2way`
- `easy boolean`
- `Note`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `ImageResizeKJv2`
- `PreviewImage`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `Fast Groups Bypasser (rgthree)`
- `easy imageSize`
- `CR Text`
- `easy compare`
- `LazySwitch1way`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy float`
- `Note`
- `DownloadAndLoadSAM2Model`
- `Sam2Segmentation`
- `GrowMaskWithBlur`
- `BlockifyMask`
- `DrawMaskOnImage`
- `WanVideoAnimateEmbeds`
- `RepeatImageBatch`
- `RHHiddenNodes`
- `BatchCount+`
- `MemoryCleaner`
- `WanVideoDecode`
- `Any Switch (rgthree)`
- `CR Text`
- `VHS_VideoInfo`
- `VHS_VideoCombine`
- `LoadImage`
- `VHS_LoadVideo`

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **80%**（73/91）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`easy int`、`easy boolean`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`SDPoseKeypointExtractor`、`BBoxYOLO`、`YOLOModelLoader`、`BatchCount+`、`ImageFromBatch`、`CLIPVisionLoader`、`DownloadAndLoadNLFModel`、`RenderNLFPoses`、`OnnxDetectionModelLoader`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`SDPoseDrawKeypoints`、`CheckpointLoaderSimple`、`DrawViTPose`、`LazySwitch1way`、`easy anythingIndexSwitch`、`WanVideoBlockSwap`、`PoseAndFaceDetection`、`ImageBatch`、`MemoryCleaner`、`easy float`、`easy mathInt`、`RepeatImageBatch`、`WanVideoContextOptions`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoLoraSelectMulti`、`LazySwitch2way`、`WanVideoModelLoader`、`ImageResizeKJv2`、`WanVideoAnimateEmbeds`、`easy imageSize`、`CR Text`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMaskWithBlur`、`BlockifyMask`、`DrawMaskOnImage`、`RHHiddenNodes`、`WanVideoDecode`、`VHS_VideoInfo`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
