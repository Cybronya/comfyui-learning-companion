---
key: 视频生成/图生视频/Wan 2.2 Animate 动作迁移222_2047170050724990977.json
name: Wan 2.2 Animate 动作迁移222_2047170050724990977.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan 2.2 Animate 动作迁移222_2047170050724990977.json
hash: 4110c66d5778c573
coverage: 0.512821
learned_at: 2026-10-15 22:37:03
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, Int, Int, WanVideoSetLoRAs, VRAMReserver, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Note, CLIPVisionLoader, GetNode, SetNode, SetNode, WanVideoClipVisionEncode, OnnxDetectionModelLoader, GetNode, GetNode, WanVideoAnimateEmbeds, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, PoseAndFaceDetection, GetNode, GetNode, PreviewImage, ImageResizeKJv2, DrawViTPose, SetNode, easy cleanGpuUsed, WanVideoContextOptions, WanVideoSetBlockSwap, RepeatImageBatch, easy mathInt, ImageFromBatch, RHHiddenNodes, BatchCount+, BatchCount+, SetNode, easy float, WanVideoLoraSelectMulti, WanVideoSampler, Int, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, SetNode, SetNode, WanVideoModelLoader, GetNode, ImageBatch, GetNode, WanVideoDecode, GetNode, GetNode, GetNode, ImageFromBatch, GetNode, WanVideoVAELoader, WanVideoBlockSwap, Int, easy float, VHS_VideoCombine, VHS_LoadVideo, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan 2.2 Animate 动作迁移222_2047170050724990977.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2047170050724990977.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（78 个）：
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `Int`
- `Int`
- `WanVideoSetLoRAs`
- `VRAMReserver`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `Note`
- `CLIPVisionLoader`
- `GetNode`
- `SetNode`
- `SetNode`
- `WanVideoClipVisionEncode`
- `OnnxDetectionModelLoader`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `GetNode`
- `easy cleanGpuUsed`
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
- `WanVideoContextOptions`
- `WanVideoSetBlockSwap`
- `RepeatImageBatch`
- `easy mathInt`
- `ImageFromBatch`
- `RHHiddenNodes`
- `BatchCount+`
- `BatchCount+`
- `SetNode`
- `easy float`
- `WanVideoLoraSelectMulti`
- `WanVideoSampler` ★核心
- `Int`
- `WanVideoLoraSelectMulti`
- `WanVideoTextEncodeCached`
- `SetNode`
- `SetNode`
- `WanVideoModelLoader`
- `GetNode`
- `ImageBatch`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageFromBatch`
- `GetNode`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `Int`
- `easy float`
- `VHS_VideoCombine`
- `VHS_LoadVideo`
- `LoadImage`

## 知识

覆盖率 **51%**（40/78）

**有卡**：`VHS_VideoInfo`、`Int`、`WanVideoSetLoRAs`、`VRAMReserver`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`PoseAndFaceDetection`、`ImageResizeKJv2`、`DrawViTPose`、`WanVideoContextOptions`、`WanVideoSetBlockSwap`、`RepeatImageBatch`、`easy mathInt`、`ImageFromBatch`、`RHHiddenNodes`、`BatchCount+`、`easy float`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`ImageBatch`、`WanVideoDecode`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoSetLoRAs、WanVideoLoraSelectMulti
