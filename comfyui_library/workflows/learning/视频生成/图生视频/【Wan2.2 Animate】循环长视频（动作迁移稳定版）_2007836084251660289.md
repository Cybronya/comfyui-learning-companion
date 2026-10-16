---
key: 视频生成/图生视频/【Wan2.2 Animate】循环长视频（动作迁移稳定版）_2007836084251660289.json
name: 【Wan2.2 Animate】循环长视频（动作迁移稳定版）_2007836084251660289.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2007836084251660289.json
hash: 733595f280144c2c
coverage: 0.504
learned_at: 2026-10-15 22:34:05
nodes: [SetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, WanVideoSetBlockSwap, SetNode, SetNode, WanVideoSetLoRAs, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, easy forLoopStart, GetNode, GetNode, easy showAnything, PreviewImage, SetNode, GetNode, easy mathInt, easy mathInt, easy compare, LazySwitch1way, easy mathInt, GetNode, GetNode, ImageResizeKJv2, GetNode, easy showAnything, easy showAnything, GetNode, PoseAndFaceDetection, DrawViTPose, easy mathInt, RepeatImageBatch, easy mathInt, SetNode, OnnxDetectionModelLoader, GetNode, ImageFromBatch, ImageBatch, easy mathInt, BatchCount+, SetNode, SetNode, easy mathInt, GetNode, SetNode, easy batchAnything, BatchCount+, easy mathInt, BatchCount+, ImageFromBatch, GetNode, GetNode, GetNode, CM_FloatToInt, GetNode, SetNode, GetNode, GetNode, easy mathInt, SetNode, SetNode, GetNode, easy showAnything, GetNode, SetNode, SetNode, GetNode, easy showAnything, easy showAnything, easy mathInt, GetNode, GetNode, WanVideoSampler, VHS_VideoCombine, GetNode, ImageFromBatch, ImageFromBatch, RepeatImageBatch, RepeatImageBatch, ImageBatchMulti, ImageFromBatch, RHHiddenNodes, BatchCount+, easy mathInt, easy compare, RHHiddenNodes, LazySwitch1way, RHHiddenNodes, RHHiddenNodes, easy mathInt, RHHiddenNodes, easy forLoopEnd, WanVideoBlockSwap, CM_IntToFloat, WanVideoAnimateEmbeds, easy int, Note, Note, WanVideoDecode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, Note, easy int, CLIPVisionLoader, WanVideoVAELoader, WanVideoTextEncodeCached, GetNode, RHHiddenNodes, LoadImage, easy int, easy int, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/【Wan2.2 Animate】循环长视频（动作迁移稳定版）_2007836084251660289.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2007836084251660289.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（125 个）：
- `SetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `easy forLoopStart`
- `GetNode`
- `GetNode`
- `easy showAnything`
- `PreviewImage`
- `SetNode`
- `GetNode`
- `easy mathInt`
- `easy mathInt`
- `easy compare`
- `LazySwitch1way`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `easy showAnything`
- `easy showAnything`
- `GetNode`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `easy mathInt`
- `RepeatImageBatch`
- `easy mathInt`
- `SetNode`
- `OnnxDetectionModelLoader`
- `GetNode`
- `ImageFromBatch`
- `ImageBatch`
- `easy mathInt`
- `BatchCount+`
- `SetNode`
- `SetNode`
- `easy mathInt`
- `GetNode`
- `SetNode`
- `easy batchAnything`
- `BatchCount+`
- `easy mathInt`
- `BatchCount+`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `CM_FloatToInt`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `easy mathInt`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `easy showAnything`
- `easy showAnything`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `GetNode`
- `ImageFromBatch`
- `ImageFromBatch`
- `RepeatImageBatch`
- `RepeatImageBatch`
- `ImageBatchMulti`
- `ImageFromBatch`
- `RHHiddenNodes`
- `BatchCount+`
- `easy mathInt`
- `easy compare`
- `RHHiddenNodes`
- `LazySwitch1way`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `easy mathInt`
- `RHHiddenNodes`
- `easy forLoopEnd`
- `WanVideoBlockSwap`
- `CM_IntToFloat`
- `WanVideoAnimateEmbeds`
- `easy int`
- `Note`
- `Note`
- `WanVideoDecode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `VHS_VideoCombine`
- `Note`
- `easy int`
- `CLIPVisionLoader`
- `WanVideoVAELoader`
- `WanVideoTextEncodeCached`
- `GetNode`
- `RHHiddenNodes`
- `LoadImage`
- `easy int`
- `easy int`
- `VHS_LoadVideo`

## 知识

覆盖率 **50%**（63/125）

**有卡**：`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`easy forLoopStart`、`easy mathInt`、`easy compare`、`LazySwitch1way`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`DrawViTPose`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`ImageFromBatch`、`ImageBatch`、`BatchCount+`、`easy batchAnything`、`CM_FloatToInt`、`WanVideoSampler`、`VHS_VideoCombine`、`ImageBatchMulti`、`RHHiddenNodes`、`easy forLoopEnd`、`WanVideoBlockSwap`、`CM_IntToFloat`、`WanVideoAnimateEmbeds`、`easy int`、`WanVideoDecode`、`CLIPVisionLoader`、`WanVideoVAELoader`、`WanVideoTextEncodeCached`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、CLIPVisionLoader
