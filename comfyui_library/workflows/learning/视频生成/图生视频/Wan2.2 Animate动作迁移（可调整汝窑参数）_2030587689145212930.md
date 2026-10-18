---
key: 视频生成/图生视频/Wan2.2 Animate动作迁移（可调整汝窑参数）_2030587689145212930.json
name: Wan2.2 Animate动作迁移（可调整汝窑参数）_2030587689145212930.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2 Animate动作迁移（可调整汝窑参数）_2030587689145212930.json
hash: c9b4090d74121254
coverage: 0.493671
learned_at: 2026-10-15 22:35:27
nodes: [GetNode, WanVideoClipVisionEncode, SetNode, GetNode, GetNode, GetNode, SetNode, CLIPVisionLoader, SetNode, SetNode, SetNode, SetNode, SetNode, easy mathInt, ImageResizeKJv2, RepeatImageBatch, BatchCount+, GetNode, SetNode, ImageFromBatch, easy cleanGpuUsed, SetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSetBlockSwap, WanVideoDecode, BatchCount+, RHHiddenNodes, Note, SetNode, ImageBatch, SetNode, PoseAndFaceDetection, DrawViTPose, easy cleanGpuUsed, SetNode, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoLoraSelect, WanVideoContextOptions, WanVideoBlockSwap, Int, VRAMReserver, SetNode, Note, PreviewImage, SetNode, VHS_VideoInfo, GetNode, GetNode, OnnxDetectionModelLoader, WanVideoTextEncodeCached, GetNode, SetNode, GetNode, GetNode, GetNode, Int, VHS_VideoCombine, Note, Int, Int, WanVideoAnimateEmbeds, LoadImage, WanVideoSampler, easy float, VHS_LoadVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 Animate动作迁移（可调整汝窑参数）_2030587689145212930.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2030587689145212930.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（79 个）：
- `GetNode`
- `WanVideoClipVisionEncode`
- `SetNode`
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
- `ImageResizeKJv2`
- `RepeatImageBatch`
- `BatchCount+`
- `GetNode`
- `SetNode`
- `ImageFromBatch`
- `easy cleanGpuUsed`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `ImageFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoDecode`
- `BatchCount+`
- `RHHiddenNodes`
- `Note`
- `SetNode`
- `ImageBatch`
- `SetNode`
- `PoseAndFaceDetection`
- `DrawViTPose`
- `easy cleanGpuUsed`
- `SetNode`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoContextOptions`
- `WanVideoBlockSwap`
- `Int`
- `VRAMReserver`
- `SetNode`
- `Note`
- `PreviewImage`
- `SetNode`
- `VHS_VideoInfo`
- `GetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `WanVideoTextEncodeCached`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `Int`
- `VHS_VideoCombine`
- `Note`
- `Int`
- `Int`
- `WanVideoAnimateEmbeds`
- `LoadImage`
- `WanVideoSampler` ★核心
- `easy float`
- `VHS_LoadVideo`

## 知识

覆盖率 **49%**（39/79）

**有卡**：`WanVideoClipVisionEncode`、`CLIPVisionLoader`、`easy mathInt`、`ImageResizeKJv2`、`RepeatImageBatch`、`BatchCount+`、`ImageFromBatch`、`easy cleanGpuUsed`、`WanVideoSetBlockSwap`、`WanVideoDecode`、`RHHiddenNodes`、`ImageBatch`、`PoseAndFaceDetection`、`DrawViTPose`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`WanVideoLoraSelectMulti`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`Int`、`VRAMReserver`、`VHS_VideoInfo`、`OnnxDetectionModelLoader`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`LoadImage`、`WanVideoSampler`、`easy float`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
