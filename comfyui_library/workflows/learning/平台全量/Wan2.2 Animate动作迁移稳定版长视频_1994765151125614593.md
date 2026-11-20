---
key: 平台全量/Wan2.2 Animate动作迁移稳定版长视频_1994765151125614593.json
name: Wan2.2 Animate动作迁移稳定版长视频_1994765151125614593
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 Animate动作迁移稳定版长视频_1994765151125614593.json
hash: d63f3b19079ddc87
coverage: 0.515625
learned_at: 2026-11-14 01:05:21
nodes: [GetNode, GetNode, GetNode, GetNode, easy showAnything, SetNode, GetNode, easy showAnything, GetNode, GetNode, GetNode, SetNode, GetNode, easy showAnything, easy showAnything, VHS_VideoCombine, VHS_VideoCombine, SetNode, SetNode, SetNode, SetNode, SetNode, easy int, Note, easy int, CM_IntToFloat, easy int, easy int, GetNode, easy cleanGpuUsed, RHHiddenNodes, GetNode, SetNode, easy forLoopEnd, WanVideoDecode, easy forLoopStart, GetNode, WanVideoSampler, WanVideoAnimateEmbeds, GetNode, GetNode, easy mathInt, GetNode, ImageFromBatch, BatchCount+, easy batchAnything, GetNode, GetNode, GetNode, GetNode, GetNode, RHHiddenNodes, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetBlockSwap, SetNode, WanVideoVAELoader, SetNode, GetNode, CLIPVisionLoader, WanVideoClipVisionEncode, SetNode, ImageBatchMulti, RHHiddenNodes, easy mathInt, easy compare, ImageFromBatch, RepeatImageBatch, easy mathInt, SetNode, BatchCount+, GetNode, GetNode, ImageFromBatch, ImageBatch, RepeatImageBatch, easy showAnything, ImageFromBatch, easy mathInt, SetNode, RHHiddenNodes, ImageFromBatch, GetNode, easy mathInt, SetNode, GetNode, CM_FloatToInt, GetNode, easy mathInt, LazySwitch1way, RHHiddenNodes, GetNode, SetNode, SetNode, GetNode, easy compare, easy mathInt, easy mathInt, RHHiddenNodes, easy mathInt, LazySwitch1way, easy mathInt, BatchCount+, SetNode, easy mathInt, BatchCount+, easy mathInt, RepeatImageBatch, PoseAndFaceDetection, GetNode, GetNode, OnnxDetectionModelLoader, SetNode, SetNode, DrawViTPose, ImageResizeKJv2, GetNode, GetNode, SetNode, Note, Note, WanVideoTextEncodeCached, easy showAnything, LoadImage, LoadImage, PreviewImage, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 平台全量/Wan2.2 Animate动作迁移稳定版长视频_1994765151125614593.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 Animate动作迁移稳定版长视频_1994765151125614593.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（128 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `easy showAnything`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy int`
- `Note`
- `easy int`
- `CM_IntToFloat`
- `easy int`
- `easy int`
- `GetNode`
- `easy cleanGpuUsed`
- `RHHiddenNodes`
- `GetNode`
- `SetNode`
- `easy forLoopEnd`
- `WanVideoDecode`
- `easy forLoopStart`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoAnimateEmbeds`
- `GetNode`
- `GetNode`
- `easy mathInt`
- `GetNode`
- `ImageFromBatch`
- `BatchCount+`
- `easy batchAnything`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `RHHiddenNodes`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoClipVisionEncode`
- `SetNode`
- `ImageBatchMulti`
- `RHHiddenNodes`
- `easy mathInt`
- `easy compare`
- `ImageFromBatch`
- `RepeatImageBatch`
- `easy mathInt`
- `SetNode`
- `BatchCount+`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `ImageBatch`
- `RepeatImageBatch`
- `easy showAnything`
- `ImageFromBatch`
- `easy mathInt`
- `SetNode`
- `RHHiddenNodes`
- `ImageFromBatch`
- `GetNode`
- `easy mathInt`
- `SetNode`
- `GetNode`
- `CM_FloatToInt`
- `GetNode`
- `easy mathInt`
- `LazySwitch1way`
- `RHHiddenNodes`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy compare`
- `easy mathInt`
- `easy mathInt`
- `RHHiddenNodes`
- `easy mathInt`
- `LazySwitch1way`
- `easy mathInt`
- `BatchCount+`
- `SetNode`
- `easy mathInt`
- `BatchCount+`
- `easy mathInt`
- `RepeatImageBatch`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `SetNode`
- `SetNode`
- `DrawViTPose`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `SetNode`
- `Note`
- `Note`
- `WanVideoTextEncodeCached`
- `easy showAnything`
- `LoadImage`
- `LoadImage`
- `PreviewImage`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **52%**（66/128）

**有卡**：`VHS_VideoCombine`、`easy int`、`CM_IntToFloat`、`easy cleanGpuUsed`、`RHHiddenNodes`、`easy forLoopEnd`、`WanVideoDecode`、`easy forLoopStart`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`easy mathInt`、`ImageFromBatch`、`BatchCount+`、`easy batchAnything`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`ImageBatchMulti`、`easy compare`、`RepeatImageBatch`、`ImageBatch`、`CM_FloatToInt`、`LazySwitch1way`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`DrawViTPose`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoSetLoRAs、CLIPVisionLoader
