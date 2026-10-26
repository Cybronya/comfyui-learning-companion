---
key: 数字人/数字人/Wan2.2 Animate动作迁移V4.1_2048652027139465218.json
name: Wan2.2 Animate动作迁移V4.1_2048652027139465218
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/Wan2.2 Animate动作迁移V4.1_2048652027139465218.json
hash: 2d18566337dc3da6
coverage: 0.4875
learned_at: 2026-10-26 01:57:52
nodes: [GetNode, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, SetNode, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, SetNode, CLIPVisionLoader, SetNode, SetNode, SetNode, SetNode, SetNode, easy mathInt, VHS_VideoInfo, SetNode, ImageResizeKJv2, RepeatImageBatch, BatchCount+, GetNode, SetNode, ImageFromBatch, easy cleanGpuUsed, SetNode, SetNode, PreviewImage, GetNode, GetNode, GetNode, WanVideoSampler, easy cleanGpuUsed, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoDecode, Note, Int, Int, VRAMReserver, BatchCount+, RHHiddenNodes, Note, GetNode, SetNode, ImageBatch, SetNode, VHS_VideoCombine, PoseAndFaceDetection, GetNode, GetNode, DrawViTPose, easy cleanGpuUsed, SetNode, WanVideoTextEncodeCached, WanVideoVAELoader, easy showAnything, Int, Int, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoLoraSelect, easy float, Note, WanVideoContextOptions, WanVideoBlockSwap, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 数字人/数字人/Wan2.2 Animate动作迁移V4.1_2048652027139465218.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/Wan2.2 Animate动作迁移V4.1_2048652027139465218.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（80 个）：
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `CLIPVisionLoader`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `easy mathInt`
- `VHS_VideoInfo`
- `SetNode`
- `ImageResizeKJv2`
- `RepeatImageBatch`
- `BatchCount+`
- `GetNode`
- `SetNode`
- `ImageFromBatch`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `PreviewImage`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `easy cleanGpuUsed`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `Note`
- `Int`
- `Int`
- `VRAMReserver`
- `BatchCount+`
- `RHHiddenNodes`
- `Note`
- `GetNode`
- `SetNode`
- `ImageBatch`
- `SetNode`
- `VHS_VideoCombine`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `DrawViTPose`
- `easy cleanGpuUsed`
- `SetNode`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `easy showAnything`
- `Int`
- `Int`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `easy float`
- `Note`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **49%**（39/80）

**有卡**：`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`easy mathInt`、`VHS_VideoInfo`、`ImageResizeKJv2`、`RepeatImageBatch`、`BatchCount+`、`ImageFromBatch`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`Int`、`VRAMReserver`、`RHHiddenNodes`、`ImageBatch`、`VHS_VideoCombine`、`PoseAndFaceDetection`、`DrawViTPose`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`easy float`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
