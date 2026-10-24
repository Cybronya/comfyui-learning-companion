---
key: 图片生成/图生图/图生视频 （Rewards+Pusa+加速）Wan2.2_1967155879348985857.json
name: 图生视频 （Rewards+Pusa+加速）Wan2.2_1967155879348985857
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/图生视频 （Rewards+Pusa+加速）Wan2.2_1967155879348985857.json
hash: 76ffe125292411b8
coverage: 0.96875
learned_at: 2026-10-23 12:44:08
nodes: [WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoTextEncodeSingle, WanVideoVAELoader, easy cleanGpuUsed, GetImageSizeAndCount, WanVideoTextEncodeSingle, WanVideoApplyNAG, ImpactInt, WanVideoDecode, easy cleanGpuUsed, ImpactInt, ImpactInt, WanVideoSampler, WanVideoSampler, CR Text, WanVideoImageToVideoEncode, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings, ImageResizeKJv2, INTConstant, Note, VHS_VideoCombine, WanVideoSetBlockSwap, SimpleMath+, easy cleanGpuUsed, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, INTConstant, LoadImage]
patterns: []
missing: []
---

# 图片生成/图生图/图生视频 （Rewards+Pusa+加速）Wan2.2_1967155879348985857.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/图生视频 （Rewards+Pusa+加速）Wan2.2_1967155879348985857.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoTextEncodeSingle`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `GetImageSizeAndCount`
- `WanVideoTextEncodeSingle`
- `WanVideoApplyNAG`
- `ImpactInt`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `ImpactInt`
- `ImpactInt`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CR Text`
- `WanVideoImageToVideoEncode`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJv2`
- `INTConstant`
- `Note`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `SimpleMath+`
- `easy cleanGpuUsed`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `INTConstant`
- `LoadImage`

## 知识

覆盖率 **97%**（31/32）

**有卡**：`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoTextEncodeSingle`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`GetImageSizeAndCount`、`WanVideoApplyNAG`、`ImpactInt`、`WanVideoDecode`、`WanVideoSampler`、`CR Text`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`INTConstant`、`VHS_VideoCombine`、`SimpleMath+`、`WanVideoLoraSelectMulti`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle、WanVideoLoraSelectMulti
