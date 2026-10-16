---
key: 视频生成/图生视频/首尾帧 加速 Wan2.2图生视频_1958076393995251714.json
name: 首尾帧 加速 Wan2.2图生视频_1958076393995251714.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1958076393995251714.json
hash: 023ee2498ec5c344
coverage: 1
learned_at: 2026-10-15 22:31:20
nodes: [WanVideoSampler, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, ImageResizeKJv2, ImageResizeKJv2, WanVideoLoraSelect, WanVideoImageToVideoEncode, SimpleMath+, WanVideoSampler, WanVideoApplyNAG, SimpleMath+, WanVideoDecode, easy cleanGpuUsed, WanVideoLoraSelect, WanVideoTextEncodeSingle, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoTextEncodeSingle, LoadImage, LoadImage, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoModelLoader, ImpactInt, ImpactInt, INTConstant, ImpactInt, CR Text, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧 加速 Wan2.2图生视频_1958076393995251714.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1958076393995251714.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（32 个）：
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `WanVideoLoraSelect`
- `WanVideoImageToVideoEncode`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `WanVideoApplyNAG`
- `SimpleMath+`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoLoraSelect`
- `WanVideoTextEncodeSingle`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTextEncodeSingle`
- `LoadImage`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `ImpactInt`
- `ImpactInt`
- `INTConstant`
- `ImpactInt`
- `CR Text`
- `VHS_VideoCombine`

## 知识

覆盖率 **100%**（32/32）

**有卡**：`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`WanVideoLoraSelect`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`WanVideoApplyNAG`、`WanVideoDecode`、`easy cleanGpuUsed`、`WanVideoTextEncodeSingle`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`ImpactInt`、`INTConstant`、`CR Text`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle、WanVideoLoraSelect
