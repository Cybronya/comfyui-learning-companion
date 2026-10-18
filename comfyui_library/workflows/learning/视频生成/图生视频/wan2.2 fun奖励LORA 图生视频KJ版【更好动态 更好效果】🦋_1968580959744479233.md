---
key: 视频生成/图生视频/wan2.2 fun奖励LORA 图生视频KJ版【更好动态 更好效果】🦋_1968580959744479233.json
name: wan2.2 fun奖励LORA 图生视频KJ版【更好动态 更好效果】🦋_1968580959744479233.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/wan2.2 fun奖励LORA 图生视频KJ版【更好动态 更好效果】🦋_1968580959744479233.json
hash: 0fb72eae43e608be
coverage: 0.966667
learned_at: 2026-10-15 22:31:45
nodes: [WanVideoTextEncodeSingle, WanVideoTorchCompileSettings, ImageResizeKJv2, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoBlockSwap, SimpleMath+, SimpleMath+, WanVideoApplyNAG, WanVideoSampler, WanVideoDecode, WanVideoSetBlockSwap, WanVideoSampler, ImpactInt, ImpactInt, ImpactInt, WanVideoSetBlockSwap, INTConstant, CR Text, LoadImage, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoModelLoader, WanVideoLoraSelectMulti, WanVideoVAELoader, WanVideoTextEncodeSingle, VHS_VideoCombine, GetImageSizeAndCount, VHS_VideoCombine, Note]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 fun奖励LORA 图生视频KJ版【更好动态 更好效果】🦋_1968580959744479233.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1968580959744479233.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoTextEncodeSingle`
- `WanVideoTorchCompileSettings`
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
- `ImpactInt`
- `ImpactInt`
- `ImpactInt`
- `WanVideoSetBlockSwap`
- `INTConstant`
- `CR Text`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoModelLoader`
- `WanVideoLoraSelectMulti`
- `WanVideoVAELoader`
- `WanVideoTextEncodeSingle`
- `VHS_VideoCombine`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `Note`

## 知识

覆盖率 **97%**（29/30）

**有卡**：`WanVideoTextEncodeSingle`、`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoBlockSwap`、`SimpleMath+`、`WanVideoApplyNAG`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoSetBlockSwap`、`ImpactInt`、`INTConstant`、`CR Text`、`LoadImage`、`WanVideoModelLoader`、`WanVideoLoraSelectMulti`、`WanVideoVAELoader`、`VHS_VideoCombine`、`GetImageSizeAndCount`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeSingle、WanVideoLoraSelectMulti
