---
key: 视频生成/图生视频/Wan2.2 （Animate） 人物替换 循环长视频_1996246888737284098.json
name: Wan2.2 （Animate） 人物替换 循环长视频_1996246888737284098.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 （Animate） 人物替换 循环长视频_1996246888737284098.json
hash: 8e38bebbe4eca5b4
coverage: 0.494318
learned_at: 2026-10-15 22:33:26
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, easy showAnything, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, DrawMaskOnImage, SetNode, GetNode, Image Blank, SetNode, GetNode, easy showAnything, OnnxDetectionModelLoader, Image Blank, SetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, BlockifyMask, SetNode, GetNode, GetNode, GetNode, CoordinatePlotter, CoordinatePlotter, LayerUtility: ImageBlendAdvance, SetNode, BatchCount+, RepeatImageBatch, SetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, easy showAnything, easy showAnything, easy showAnything, GetNode, GetNode, GetNode, BatchCount+, easy mathInt, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, CM_FloatToInt, SetNode, GetNode, GetNode, ImageResizeKJv2, PrimitiveInt, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, GrowMask, VHS_VideoCombine, GetNode, SeCModelLoader, DrawViTPose, VHS_VideoCombine, VHS_VideoCombine, SetNode, PoseAndFaceDetection, LayerUtility: ImageBlend, PreviewImage, WanVideoVAELoader, BatchCount+, easy mathInt, SetNode, GetNode, BatchCount+, GetNode, easy forLoopEnd, LazySwitch1way, ImageFromBatch, BatchCount+, easy mathInt, RHHiddenNodes, easy batchAnything, GetNode, SetNode, easy mathInt, LazySwitch1way, easy mathInt, GetNode, easy mathInt, easy mathInt, easy mathInt, SetNode, easy mathInt, GetNode, BatchCount+, easy mathInt, LazySwitch1way, easy compare, ImageFromBatch, ImageFromBatch, GetNode, SetNode, PreviewImage, WanVideoTextEncodeCached, ImpactInt, ImpactInt, WanVideoDecode, easy cleanGpuUsed, ImpactInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, easy mathInt, RepeatImageBatch, easy mathInt, RepeatImageBatch, ImageFromBatch, ImageFromBatch, CLIPVisionLoader, WanVideoClipVisionEncode, easy mathInt, RHHiddenNodes, RepeatImageBatch, ImageBatch, easy mathInt, easy mathInt, WanVideoSetBlockSwap, easy compare, ImageBatchMulti, easy mathInt, WanVideoBlockSwap, VHS_LoadVideo, LoadImage, PointsEditor, SeCVideoSegmentation, GetNode, Note, WanVideoAnimateEmbeds, easy forLoopStart, WanVideoSampler, VHS_VideoCombine, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 （Animate） 人物替换 循环长视频_1996246888737284098.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1996246888737284098.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（176 个）：
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
- `SeCModelLoader`
- `DrawViTPose`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `PoseAndFaceDetection`
- `LayerUtility: ImageBlend`
- `PreviewImage`
- `WanVideoVAELoader`
- `BatchCount+`
- `easy mathInt`
- `SetNode`
- `GetNode`
- `BatchCount+`
- `GetNode`
- `easy forLoopEnd`
- `LazySwitch1way`
- `ImageFromBatch`
- `BatchCount+`
- `easy mathInt`
- `RHHiddenNodes`
- `easy batchAnything`
- `GetNode`
- `SetNode`
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
- `VHS_LoadVideo`
- `LoadImage`
- `PointsEditor`
- `SeCVideoSegmentation`
- `GetNode`
- `Note`
- `WanVideoAnimateEmbeds`
- `easy forLoopStart`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `Note`

## 知识

覆盖率 **49%**（87/176）

**有卡**：`DrawMaskOnImage`、`Image Blank`、`OnnxDetectionModelLoader`、`ImageFromBatch`、`BlockifyMask`、`CoordinatePlotter`、`LayerUtility: ImageBlendAdvance`、`BatchCount+`、`RepeatImageBatch`、`easy mathInt`、`VHS_VideoInfo`、`CM_FloatToInt`、`ImageResizeKJv2`、`VHS_VideoCombine`、`GrowMask`、`SeCModelLoader`、`DrawViTPose`、`PoseAndFaceDetection`、`LayerUtility: ImageBlend`、`WanVideoVAELoader`、`easy forLoopEnd`、`LazySwitch1way`、`RHHiddenNodes`、`easy batchAnything`、`easy compare`、`WanVideoTextEncodeCached`、`ImpactInt`、`WanVideoDecode`、`easy cleanGpuUsed`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`ImageBatch`、`WanVideoSetBlockSwap`、`ImageBatchMulti`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`LoadImage`、`PointsEditor`、`SeCVideoSegmentation`、`WanVideoAnimateEmbeds`、`easy forLoopStart`、`WanVideoSampler`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、CLIPVisionLoader、ImageResizeKJv2
