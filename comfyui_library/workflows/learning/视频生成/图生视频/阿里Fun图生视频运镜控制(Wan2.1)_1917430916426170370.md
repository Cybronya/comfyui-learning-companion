---
key: 视频生成/图生视频/阿里Fun图生视频运镜控制(Wan2.1)_1917430916426170370.json
name: 阿里Fun图生视频运镜控制(Wan2.1)_1917430916426170370.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/阿里Fun图生视频运镜控制(Wan2.1)_1917430916426170370.json
hash: 71471252db107ccf
coverage: 0.727273
learned_at: 2026-10-15 22:29:40
nodes: [MarkdownNote, SetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoTextEncode, Primitive integer [Crystools], Primitive integer [Crystools], SetNode, GetNode, WanVideoImageToVideoEncode, Reroute, WanVideoTeaCache, GetNode, WanVideoDecode, GetNode, ImageConcatMulti, VHS_VideoCombine, PreviewImage, ImageResizeKJ, WanVideoModelLoader, WanVideoExperimentalArgs, CameraPoseVisualizer, WanVideoFunCameraEmbeds, VHS_VideoCombine, LoadImage, INTConstant, WanVideoSampler, Text Multiline, Note, ADE_CameraPoseBasic, ADE_CameraPoseBasic]
patterns: []
missing: []
---

# 视频生成/图生视频/阿里Fun图生视频运镜控制(Wan2.1)_1917430916426170370.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1917430916426170370.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（33 个）：
- `MarkdownNote`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `SetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `Reroute`
- `WanVideoTeaCache`
- `GetNode`
- `WanVideoDecode`
- `GetNode`
- `ImageConcatMulti`
- `VHS_VideoCombine`
- `PreviewImage`
- `ImageResizeKJ`
- `WanVideoModelLoader`
- `WanVideoExperimentalArgs`
- `CameraPoseVisualizer`
- `WanVideoFunCameraEmbeds`
- `VHS_VideoCombine`
- `LoadImage`
- `INTConstant`
- `WanVideoSampler` ★核心
- `Text Multiline`
- `Note`
- `ADE_CameraPoseBasic`
- `ADE_CameraPoseBasic`

## 知识

覆盖率 **73%**（24/33）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`Primitive integer [Crystools]`、`WanVideoImageToVideoEncode`、`WanVideoTeaCache`、`WanVideoDecode`、`ImageConcatMulti`、`VHS_VideoCombine`、`ImageResizeKJ`、`WanVideoModelLoader`、`WanVideoExperimentalArgs`、`CameraPoseVisualizer`、`WanVideoFunCameraEmbeds`、`LoadImage`、`INTConstant`、`WanVideoSampler`、`Text Multiline`、`ADE_CameraPoseBasic`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、ImageResizeKJ
