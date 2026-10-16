---
key: 视频生成/图生视频/首尾帧-Rewards+Pusa+加速 Wan2.2_1967120522687418370.json
name: 首尾帧-Rewards+Pusa+加速 Wan2.2_1967120522687418370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1967120522687418370.json
hash: 0ab254e1ef3828d0
coverage: 1
learned_at: 2026-10-15 22:31:40
nodes: [WanVideoSampler, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoApplyNAG, SimpleMath+, WanVideoModelLoader, WanVideoSetBlockSwap, INTConstant, ImpactInt, WanVideoModelLoader, WanVideoDecode, WanVideoImageToVideoEncode, easy cleanGpuUsed, easy cleanGpuUsed, ImageResizeKJv2, ImageResizeKJv2, WanVideoBlockSwap, LoadImage, LoadImage, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoSetBlockSwap, WanVideoTextEncodeSingle, WanVideoTextEncodeSingle, ImpactInt, ImpactInt, CR Text, WanVideoLoraSelectMulti, WanVideoSetLoRAs, WanVideoSetLoRAs, SimpleMath+, VHS_VideoCombine, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧-Rewards+Pusa+加速 Wan2.2_1967120522687418370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967120522687418370.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（33 个）：
- `WanVideoSampler` ★核心
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `WanVideoApplyNAG`
- `SimpleMath+`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `ImpactInt`
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `LoadImage`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeSingle`
- `WanVideoTextEncodeSingle`
- `ImpactInt`
- `ImpactInt`
- `CR Text`
- `WanVideoLoraSelectMulti`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `SimpleMath+`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **100%**（33/33）

**有卡**：`WanVideoSampler`、`WanVideoTorchCompileSettings`、`WanVideoApplyNAG`、`SimpleMath+`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`INTConstant`、`ImpactInt`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`easy cleanGpuUsed`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncodeSingle`、`CR Text`、`WanVideoLoraSelectMulti`、`WanVideoSetLoRAs`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle、WanVideoSetLoRAs
