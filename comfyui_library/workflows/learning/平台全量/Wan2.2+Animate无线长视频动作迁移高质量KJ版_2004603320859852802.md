---
key: 平台全量/Wan2.2+Animate无线长视频动作迁移高质量KJ版_2004603320859852802.json
name: Wan2.2+Animate无线长视频动作迁移高质量KJ版_2004603320859852802
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2+Animate无线长视频动作迁移高质量KJ版_2004603320859852802.json
hash: 7501105db72b0139
coverage: 0.515789
learned_at: 2026-11-14 01:05:50
nodes: [ImageResizeKJv2, GetNode, GetNode, PoseAndFaceDetection, easy cleanGpuUsed, OnnxDetectionModelLoader, BatchCount+, SetNode, MathExpression|pysssss, BatchCount+, easy compare, easy compare, easy mathInt, LazySwitch1way, MathExpression|pysssss, SetNode, ImageBatch, ImageBatch, easy mathInt, ImageFromBatch, RepeatImageBatch, RepeatImageBatch, easy mathInt, easy mathInt, easy mathInt, BatchCount+, LazySwitch1way, SetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, easy cleanGpuUsed, SetNode, DrawViTPose, SetNode, Int, Int, Int, Int, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, SetNode, VHS_LoadVideo, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, WanVideoTeaCache, WanVideoSampler, GetNode, WanVideoDecode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, SetNode, JjkText, GetNode, CLIPVisionLoader, SetNode, SetNode, SetNode, WanVideoClipVisionEncode, GetNode, WanVideoTextEncodeCached, WanVideoAnimateEmbeds, VHS_VideoCombine, SetNode, SetNode, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoModelLoader, LoadImage, Int]
patterns: []
missing: []
---

# 平台全量/Wan2.2+Animate无线长视频动作迁移高质量KJ版_2004603320859852802.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2+Animate无线长视频动作迁移高质量KJ版_2004603320859852802.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（95 个）：
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `PoseAndFaceDetection`
- `easy cleanGpuUsed`
- `OnnxDetectionModelLoader`
- `BatchCount+`
- `SetNode`
- `MathExpression|pysssss`
- `BatchCount+`
- `easy compare`
- `easy compare`
- `easy mathInt`
- `LazySwitch1way`
- `MathExpression|pysssss`
- `SetNode`
- `ImageBatch`
- `ImageBatch`
- `easy mathInt`
- `ImageFromBatch`
- `RepeatImageBatch`
- `RepeatImageBatch`
- `easy mathInt`
- `easy mathInt`
- `easy mathInt`
- `BatchCount+`
- `LazySwitch1way`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `easy cleanGpuUsed`
- `SetNode`
- `DrawViTPose`
- `SetNode`
- `Int`
- `Int`
- `Int`
- `Int`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_LoadVideo`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoTeaCache`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoDecode`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `JjkText`
- `GetNode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `GetNode`
- `WanVideoTextEncodeCached`
- `WanVideoAnimateEmbeds`
- `VHS_VideoCombine`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `LoadImage`
- `Int`

## 知识

覆盖率 **52%**（49/95）

**有卡**：`ImageResizeKJv2`、`PoseAndFaceDetection`、`easy cleanGpuUsed`、`OnnxDetectionModelLoader`、`BatchCount+`、`MathExpression|pysssss`、`easy compare`、`easy mathInt`、`LazySwitch1way`、`ImageBatch`、`ImageFromBatch`、`RepeatImageBatch`、`DrawViTPose`、`Int`、`VHS_VideoInfo`、`VHS_LoadVideo`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoDecode`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoTextEncodeCached`、`WanVideoAnimateEmbeds`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
