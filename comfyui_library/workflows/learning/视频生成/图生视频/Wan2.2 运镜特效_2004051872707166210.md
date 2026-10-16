---
key: 视频生成/图生视频/Wan2.2 运镜特效_2004051872707166210.json
name: Wan2.2 运镜特效_2004051872707166210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2004051872707166210.json
hash: c1e08061c0e3f451
coverage: 0.690476
learned_at: 2026-10-15 22:33:52
nodes: [GetNode, Primitive integer [Crystools], PrimitiveNode, PrimitiveNode, SetNode, WanVideoImageToVideoEncode, WanVideoSampler, WanVideoSampler, PrimitiveNode, PrimitiveNode, WanVideoVAELoader, SetNode, GetNode, ImageConcatMulti, GetNode, GetNode, WanVideoDecode, ImageConcatMulti, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoModelLoader, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncodeCached, VHS_VideoCombine, VHS_VideoCombine, SetNode, PreviewImage, ImageResizeKJv2, WanVideoFunCameraEmbeds, CameraPoseVisualizer, ADE_CameraPoseCombo, PrimitiveNode, WanVideoImageToVideoEncode, Text Multiline, Primitive integer [Crystools], LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 运镜特效_2004051872707166210.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2004051872707166210.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（42 个）：
- `GetNode`
- `Primitive integer [Crystools]`
- `PrimitiveNode`
- `PrimitiveNode`
- `SetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `PrimitiveNode`
- `PrimitiveNode`
- `WanVideoVAELoader`
- `SetNode`
- `GetNode`
- `ImageConcatMulti`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `ImageConcatMulti`
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
- `WanVideoTextEncodeCached`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `SetNode`
- `PreviewImage`
- `ImageResizeKJv2`
- `WanVideoFunCameraEmbeds`
- `CameraPoseVisualizer`
- `ADE_CameraPoseCombo`
- `PrimitiveNode`
- `WanVideoImageToVideoEncode`
- `Text Multiline`
- `Primitive integer [Crystools]`
- `LoadImage`

## 知识

覆盖率 **69%**（29/42）

**有卡**：`Primitive integer [Crystools]`、`WanVideoImageToVideoEncode`、`WanVideoSampler`、`WanVideoVAELoader`、`ImageConcatMulti`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoTextEncodeCached`、`VHS_VideoCombine`、`ImageResizeKJv2`、`WanVideoFunCameraEmbeds`、`CameraPoseVisualizer`、`ADE_CameraPoseCombo`、`Text Multiline`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、WanVideoDecode、WanVideoVAELoader、WanVideoImageToVideoEncode、WanVideoTextEncodeCached、WanVideoLoraSelect、WanVideoSetLoRAs
