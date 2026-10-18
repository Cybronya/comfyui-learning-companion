---
key: 视频生成/图生视频/WAN2.1 万相阿里Fun图生视频运镜控制_1918948189318086658.json
name: WAN2.1 万相阿里Fun图生视频运镜控制_1918948189318086658.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.1 万相阿里Fun图生视频运镜控制_1918948189318086658.json
hash: d46677af2963038f
coverage: 0.727273
learned_at: 2026-10-15 22:29:41
nodes: [MarkdownNote, SetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoTextEncode, Primitive integer [Crystools], Primitive integer [Crystools], SetNode, GetNode, WanVideoImageToVideoEncode, Reroute, WanVideoTeaCache, GetNode, WanVideoDecode, GetNode, ImageConcatMulti, PreviewImage, ImageResizeKJ, WanVideoModelLoader, WanVideoExperimentalArgs, CameraPoseVisualizer, WanVideoFunCameraEmbeds, INTConstant, Text Multiline, ADE_CameraPoseBasic, LoadImage, Note, ADE_CameraPoseBasic, WanVideoSampler, VHS_VideoCombine, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.1 万相阿里Fun图生视频运镜控制_1918948189318086658.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1918948189318086658.json`

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
- `PreviewImage`
- `ImageResizeKJ`
- `WanVideoModelLoader`
- `WanVideoExperimentalArgs`
- `CameraPoseVisualizer`
- `WanVideoFunCameraEmbeds`
- `INTConstant`
- `Text Multiline`
- `ADE_CameraPoseBasic`
- `LoadImage`
- `Note`
- `ADE_CameraPoseBasic`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `VHS_VideoCombine`

## 知识

覆盖率 **73%**（24/33）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`Primitive integer [Crystools]`、`WanVideoImageToVideoEncode`、`WanVideoTeaCache`、`WanVideoDecode`、`ImageConcatMulti`、`ImageResizeKJ`、`WanVideoModelLoader`、`WanVideoExperimentalArgs`、`CameraPoseVisualizer`、`WanVideoFunCameraEmbeds`、`INTConstant`、`Text Multiline`、`ADE_CameraPoseBasic`、`LoadImage`、`WanVideoSampler`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、ImageResizeKJ
