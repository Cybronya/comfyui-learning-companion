---
key: 视频生成/图生视频/WH-AI-Studio-wan2.2官方专用运镜模型图生视频_2015621060615475201.json
name: WH-AI-Studio-wan2.2官方专用运镜模型图生视频_2015621060615475201.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WH-AI-Studio-wan2.2官方专用运镜模型图生视频_2015621060615475201.json
hash: 228620e261cb3a99
coverage: 0.731707
learned_at: 2026-10-15 22:34:39
nodes: [GetNode, SetNode, WanVideoSetBlockSwap, WanVideoBlockSwap, WanVideoSetLoRAs, PrimitiveNode, WanVideoFunCameraEmbeds, SetNode, PrimitiveNode, PrimitiveNode, WanVideoTorchCompileSettings, SimpleMath+, WanVideoDecode, VHS_VideoCombine, WanVideoSetBlockSwap, WanVideoSetLoRAs, SetNode, ImageResizeKJv2, WanVideoTextEncodeCached, WanVideoSampler, WanVideoSampler, PrimitiveNode, VHS_VideoCombine, WanVideoImageToVideoEncode, Note, WanVideoModelLoader, WanVideoModelLoader, PreviewImage, GetNode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVAELoader, RIFE VFI, WanVideoImageToVideoEncode, Primitive integer [Crystools], CameraPoseVisualizer, ImpactInt, Primitive integer [Crystools], ADE_CameraPoseCombo, LoadImage, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/WH-AI-Studio-wan2.2官方专用运镜模型图生视频_2015621060615475201.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2015621060615475201.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `GetNode`
- `SetNode`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `WanVideoFunCameraEmbeds`
- `SetNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoTorchCompileSettings`
- `SimpleMath+`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `SetNode`
- `ImageResizeKJv2`
- `WanVideoTextEncodeCached`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `VHS_VideoCombine`
- `WanVideoImageToVideoEncode`
- `Note`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `PreviewImage`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `RIFE VFI`
- `WanVideoImageToVideoEncode`
- `Primitive integer [Crystools]`
- `CameraPoseVisualizer`
- `ImpactInt`
- `Primitive integer [Crystools]`
- `ADE_CameraPoseCombo`
- `LoadImage`
- `Text Multiline`

## 知识

覆盖率 **73%**（30/41）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoFunCameraEmbeds`、`WanVideoTorchCompileSettings`、`SimpleMath+`、`WanVideoDecode`、`VHS_VideoCombine`、`ImageResizeKJv2`、`WanVideoTextEncodeCached`、`WanVideoSampler`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`RIFE VFI`、`Primitive integer [Crystools]`、`CameraPoseVisualizer`、`ImpactInt`、`ADE_CameraPoseCombo`、`LoadImage`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
