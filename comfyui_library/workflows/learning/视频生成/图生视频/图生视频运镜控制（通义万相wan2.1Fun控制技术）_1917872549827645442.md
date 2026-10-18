---
key: 视频生成/图生视频/图生视频运镜控制（通义万相wan2.1Fun控制技术）_1917872549827645442.json
name: 图生视频运镜控制（通义万相wan2.1Fun控制技术）_1917872549827645442.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/图生视频运镜控制（通义万相wan2.1Fun控制技术）_1917872549827645442.json
hash: 022c72e651112d45
coverage: 0.727273
learned_at: 2026-10-15 22:29:40
nodes: [SetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoTextEncode, Primitive integer [Crystools], Primitive integer [Crystools], SetNode, GetNode, WanVideoImageToVideoEncode, Reroute, WanVideoTeaCache, GetNode, WanVideoDecode, GetNode, ImageConcatMulti, WanVideoExperimentalArgs, WanVideoFunCameraEmbeds, VHS_VideoCombine, INTConstant, WanVideoSampler, LoadImage, ADE_CameraPoseBasic, ADE_CameraPoseBasic, WanVideoBlockSwap, WanVideoModelLoader, WanVideoTorchCompileSettings, MarkdownNote, PreviewImage, CameraPoseVisualizer, Note, ImageResizeKJ, Text Multiline, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/图生视频运镜控制（通义万相wan2.1Fun控制技术）_1917872549827645442.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1917872549827645442.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（33 个）：
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
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
- `WanVideoExperimentalArgs`
- `WanVideoFunCameraEmbeds`
- `VHS_VideoCombine`
- `INTConstant`
- `WanVideoSampler` ★核心
- `LoadImage`
- `ADE_CameraPoseBasic`
- `ADE_CameraPoseBasic`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoTorchCompileSettings`
- `MarkdownNote`
- `PreviewImage`
- `CameraPoseVisualizer`
- `Note`
- `ImageResizeKJ`
- `Text Multiline`
- `VHS_VideoCombine`

## 知识

覆盖率 **73%**（24/33）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`Primitive integer [Crystools]`、`WanVideoImageToVideoEncode`、`WanVideoTeaCache`、`WanVideoDecode`、`ImageConcatMulti`、`WanVideoExperimentalArgs`、`WanVideoFunCameraEmbeds`、`VHS_VideoCombine`、`INTConstant`、`WanVideoSampler`、`LoadImage`、`ADE_CameraPoseBasic`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`WanVideoTorchCompileSettings`、`CameraPoseVisualizer`、`ImageResizeKJ`、`Text Multiline`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、ImageResizeKJ
