---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移_内部使用_2031632243076112386.json
name: Wan2.2 Animate动作迁移_内部使用_2031632243076112386.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2031632243076112386.json
hash: 8674152a98e7d047
coverage: 0.493671
learned_at: 2026-10-15 22:35:32
nodes: [GetNode, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, SetNode, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, SetNode, CLIPVisionLoader, SetNode, SetNode, SetNode, SetNode, SetNode, easy mathInt, VHS_VideoInfo, SetNode, RepeatImageBatch, BatchCount+, GetNode, SetNode, ImageFromBatch, easy cleanGpuUsed, SetNode, SetNode, GetNode, GetNode, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, WanVideoSetBlockSwap, WanVideoDecode, Note, BatchCount+, RHHiddenNodes, Note, GetNode, SetNode, ImageBatch, SetNode, PoseAndFaceDetection, GetNode, GetNode, DrawViTPose, easy cleanGpuUsed, SetNode, WanVideoTextEncodeCached, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoModelLoader, Note, WanVideoContextOptions, WanVideoBlockSwap, Int, Int, WanVideoLoraSelect, easy float, ImageResizeKJv2, easy cleanGpuUsed, WanVideoSampler, PreviewImage, LoadImage, VRAMReserver, VHS_VideoCombine, VHS_LoadVideo, Int, Int]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移_内部使用_2031632243076112386.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2031632243076112386.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（79 个）：
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
- `RepeatImageBatch`
- `BatchCount+`
- `GetNode`
- `SetNode`
- `ImageFromBatch`
- `easy cleanGpuUsed`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
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
- `BatchCount+`
- `RHHiddenNodes`
- `Note`
- `GetNode`
- `SetNode`
- `ImageBatch`
- `SetNode`
- `PoseAndFaceDetection`
- `GetNode`
- `GetNode`
- `DrawViTPose`
- `easy cleanGpuUsed`
- `SetNode`
- `WanVideoTextEncodeCached`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `Note`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `Int`
- `Int`
- `WanVideoLoraSelect`
- `easy float`
- `ImageResizeKJv2`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `PreviewImage`
- `LoadImage`
- `VRAMReserver`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `Int`
- `Int`

## 知识

覆盖率 **49%**（39/79）

**有卡**：`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`easy mathInt`、`VHS_VideoInfo`、`RepeatImageBatch`、`BatchCount+`、`ImageFromBatch`、`easy cleanGpuUsed`、`WanVideoAnimateEmbeds`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`RHHiddenNodes`、`ImageBatch`、`PoseAndFaceDetection`、`DrawViTPose`、`WanVideoTextEncodeCached`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`Int`、`WanVideoLoraSelect`、`easy float`、`ImageResizeKJv2`、`WanVideoSampler`、`LoadImage`、`VRAMReserver`、`VHS_VideoCombine`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
