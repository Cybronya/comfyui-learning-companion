---
key: 视频生成/图生视频/Wan2.1 AI视频 首尾帧 丝滑动画过渡 工作流_1985915775540178945.json
name: Wan2.1 AI视频 首尾帧 丝滑动画过渡 工作流_1985915775540178945.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1 AI视频 首尾帧 丝滑动画过渡 工作流_1985915775540178945.json
hash: 92b61b9d88c1fc30
coverage: 0.847826
learned_at: 2026-10-15 22:32:53
nodes: [Note, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTorchCompileSettings, easy cleanGpuUsed, WanVideoDecode, easy cleanGpuUsed, WanVideoTeaCache, WanVideoBlockSwap, ImageConcanate, LayerUtility: PurgeVRAM, WanVideoClipVisionEncode, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, Note, CR Simple Image Compare, easy cleanGpuUsed, VHS_VideoCombine, WanVideoSLG, ImageBatchRepeatInterleaving, PrimitiveNode, Note, Note, easy imageSize, easy imageSize, WanVideoImageToVideoEncode, easy cleanGpuUsed, Int, easy imageConcat, WanVideoTextEncode, WanVideoSampler, easy imageSize, EmptyImage, LoadWanVideoT5TextEncoder, WanVideoEnhanceAVideo, WanVideoModelLoader, LoadWanVideoClipTextEncoder, WanVideoVAELoader, LayerUtility: ImageScaleByAspectRatio V2, CR Text, VHS_VideoCombine, VHS_VideoCombine, LoadImage, LoadImage, CR Text]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 AI视频 首尾帧 丝滑动画过渡 工作流_1985915775540178945.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1985915775540178945.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（46 个）：
- `Note`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTorchCompileSettings`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `WanVideoTeaCache`
- `WanVideoBlockSwap`
- `ImageConcanate`
- `LayerUtility: PurgeVRAM`
- `WanVideoClipVisionEncode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Note`
- `CR Simple Image Compare`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `WanVideoSLG`
- `ImageBatchRepeatInterleaving`
- `PrimitiveNode`
- `Note`
- `Note`
- `easy imageSize`
- `easy imageSize`
- `WanVideoImageToVideoEncode`
- `easy cleanGpuUsed`
- `Int`
- `easy imageConcat`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `easy imageSize`
- `EmptyImage`
- `LoadWanVideoT5TextEncoder`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `CR Text`

## 知识

覆盖率 **85%**（39/46）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTorchCompileSettings`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`ImageConcanate`、`LayerUtility: PurgeVRAM`、`WanVideoClipVisionEncode`、`CR Simple Image Compare`、`VHS_VideoCombine`、`WanVideoSLG`、`ImageBatchRepeatInterleaving`、`easy imageSize`、`WanVideoImageToVideoEncode`、`Int`、`easy imageConcat`、`WanVideoTextEncode`、`WanVideoSampler`、`EmptyImage`、`LoadWanVideoT5TextEncoder`、`WanVideoEnhanceAVideo`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`CR Text`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
