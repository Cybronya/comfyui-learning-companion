---
key: 平台全量/傻瓜式 Wan2.2×Animate动作迁移_V1_2043704383359160322.json
name: 傻瓜式 Wan2.2×Animate动作迁移_V1_2043704383359160322
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/傻瓜式 Wan2.2×Animate动作迁移_V1_2043704383359160322.json
hash: 3edf1254f9d93f6b
coverage: 0.512821
learned_at: 2026-11-14 01:39:28
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, Int, Int, WanVideoSetLoRAs, VRAMReserver, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Note, CLIPVisionLoader, GetNode, SetNode, SetNode, WanVideoClipVisionEncode, OnnxDetectionModelLoader, GetNode, GetNode, WanVideoAnimateEmbeds, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, PoseAndFaceDetection, GetNode, GetNode, PreviewImage, ImageResizeKJv2, DrawViTPose, SetNode, easy cleanGpuUsed, WanVideoContextOptions, WanVideoBlockSwap, WanVideoSetBlockSwap, RepeatImageBatch, easy mathInt, ImageFromBatch, RHHiddenNodes, BatchCount+, BatchCount+, SetNode, easy float, WanVideoLoraSelectMulti, WanVideoSampler, Int, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, SetNode, SetNode, WanVideoModelLoader, GetNode, ImageBatch, GetNode, WanVideoDecode, GetNode, GetNode, GetNode, ImageFromBatch, GetNode, WanVideoVAELoader, VHS_LoadVideo, Int, LoadImage, easy float, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/傻瓜式 Wan2.2×Animate动作迁移_V1_2043704383359160322.json

> 来源文件 `comfyui_library/workflows/平台全量/傻瓜式 Wan2.2×Animate动作迁移_V1_2043704383359160322.json`

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
- `WanVideoBlockSwap`
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
- `VHS_LoadVideo`
- `Int`
- `LoadImage`
- `easy float`
- `VHS_VideoCombine`

## 知识

覆盖率 **51%**（40/78）

**有卡**：`VHS_VideoInfo`、`Int`、`WanVideoSetLoRAs`、`VRAMReserver`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`PoseAndFaceDetection`、`ImageResizeKJv2`、`DrawViTPose`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`RepeatImageBatch`、`easy mathInt`、`ImageFromBatch`、`RHHiddenNodes`、`BatchCount+`、`easy float`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`ImageBatch`、`WanVideoDecode`、`WanVideoVAELoader`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
