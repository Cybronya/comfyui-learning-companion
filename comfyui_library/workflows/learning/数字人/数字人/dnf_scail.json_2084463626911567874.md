---
key: 数字人/数字人/dnf_scail.json_2084463626911567874.json
name: dnf_scail.json_2084463626911567874
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/dnf_scail.json_2084463626911567874.json
hash: aabfa32e9ab7faf7
coverage: 0.506494
learned_at: 2026-10-18 19:07:47
nodes: [WanVideoClipVisionEncode, GetNode, GetNode, SetNode, GetNode, GetNode, GetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, SetNode, ImageFromBatch, SetNode, ImageFromBatch, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, ImageBatch, RepeatImageBatch, GetNode, BatchCount+, RHHiddenNodes, SetNode, WanVideoSetBlockSwap, easy mathInt, BatchCount+, easy showAnything, WanVideoLoraSelect, GetNode, ImageResizeKJv2, GetNode, CLIPVisionLoader, Int, Int, PreviewImage, MemoryCleaner, SetNode, SetNode, SetNode, SetNode, GetNode, OnnxDetectionModelLoader, WanVideoBlockSwap, MemoryCleaner, WanVideoModelLoader, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, MemoryCleaner, SetNode, GetNode, VRAMReserver, GetNode, easy float, WanVideoDecode, WanVideoTextEncodeCached, WanVideoSetLoRAs, DrawViTPose, WanVideoVAELoader, easy cleanGpuUsed, VHS_VideoCombine, WanVideoSampler, WanVideoLoraSelectMulti, GetNode, PoseAndFaceDetection, Int, Int, LoadImage, VHS_LoadVideo]
patterns: []
missing: []
---

# 数字人/数字人/dnf_scail.json_2084463626911567874.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/dnf_scail.json_2084463626911567874.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（77 个）：
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
- `ImageFromBatch`
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
- `WanVideoSetBlockSwap`
- `easy mathInt`
- `BatchCount+`
- `easy showAnything`
- `WanVideoLoraSelect`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `CLIPVisionLoader`
- `Int`
- `Int`
- `PreviewImage`
- `MemoryCleaner`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `OnnxDetectionModelLoader`
- `WanVideoBlockSwap`
- `MemoryCleaner`
- `WanVideoModelLoader`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoAnimateEmbeds`
- `MemoryCleaner`
- `SetNode`
- `GetNode`
- `VRAMReserver`
- `GetNode`
- `easy float`
- `WanVideoDecode`
- `WanVideoTextEncodeCached`
- `WanVideoSetLoRAs`
- `DrawViTPose`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelectMulti`
- `GetNode`
- `PoseAndFaceDetection`
- `Int`
- `Int`
- `LoadImage`
- `VHS_LoadVideo`

## 知识

覆盖率 **51%**（39/77）

**有卡**：`WanVideoClipVisionEncode`、`VHS_VideoInfo`、`ImageFromBatch`、`ImageBatch`、`RepeatImageBatch`、`BatchCount+`、`RHHiddenNodes`、`WanVideoSetBlockSwap`、`easy mathInt`、`WanVideoLoraSelect`、`ImageResizeKJv2`、`CLIPVisionLoader`、`Int`、`MemoryCleaner`、`OnnxDetectionModelLoader`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoAnimateEmbeds`、`VRAMReserver`、`easy float`、`WanVideoDecode`、`WanVideoTextEncodeCached`、`WanVideoSetLoRAs`、`DrawViTPose`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`WanVideoSampler`、`WanVideoLoraSelectMulti`、`PoseAndFaceDetection`、`LoadImage`、`VHS_LoadVideo`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoClipVisionEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
