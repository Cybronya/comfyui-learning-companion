---
key: 平台全量/Wan2.2 SVI Pro视频延长循环_2017568074668449793.json
name: Wan2.2 SVI Pro视频延长循环_2017568074668449793
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2 SVI Pro视频延长循环_2017568074668449793.json
hash: 7afa021ad071cb5a
coverage: 0.706897
learned_at: 2026-11-14 01:05:32
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, SetNode, SetNode, WanVideoVAELoader, SetNode, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, VHS_LoadVideo, LoadImage, PreviewImage, easy ifElse, Note, VHS_VideoInfo, GetImageRangeFromBatch, SimpleMath+, GetImageRangeFromBatch, SimpleMath+, GetNode, WanVideoEncode, SetNode, WanVideoEncode, GetNode, WanVideoSigmaToStep, WanVideoTextEncode, Note, WanVideoSVIProEmbeds, GetNode, WanVideoDecode, SetNode, JjkText, WanVideoSchedulerv2, SetNode, SetNode, WanVideoSamplerv2, WanVideoSamplerv2, WanVideoSchedulerv2, VHS_VideoCombine, ImageResizeKJv2, ImageBatchExtendWithOverlap, INTConstant, INTConstant]
patterns: []
missing: []
---

# 平台全量/Wan2.2 SVI Pro视频延长循环_2017568074668449793.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2 SVI Pro视频延长循环_2017568074668449793.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（58 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `SetNode`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `VHS_LoadVideo`
- `LoadImage`
- `PreviewImage`
- `easy ifElse`
- `Note`
- `VHS_VideoInfo`
- `GetImageRangeFromBatch`
- `SimpleMath+`
- `GetImageRangeFromBatch`
- `SimpleMath+`
- `GetNode`
- `WanVideoEncode`
- `SetNode`
- `WanVideoEncode`
- `GetNode`
- `WanVideoSigmaToStep`
- `WanVideoTextEncode`
- `Note`
- `WanVideoSVIProEmbeds`
- `GetNode`
- `WanVideoDecode`
- `SetNode`
- `JjkText`
- `WanVideoSchedulerv2`
- `SetNode`
- `SetNode`
- `WanVideoSamplerv2` ★核心
- `WanVideoSamplerv2` ★核心
- `WanVideoSchedulerv2`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `ImageBatchExtendWithOverlap`
- `INTConstant`
- `INTConstant`

## 知识

覆盖率 **71%**（41/58）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`VHS_LoadVideo`、`LoadImage`、`VHS_VideoInfo`、`GetImageRangeFromBatch`、`SimpleMath+`、`WanVideoEncode`、`WanVideoSigmaToStep`、`WanVideoTextEncode`、`WanVideoSVIProEmbeds`、`WanVideoDecode`、`WanVideoSchedulerv2`、`WanVideoSamplerv2`、`VHS_VideoCombine`、`ImageResizeKJv2`、`ImageBatchExtendWithOverlap`、`INTConstant`

**用到的条目**：LoadImage、WanVideoSamplerv2、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoEncode、WanVideoTextEncode、WanVideoVAELoader、WanVideoLoraSelect
