---
key: 视频生成/图生视频/Wan2.2AnimateV2 视频角色动作迁移与角色注入_ 视频重绘 _ 动作克隆 _ 角色一致性_2054844641391980546.json
name: Wan2.2AnimateV2 视频角色动作迁移与角色注入_ 视频重绘 _ 动作克隆 _ 角色一致性_2054844641391980546.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2AnimateV2 视频角色动作迁移与角色注入_ 视频重绘 _ 动作克隆 _ 角色一致性_2054844641391980546.json
hash: a0d806bb3c8c520a
coverage: 0.430303
learned_at: 2026-10-15 22:37:52
nodes: [GetNode, WanVideoClipVisionEncode, SetNode, SetNode, easy int, LayerUtility: ImageScaleByAspectRatio V2, CR Text, Note, easy imageSize, PrimitiveFloat, PrimitiveFloat, easy boolean, SetNode, SetNode, SetNode, SetNode, PrimitiveFloat, LazySwitch2way, easy int, SetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, SetNode, SetNode, CR Text, easy int, easy compare, easy boolean, PreviewImage, LazySwitch1way, PreviewAny, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, easy cleanGpuUsed, GetNode, WanVideoSampler, easy cleanGpuUsed, GetNode, GetNode, WanVideoUni3C_embeds, GetNode, WanVideoEncode, WanVideoUni3C_ControlnetLoader, PrimitiveFloat, SetNode, SetNode, WanVideoContextOptions, SetNode, GetNode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoVAELoader, WanVideoTextEncodeCached, SetNode, CLIPVisionLoader, SetNode, SetNode, GetNode, SDPoseOODLoader, SDPoseOODProcessor, PoseDetectionVitPoseToDWPose, OnnxDetectionModelLoader, NLFPredict, GetNode, GetNode, PoseDetectionVitPoseToDWPose, OnnxDetectionModelLoader, GetNode, RenderNLFPoses, easy cleanGpuUsed, RepeatImageBatch, PoseAndFaceDetection, GetNode, GetNode, PreviewImage, PreviewImage, PreviewImage, GetNode, GetNode, GetNode, GetNode, easy mathInt, easy mathInt, ImageFromBatch, RepeatImageBatch, ImageBatch, BatchCount+, DownloadAndLoadNLFModel, WanVideoModelLoader, PreviewAny, GetNode, PoseAndFaceDetection, GetNode, GetNode, YOLOModelLoader, GetNode, WanVideoBlockSwap, GetNode, easy int, ImageResizeKJv2, GetNode, SetNode, easy mathInt, BatchCount+, PreviewImage, easy mathInt, PreviewAny, PreviewAny, PreviewAny, PreviewAny, easy mathInt, PreviewAny, GetNode, GetNode, GetNode, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, PreviewImage, DrawViTPose, LoadImage, RHHiddenNodes, 孤海注释, VHS_LoadVideo, PreviewImage, VHS_VideoCombine, PreviewAny, VHS_VideoCombine, VHS_VideoCombine, PreviewImage, SetNode, SetNode, SetNode, GetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, LoadImage, LazySwitch1way, RunningHub Deepcleaner, easy anythingIndexSwitch, RunningHub Deepcleaner, ImageFromBatch, RunningHub Deepcleaner, WanVideoDecode, RunningHub Deepcleaner]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2AnimateV2 视频角色动作迁移与角色注入_ 视频重绘 _ 动作克隆 _ 角色一致性_2054844641391980546.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2054844641391980546.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（165 个）：
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `SetNode`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `Note`
- `easy imageSize`
- `PrimitiveFloat`
- `PrimitiveFloat`
- `easy boolean`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `PrimitiveFloat`
- `LazySwitch2way`
- `easy int`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CR Text`
- `easy int`
- `easy compare`
- `easy boolean`
- `PreviewImage`
- `LazySwitch1way`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `easy cleanGpuUsed`
- `GetNode`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `WanVideoUni3C_embeds`
- `GetNode`
- `WanVideoEncode`
- `WanVideoUni3C_ControlnetLoader`
- `PrimitiveFloat`
- `SetNode`
- `SetNode`
- `WanVideoContextOptions`
- `SetNode`
- `GetNode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `SDPoseOODLoader`
- `SDPoseOODProcessor`
- `PoseDetectionVitPoseToDWPose`
- `OnnxDetectionModelLoader`
- `NLFPredict`
- `GetNode`
- `GetNode`
- `PoseDetectionVitPoseToDWPose`
- `OnnxDetectionModelLoader`
- `GetNode`
- `RenderNLFPoses`
- `easy cleanGpuUsed`
- `RepeatImageBatch`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy mathInt`
- `easy mathInt`
- `ImageFromBatch`
- `RepeatImageBatch`
- `ImageBatch`
- `BatchCount+`
- `DownloadAndLoadNLFModel`
- `WanVideoModelLoader`
- `PreviewAny`
- `GetNode`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `YOLOModelLoader`
- `GetNode`
- `WanVideoBlockSwap`
- `GetNode`
- `easy int`
- `ImageResizeKJv2`
- `GetNode`
- `SetNode`
- `easy mathInt`
- `BatchCount+`
- `PreviewImage`
- `easy mathInt`
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `PreviewAny`
- `easy mathInt`
- `PreviewAny`
- `GetNode`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `PreviewImage`
- `DrawViTPose`
- `LoadImage`
- `RHHiddenNodes`
- `孤海注释`
- `VHS_LoadVideo`
- `PreviewImage`
- `VHS_VideoCombine`
- `PreviewAny`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `LoadImage`
- `LazySwitch1way`
- `RunningHub Deepcleaner`
- `easy anythingIndexSwitch`
- `RunningHub Deepcleaner`
- `ImageFromBatch`
- `RunningHub Deepcleaner`
- `WanVideoDecode`
- `RunningHub Deepcleaner`

## 知识

覆盖率 **43%**（71/165）

**有卡**：`WanVideoClipVisionEncode`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`CR Text`、`easy imageSize`、`easy boolean`、`LazySwitch2way`、`VHS_VideoInfo`、`easy compare`、`LazySwitch1way`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoUni3C_embeds`、`WanVideoEncode`、`WanVideoUni3C_ControlnetLoader`、`WanVideoContextOptions`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`CLIPVisionLoader`、`SDPoseOODLoader`、`SDPoseOODProcessor`、`PoseDetectionVitPoseToDWPose`、`OnnxDetectionModelLoader`、`NLFPredict`、`RenderNLFPoses`、`RepeatImageBatch`、`PoseAndFaceDetection`、`easy mathInt`、`ImageFromBatch`、`ImageBatch`、`BatchCount+`、`DownloadAndLoadNLFModel`、`WanVideoModelLoader`、`YOLOModelLoader`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`DrawViTPose`、`LoadImage`、`RHHiddenNodes`、`VHS_LoadVideo`、`VHS_VideoCombine`、`RunningHub Deepcleaner`、`easy anythingIndexSwitch`、`WanVideoDecode`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoUni3C_ControlnetLoader、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached
