---
key: 视频生成/图生视频/图生视频 （wan2.2加速）_1958079800877469697.json
name: 图生视频 （wan2.2加速）_1958079800877469697.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958079800877469697.json
hash: 86a2353a7c2b3189
coverage: 1
learned_at: 2026-10-15 22:31:20
nodes: [INTConstant, LoadImage, CR Text, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoModelLoader, SimpleMath+, LoadWanVideoT5TextEncoder, WanVideoTextEncodeSingle, WanVideoSampler, ImageResizeKJv2, WanVideoVAELoader, easy cleanGpuUsed, ImpactInt, ImpactInt, WanVideoSetBlockSwap, easy cleanGpuUsed, GetImageSizeAndCount, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoBlockSwap, WanVideoTextEncodeSingle, WanVideoApplyNAG, ImpactInt, WanVideoTorchCompileSettings, SimpleMath+, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频 （wan2.2加速）_1958079800877469697.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958079800877469697.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `INTConstant`
- `LoadImage`
- `CR Text`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `SimpleMath+`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncodeSingle`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `ImpactInt`
- `ImpactInt`
- `WanVideoSetBlockSwap`
- `easy cleanGpuUsed`
- `GetImageSizeAndCount`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `ImpactInt`
- `WanVideoTorchCompileSettings`
- `SimpleMath+`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`INTConstant`、`LoadImage`、`CR Text`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`SimpleMath+`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncodeSingle`、`WanVideoSampler`、`ImageResizeKJv2`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`ImpactInt`、`GetImageSizeAndCount`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`WanVideoApplyNAG`、`WanVideoTorchCompileSettings`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle、WanVideoLoraSelect
