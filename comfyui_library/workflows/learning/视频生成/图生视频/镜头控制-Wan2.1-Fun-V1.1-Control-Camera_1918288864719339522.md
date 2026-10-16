---
key: 视频生成/图生视频/镜头控制-Wan2.1-Fun-V1.1-Control-Camera_1918288864719339522.json
name: 镜头控制-Wan2.1-Fun-V1.1-Control-Camera_1918288864719339522.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1918288864719339522.json
hash: 839a23b6a1e565e2
coverage: 0.962264
learned_at: 2026-10-15 22:29:40
nodes: [LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoTextEncode, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoSampler, WanVideoExperimentalArgs, INTConstant, WanVideoFunCameraEmbeds, CameraPoseVisualizer, PreviewImage, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoTeaCache, ImageResizeKJ, Florence2ModelLoader, Florence2Run, LayerUtility: PurgeVRAM V2, LoadImage, ADE_CameraPoseBasic, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoTextEncode, WanVideoEnhanceAVideo, WanVideoSLG, WanVideoSampler, WanVideoExperimentalArgs, ImageConcatMulti, WanVideoFunCameraEmbeds, CameraPoseVisualizer, PreviewImage, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoTeaCache, ImageResizeKJ, Florence2ModelLoader, Florence2Run, LayerUtility: PurgeVRAM V2, INTConstant, ADE_CameraPoseBasic, ADE_CameraPoseBasic, LoadImage, VHS_VideoCombine, ImageConcatMulti, WanVideoDecode, VHS_VideoCombine, VHS_VideoCombine, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/镜头控制-Wan2.1-Fun-V1.1-Control-Camera_1918288864719339522.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1918288864719339522.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（53 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `INTConstant`
- `WanVideoFunCameraEmbeds`
- `CameraPoseVisualizer`
- `PreviewImage`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `WanVideoTeaCache`
- `ImageResizeKJ`
- `Florence2ModelLoader`
- `Florence2Run`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `ADE_CameraPoseBasic`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoTextEncode`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `ImageConcatMulti`
- `WanVideoFunCameraEmbeds`
- `CameraPoseVisualizer`
- `PreviewImage`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `WanVideoTeaCache`
- `ImageResizeKJ`
- `Florence2ModelLoader`
- `Florence2Run`
- `LayerUtility: PurgeVRAM V2`
- `INTConstant`
- `ADE_CameraPoseBasic`
- `ADE_CameraPoseBasic`
- `LoadImage`
- `VHS_VideoCombine`
- `ImageConcatMulti`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **96%**（51/53）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`INTConstant`、`WanVideoFunCameraEmbeds`、`CameraPoseVisualizer`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoTeaCache`、`ImageResizeKJ`、`Florence2ModelLoader`、`Florence2Run`、`LayerUtility: PurgeVRAM V2`、`LoadImage`、`ADE_CameraPoseBasic`、`ImageConcatMulti`、`VHS_VideoCombine`、`WanVideoDecode`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、ImageResizeKJ
