---
key: 视频生成/文生视频/Wan2.2图生视频性价比极致加速V3_2072999534260953088.json
name: Wan2.2图生视频性价比极致加速V3_2072999534260953088
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V3_2072999534260953088.json
hash: b401d2df20822e60
coverage: 0.75
learned_at: 2026-10-15 22:47:14
nodes: [GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSampler, WanVideoSetRadialAttention, PrimitiveNode, WanVideoDecode, WanVideoSetRadialAttention, WanVideoScheduler, PrimitiveNode, WanVideoBlockSwap, VHS_VideoCombine, WanVideoTextEncode, WanVideoScheduler, WanVideoModelLoader, easy seed, WanVideoTorchCompileSettings, easy globalSeed, WanVideoImageToVideoEncode, GetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, Note, easy showAnything, PreviewImage, easy showAnything, ImageResizeKJv2, Int, Int, WanVideoModelLoader, WanVideoLoraSelect, Int, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, String Literal, PrimitiveNode, LoadImage, WanVideoSigmaToStep]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2图生视频性价比极致加速V3_2072999534260953088.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V3_2072999534260953088.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（48 个）：
- `GetNode`
- `SetNode`
- `Note`
- `WanVideoSetBlockSwap`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoSetRadialAttention`
- `PrimitiveNode`
- `WanVideoDecode`
- `WanVideoSetRadialAttention`
- `WanVideoScheduler`
- `PrimitiveNode`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoScheduler`
- `WanVideoModelLoader`
- `easy seed`
- `WanVideoTorchCompileSettings`
- `easy globalSeed`
- `WanVideoImageToVideoEncode`
- `GetNode`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `Note`
- `easy showAnything`
- `PreviewImage`
- `easy showAnything`
- `ImageResizeKJv2`
- `Int`
- `Int`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `Int`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `String Literal`
- `PrimitiveNode`
- `LoadImage`
- `WanVideoSigmaToStep`

## 知识

覆盖率 **75%**（36/48）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoSetRadialAttention`、`WanVideoDecode`、`WanVideoScheduler`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoModelLoader`、`easy seed`、`WanVideoTorchCompileSettings`、`easy globalSeed`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJv2`、`Int`、`WanVideoLoraSelect`、`String Literal`、`LoadImage`、`WanVideoSigmaToStep`

**用到的条目**：LoadImage、WanVideoSampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
