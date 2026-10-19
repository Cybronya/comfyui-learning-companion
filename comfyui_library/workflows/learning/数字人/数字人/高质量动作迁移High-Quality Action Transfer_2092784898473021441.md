---
key: 数字人/数字人/高质量动作迁移High-Quality Action Transfer_2092784898473021441.json
name: 高质量动作迁移High-Quality Action Transfer_2092784898473021441
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/高质量动作迁移High-Quality Action Transfer_2092784898473021441.json
hash: 54083d3cb402d83f
coverage: 0.5125
learned_at: 2026-10-18 22:17:18
nodes: [WanVideoClipVisionEncode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, ImageFromBatch, SetNode, GetNode, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageBatch, RepeatImageBatch, GetNode, BatchCount+, RHHiddenNodes, SetNode, SetNode, SetNode, GetNode, WanVideoDecode, DrawViTPose, easy cleanGpuUsed, GetNode, SetNode, VHS_VideoCombine, WanVideoAnimateEmbeds, WanVideoContextOptions, WanVideoSetBlockSwap, SetNode, easy mathInt, SetNode, BatchCount+, WanVideoSampler, WanVideoVAELoader, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoLoraSelect, GetNode, GetNode, GetNode, ImageResizeKJv2, MemoryCleaner, PoseAndFaceDetection, OnnxDetectionModelLoader, GetNode, CLIPVisionLoader, WanVideoTextEncodeCached, WanVideoBlockSwap, PreviewImage, MemoryCleaner, MemoryCleaner, MemoryCleaner, VHS_LoadVideo, LoadImage, Int, Int, Int, easy showAnything, Int, VRAMReserver, easy float, Note]
patterns: []
missing: []
---

# 数字人/数字人/高质量动作迁移High-Quality Action Transfer_2092784898473021441.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/高质量动作迁移High-Quality Action Transfer_2092784898473021441.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（80 个）：
- `WanVideoClipVisionEncode`
- `GetNode`
- `GetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `VHS_VideoInfo`
- `SetNode`
- `SetNode`
- `ImageFromBatch`
- `SetNode`
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
- `ImageBatch`
- `RepeatImageBatch`
- `GetNode`
- `BatchCount+`
- `RHHiddenNodes`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `DrawViTPose`
- `easy cleanGpuUsed`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `WanVideoAnimateEmbeds`
- `WanVideoContextOptions`
- `WanVideoSetBlockSwap`
- `SetNode`
- `easy mathInt`
- `SetNode`
- `BatchCount+`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `GetNode`
- `ImageResizeKJv2`
- `MemoryCleaner`
- `PoseAndFaceDetection`
- `OnnxDetectionModelLoader`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoTextEncodeCached`
- `WanVideoBlockSwap`
- `PreviewImage`
- `MemoryCleaner`
- `MemoryCleaner`
- `MemoryCleaner`
- `VHS_LoadVideo`
- `LoadImage`
- `Int`
- `Int`
- `Int`
- `easy showAnything`
- `Int`
- `VRAMReserver`
- `easy float`
- `Note`

## 知识

覆盖率 **51%**（41/80）

**有卡**：`WanVideoClipVisionEncode`、`VHS_VideoInfo`、`ImageFromBatch`、`ImageBatch`、`RepeatImageBatch`、`BatchCount+`、`RHHiddenNodes`、`WanVideoDecode`、`DrawViTPose`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`WanVideoAnimateEmbeds`、`WanVideoContextOptions`、`WanVideoSetBlockSwap`、`easy mathInt`、`WanVideoSampler`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`ImageResizeKJv2`、`MemoryCleaner`、`PoseAndFaceDetection`、`OnnxDetectionModelLoader`、`CLIPVisionLoader`、`WanVideoTextEncodeCached`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`LoadImage`、`Int`、`VRAMReserver`、`easy float`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
