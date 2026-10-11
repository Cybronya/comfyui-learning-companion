---
key: 视频生成/文生视频/Wan2.2 V5-MoE Fast I2V for Characters_2072999497279774720.json
name: Wan2.2 V5-MoE Fast I2V for Characters_2072999497279774720
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2 V5-MoE Fast I2V for Characters_2072999497279774720.json
hash: f2d8b87e1e5612ea
coverage: 0.6875
learned_at: 2026-10-11 20:21:31
nodes: [GetNode, SetNode, Note, WanVideoSetBlockSwap, Note, WanVideoSetBlockSwap, WanVideoSampler, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSampler, WanVideoSetRadialAttention, PrimitiveNode, WanVideoDecode, WanVideoSetRadialAttention, WanVideoScheduler, WanVideoBlockSwap, VHS_VideoCombine, WanVideoTextEncode, WanVideoScheduler, WanVideoModelLoader, easy seed, WanVideoTorchCompileSettings, easy globalSeed, WanVideoImageToVideoEncode, GetNode, WanVideoVAELoader, LoadWanVideoT5TextEncoder, Note, easy showAnything, PreviewImage, easy showAnything, ImageResizeKJv2, WanVideoModelLoader, Int, PrimitiveNode, WanVideoSigmaToStep, WanVideoLoraSelect, WanVideoLoraSelect, PrimitiveNode, Int, Int, LoadImage, String Literal, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect]
patterns: []
missing: [String Literal, easy globalSeed, easy seed]
discoveries: [次要节点 `String Literal` 知识库中没有该节点类型的任何知识, 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明, 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2 V5-MoE Fast I2V for Characters_2072999497279774720.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2 V5-MoE Fast I2V for Characters_2072999497279774720.json`

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

覆盖率 **69%**（33/48）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSampler`、`WanVideoSetLoRAs`、`WanVideoSetRadialAttention`、`WanVideoDecode`、`WanVideoScheduler`、`WanVideoBlockSwap`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`ImageResizeKJv2`、`Int`、`WanVideoSigmaToStep`、`WanVideoLoraSelect`、`LoadImage`

**缺卡**（3）：`String Literal`、`easy globalSeed`、`easy seed`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoLoraSelect

## 学习发现

- 次要节点 `String Literal` 知识库中没有该节点类型的任何知识
- 次要节点 `easy globalSeed` 仅有 KSampler 的通用知识，没有该节点自己的说明
- 次要节点 `easy seed` 仅有 KSampler 的通用知识，没有该节点自己的说明
