---
key: 视频生成/图生视频/Wan2.2-ControlCamera镜头控制_2004354618245214209.json
name: Wan2.2-ControlCamera镜头控制_2004354618245214209.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2-ControlCamera镜头控制_2004354618245214209.json
hash: eb2f2cf3d31d9ac0
coverage: 0.704545
learned_at: 2026-10-15 22:33:54
nodes: [GetNode, WanVideoImageToVideoEncode, WanVideoVAELoader, SetNode, ImageConcatMulti, GetNode, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoImageToVideoEncode, Primitive integer [Crystools], LoadImage, PrimitiveNode, PrimitiveNode, SimpleMath+, ImpactInt, ADE_CameraPoseCombo, Note, Text Multiline, CameraPoseVisualizer, WanVideoFunCameraEmbeds, SetNode, ImageResizeKJv2, SetNode, WanVideoTextEncodeCached, WanVideoSampler, PrimitiveNode, PrimitiveNode, WanVideoSampler, WanVideoDecode, GetNode, ImageConcatMulti, GetNode, VHS_VideoCombine, PreviewImage, VHS_VideoCombine, Primitive integer [Crystools]]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-ControlCamera镜头控制_2004354618245214209.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2004354618245214209.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（44 个）：
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `SetNode`
- `ImageConcatMulti`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `Primitive integer [Crystools]`
- `LoadImage`
- `PrimitiveNode`
- `PrimitiveNode`
- `SimpleMath+`
- `ImpactInt`
- `ADE_CameraPoseCombo`
- `Note`
- `Text Multiline`
- `CameraPoseVisualizer`
- `WanVideoFunCameraEmbeds`
- `SetNode`
- `ImageResizeKJv2`
- `SetNode`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `VHS_VideoCombine`
- `PreviewImage`
- `VHS_VideoCombine`
- `Primitive integer [Crystools]`

## 知识

覆盖率 **70%**（31/44）

**有卡**：`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`ImageConcatMulti`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`Primitive integer [Crystools]`、`LoadImage`、`SimpleMath+`、`ImpactInt`、`ADE_CameraPoseCombo`、`Text Multiline`、`CameraPoseVisualizer`、`WanVideoFunCameraEmbeds`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoDecode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
