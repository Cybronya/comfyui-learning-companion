---
key: 平台全量/Wan2.2-Fun-Camera运镜控制_2018144816646856706.json
name: Wan2.2-Fun-Camera运镜控制_2018144816646856706
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.2-Fun-Camera运镜控制_2018144816646856706.json
hash: 156951c774075d3e
coverage: 0.644444
learned_at: 2026-11-14 01:05:58
nodes: [GetNode, GetNode, SetNode, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, CameraPoseVisualizer, SetNode, PreviewImage, ImageConcatMulti, ImageConcatMulti, WanVideoTorchCompileSettings, Note, Note, GetNode, GetNode, WanVideoSampler, WanVideoImageToVideoEncode, WanVideoBlockSwap, WanVideoFunCameraEmbeds, PrimitiveNode, WanVideoImageToVideoEncode, ImageResizeKJv2, Note, Primitive integer [Crystools], WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVAELoader, VHS_VideoCombine, WanVideoDecode, Primitive integer [Crystools], PrimitiveNode, PrimitiveNode, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncodeCached, PrimitiveNode, PrimitiveNode, ADE_CameraPoseCombo, VHS_VideoCombine, Text Multiline, LoadImage]
patterns: []
missing: []
---

# 平台全量/Wan2.2-Fun-Camera运镜控制_2018144816646856706.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.2-Fun-Camera运镜控制_2018144816646856706.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（45 个）：
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
- `ImageConcatMulti`
- `ImageConcatMulti`
- `WanVideoTorchCompileSettings`
- `Note`
- `Note`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `WanVideoBlockSwap`
- `WanVideoFunCameraEmbeds`
- `PrimitiveNode`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJv2`
- `Note`
- `Primitive integer [Crystools]`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `Primitive integer [Crystools]`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncodeCached`
- `PrimitiveNode`
- `PrimitiveNode`
- `ADE_CameraPoseCombo`
- `VHS_VideoCombine`
- `Text Multiline`
- `LoadImage`

## 知识

覆盖率 **64%**（29/45）

**有卡**：`WanVideoSampler`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`CameraPoseVisualizer`、`ImageConcatMulti`、`WanVideoTorchCompileSettings`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`WanVideoFunCameraEmbeds`、`ImageResizeKJv2`、`Primitive integer [Crystools]`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`VHS_VideoCombine`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoTextEncodeCached`、`ADE_CameraPoseCombo`、`Text Multiline`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoVAELoader、WanVideoLoraSelect、WanVideoSetLoRAs
