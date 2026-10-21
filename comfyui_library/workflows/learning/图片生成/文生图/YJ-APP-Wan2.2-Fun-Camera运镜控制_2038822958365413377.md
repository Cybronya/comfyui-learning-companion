---
key: 图片生成/文生图/YJ-APP-Wan2.2-Fun-Camera运镜控制_2038822958365413377.json
name: YJ-APP-Wan2.2-Fun-Camera运镜控制_2038822958365413377
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/YJ-APP-Wan2.2-Fun-Camera运镜控制_2038822958365413377.json
hash: f68875d4141e6967
coverage: 0.767857
learned_at: 2026-10-21 02:55:27
nodes: [GetNode, GetNode, SetNode, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, CameraPoseVisualizer, SetNode, PreviewImage, WanVideoTorchCompileSettings, Note, Note, WanVideoSampler, WanVideoImageToVideoEncode, WanVideoBlockSwap, ImageResizeKJv2, Note, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVAELoader, WanVideoDecode, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncodeCached, PrimitiveNode, PrimitiveNode, LoadImage, PrimitiveNode, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, Switch, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, Int, VHS_VideoCombine, WanVideoFunCameraEmbeds, PrimitiveNode, WanVideoImageToVideoEncode, ADE_CameraPoseCombo, SimpleMath+, Int, Int, Int, Primitive integer [Crystools], Primitive integer [Crystools], Text]
patterns: []
missing: []
---

# 图片生成/文生图/YJ-APP-Wan2.2-Fun-Camera运镜控制_2038822958365413377.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/YJ-APP-Wan2.2-Fun-Camera运镜控制_2038822958365413377.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（56 个）：
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `CameraPoseVisualizer`
- `SetNode`
- `PreviewImage`
- `WanVideoTorchCompileSettings`
- `Note`
- `Note`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `WanVideoBlockSwap`
- `ImageResizeKJv2`
- `Note`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `PrimitiveNode`
- `PrimitiveNode`
- `LoadImage`
- `PrimitiveNode`
- `ADE_CameraPoseCombo`
- `ADE_CameraPoseCombo`
- `ADE_CameraPoseCombo`
- `ADE_CameraPoseCombo`
- `ADE_CameraPoseCombo`
- `ADE_CameraPoseCombo`
- `ADE_CameraPoseCombo`
- `ADE_CameraPoseCombo`
- `Switch`
- `ADE_CameraPoseCombo`
- `ADE_CameraPoseCombo`
- `ADE_CameraPoseCombo`
- `Int`
- `VHS_VideoCombine`
- `WanVideoFunCameraEmbeds`
- `PrimitiveNode`
- `WanVideoImageToVideoEncode`
- `ADE_CameraPoseCombo`
- `SimpleMath+`
- `Int`
- `Int`
- `Int`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `Text`

## 知识

覆盖率 **77%**（43/56）

**有卡**：`WanVideoSampler`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CameraPoseVisualizer`、`WanVideoTorchCompileSettings`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`ImageResizeKJv2`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`LoadImage`、`ADE_CameraPoseCombo`、`Switch`、`Int`、`VHS_VideoCombine`、`WanVideoFunCameraEmbeds`、`SimpleMath+`、`Primitive integer [Crystools]`、`Text`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
