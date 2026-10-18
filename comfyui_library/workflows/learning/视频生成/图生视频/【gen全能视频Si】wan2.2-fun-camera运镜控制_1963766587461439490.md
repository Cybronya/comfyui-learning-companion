---
key: 视频生成/图生视频/【gen全能视频Si】wan2.2-fun-camera运镜控制_1963766587461439490.json
name: 【gen全能视频Si】wan2.2-fun-camera运镜控制_1963766587461439490.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/【gen全能视频Si】wan2.2-fun-camera运镜控制_1963766587461439490.json
hash: 2f554f28cdeb1f1c
coverage: 0.659574
learned_at: 2026-10-15 22:31:33
nodes: [GetNode, SetNode, WanVideoTextEncodeCached, PrimitiveNode, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoLoraSelect, WanVideoSampler, ImageResizeKJv2, LoadImage, WanVideoImageToVideoEncode, CameraPoseVisualizer, SetNode, WanVideoFunCameraEmbeds, PrimitiveNode, PrimitiveNode, PrimitiveNode, GetNode, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, Note, WanVideoImageToVideoEncode, WanVideoSetLoRAs, Note, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, ImageConcatMulti, ImageConcatMulti, GetNode, GetNode, WanVideoDecode, WanVideoSampler, ADE_CameraPoseCombo, WanVideoBlockSwap, WanVideoVAELoader, SetNode, Note, Primitive integer [Crystools], PrimitiveNode, Primitive integer [Crystools], PreViewVideo, CreateVideo, WanVideoSetLoRAs, Text Multiline]
patterns: []
missing: []
---

# 视频生成/图生视频/【gen全能视频Si】wan2.2-fun-camera运镜控制_1963766587461439490.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1963766587461439490.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（47 个）：
- `GetNode`
- `SetNode`
- `WanVideoTextEncodeCached`
- `PrimitiveNode`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `LoadImage`
- `WanVideoImageToVideoEncode`
- `CameraPoseVisualizer`
- `SetNode`
- `WanVideoFunCameraEmbeds`
- `PrimitiveNode`
- `PrimitiveNode`
- `PrimitiveNode`
- `GetNode`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `Note`
- `WanVideoImageToVideoEncode`
- `WanVideoSetLoRAs`
- `Note`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `ADE_CameraPoseCombo`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `SetNode`
- `Note`
- `Primitive integer [Crystools]`
- `PrimitiveNode`
- `Primitive integer [Crystools]`
- `PreViewVideo`
- `CreateVideo`
- `WanVideoSetLoRAs`
- `Text Multiline`

## 知识

覆盖率 **66%**（31/47）

**有卡**：`WanVideoTextEncodeCached`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoLoraSelect`、`WanVideoSampler`、`ImageResizeKJv2`、`LoadImage`、`WanVideoImageToVideoEncode`、`CameraPoseVisualizer`、`WanVideoFunCameraEmbeds`、`WanVideoTorchCompileSettings`、`WanVideoSetLoRAs`、`VHS_VideoCombine`、`ImageConcatMulti`、`WanVideoDecode`、`ADE_CameraPoseCombo`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`Primitive integer [Crystools]`、`PreViewVideo`、`CreateVideo`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
