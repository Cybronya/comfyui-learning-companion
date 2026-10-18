---
key: 视频生成/图生视频/Wan2.2图生视频性价比极致加速_1959896744446341122.json
name: Wan2.2图生视频性价比极致加速_1959896744446341122.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2图生视频性价比极致加速_1959896744446341122.json
hash: cf70980d7360f58f
coverage: 0.74359
learned_at: 2026-10-15 22:31:25
nodes: [GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoTorchCompileSettings, PrimitiveNode, WanVideoDecode, PrimitiveNode, PrimitiveNode, StringToFloatList, PrimitiveNode, easy globalSeed, PrimitiveNode, GetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSampler, WanVideoTextEncode, easy seed, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoBlockSwap, VHS_VideoCombine, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoContextOptions, WanVideoSetRadialAttention, WanVideoSetRadialAttention, ImageResizeKJv2, FloatToSigmas, WanVideoLoraSelect, WanVideoLoraSelect, LoadImage, String Literal, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频性价比极致加速_1959896744446341122.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1959896744446341122.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（39 个）：
- `GetNode`
- `SetNode`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoTorchCompileSettings`
- `PrimitiveNode`
- `WanVideoDecode`
- `PrimitiveNode`
- `PrimitiveNode`
- `StringToFloatList`
- `PrimitiveNode`
- `easy globalSeed`
- `PrimitiveNode`
- `GetNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `easy seed`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoContextOptions`
- `WanVideoSetRadialAttention`
- `WanVideoSetRadialAttention`
- `ImageResizeKJv2`
- `FloatToSigmas`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadImage`
- `String Literal`
- `WanVideoLoraSelect`

## 知识

覆盖率 **74%**（29/39）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`StringToFloatList`、`easy globalSeed`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSampler`、`WanVideoTextEncode`、`easy seed`、`WanVideoSetLoRAs`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`WanVideoContextOptions`、`WanVideoSetRadialAttention`、`ImageResizeKJv2`、`FloatToSigmas`、`WanVideoLoraSelect`、`LoadImage`、`String Literal`

**用到的条目**：LoadImage、WanVideoSampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
