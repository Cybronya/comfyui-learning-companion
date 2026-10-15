---
key: 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5-1030-非人_1984904372494680065.json
name: Wan2.2图生视频性价比极致加速V5-1030-非人_1984904372494680065
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V5-1030-非人_1984904372494680065.json
hash: d230a7fd08b834f2
coverage: 0.75
learned_at: 2026-10-15 22:47:14
nodes: [String Literal, Note, WanVideoSetBlockSwap, Note, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSampler, WanVideoSetRadialAttention, PrimitiveNode, WanVideoSetRadialAttention, WanVideoScheduler, WanVideoBlockSwap, VHS_VideoCombine, WanVideoTextEncode, WanVideoScheduler, WanVideoModelLoader, easy seed, WanVideoTorchCompileSettings, easy globalSeed, WanVideoImageToVideoEncode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, easy showAnything, PreviewImage, easy showAnything, ImageResizeKJv2, WanVideoModelLoader, Int, PrimitiveNode, WanVideoSigmaToStep, WanVideoLoraSelect, PrimitiveNode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoDecode, LoadImage, GetNode, SetNode, GetNode, WanVideoLoraSelect, Note, Int, Int]
patterns: []
missing: []
---

# 视频生成/文生视频/Wan2.2图生视频性价比极致加速V5-1030-非人_1984904372494680065.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2图生视频性价比极致加速V5-1030-非人_1984904372494680065.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（48 个）：
- `String Literal`
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
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `easy showAnything`
- `PreviewImage`
- `easy showAnything`
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `Int`
- `PrimitiveNode`
- `WanVideoSigmaToStep`
- `WanVideoLoraSelect`
- `PrimitiveNode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoDecode`
- `LoadImage`
- `GetNode`
- `SetNode`
- `GetNode`
- `WanVideoLoraSelect`
- `Note`
- `Int`
- `Int`

## 知识

覆盖率 **75%**（36/48）

**有卡**：`String Literal`、`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoSetRadialAttention`、`WanVideoScheduler`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoModelLoader`、`easy seed`、`WanVideoTorchCompileSettings`、`easy globalSeed`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJv2`、`Int`、`WanVideoSigmaToStep`、`WanVideoLoraSelect`、`WanVideoDecode`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、easy globalSeed、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
