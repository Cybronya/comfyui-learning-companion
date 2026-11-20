---
key: 平台全量/傻瓜式 Wan2.2×Animate动作迁移_V1_2032715239485083649.json
name: 傻瓜式 Wan2.2×Animate动作迁移_V1_2032715239485083649
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/傻瓜式 Wan2.2×Animate动作迁移_V1_2032715239485083649.json
hash: 083f462e2c545006
coverage: 0.512821
learned_at: 2026-11-14 01:39:26
nodes: [SetNode, SetNode, SetNode, SetNode, SetNode, SetNode, VHS_VideoInfo, SetNode, Int, Int, Int, Int, WanVideoSetLoRAs, VRAMReserver, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, Note, CLIPVisionLoader, GetNode, SetNode, SetNode, WanVideoClipVisionEncode, OnnxDetectionModelLoader, GetNode, GetNode, GetNode, WanVideoAnimateEmbeds, GetNode, easy cleanGpuUsed, WanVideoDecode, easy cleanGpuUsed, SetNode, PoseAndFaceDetection, GetNode, GetNode, PreviewImage, ImageResizeKJv2, DrawViTPose, SetNode, easy cleanGpuUsed, WanVideoContextOptions, WanVideoBlockSwap, WanVideoSetBlockSwap, GetNode, ImageFromBatch, GetNode, GetNode, GetNode, VHS_VideoCombine, RepeatImageBatch, ImageBatch, easy mathInt, ImageFromBatch, RHHiddenNodes, BatchCount+, GetNode, BatchCount+, SetNode, SetNode, SetNode, VHS_LoadVideo, WanVideoLoraSelectMulti, easy float, LoadImage, WanVideoLoraSelectMulti, easy float, WanVideoVAELoader, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncodeCached]
patterns: []
missing: []
---

# 平台全量/傻瓜式 Wan2.2×Animate动作迁移_V1_2032715239485083649.json

> 来源文件 `comfyui_library/workflows/平台全量/傻瓜式 Wan2.2×Animate动作迁移_V1_2032715239485083649.json`

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
- `VHS_LoadVideo`
- `WanVideoLoraSelectMulti`
- `easy float`
- `LoadImage`
- `WanVideoLoraSelectMulti`
- `easy float`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoTextEncodeCached`

## 知识

覆盖率 **51%**（40/78）

**有卡**：`VHS_VideoInfo`、`Int`、`WanVideoSetLoRAs`、`VRAMReserver`、`CLIPVisionLoader`、`WanVideoClipVisionEncode`、`OnnxDetectionModelLoader`、`WanVideoAnimateEmbeds`、`easy cleanGpuUsed`、`WanVideoDecode`、`PoseAndFaceDetection`、`ImageResizeKJv2`、`DrawViTPose`、`WanVideoContextOptions`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`ImageFromBatch`、`VHS_VideoCombine`、`RepeatImageBatch`、`ImageBatch`、`easy mathInt`、`RHHiddenNodes`、`BatchCount+`、`VHS_LoadVideo`、`WanVideoLoraSelectMulti`、`easy float`、`LoadImage`、`WanVideoVAELoader`、`WanVideoModelLoader`、`WanVideoSampler`、`WanVideoTextEncodeCached`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelectMulti、WanVideoSetLoRAs
