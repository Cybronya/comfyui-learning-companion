---
key: 视频生成/图生视频/Wan2.1 Control Camera 运镜_1948615689729912833.json
name: Wan2.1 Control Camera 运镜_1948615689729912833.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 Control Camera 运镜_1948615689729912833.json
hash: f6aa0bab87d6b72c
coverage: 0.678571
learned_at: 2026-10-15 22:30:47
nodes: [GetNode, GetNode, GetNode, WanVideoImageToVideoEncode, ImageConcatMulti, ImageResizeKJv2, SetNode, LoadImage, MarkdownNote, Note, WanVideoModelLoader, LoadWanVideoT5TextEncoder, SetNode, WanVideoVAELoader, INTConstant, ADE_CameraPoseBasic, WanVideoFunCameraEmbeds, CameraPoseVisualizer, WanVideoExperimentalArgs, WanVideoTeaCache, Reroute, PreviewImage, WanVideoSampler, WanVideoDecode, Note Plus (mtb), LoadImageFromUrl, WanVideoTextEncode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 Control Camera 运镜_1948615689729912833.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1948615689729912833.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（28 个）：
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `SetNode`
- `LoadImage`
- `MarkdownNote`
- `Note`
- `WanVideoModelLoader`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `WanVideoVAELoader`
- `INTConstant`
- `ADE_CameraPoseBasic`
- `WanVideoFunCameraEmbeds`
- `CameraPoseVisualizer`
- `WanVideoExperimentalArgs`
- `WanVideoTeaCache`
- `Reroute`
- `PreviewImage`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `Note Plus (mtb)`
- `LoadImageFromUrl`
- `WanVideoTextEncode`
- `VHS_VideoCombine`

## 知识

覆盖率 **68%**（19/28）

**有卡**：`WanVideoImageToVideoEncode`、`ImageConcatMulti`、`ImageResizeKJv2`、`LoadImage`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`INTConstant`、`ADE_CameraPoseBasic`、`WanVideoFunCameraEmbeds`、`CameraPoseVisualizer`、`WanVideoExperimentalArgs`、`WanVideoTeaCache`、`WanVideoSampler`、`WanVideoDecode`、`Note Plus (mtb)`、`LoadImageFromUrl`、`WanVideoTextEncode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode、ImageResizeKJv2
