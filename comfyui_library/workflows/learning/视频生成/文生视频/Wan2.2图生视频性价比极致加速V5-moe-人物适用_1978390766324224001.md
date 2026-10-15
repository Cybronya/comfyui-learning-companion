---
key: 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5-moe-人物适用_1978390766324224001.json
name: Wan2.2图生视频性价比极致加速V5-moe-人物适用_1978390766324224001
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V5-moe-人物适用_1978390766324224001.json
hash: 6d19b742aa778f5c
coverage: 0.75
learned_at: 2026-10-15 22:47:14
nodes: [GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSampler, WanVideoSetRadialAttention, PrimitiveNode, WanVideoDecode, WanVideoSetRadialAttention, WanVideoScheduler, WanVideoBlockSwap, VHS_VideoCombine, WanVideoTextEncode, WanVideoScheduler, WanVideoModelLoader, easy seed, WanVideoTorchCompileSettings, easy globalSeed, WanVideoImageToVideoEncode, GetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, Note, easy showAnything, PreviewImage, easy showAnything, ImageResizeKJv2, WanVideoModelLoader, Int, PrimitiveNode, WanVideoSigmaToStep, WanVideoLoraSelect, WanVideoLoraSelect, PrimitiveNode, Int, Int, LoadImage, String Literal, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5-moe-人物适用_1978390766324224001.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V5-moe-人物适用_1978390766324224001.json`

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
- `WanVideoModelLoader`
- `Int`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `Int`
- `Int`
- `LoadImage`
- `String Literal`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`

## 知识

覆盖率 **75%**（36/48）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoSetRadialAttention`、`WanVideoDecode`、`WanVideoScheduler`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoModelLoader`、`easy seed`、`WanVideoTorchCompileSettings`、`easy globalSeed`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJv2`、`Int`、`WanVideoSigmaToStep`、`WanVideoLoraSelect`、`LoadImage`、`String Literal`

**用到的条目**：LoadImage、WanVideoSampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
