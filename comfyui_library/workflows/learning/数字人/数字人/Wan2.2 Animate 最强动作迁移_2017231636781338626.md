---
key: 数字人/数字人/Wan2.2 Animate 最强动作迁移_2017231636781338626.json
name: Wan2.2 Animate 最强动作迁移_2017231636781338626
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2 Animate 最强动作迁移_2017231636781338626.json
hash: 35db7670dad93ab3
coverage: 0.453488
learned_at: 2026-10-26 01:57:50
nodes: [OnnxDetectionModelLoader, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, VHS_VideoCombine, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, WanVideoSampler, Int, GetNode, GetNode, ImageResizeKJv2, SetNode, PreviewImage, SetNode, SetNode, Int, SetNode, GetNode, BatchCount+, easy showAnything, easy mathInt, easy showAnything, easy mathInt, easy showAnything, easy mathInt, easy showAnything, easy mathInt, easy showAnything, easy showAnything, ImageFromBatch, SetNode, WanVideoAnimateEmbeds, GetNode, WanVideoDecode, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoContextOptions, GetNode, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, DrawViTPose, SetNode, SetNode, WanVideoVAELoader, SetNode, CLIPVisionLoader, GetNode, WanVideoClipVisionEncode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoModelLoader, SetNode, WanVideoTextEncodeCached, SetNode, SetNode, PoseAndFaceDetection, GetNode, GetNode, GetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, SetNode, easy mathInt, GetNode, GetNode, Int, RepeatImageBatch, ImageBatch, SetNode, BatchCount+, PreviewImage, PreviewImage, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.2 Animate 最强动作迁移_2017231636781338626.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2 Animate 最强动作迁移_2017231636781338626.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（86 个）：
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `Int`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `SetNode`
- `PreviewImage`
- `SetNode`
- `SetNode`
- `Int`
- `SetNode`
- `GetNode`
- `BatchCount+`
- `easy showAnything`
- `easy mathInt`
- `easy showAnything`
- `easy mathInt`
- `easy showAnything`
- `easy mathInt`
- `easy showAnything`
- `easy mathInt`
- `easy showAnything`
- `easy showAnything`
- `ImageFromBatch`
- `SetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoContextOptions`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `DrawViTPose`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `CLIPVisionLoader`
- `GetNode`
- `WanVideoClipVisionEncode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `SetNode`
- `WanVideoTextEncodeCached`
- `SetNode`
- `SetNode`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy mathInt`
- `GetNode`
- `GetNode`
- `Int`
- `RepeatImageBatch`
- `ImageBatch`
- `SetNode`
- `BatchCount+`
- `PreviewImage`
- `PreviewImage`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **45%**（39/86）

**有卡**：`OnnxDetectionModelLoader`、`VHS_VideoCombine`、`ImageFromBatch`、`WanVideoSampler`、`Int`、`ImageResizeKJv2`、`BatchCount+`、`easy mathInt`、`WanVideoAnimateEmbeds`、`WanVideoDecode`、`easy cleanGpuUsed`、`WanVideoContextOptions`、`DrawViTPose`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`PoseAndFaceDetection`、`VHS_VideoInfo`、`RepeatImageBatch`、`ImageBatch`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
