---
key: 平台全量/Wan2.2 SVI Pro视频延长循环_2014743840191680513.json
name: Wan2.2 SVI Pro视频延长循环_2014743840191680513
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 SVI Pro视频延长循环_2014743840191680513.json
hash: 916468727a86955d
coverage: 0.658824
learned_at: 2026-11-14 01:05:32
nodes: [WanVideoSamplerv2, WanVideoSchedulerv2, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, SetNode, WanVideoSVIProEmbeds, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSchedulerv2, WanVideoSigmaToStep, WanVideoTorchCompileSettings, WanVideoVAELoader, GetNode, GetNode, SetNode, VHS_VideoCombine, GetNode, WanVideoSamplerv2, SetNode, GetNode, GetNode, Note, GetNode, WanVideoTextEncode, GetNode, SetNode, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoDecode, VHS_VideoCombine, SetNode, Text Load Line From File, GetNode, easy batchAnything, easy forLoopEnd, VHS_VideoCombine, VHS_VideoCombine, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, SetNode, WanVideoSVIProEmbeds, WanVideoEncode, easy forLoopStart, GetNode, WanVideoSamplerv2, WanVideoSamplerv2, easy seed, WanVideoBlockSwap, WanVideoEncode, ImageBatchExtendWithOverlap, WanVideoDecode, SetNode, ImageBatchExtendWithOverlap, PrimitiveStringMultiline, INTConstant, INTConstant, VHS_LoadVideo, LoadImage, WanVideoTextEncode, VHS_VideoInfo, ImageResizeKJv2, SimpleMath+, SimpleMath+, GetImageRangeFromBatch, GetImageRangeFromBatch, PreviewImage, easy ifElse, WanVideoLoraSelect]
patterns: []
missing: []
---

# 平台全量/Wan2.2 SVI Pro视频延长循环_2014743840191680513.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 SVI Pro视频延长循环_2014743840191680513.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（85 个）：
- `WanVideoSamplerv2` ★核心
- `WanVideoSchedulerv2`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoSVIProEmbeds`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSchedulerv2`
- `WanVideoSigmaToStep`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `GetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `SetNode`
- `GetNode`
- `GetNode`
- `Note`
- `GetNode`
- `WanVideoTextEncode`
- `GetNode`
- `SetNode`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `SetNode`
- `Text Load Line From File`
- `GetNode`
- `easy batchAnything`
- `easy forLoopEnd`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `SetNode`
- `WanVideoSVIProEmbeds`
- `WanVideoEncode`
- `easy forLoopStart`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `WanVideoSamplerv2` ★核心
- `easy seed`
- `WanVideoBlockSwap`
- `WanVideoEncode`
- `ImageBatchExtendWithOverlap`
- `WanVideoDecode`
- `SetNode`
- `ImageBatchExtendWithOverlap`
- `PrimitiveStringMultiline`
- `INTConstant`
- `INTConstant`
- `VHS_LoadVideo`
- `LoadImage`
- `WanVideoTextEncode`
- `VHS_VideoInfo`
- `ImageResizeKJv2`
- `SimpleMath+`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `PreviewImage`
- `easy ifElse`
- `WanVideoLoraSelect`

## 知识

覆盖率 **66%**（56/85）

**有卡**：`WanVideoSamplerv2`、`WanVideoSchedulerv2`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSVIProEmbeds`、`WanVideoSigmaToStep`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`Text Load Line From File`、`easy batchAnything`、`easy forLoopEnd`、`WanVideoModelLoader`、`INTConstant`、`WanVideoEncode`、`easy forLoopStart`、`easy seed`、`WanVideoBlockSwap`、`ImageBatchExtendWithOverlap`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoInfo`、`ImageResizeKJv2`、`SimpleMath+`、`GetImageRangeFromBatch`

**用到的条目**：LoadImage、easy seed、WanVideoSamplerv2、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader
