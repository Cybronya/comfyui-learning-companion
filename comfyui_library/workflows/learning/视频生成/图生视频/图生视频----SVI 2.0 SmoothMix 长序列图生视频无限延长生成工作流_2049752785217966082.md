---
key: 视频生成/图生视频/图生视频----SVI 2.0 SmoothMix 长序列图生视频无限延长生成工作流_2049752785217966082.json
name: 图生视频----SVI 2.0 SmoothMix 长序列图生视频无限延长生成工作流_2049752785217966082.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2049752785217966082.json
hash: 15f1341d19f619f0
coverage: 0.727642
learned_at: 2026-10-15 22:37:15
nodes: [GetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetBlockSwap, SetNode, WanVideoSetBlockSwap, SetNode, GetImageSizeAndCount, WanVideoDecode, GetImageSizeAndCount, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, GetImageSizeAndCount, GetNode, WanVideoImageToVideoEncode, GetNode, SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoImageToVideoEncode, SetNode, SetNode, RepeatImageBatch, Reroute, WanVideoVACEStartToEndFrame, InvertMask, WanVideoVACEStartToEndFrame, InvertMask, GetImageSizeAndCount, GetImageRangeFromBatch, GetNode, GetNode, GetNode, WanVideoDecode, GetImageSizeAndCount, GetNode, WanVideoImageToVideoEncode, GetNode, SimpleMath+, INTConstant, GetImageRangeFromBatch, InvertMask, VHS_VideoCombine, WanVideoVACEStartToEndFrame, ImageBatchMulti, GetImageSizeAndCount, GetImageRangeFromBatch, GetNode, GetNode, GetNode, WanVideoDecode, GetImageSizeAndCount, GetNode, WanVideoImageToVideoEncode, GetNode, INTConstant, Reroute, GetImageRangeFromBatch, InvertMask, WanVideoVACEStartToEndFrame, SimpleMath+, ImageBatchMulti, GetImageSizeAndCount, GetImageRangeFromBatch, GetNode, GetNode, GetNode, WanVideoDecode, GetImageSizeAndCount, GetNode, WanVideoImageToVideoEncode, SimpleMath+, INTConstant, Reroute, GetImageRangeFromBatch, InvertMask, VHS_VideoCombine, GetImageSizeAndCount, GetImageRangeFromBatch, GetNode, GetNode, GetNode, WanVideoDecode, GetImageSizeAndCount, GetNode, WanVideoImageToVideoEncode, GetNode, SimpleMath+, INTConstant, Reroute, GetImageRangeFromBatch, InvertMask, WanVideoVACEStartToEndFrame, ImageBatchMulti, GetImageSizeAndCount, GetImageRangeFromBatch, GetNode, INTConstant, INTConstant, GetNode, GetNode, WanVideoDecode, GetImageSizeAndCount, GetNode, WanVideoImageToVideoEncode, GetNode, INTConstant, Reroute, GetImageRangeFromBatch, InvertMask, WanVideoVACEStartToEndFrame, SimpleMath+, ImageBatchMulti, Reroute, ImageBatchMulti, Reroute, GetImageSizeAndCount, GetImageRangeFromBatch, GetNode, INTConstant, INTConstant, GetNode, GetNode, WanVideoDecode, GetImageSizeAndCount, GetNode, WanVideoImageToVideoEncode, GetNode, SimpleMath+, INTConstant, Reroute, WanVideoVACEStartToEndFrame, InvertMask, VHS_VideoCombine, GetImageSizeAndCount, GetImageRangeFromBatch, GetNode, INTConstant, INTConstant, GetNode, GetNode, WanVideoDecode, GetImageSizeAndCount, GetNode, WanVideoImageToVideoEncode, GetNode, SimpleMath+, INTConstant, Reroute, GetImageRangeFromBatch, InvertMask, VHS_VideoCombine, WanVideoVACEStartToEndFrame, ImageBatchMulti, GetImageSizeAndCount, GetImageRangeFromBatch, GetNode, INTConstant, INTConstant, GetNode, GetNode, WanVideoDecode, ImageBatchMulti, GetImageSizeAndCount, GetNode, WanVideoImageToVideoEncode, GetNode, INTConstant, Reroute, GetImageRangeFromBatch, InvertMask, WanVideoVACEStartToEndFrame, SimpleMath+, ImageBatchMulti, Reroute, GetImageRangeFromBatch, ImageBatchMulti, WanVideoTextEncode, WanVideoTextEncode, WanVideoTextEncode, WanVideoTextEncode, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoSampler, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, INTConstant, INTConstant, ImageResizeKJv2, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, INTConstant, WanVideoTextEncode, WanVideoTextEncode, WanVideoTextEncode, WanVideoTextEncode, WanVideoTextEncode, WanVideoTextEncode, VHS_VideoCombine, GetNode, VHS_VideoCombine, WanVideoVACEStartToEndFrame, SimpleMath+, GetImageRangeFromBatch, GetImageRangeFromBatch, INTConstant, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频----SVI 2.0 SmoothMix 长序列图生视频无限延长生成工作流_2049752785217966082.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2049752785217966082.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（246 个）：
- `GetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `SetNode`
- `SetNode`
- `RepeatImageBatch`
- `Reroute`
- `WanVideoVACEStartToEndFrame`
- `InvertMask`
- `WanVideoVACEStartToEndFrame`
- `InvertMask`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `SimpleMath+`
- `INTConstant`
- `GetImageRangeFromBatch`
- `InvertMask`
- `VHS_VideoCombine`
- `WanVideoVACEStartToEndFrame`
- `ImageBatchMulti`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `INTConstant`
- `Reroute`
- `GetImageRangeFromBatch`
- `InvertMask`
- `WanVideoVACEStartToEndFrame`
- `SimpleMath+`
- `ImageBatchMulti`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `SimpleMath+`
- `INTConstant`
- `Reroute`
- `GetImageRangeFromBatch`
- `InvertMask`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `SimpleMath+`
- `INTConstant`
- `Reroute`
- `GetImageRangeFromBatch`
- `InvertMask`
- `WanVideoVACEStartToEndFrame`
- `ImageBatchMulti`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `INTConstant`
- `Reroute`
- `GetImageRangeFromBatch`
- `InvertMask`
- `WanVideoVACEStartToEndFrame`
- `SimpleMath+`
- `ImageBatchMulti`
- `Reroute`
- `ImageBatchMulti`
- `Reroute`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `SimpleMath+`
- `INTConstant`
- `Reroute`
- `WanVideoVACEStartToEndFrame`
- `InvertMask`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `SimpleMath+`
- `INTConstant`
- `Reroute`
- `GetImageRangeFromBatch`
- `InvertMask`
- `VHS_VideoCombine`
- `WanVideoVACEStartToEndFrame`
- `ImageBatchMulti`
- `GetImageSizeAndCount`
- `GetImageRangeFromBatch`
- `GetNode`
- `INTConstant`
- `INTConstant`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `ImageBatchMulti`
- `GetImageSizeAndCount`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `INTConstant`
- `Reroute`
- `GetImageRangeFromBatch`
- `InvertMask`
- `WanVideoVACEStartToEndFrame`
- `SimpleMath+`
- `ImageBatchMulti`
- `Reroute`
- `GetImageRangeFromBatch`
- `ImageBatchMulti`
- `WanVideoTextEncode`
- `WanVideoTextEncode`
- `WanVideoTextEncode`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `INTConstant`
- `INTConstant`
- `ImageResizeKJv2`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `INTConstant`
- `WanVideoTextEncode`
- `WanVideoTextEncode`
- `WanVideoTextEncode`
- `WanVideoTextEncode`
- `WanVideoTextEncode`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `GetNode`
- `VHS_VideoCombine`
- `WanVideoVACEStartToEndFrame`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `GetImageRangeFromBatch`
- `INTConstant`
- `LoadImage`

## 知识

覆盖率 **73%**（179/246）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`RepeatImageBatch`、`WanVideoVACEStartToEndFrame`、`InvertMask`、`GetImageRangeFromBatch`、`SimpleMath+`、`INTConstant`、`VHS_VideoCombine`、`ImageBatchMulti`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoModelLoader`、`ImageResizeKJv2`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect
