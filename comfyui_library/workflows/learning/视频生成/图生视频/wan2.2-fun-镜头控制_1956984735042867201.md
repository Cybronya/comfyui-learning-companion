---
key: 视频生成/图生视频/wan2.2-fun-镜头控制_1956984735042867201.json
name: wan2.2-fun-镜头控制_1956984735042867201.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1956984735042867201.json
hash: d8278aa5282908ed
coverage: 0.748387
learned_at: 2026-10-15 22:31:15
nodes: [GetNode, WanVideoTextEncode, SetNode, Note, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoVAELoader, LoadWanVideoT5TextEncoder, FloatToSigmas, PrimitiveNode, WanVideoDecode, Note, PrimitiveNode, PrimitiveNode, StringToFloatList, PrimitiveNode, easy globalSeed, PrimitiveNode, WanVideoSampler, WanVideoSampler, GetNode, CameraPoseVisualizer, PreviewImage, ImageResizeKJv2, WanVideoFunCameraEmbeds, String Literal, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, LoadImage, RH_Captioner, WanVideoModelLoader, WanVideoTextEncode, Note, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, WanVideoBlockSwap, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, FloatToSigmas, PrimitiveNode, VHS_VideoCombine, WanVideoDecode, Note, PrimitiveNode, PrimitiveNode, StringToFloatList, PrimitiveNode, easy globalSeed, PrimitiveNode, WanVideoSampler, WanVideoSampler, CameraPoseVisualizer, PreviewImage, ImageResizeKJv2, WanVideoFunCameraEmbeds, String Literal, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, RH_Captioner, WanVideoModelLoader, WanVideoModelLoader, LoadImage, WanVideoVAELoader, WanVideoTextEncode, Note, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, WanVideoBlockSwap, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, FloatToSigmas, PrimitiveNode, WanVideoDecode, Note, PrimitiveNode, PrimitiveNode, PrimitiveNode, easy globalSeed, PrimitiveNode, WanVideoSampler, WanVideoSampler, CameraPoseVisualizer, PreviewImage, ImageResizeKJv2, WanVideoFunCameraEmbeds, String Literal, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, RH_Captioner, WanVideoModelLoader, WanVideoVAELoader, LoadImage, WanVideoModelLoader, WanVideoModelLoader, WanVideoImageToVideoEncode, WanVideoImageToVideoEncode, WanVideoImageToVideoEncode, WanVideoImageToVideoEncode, WanVideoImageToVideoEncode, WanVideoImageToVideoEncode, WanVideoTextEncode, Note, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Note, WanVideoBlockSwap, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, FloatToSigmas, PrimitiveNode, WanVideoDecode, Note, PrimitiveNode, PrimitiveNode, StringToFloatList, PrimitiveNode, easy globalSeed, PrimitiveNode, WanVideoSampler, WanVideoSampler, CameraPoseVisualizer, PreviewImage, ImageResizeKJv2, WanVideoFunCameraEmbeds, String Literal, WanVideoLoraSelectMulti, WanVideoLoraSelectMulti, RH_Captioner, WanVideoModelLoader, WanVideoVAELoader, WanVideoModelLoader, WanVideoImageToVideoEncode, ADE_CameraPoseAdvanced, LoadImage, ADE_CameraPoseAdvanced, ADE_CameraPoseAdvanced, WanVideoImageToVideoEncode, StringToFloatList, ADE_CameraPoseAdvanced, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-fun-镜头控制_1956984735042867201.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1956984735042867201.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（155 个）：
- `GetNode`
- `WanVideoTextEncode`
- `SetNode`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `FloatToSigmas`
- `PrimitiveNode`
- `WanVideoDecode`
- `Note`
- `PrimitiveNode`
- `PrimitiveNode`
- `StringToFloatList`
- `PrimitiveNode`
- `easy globalSeed`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `GetNode`
- `CameraPoseVisualizer`
- `PreviewImage`
- `ImageResizeKJv2`
- `WanVideoFunCameraEmbeds`
- `String Literal`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `LoadImage`
- `RH_Captioner`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `FloatToSigmas`
- `PrimitiveNode`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `Note`
- `PrimitiveNode`
- `PrimitiveNode`
- `StringToFloatList`
- `PrimitiveNode`
- `easy globalSeed`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CameraPoseVisualizer`
- `PreviewImage`
- `ImageResizeKJv2`
- `WanVideoFunCameraEmbeds`
- `String Literal`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `RH_Captioner`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadImage`
- `WanVideoVAELoader`
- `WanVideoTextEncode`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `FloatToSigmas`
- `PrimitiveNode`
- `WanVideoDecode`
- `Note`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `easy globalSeed`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CameraPoseVisualizer`
- `PreviewImage`
- `ImageResizeKJv2`
- `WanVideoFunCameraEmbeds`
- `String Literal`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `RH_Captioner`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadImage`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncode`
- `Note`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `FloatToSigmas`
- `PrimitiveNode`
- `WanVideoDecode`
- `Note`
- `PrimitiveNode`
- `PrimitiveNode`
- `StringToFloatList`
- `PrimitiveNode`
- `easy globalSeed`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `CameraPoseVisualizer`
- `PreviewImage`
- `ImageResizeKJv2`
- `WanVideoFunCameraEmbeds`
- `String Literal`
- `WanVideoLoraSelectMulti`
- `WanVideoLoraSelectMulti`
- `RH_Captioner`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `ADE_CameraPoseAdvanced`
- `LoadImage`
- `ADE_CameraPoseAdvanced`
- `ADE_CameraPoseAdvanced`
- `WanVideoImageToVideoEncode`
- `StringToFloatList`
- `ADE_CameraPoseAdvanced`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **75%**（116/155）

**有卡**：`WanVideoTextEncode`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`FloatToSigmas`、`WanVideoDecode`、`StringToFloatList`、`easy globalSeed`、`WanVideoSampler`、`CameraPoseVisualizer`、`ImageResizeKJv2`、`WanVideoFunCameraEmbeds`、`String Literal`、`WanVideoLoraSelectMulti`、`LoadImage`、`RH_Captioner`、`WanVideoModelLoader`、`VHS_VideoCombine`、`WanVideoImageToVideoEncode`、`ADE_CameraPoseAdvanced`

**用到的条目**：LoadImage、WanVideoSampler、easy globalSeed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
