---
key: 平台全量/【Wan2.1系列】轻松生成电影级运镜画面！Fun Camera模型实战解析轻松掌握运镜_1921554498571943938.json
name: 【Wan2.1系列】轻松生成电影级运镜画面！Fun Camera模型实战解析轻松掌握运镜_1921554498571943938
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/【Wan2.1系列】轻松生成电影级运镜画面！Fun Camera模型实战解析轻松掌握运镜_1921554498571943938.json
hash: 40041c4c988afce0
coverage: 0.782609
learned_at: 2026-11-14 01:22:21
nodes: [GetNode, GetNode, GetNode, WanVideoDecode, WanVideoTeaCache, Reroute, ImageConcatMulti, SetNode, WanVideoImageToVideoEncode, PreviewImage, ImageResizeKJv2, WanVideoBlockSwap, WanVideoExperimentalArgs, LoadImage, WanVideoSampler, WanVideoTextEncode, WanVideoModelLoader, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SetNode, CameraPoseVisualizer, PreviewImage, WanVideoFunCameraEmbeds, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoTorchCompileSettings, VHS_VideoCombine, ADE_CameraPoseBasic, ADE_CameraPoseBasic, VHS_VideoCombine, Note, INTConstant, VHS_VideoCombine, ADE_CameraPoseBasic, MarkdownNote]
patterns: []
missing: []
---

# 平台全量/【Wan2.1系列】轻松生成电影级运镜画面！Fun Camera模型实战解析轻松掌握运镜_1921554498571943938.json

> 来源文件 `comfyui_library/workflows/平台全量/【Wan2.1系列】轻松生成电影级运镜画面！Fun Camera模型实战解析轻松掌握运镜_1921554498571943938.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（46 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoTeaCache`
- `Reroute`
- `ImageConcatMulti`
- `SetNode`
- `WanVideoImageToVideoEncode`
- `PreviewImage`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `WanVideoExperimentalArgs`
- `LoadImage`
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `SetNode`
- `CameraPoseVisualizer`
- `PreviewImage`
- `WanVideoFunCameraEmbeds`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoTorchCompileSettings`
- `VHS_VideoCombine`
- `ADE_CameraPoseBasic`
- `ADE_CameraPoseBasic`
- `VHS_VideoCombine`
- `Note`
- `INTConstant`
- `VHS_VideoCombine`
- `ADE_CameraPoseBasic`
- `MarkdownNote`

## 知识

覆盖率 **78%**（36/46）

**有卡**：`WanVideoDecode`、`WanVideoTeaCache`、`ImageConcatMulti`、`WanVideoImageToVideoEncode`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`WanVideoExperimentalArgs`、`LoadImage`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`CameraPoseVisualizer`、`WanVideoFunCameraEmbeds`、`VHS_VideoCombine`、`WanVideoTorchCompileSettings`、`ADE_CameraPoseBasic`、`INTConstant`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncode、WanVideoVAELoader、ImageResizeKJv2
