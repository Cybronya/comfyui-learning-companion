---
key: 视频生成/文生视频/Wan.-.2.2.SVI.Pro.·图生视频延长循环_2006963154827354113.json
name: Wan.-.2.2.SVI.Pro.·图生视频延长循环_2006963154827354113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan.-.2.2.SVI.Pro.·图生视频延长循环_2006963154827354113.json
hash: 28035532aed69aa9
coverage: 0.635135
learned_at: 2026-10-15 22:47:07
nodes: [WanVideoSchedulerv2, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSchedulerv2, WanVideoSigmaToStep, WanVideoTorchCompileSettings, WanVideoVAELoader, SetNode, GetNode, SetNode, VHS_VideoCombine, GetNode, WanVideoSamplerv2, SetNode, SetNode, GetNode, GetNode, Note, GetNode, WanVideoTextEncode, GetNode, SetNode, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoDecode, VHS_VideoCombine, SetNode, Text Load Line From File, GetNode, easy forLoopEnd, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, GetNode, easy forLoopStart, INTConstant, WanVideoEncode, ImageBatchExtendWithOverlap, INTConstant, INTConstant, LoadImage, WanVideoBlockSwap, easy seed, WanVideoSamplerv2, WanVideoSamplerv2, WanVideoLoraSelect, WanVideoLoraSelect, ImageResizeKJv2, WanVideoTextEncode, PrimitiveStringMultiline, WanVideoSamplerv2, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSVIProEmbeds, WanVideoSVIProEmbeds, GetNode, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan.-.2.2.SVI.Pro.·图生视频延长循环_2006963154827354113.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan.-.2.2.SVI.Pro.·图生视频延长循环_2006963154827354113.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（74 个）：
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
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoSchedulerv2`
- `WanVideoSigmaToStep`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `SetNode`
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
- `WanVideoDecode`
- `VHS_VideoCombine`
- `SetNode`
- `Text Load Line From File`
- `GetNode`
- `easy forLoopEnd`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetNode`
- `GetNode`
- `easy forLoopStart`
- `INTConstant`
- `WanVideoEncode`
- `ImageBatchExtendWithOverlap`
- `INTConstant`
- `INTConstant`
- `LoadImage`
- `WanVideoBlockSwap`
- `easy seed`
- `WanVideoSamplerv2` ★核心
- `WanVideoSamplerv2` ★核心
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `ImageResizeKJv2`
- `WanVideoTextEncode`
- `PrimitiveStringMultiline`
- `WanVideoSamplerv2` ★核心
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSVIProEmbeds`
- `WanVideoSVIProEmbeds`
- `GetNode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **64%**（47/74）

**有卡**：`WanVideoSchedulerv2`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSigmaToStep`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoSamplerv2`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`Text Load Line From File`、`easy forLoopEnd`、`WanVideoModelLoader`、`easy forLoopStart`、`INTConstant`、`WanVideoEncode`、`ImageBatchExtendWithOverlap`、`LoadImage`、`WanVideoBlockSwap`、`easy seed`、`ImageResizeKJv2`、`WanVideoSVIProEmbeds`

**用到的条目**：LoadImage、WanVideoSamplerv2、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode
