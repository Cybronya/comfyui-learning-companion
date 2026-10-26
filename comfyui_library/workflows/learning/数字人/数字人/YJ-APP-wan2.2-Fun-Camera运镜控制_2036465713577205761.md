---
key: 数字人/数字人/YJ-APP-wan2.2-Fun-Camera运镜控制_2036465713577205761.json
name: YJ-APP-wan2.2-Fun-Camera运镜控制_2036465713577205761
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/YJ-APP-wan2.2-Fun-Camera运镜控制_2036465713577205761.json
hash: 336ed361cca19495
coverage: 0.807692
learned_at: 2026-10-26 01:58:14
nodes: [GetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoLoraSelect, GetNode, PreviewImage, SetNode, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTorchCompileSettings, WanVideoSampler, WanVideoModelLoader, WanVideoModelLoader, WanVideoImageToVideoEncode, WanVideoTextEncodeCached, WanVideoImageToVideoEncode, WanVideoDecode, VHS_VideoCombine, SetNode, ImageResizeKJv2, LoadImage, CameraPoseVisualizer, WanVideoFunCameraEmbeds, Int, Int, WanVideoSampler, PrimitiveNode, WanVideoVAELoader, TextInput_, Int, SetNode, PrimitiveNode, PrimitiveNode, PrimitiveNode, Int, WanVideoBlockSwap, Float, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, ADE_CameraPoseCombo, Switch, ADE_CameraPoseCombo, ADE_CameraPoseCombo, SimpleMath+]
patterns: []
missing: []
---

# 数字人/数字人/YJ-APP-wan2.2-Fun-Camera运镜控制_2036465713577205761.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/YJ-APP-wan2.2-Fun-Camera运镜控制_2036465713577205761.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（52 个）：
- `GetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetNode`
- `PreviewImage`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncodeCached`
- `WanVideoImageToVideoEncode`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `SetNode`
- `ImageResizeKJv2`
- `LoadImage`
- `CameraPoseVisualizer`
- `WanVideoFunCameraEmbeds`
- `Int`
- `Int`
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `WanVideoVAELoader`
- `TextInput_`
- `Int`
- `SetNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `Int`
- `WanVideoBlockSwap`
- `Float`
- `ADE_CameraPoseCombo`
- `ADE_CameraPoseCombo`
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
- `SimpleMath+`

## 知识

覆盖率 **81%**（42/52）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`WanVideoModelLoader`、`WanVideoImageToVideoEncode`、`WanVideoTextEncodeCached`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageResizeKJv2`、`LoadImage`、`CameraPoseVisualizer`、`WanVideoFunCameraEmbeds`、`Int`、`WanVideoVAELoader`、`TextInput_`、`WanVideoBlockSwap`、`Float`、`ADE_CameraPoseCombo`、`Switch`、`SimpleMath+`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
