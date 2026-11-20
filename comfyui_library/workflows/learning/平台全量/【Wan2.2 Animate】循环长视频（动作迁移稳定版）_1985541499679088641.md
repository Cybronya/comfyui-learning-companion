---
key: 平台全量/【Wan2.2 Animate】循环长视频（动作迁移稳定版）_1985541499679088641.json
name: 【Wan2.2 Animate】循环长视频（动作迁移稳定版）_1985541499679088641
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【Wan2.2 Animate】循环长视频（动作迁移稳定版）_1985541499679088641.json
hash: a4d75dc517d44000
coverage: 0.504
learned_at: 2026-11-14 01:22:22
nodes: [GetNode, CLIPVisionLoader, SetNode, WanVideoClipVisionEncode, GetNode, GetNode, GetNode, GetNode, WanVideoSetBlockSwap, SetNode, SetNode, WanVideoSetLoRAs, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, easy forLoopStart, GetNode, GetNode, easy showAnything, PreviewImage, SetNode, GetNode, easy mathInt, easy mathInt, easy compare, LazySwitch1way, easy mathInt, GetNode, GetNode, ImageResizeKJv2, GetNode, easy showAnything, easy showAnything, GetNode, PoseAndFaceDetection, DrawViTPose, easy mathInt, RepeatImageBatch, easy mathInt, SetNode, OnnxDetectionModelLoader, GetNode, ImageFromBatch, ImageBatch, easy mathInt, BatchCount+, SetNode, SetNode, easy mathInt, GetNode, SetNode, easy batchAnything, BatchCount+, easy mathInt, BatchCount+, ImageFromBatch, GetNode, GetNode, GetNode, CM_FloatToInt, GetNode, SetNode, GetNode, GetNode, easy mathInt, SetNode, SetNode, GetNode, easy showAnything, GetNode, SetNode, SetNode, GetNode, easy showAnything, easy showAnything, easy mathInt, GetNode, GetNode, WanVideoSampler, WanVideoVAELoader, VHS_VideoCombine, RHHiddenNodes, GetNode, ImageFromBatch, ImageFromBatch, RepeatImageBatch, RepeatImageBatch, ImageBatchMulti, ImageFromBatch, RHHiddenNodes, BatchCount+, easy mathInt, easy compare, RHHiddenNodes, LazySwitch1way, RHHiddenNodes, RHHiddenNodes, easy mathInt, RHHiddenNodes, easy forLoopEnd, WanVideoBlockSwap, easy int, easy int, CM_IntToFloat, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, easy int, Note, Note, WanVideoDecode, SetNode, SetNode, SetNode, SetNode, SetNode, GetNode, VHS_VideoCombine, easy int, Note, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 平台全量/【Wan2.2 Animate】循环长视频（动作迁移稳定版）_1985541499679088641.json

> 来源文件 `comfyui_library/workflows/平台全量/【Wan2.2 Animate】循环长视频（动作迁移稳定版）_1985541499679088641.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（125 个）：
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
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `RHHiddenNodes`
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
- `easy int`
- `easy int`
- `CM_IntToFloat`
- `WanVideoTextEncodeCached`
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
- `easy int`
- `Note`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **50%**（63/125）

**有卡**：`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`easy forLoopStart`、`easy mathInt`、`easy compare`、`LazySwitch1way`、`ImageResizeKJv2`、`PoseAndFaceDetection`、`DrawViTPose`、`RepeatImageBatch`、`OnnxDetectionModelLoader`、`ImageFromBatch`、`ImageBatch`、`BatchCount+`、`easy batchAnything`、`CM_FloatToInt`、`WanVideoSampler`、`WanVideoVAELoader`、`VHS_VideoCombine`、`RHHiddenNodes`、`ImageBatchMulti`、`easy forLoopEnd`、`WanVideoBlockSwap`、`easy int`、`CM_IntToFloat`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoSetLoRAs、CLIPVisionLoader
