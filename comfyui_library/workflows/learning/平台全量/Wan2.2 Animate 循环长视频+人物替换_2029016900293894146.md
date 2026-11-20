---
key: 平台全量/Wan2.2 Animate 循环长视频+人物替换_2029016900293894146.json
name: Wan2.2 Animate 循环长视频+人物替换_2029016900293894146
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate 循环长视频+人物替换_2029016900293894146.json
hash: 66aa8dfc04132f9c
coverage: 0.472826
learned_at: 2026-11-14 01:05:00
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, easy showAnything, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, Image Blank, SetNode, GetNode, easy showAnything, OnnxDetectionModelLoader, Image Blank, SetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, BlockifyMask, SetNode, GetNode, GetNode, GetNode, CoordinatePlotter, CoordinatePlotter, GetNode, LayerUtility: ImageBlendAdvance, SetNode, BatchCount+, RepeatImageBatch, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, easy showAnything, easy showAnything, easy showAnything, GetNode, GetNode, GetNode, BatchCount+, easy mathInt, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, CM_FloatToInt, SetNode, GetNode, GetNode, ImageResizeKJv2, PrimitiveInt, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GrowMask, VHS_VideoCombine, GetNode, SeCVideoSegmentation, SeCModelLoader, DrawViTPose, VHS_VideoCombine, VHS_VideoCombine, SetNode, PoseAndFaceDetection, LayerUtility: ImageBlend, Note, Note, Note, Note, Note, Note, Note, Note, Note, Note, PreviewImage, WanVideoVAELoader, BatchCount+, easy mathInt, SetNode, GetNode, WanVideoAnimateEmbeds, easy forLoopStart, WanVideoSampler, BatchCount+, GetNode, easy forLoopEnd, LazySwitch1way, ImageFromBatch, BatchCount+, easy mathInt, RHHiddenNodes, easy batchAnything, VHS_VideoCombine, GetNode, SetNode, PointsEditor, easy mathInt, LazySwitch1way, easy mathInt, GetNode, easy mathInt, easy mathInt, easy mathInt, SetNode, easy mathInt, GetNode, BatchCount+, easy mathInt, LazySwitch1way, easy compare, ImageFromBatch, ImageFromBatch, GetNode, SetNode, PreviewImage, WanVideoTextEncodeCached, ImpactInt, ImpactInt, WanVideoDecode, easy cleanGpuUsed, ImpactInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, RepeatImageBatch, easy mathInt, RepeatImageBatch, ImageFromBatch, ImageFromBatch, CLIPVisionLoader, WanVideoClipVisionEncode, easy mathInt, RHHiddenNodes, RepeatImageBatch, ImageBatch, easy mathInt, easy mathInt, WanVideoSetBlockSwap, easy compare, ImageBatchMulti, easy mathInt, WanVideoBlockSwap, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate 循环长视频+人物替换_2029016900293894146.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate 循环长视频+人物替换_2029016900293894146.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（184 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `DrawMaskOnImage`
- `SetNode`
- `GetNode`
- `Image Blank`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `OnnxDetectionModelLoader`
- `Image Blank`
- `SetNode`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `BlockifyMask`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `CoordinatePlotter`
- `CoordinatePlotter`
- `GetNode`
- `LayerUtility: ImageBlendAdvance`
- `SetNode`
- `BatchCount+`
- `RepeatImageBatch`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy showAnything`
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `BatchCount+`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `CM_FloatToInt`
- `SetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `PrimitiveInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `GrowMask`
- `VHS_VideoCombine`
- `GetNode`
- `SeCVideoSegmentation`
- `SeCModelLoader`
- `DrawViTPose`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `PoseAndFaceDetection`
- `LayerUtility: ImageBlend`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `PreviewImage`
- `WanVideoVAELoader`
- `BatchCount+`
- `easy mathInt`
- `SetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `easy forLoopStart`
- `WanVideoSampler` ★核心
- `BatchCount+`
- `GetNode`
- `easy forLoopEnd`
- `LazySwitch1way`
- `ImageFromBatch`
- `BatchCount+`
- `easy mathInt`
- `RHHiddenNodes`
- `easy batchAnything`
- `VHS_VideoCombine`
- `GetNode`
- `SetNode`
- `PointsEditor`
- `easy mathInt`
- `LazySwitch1way`
- `easy mathInt`
- `GetNode`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `SetNode`
- `easy mathInt`
- `GetNode`
- `BatchCount+`
- `easy mathInt`
- `LazySwitch1way`
- `easy compare`
- `ImageFromBatch`
- `ImageFromBatch`
- `GetNode`
- `SetNode`
- `PreviewImage`
- `WanVideoTextEncodeCached`
- `ImpactInt`
- `ImpactInt`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `ImpactInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `RepeatImageBatch`
- `easy mathInt`
- `RepeatImageBatch`
- `ImageFromBatch`
- `ImageFromBatch`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `easy mathInt`
- `RHHiddenNodes`
- `RepeatImageBatch`
- `ImageBatch`
- `easy mathInt`
- `easy mathInt`
- `WanVideoSetBlockSwap`
- `easy compare`
- `ImageBatchMulti`
- `easy mathInt`
- `WanVideoBlockSwap`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **47%**（87/184）

**有卡**：`DrawMaskOnImage`、`Image Blank`、`OnnxDetectionModelLoader`、`ImageFromBatch`、`BlockifyMask`、`CoordinatePlotter`、`LayerUtility: ImageBlendAdvance`、`BatchCount+`、`RepeatImageBatch`、`easy mathInt`、`VHS_VideoInfo`、`CM_FloatToInt`、`ImageResizeKJv2`、`VHS_VideoCombine`、`GrowMask`、`SeCVideoSegmentation`、`SeCModelLoader`、`DrawViTPose`、`PoseAndFaceDetection`、`LayerUtility: ImageBlend`、`WanVideoVAELoader`、`WanVideoAnimateEmbeds`、`easy forLoopStart`、`WanVideoSampler`、`easy forLoopEnd`、`LazySwitch1way`、`RHHiddenNodes`、`easy batchAnything`、`PointsEditor`、`easy compare`、`WanVideoTextEncodeCached`、`ImpactInt`、`WanVideoDecode`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`ImageBatch`、`WanVideoSetBlockSwap`、`ImageBatchMulti`、`WanVideoBlockSwap`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、CLIPVisionLoader、ImageResizeKJv2
