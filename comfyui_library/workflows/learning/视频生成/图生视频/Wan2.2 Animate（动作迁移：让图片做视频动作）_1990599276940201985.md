---
key: 视频生成/图生视频/Wan2.2 Animate（动作迁移：让图片做视频动作）_1990599276940201985.json
name: Wan2.2 Animate（动作迁移：让图片做视频动作）_1990599276940201985.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1990599276940201985.json
hash: 3199fe63d5b53d55
coverage: 0.484848
learned_at: 2026-10-15 22:33:11
nodes: [GetNode, CLIPVisionLoader, SetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, WanVideoSetBlockSwap, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, GetNode, easy mathInt, easy mathInt, easy compare, LazySwitch1way, easy mathInt, GetNode, GetNode, WanVideoAnimateEmbeds, GetNode, easy showAnything, GetNode, PoseAndFaceDetection, DrawViTPose, easy mathInt, RepeatImageBatch, easy mathInt, SetNode, OnnxDetectionModelLoader, ImageFromBatch, ImageBatch, easy mathInt, BatchCount+, SetNode, SetNode, easy mathInt, GetNode, SetNode, easy batchAnything, BatchCount+, easy mathInt, BatchCount+, ImageFromBatch, GetNode, GetNode, CM_FloatToInt, GetNode, SetNode, GetNode, GetNode, easy mathInt, SetNode, SetNode, GetNode, easy showAnything, GetNode, SetNode, SetNode, GetNode, easy showAnything, easy showAnything, easy mathInt, GetNode, GetNode, WanVideoVAELoader, GetNode, ImageFromBatch, ImageFromBatch, RepeatImageBatch, RepeatImageBatch, ImageBatchMulti, ImageFromBatch, RHHiddenNodes, BatchCount+, easy mathInt, easy compare, RHHiddenNodes, LazySwitch1way, RHHiddenNodes, easy mathInt, SetNode, SetNode, SetNode, SetNode, SetNode, CM_IntToFloat, Note, RHHiddenNodes, SetNode, easy forLoopEnd, WanVideoSampler, WanVideoBlockSwap, easy forLoopStart, Note, Note, Note, Note, easy int, easy int, easy int, Note, easy showAnything, Note, RHHiddenNodes, WanVideoSetLoRAs, easy showAnything, ImageResizeKJv2, RHHiddenNodes, WanVideoDecode, easy cleanGpuUsed, GetNode, GetNode, LazySwitch1way, VHS_VideoCombine, Note, WanVideoTextEncodeCached, Note, Note, Note, VHS_LoadVideo, LoadImage, easy int]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate（动作迁移：让图片做视频动作）_1990599276940201985.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1990599276940201985.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（132 个）：
- `GetNode`
- `CLIPVisionLoader`
- `SetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `easy mathInt`
- `easy mathInt`
- `easy compare`
- `LazySwitch1way`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `easy showAnything`
- `GetNode`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `easy mathInt`
- `RepeatImageBatch`
- `easy mathInt`
- `SetNode`
- `OnnxDetectionModelLoader`
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
- `WanVideoVAELoader`
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
- `easy mathInt`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `CM_IntToFloat`
- `Note`
- `RHHiddenNodes`
- `SetNode`
- `easy forLoopEnd`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `easy forLoopStart`
- `Note`
- `Note`
- `Note`
- `Note`
- `easy int`
- `easy int`
- `easy int`
- `Note`
- `easy showAnything`
- `Note`
- `RHHiddenNodes`
- `WanVideoSetLoRAs`
- `easy showAnything`
- `ImageResizeKJv2`
- `RHHiddenNodes`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `GetNode`
- `GetNode`
- `LazySwitch1way`
- `VHS_VideoCombine`
- `Note`
- `WanVideoTextEncodeCached`
- `Note`
- `Note`
- `Note`
- `VHS_LoadVideo`
- `LoadImage`
- `easy int`

## 知识

覆盖率 **48%**（64/132）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`easy mathInt`、`easy compare`、`LazySwitch1way`、`WanVideoAnimateEmbeds`、`PoseAndFaceDetection`、`DrawViTPose`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`ImageFromBatch`、`ImageBatch`、`BatchCount+`、`easy batchAnything`、`CM_FloatToInt`、`WanVideoVAELoader`、`ImageBatchMulti`、`RHHiddenNodes`、`CM_IntToFloat`、`easy forLoopEnd`、`WanVideoSampler`、`WanVideoBlockSwap`、`easy forLoopStart`、`easy int`、`WanVideoSetLoRAs`、`ImageResizeKJv2`、`WanVideoDecode`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`WanVideoTextEncodeCached`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、CLIPVisionLoader
