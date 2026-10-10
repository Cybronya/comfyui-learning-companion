---
key: 视频生成/文生视频/Wan.-.2.2.SVI.Pro.·图生视频延长循环_2006963154827354113.json
name: Wan.-.2.2.SVI.Pro.·图生视频延长循环_2006963154827354113
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan.-.2.2.SVI.Pro.·图生视频延长循环_2006963154827354113.json
hash: 28035532aed69aa9
coverage: 0.581081
learned_at: 2026-10-11 03:07:12
nodes: [WanVideoSchedulerv2, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, SetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSchedulerv2, WanVideoSigmaToStep, WanVideoTorchCompileSettings, WanVideoVAELoader, SetNode, GetNode, SetNode, VHS_VideoCombine, GetNode, WanVideoSamplerv2, SetNode, SetNode, GetNode, GetNode, Note, GetNode, WanVideoTextEncode, GetNode, SetNode, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoDecode, WanVideoDecode, VHS_VideoCombine, SetNode, Text Load Line From File, GetNode, easy forLoopEnd, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, GetNode, easy forLoopStart, INTConstant, WanVideoEncode, ImageBatchExtendWithOverlap, INTConstant, INTConstant, LoadImage, WanVideoBlockSwap, easy seed, WanVideoSamplerv2, WanVideoSamplerv2, WanVideoLoraSelect, WanVideoLoraSelect, ImageResizeKJv2, WanVideoTextEncode, PrimitiveStringMultiline, WanVideoSamplerv2, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSVIProEmbeds, WanVideoSVIProEmbeds, GetNode, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: [Text Load Line From File, easy forLoopEnd, easy forLoopStart, easy seed]
discoveries: [次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
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

覆盖率 **58%**（43/74）

**有卡**：`WanVideoSchedulerv2`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSigmaToStep`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoSamplerv2`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoModelLoader`、`INTConstant`、`WanVideoEncode`、`ImageBatchExtendWithOverlap`、`LoadImage`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`WanVideoSVIProEmbeds`

**缺卡**（4）：`Text Load Line From File`、`easy forLoopEnd`、`easy forLoopStart`、`easy seed`

**用到的条目**：LoadImage、WanVideoSamplerv2、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect

## 学习发现

- 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
