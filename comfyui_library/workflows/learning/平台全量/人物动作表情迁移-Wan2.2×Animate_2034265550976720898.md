---
key: 平台全量/人物动作表情迁移-Wan2.2×Animate_2034265550976720898.json
name: 人物动作表情迁移-Wan2.2×Animate_2034265550976720898
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/人物动作表情迁移-Wan2.2×Animate_2034265550976720898.json
hash: 407617389bb5808b
coverage: 0.506494
learned_at: 2026-11-14 01:37:01
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, WanVideoLoraSelect, Int, Int, Int, Int, WanVideoSetLoRAs, VRAMReserver, GetNode, easy float, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, VHS_LoadVideo, Note, WanVideoLoraSelectMulti, WanVideoModelLoader, CLIPVisionLoader, GetNode, WanVideoTextEncodeCached, SetNode, WanVideoVAELoader, SetNode, WanVideoClipVisionEncode, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, GetNode, easy cleanGpuUsed, WanVideoDecode, easy cleanGpuUsed, SetNode, PoseAndFaceDetection, GetNode, GetNode, PreviewImage, ImageResizeKJv2, DrawViTPose, SetNode, easy cleanGpuUsed, WanVideoSampler, WanVideoContextOptions, WanVideoBlockSwap, WanVideoSetBlockSwap, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, VHS_VideoCombine, RepeatImageBatch, ImageBatch, easy mathInt, ImageFromBatch, RHHiddenNodes, BatchCount+, GetNode, BatchCount+, SetNode, SetNode, SetNode, LoadImage]
patterns: []
missing: []
---

# 平台全量/人物动作表情迁移-Wan2.2×Animate_2034265550976720898.json

> 来源文件 `comfyui_library/workflows/平台全量/人物动作表情迁移-Wan2.2×Animate_2034265550976720898.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（77 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `WanVideoLoraSelect`
- `Int`
- `Int`
- `Int`
- `Int`
- `WanVideoSetLoRAs`
- `VRAMReserver`
- `GetNode`
- `easy float`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_LoadVideo`
- `Note`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `CLIPVisionLoader`
- `GetNode`
- `WanVideoTextEncodeCached`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoClipVisionEncode`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `SetNode`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `ImageResizeKJv2`
- `DrawViTPose`
- `SetNode`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`
- `RepeatImageBatch`
- `ImageBatch`
- `easy mathInt`
- `ImageFromBatch`
- `RHHiddenNodes`
- `BatchCount+`
- `GetNode`
- `BatchCount+`
- `SetNode`
- `SetNode`
- `SetNode`
- `LoadImage`

## 知识

覆盖率 **51%**（39/77）

**有卡**：`VHS_VideoInfo`、`WanVideoLoraSelect`、`Int`、`WanVideoSetLoRAs`、`VRAMReserver`、`easy float`、`VHS_LoadVideo`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`WanVideoDecode`、`PoseAndFaceDetection`、`ImageResizeKJv2`、`DrawViTPose`、`WanVideoSampler`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`ImageFromBatch`、`VHS_VideoCombine`、`RepeatImageBatch`、`ImageBatch`、`easy mathInt`、`RHHiddenNodes`、`BatchCount+`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelect、WanVideoLoraSelectMulti
