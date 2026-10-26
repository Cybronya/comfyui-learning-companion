---
key: 数字人/数字人/Wan2.2 Animate动作迁移-AIGCTV_2043534137943920642.json
name: Wan2.2 Animate动作迁移-AIGCTV_2043534137943920642
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2 Animate动作迁移-AIGCTV_2043534137943920642.json
hash: dc70cd53d3e7b248
coverage: 0.797872
learned_at: 2026-10-26 01:57:51
nodes: [WanVideoClipVisionEncode, WanVideoDecode, WanVideoVAELoader, WanVideoTextEncodeCached, easy int, easy int, Note, Note, Note, Note, easy int, easy boolean, easy int, ImpactSwitch, easy int, easy int, WanVideoSetLoRAs, WanVideoSetBlockSwap, SDPoseKeypointExtractor, BBoxYOLO, YOLOModelLoader, BatchCount+, ImageFromBatch, CLIPVisionLoader, DownloadAndLoadNLFModel, RenderNLFPoses, OnnxDetectionModelLoader, NLFPredict, PoseDetectionVitPoseToDWPose, PoseDetectionVitPoseToDWPose, SDPoseDrawKeypoints, CheckpointLoaderSimple, Reroute, Note, DrawViTPose, OnnxDetectionModelLoader, LazySwitch1way, easy anythingIndexSwitch, WanVideoBlockSwap, PoseAndFaceDetection, ImageBatch, MemoryCleaner, easy float, easy float, Note, Note, easy mathInt, RepeatImageBatch, PoseAndFaceDetection, WanVideoContextOptions, MemoryCleaner, VHS_VideoCombine, ImageFromBatch, WanVideoSampler, Note, Note, WanVideoLoraSelectMulti, Any Switch (rgthree), LazySwitch2way, easy boolean, VHS_VideoCombine, MarkdownNote, Note, Note, Note, WanVideoModelLoader, WanVideoLoraSelectMulti, VHS_LoadVideo, VHS_VideoInfo, ImageResizeKJv2, PreviewImage, Label (rgthree), Label (rgthree), VHS_VideoCombine, WanVideoAnimateEmbeds, Fast Groups Bypasser (rgthree), LoadImage, easy imageSize, CR Text, CR Text, easy compare, LazySwitch1way, LayerUtility: ImageScaleByAspectRatio V2, easy float, Note, DownloadAndLoadSAM2Model, Sam2Segmentation, GrowMaskWithBlur, BlockifyMask, DrawMaskOnImage, WanVideoAnimateEmbeds, RepeatImageBatch, RHHiddenNodes, BatchCount+]
patterns: []
missing: []
parameters: {"checkpoint": "sdpose_wholebody_fp16.safetensors"}
---

# 数字人/数字人/Wan2.2 Animate动作迁移-AIGCTV_2043534137943920642.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2 Animate动作迁移-AIGCTV_2043534137943920642.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（94 个）：
- `WanVideoClipVisionEncode`
- `WanVideoDecode`
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
- `MemoryCleaner`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `WanVideoSampler` ★核心
- `Note`
- `Note`
- `WanVideoLoraSelectMulti`
- `Any Switch (rgthree)`
- `LazySwitch2way`
- `easy boolean`
- `VHS_VideoCombine`
- `MarkdownNote`
- `Note`
- `Note`
- `Note`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `VHS_LoadVideo`
- `VHS_VideoInfo`
- `ImageResizeKJv2`
- `PreviewImage`
- `Label (rgthree)`
- `Label (rgthree)`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `Fast Groups Bypasser (rgthree)`
- `LoadImage`
- `easy imageSize`
- `CR Text`
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

## 关键参数

- `checkpoint` = `sdpose_wholebody_fp16.safetensors`

## 知识

覆盖率 **80%**（75/94）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`easy int`、`easy boolean`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`SDPoseKeypointExtractor`、`BBoxYOLO`、`YOLOModelLoader`、`BatchCount+`、`ImageFromBatch`、`CLIPVisionLoader`、`DownloadAndLoadNLFModel`、`RenderNLFPoses`、`OnnxDetectionModelLoader`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`SDPoseDrawKeypoints`、`CheckpointLoaderSimple`、`DrawViTPose`、`LazySwitch1way`、`easy anythingIndexSwitch`、`WanVideoBlockSwap`、`PoseAndFaceDetection`、`ImageBatch`、`MemoryCleaner`、`easy float`、`easy mathInt`、`RepeatImageBatch`、`WanVideoContextOptions`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoLoraSelectMulti`、`LazySwitch2way`、`WanVideoModelLoader`、`VHS_LoadVideo`、`VHS_VideoInfo`、`ImageResizeKJv2`、`Label (rgthree)`、`WanVideoAnimateEmbeds`、`LoadImage`、`easy imageSize`、`CR Text`、`easy compare`、`LayerUtility: ImageScaleByAspectRatio V2`、`DownloadAndLoadSAM2Model`、`Sam2Segmentation`、`GrowMaskWithBlur`、`BlockifyMask`、`DrawMaskOnImage`、`RHHiddenNodes`

**用到的条目**：CheckpointLoaderSimple、LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
