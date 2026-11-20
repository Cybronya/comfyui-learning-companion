---
key: 平台全量/wan2.2 首尾帧及插帧辅助图生视频工作流_1984488129035976706.json
name: wan2.2 首尾帧及插帧辅助图生视频工作流_1984488129035976706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/wan2.2 首尾帧及插帧辅助图生视频工作流_1984488129035976706.json
hash: 3e79e74d5f551994
coverage: 0.621212
learned_at: 2026-11-14 01:19:24
nodes: [WanVideoModelLoader, WanVideoVAELoader, SetNode, SetNode, GetNode, GetNode, CLIPVisionLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, SetNode, GetNode, WanVideoTorchCompileSettings, SetNode, SetNode, GetNode, GetNode, GetNode, easy cleanGpuUsed, WanVideoSampler, GetNode, WanVideoDecode, GetNode, GetNode, ImageStitch, ImageStitch, ImageStitch, VHS_VideoCombine, ImpactImageBatchToImageList, SetNode, Int, Int, ImageResizeKJv2, SetNode, LoadImage, SimpleMath+, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoLoraSelectMulti, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, Int, LoadImage, WanVideoSampler, WanVideoEncodeLatentBatch, SetNode, LoadImage, LoadImage, GetNode, WanVideoContextOptions, GetNode, ImageResizeKJv2, ImageResizeKJv2, GetNode, ImageBatchMulti, Reroute, AILab_MiniCPM_4_V_Advanced, WanVideoTextEncodeCached, easy showAnything, WanVideoClipVisionEncode, WanVideoImageToVideoEncode, SetNode, GetNode, GetNode, VHS_VideoCombine]
patterns: []
missing: []
---

# 平台全量/wan2.2 首尾帧及插帧辅助图生视频工作流_1984488129035976706.json

> 来源文件 `comfyui_library/workflows/平台全量/wan2.2 首尾帧及插帧辅助图生视频工作流_1984488129035976706.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（66 个）：
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `CLIPVisionLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `SetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `GetNode`
- `ImageStitch`
- `ImageStitch`
- `ImageStitch`
- `VHS_VideoCombine`
- `ImpactImageBatchToImageList`
- `SetNode`
- `Int`
- `Int`
- `ImageResizeKJv2`
- `SetNode`
- `LoadImage`
- `SimpleMath+`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelectMulti`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `Int`
- `LoadImage`
- `WanVideoSampler` ★核心
- `WanVideoEncodeLatentBatch`
- `SetNode`
- `LoadImage`
- `LoadImage`
- `GetNode`
- `WanVideoContextOptions`
- `GetNode`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `GetNode`
- `ImageBatchMulti`
- `Reroute`
- `AILab_MiniCPM_4_V_Advanced`
- `WanVideoTextEncodeCached`
- `easy showAnything`
- `WanVideoClipVisionEncode`
- `WanVideoImageToVideoEncode`
- `SetNode`
- `GetNode`
- `GetNode`
- `VHS_VideoCombine`

## 知识

覆盖率 **62%**（41/66）

**有卡**：`WanVideoModelLoader`、`WanVideoVAELoader`、`CLIPVisionLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoDecode`、`ImageStitch`、`VHS_VideoCombine`、`ImpactImageBatchToImageList`、`Int`、`ImageResizeKJv2`、`LoadImage`、`SimpleMath+`、`WanVideoLoraSelect`、`WanVideoLoraSelectMulti`、`WanVideoEncodeLatentBatch`、`WanVideoContextOptions`、`ImageBatchMulti`、`AILab_MiniCPM_4_V_Advanced`、`WanVideoTextEncodeCached`、`WanVideoClipVisionEncode`、`WanVideoImageToVideoEncode`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoClipVisionEncode、WanVideoDecode、WanVideoEncodeLatentBatch、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader
