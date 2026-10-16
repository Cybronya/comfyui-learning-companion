---
key: 视频生成/文生视频/最新阿里Wan2.1图生视频运镜控制_1929007015320829954.json
name: 最新阿里Wan2.1图生视频运镜控制_1929007015320829954.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1929007015320829954.json
hash: 45f32c50dc8acb61
coverage: 0.956522
learned_at: 2026-10-15 22:43:25
nodes: [LoadImage, INTConstant, CameraPoseVisualizer, PreviewImage, ADE_CameraPoseBasic, ADE_CameraPoseBasic, WanVideoTorchCompileSettings, WanVideoBlockSwap, Text Multiline, WanVideoSampler, WanVideoExperimentalArgs, WanVideoTeaCache, WanVideoFunCameraEmbeds, WanVideoImageToVideoEncode, WanVideoVAELoader, ImageConcatMulti, ImageResizeKJ, WanVideoDecode, WanVideoModelLoader, WanVideoTextEncode, LoadWanVideoT5TextEncoder, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/文生视频/最新阿里Wan2.1图生视频运镜控制_1929007015320829954.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1929007015320829954.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（23 个）：
- `LoadImage`
- `INTConstant`
- `CameraPoseVisualizer`
- `PreviewImage`
- `ADE_CameraPoseBasic`
- `ADE_CameraPoseBasic`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `Text Multiline`
- `WanVideoSampler` ★核心
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `WanVideoFunCameraEmbeds`
- `WanVideoImageToVideoEncode`
- `WanVideoVAELoader`
- `ImageConcatMulti`
- `ImageResizeKJ`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **96%**（22/23）

**有卡**：`LoadImage`、`INTConstant`、`CameraPoseVisualizer`、`ADE_CameraPoseBasic`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`Text Multiline`、`WanVideoSampler`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoFunCameraEmbeds`、`WanVideoImageToVideoEncode`、`WanVideoVAELoader`、`ImageConcatMulti`、`ImageResizeKJ`、`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoTextEncode`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、ImageResizeKJ
