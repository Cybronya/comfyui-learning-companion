---
key: 平台全量/阿里Wan2.1图生视频运镜控制_1919936152940515330.json
name: 阿里Wan2.1图生视频运镜控制_1919936152940515330
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/阿里Wan2.1图生视频运镜控制_1919936152940515330.json
hash: c291d8959a7802a3
coverage: 0.5
learned_at: 2026-11-14 02:49:42
nodes: [GetNode, GetNode, GetNode, GetNode, GetNode, WanVideoVAELoader, SetNode, WanVideoTorchCompileSettings, WanVideoBlockSwap, Note, Note, MarkdownNote, Note, LoadWanVideoT5TextEncoder, SetNode, SetNode, GetNode, GetNode, GetNode, WanVideoModelLoader, GetNode, ImageResizeKJ, GetNode, WanVideoImageToVideoEncode, WanVideoTextEncode, Reroute, PreviewImage, CameraPoseVisualizer, WanVideoFunCameraEmbeds, WanVideoSLG, WanVideoSampler, WanVideoExperimentalArgs, WanVideoEnhanceAVideo, Note, ADE_CameraPoseBasic, WanVideoTeaCache, ADE_CameraPoseBasic, Note, LoadImage, CR Text, VHS_VideoCombine, ImageConcanate, VHS_VideoCombine, WanVideoDecode, PreviewImage, SetNode, Int, SetNode, SetNode, Int, SetNode, Int]
patterns: []
missing: []
---

# 平台全量/阿里Wan2.1图生视频运镜控制_1919936152940515330.json

> 来源文件 `comfyui_library/workflows/平台全量/阿里Wan2.1图生视频运镜控制_1919936152940515330.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（52 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `Note`
- `Note`
- `MarkdownNote`
- `Note`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `SetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoModelLoader`
- `GetNode`
- `ImageResizeKJ`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoTextEncode`
- `Reroute`
- `PreviewImage`
- `CameraPoseVisualizer`
- `WanVideoFunCameraEmbeds`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `WanVideoEnhanceAVideo`
- `Note`
- `ADE_CameraPoseBasic`
- `WanVideoTeaCache`
- `ADE_CameraPoseBasic`
- `Note`
- `LoadImage`
- `CR Text`
- `VHS_VideoCombine`
- `ImageConcanate`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `PreviewImage`
- `SetNode`
- `Int`
- `SetNode`
- `SetNode`
- `Int`
- `SetNode`
- `Int`

## 知识

覆盖率 **50%**（26/52）

**有卡**：`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`ImageResizeKJ`、`WanVideoImageToVideoEncode`、`WanVideoTextEncode`、`CameraPoseVisualizer`、`WanVideoFunCameraEmbeds`、`WanVideoSLG`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`WanVideoEnhanceAVideo`、`ADE_CameraPoseBasic`、`WanVideoTeaCache`、`LoadImage`、`CR Text`、`VHS_VideoCombine`、`ImageConcanate`、`WanVideoDecode`、`Int`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncode、WanVideoVAELoader、ImageResizeKJ
