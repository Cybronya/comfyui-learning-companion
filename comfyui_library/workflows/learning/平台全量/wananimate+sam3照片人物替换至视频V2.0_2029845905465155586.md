---
key: 平台全量/wananimate+sam3照片人物替换至视频V2.0_2029845905465155586.json
name: wananimate+sam3照片人物替换至视频V2.0_2029845905465155586
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wananimate+sam3照片人物替换至视频V2.0_2029845905465155586.json
hash: ecac315909c2f460
coverage: 0.552381
learned_at: 2026-11-14 01:20:05
nodes: [SetNode, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, easy cleanGpuUsed, easy clearCacheAll, PrimitiveInt, GetNode, GetNode, PrimitiveInt, SetNode, SetNode, VHS_VideoInfoLoaded, GetNode, DrawViTPose, GetNode, GetNode, SetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, ImageFromBatch, GetNode, GetImageSizeAndCount, easy cleanGpuUsed, easy clearCacheAll, SetNode, GetNode, GetNode, easy cleanGpuUsed, GetNode, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, RenderNLFPoses, SetNode, GetNode, SimpleMath+, SimpleMath+, PreviewAnimation, easy clearCacheAll, CLIPVisionLoader, DWPreprocessor, GetNode, PoseAndFaceDetection, GetNode, DownloadAndLoadNLFModel, NLFPredict, PoseDetectionVitPoseToDWPose, PoseDetectionVitPoseToDWPose, OnnxDetectionModelLoader, GetNode, SetNode, easy sam3VideoSegmentation, YOLOModelLoader, easy cleanGpuUsed, workflow>背景与主体遮罩, GetNode, easy framesEditor, SimpleMath+, PrimitiveInt, GetNode, GetNode, GetNode, SDPoseOODLoader, SDPoseOODProcessor, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, easy sam3VideoModelExtraConfig, VHS_VideoCombine, SetNode, GetNode, GetNode, GetNode, WanVideoDecode, VHS_VideoCombine, DrawMaskOnImage, ImageBlend, easy sam3ModelLoader, WanVideoContextOptions, WanVideoAnimateEmbeds, WanVideoSampler, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, SetNode, GetNode, GetNode, ImageResizeKJv2, LoadImage, VHS_LoadVideo, WanVideoModelLoader, WanVideoLoraSelectMulti, OnnxDetectionModelLoader, WanVideoVAELoader]
patterns: []
missing: []
---

# 平台全量/wananimate+sam3照片人物替换至视频V2.0_2029845905465155586.json

> 来源文件 `comfyui_library/workflows/平台全量/wananimate+sam3照片人物替换至视频V2.0_2029845905465155586.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（105 个）：
- `SetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `VHS_VideoInfoLoaded`
- `GetNode`
- `DrawViTPose`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `GetImageSizeAndCount`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `GetNode`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `RenderNLFPoses`
- `SetNode`
- `GetNode`
- `SimpleMath+`
- `SimpleMath+`
- `PreviewAnimation`
- `easy clearCacheAll`
- `CLIPVisionLoader`
- `DWPreprocessor`
- `GetNode`
- `PoseAndFaceDetection`
- `GetNode`
- `DownloadAndLoadNLFModel`
- `NLFPredict`
- `PoseDetectionVitPoseToDWPose`
- `PoseDetectionVitPoseToDWPose`
- `OnnxDetectionModelLoader`
- `GetNode`
- `SetNode`
- `easy sam3VideoSegmentation`
- `YOLOModelLoader`
- `easy cleanGpuUsed`
- `workflow>背景与主体遮罩`
- `GetNode`
- `easy framesEditor`
- `SimpleMath+`
- `PrimitiveInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `easy sam3VideoModelExtraConfig`
- `VHS_VideoCombine`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `DrawMaskOnImage`
- `ImageBlend`
- `easy sam3ModelLoader`
- `WanVideoContextOptions`
- `WanVideoAnimateEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `VHS_LoadVideo`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `OnnxDetectionModelLoader`
- `WanVideoVAELoader`

## 知识

覆盖率 **55%**（58/105）

**有卡**：`WanVideoClipVisionEncode`、`easy cleanGpuUsed`、`easy clearCacheAll`、`VHS_VideoInfoLoaded`、`DrawViTPose`、`ImageFromBatch`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`RenderNLFPoses`、`SimpleMath+`、`PreviewAnimation`、`CLIPVisionLoader`、`DWPreprocessor`、`PoseAndFaceDetection`、`DownloadAndLoadNLFModel`、`NLFPredict`、`PoseDetectionVitPoseToDWPose`、`OnnxDetectionModelLoader`、`easy sam3VideoSegmentation`、`YOLOModelLoader`、`workflow>背景与主体遮罩`、`easy framesEditor`、`SDPoseOODLoader`、`SDPoseOODProcessor`、`WanVideoTextEncodeCached`、`WanVideoTorchCompileSettings`、`easy sam3VideoModelExtraConfig`、`WanVideoDecode`、`DrawMaskOnImage`、`ImageBlend`、`easy sam3ModelLoader`、`WanVideoContextOptions`、`WanVideoAnimateEmbeds`、`WanVideoSampler`、`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`LoadImage`、`VHS_LoadVideo`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
