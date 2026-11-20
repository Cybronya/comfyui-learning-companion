---
key: 平台全量/傻瓜式 Wan2.2×Animate动作迁移_V1_2045885949283934210.json
name: 傻瓜式 Wan2.2×Animate动作迁移_V1_2045885949283934210
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/傻瓜式 Wan2.2×Animate动作迁移_V1_2045885949283934210.json
hash: 6bc88cdc98338dbc
coverage: 0.512821
learned_at: 2026-11-14 01:39:28
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, Int, Int, WanVideoSetLoRAs, VRAMReserver, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Note, CLIPVisionLoader, GetNode, SetNode, SetNode, WanVideoClipVisionEncode, OnnxDetectionModelLoader, GetNode, GetNode, WanVideoAnimateEmbeds, GetNode, easy cleanGpuUsed, easy cleanGpuUsed, SetNode, PoseAndFaceDetection, GetNode, GetNode, PreviewImage, ImageResizeKJv2, DrawViTPose, SetNode, easy cleanGpuUsed, WanVideoContextOptions, WanVideoSetBlockSwap, RepeatImageBatch, easy mathInt, ImageFromBatch, RHHiddenNodes, BatchCount+, BatchCount+, SetNode, easy float, WanVideoLoraSelectMulti, WanVideoSampler, Int, WanVideoLoraSelectMulti, WanVideoTextEncodeCached, SetNode, SetNode, WanVideoModelLoader, GetNode, ImageBatch, GetNode, WanVideoDecode, GetNode, GetNode, GetNode, ImageFromBatch, GetNode, WanVideoVAELoader, VHS_VideoCombine, WanVideoBlockSwap, VHS_LoadVideo, Int, LoadImage, easy float]
patterns: []
missing: []
---

# 平台全量/傻瓜式 Wan2.2×Animate动作迁移_V1_2045885949283934210.json

> 来源文件 `comfyui_library/workflows/平台全量/傻瓜式 Wan2.2×Animate动作迁移_V1_2045885949283934210.json`

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
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `VHS_LoadVideo`
- `Int`
- `LoadImage`
- `easy float`

## 知识

覆盖率 **51%**（40/78）

**有卡**：`VHS_VideoInfo`、`Int`、`WanVideoSetLoRAs`、`VRAMReserver`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`PoseAndFaceDetection`、`ImageResizeKJv2`、`DrawViTPose`、`WanVideoContextOptions`、`WanVideoSetBlockSwap`、`RepeatImageBatch`、`easy mathInt`、`ImageFromBatch`、`RHHiddenNodes`、`BatchCount+`、`easy float`、`WanVideoLoraSelectMulti`、`WanVideoSampler`、`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`ImageBatch`、`WanVideoDecode`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
