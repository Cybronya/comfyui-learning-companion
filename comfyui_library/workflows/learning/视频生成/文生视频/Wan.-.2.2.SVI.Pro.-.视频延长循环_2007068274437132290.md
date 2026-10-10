---
key: 视频生成/文生视频/Wan.-.2.2.SVI.Pro.-.视频延长循环_2007068274437132290.json
name: Wan.-.2.2.SVI.Pro.-.视频延长循环_2007068274437132290
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan.-.2.2.SVI.Pro.-.视频延长循环_2007068274437132290.json
hash: 0f55dbdc1364ad24
coverage: 0.576471
learned_at: 2026-10-11 03:07:12
nodes: [WanVideoSamplerv2, WanVideoSchedulerv2, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, SetNode, WanVideoSVIProEmbeds, GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoSchedulerv2, WanVideoSigmaToStep, WanVideoTorchCompileSettings, WanVideoVAELoader, GetNode, GetNode, SetNode, VHS_VideoCombine, GetNode, WanVideoSamplerv2, SetNode, GetNode, GetNode, Note, GetNode, WanVideoTextEncode, GetNode, SetNode, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoDecode, VHS_VideoCombine, SetNode, Text Load Line From File, GetNode, easy batchAnything, easy forLoopEnd, VHS_VideoCombine, VHS_VideoCombine, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, SetNode, VHS_VideoInfo, SimpleMath+, GetImageRangeFromBatch, INTConstant, INTConstant, WanVideoSVIProEmbeds, WanVideoEncode, easy forLoopStart, GetNode, WanVideoSamplerv2, WanVideoSamplerv2, easy seed, ImageResizeKJv2, WanVideoBlockSwap, LoadImage, SimpleMath+, WanVideoEncode, GetImageRangeFromBatch, ImageBatchExtendWithOverlap, WanVideoDecode, SetNode, ImageBatchExtendWithOverlap, WanVideoTextEncode, PrimitiveStringMultiline, VHS_LoadVideo, PreviewImage, easy ifElse]
patterns: []
missing: [SimpleMath+, SimpleMath+, Text Load Line From File, easy batchAnything, easy forLoopEnd, easy forLoopStart, easy seed]
discoveries: [次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识, 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识, 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识, 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan.-.2.2.SVI.Pro.-.视频延长循环_2007068274437132290.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan.-.2.2.SVI.Pro.-.视频延长循环_2007068274437132290.json`

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
- `WanVideoLoraSelect`
- `SetNode`
- `VHS_VideoInfo`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `INTConstant`
- `INTConstant`
- `WanVideoSVIProEmbeds`
- `WanVideoEncode`
- `easy forLoopStart`
- `GetNode`
- `WanVideoSamplerv2` ★核心
- `WanVideoSamplerv2` ★核心
- `easy seed`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `LoadImage`
- `SimpleMath+`
- `WanVideoEncode`
- `GetImageRangeFromBatch`
- `ImageBatchExtendWithOverlap`
- `WanVideoDecode`
- `SetNode`
- `ImageBatchExtendWithOverlap`
- `WanVideoTextEncode`
- `PrimitiveStringMultiline`
- `VHS_LoadVideo`
- `PreviewImage`
- `easy ifElse`

## 知识

覆盖率 **58%**（49/85）

**有卡**：`WanVideoSamplerv2`、`WanVideoSchedulerv2`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSVIProEmbeds`、`WanVideoSigmaToStep`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoModelLoader`、`INTConstant`、`VHS_VideoInfo`、`GetImageRangeFromBatch`、`WanVideoEncode`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`LoadImage`、`ImageBatchExtendWithOverlap`、`VHS_LoadVideo`

**缺卡**（7）：`SimpleMath+`、`SimpleMath+`、`Text Load Line From File`、`easy batchAnything`、`easy forLoopEnd`、`easy forLoopStart`、`easy seed`

**用到的条目**：LoadImage、WanVideoSamplerv2、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoEncode、WanVideoLoraSelect

## 学习发现

- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `SimpleMath+` 知识库中没有该节点类型的任何知识
- 次要节点 `Text Load Line From File` 知识库中没有该节点类型的任何知识
- 次要节点 `easy batchAnything` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopEnd` 知识库中没有该节点类型的任何知识
- 次要节点 `easy forLoopStart` 知识库中没有该节点类型的任何知识
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
