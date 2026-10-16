---
key: 视频生成/图生视频/wan2.2 fun奖励LORA 图生视频-KJ版-更好动态 更好效果_1991002919573102593.json
name: wan2.2 fun奖励LORA 图生视频-KJ版-更好动态 更好效果_1991002919573102593.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1991002919573102593.json
hash: 6d58bc2d85bdc811
coverage: 1
learned_at: 2026-10-15 22:33:12
nodes: [WanVideoTextEncodeSingle, ImageResizeKJv2, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, SimpleMath+, SimpleMath+, WanVideoApplyNAG, WanVideoSampler, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoTextEncodeSingle, LoadImage, WanVideoTorchCompileSettings, INTConstant, ImpactInt, ImpactInt, ImpactInt, CR Text, GetImageSizeAndCount, VHS_VideoCombine, VHS_VideoCombine, WanVideoLoraSelectMulti]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 fun奖励LORA 图生视频-KJ版-更好动态 更好效果_1991002919573102593.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1991002919573102593.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（29 个）：
- `WanVideoTextEncodeSingle`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoBlockSwap`
- `SimpleMath+`
- `SimpleMath+`
- `WanVideoApplyNAG`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoTextEncodeSingle`
- `LoadImage`
- `WanVideoTorchCompileSettings`
- `INTConstant`
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `CR Text`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoLoraSelectMulti`

## 知识

覆盖率 **100%**（29/29）

**有卡**：`WanVideoTextEncodeSingle`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`SimpleMath+`、`WanVideoApplyNAG`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`LoadImage`、`WanVideoTorchCompileSettings`、`INTConstant`、`ImpactInt`、`CR Text`、`GetImageSizeAndCount`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle、WanVideoLoraSelectMulti
