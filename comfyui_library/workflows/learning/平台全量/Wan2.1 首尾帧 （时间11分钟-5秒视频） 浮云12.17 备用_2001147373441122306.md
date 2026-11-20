---
key: 平台全量/Wan2.1 首尾帧 （时间11分钟-5秒视频） 浮云12.17 备用_2001147373441122306.json
name: Wan2.1 首尾帧 （时间11分钟-5秒视频） 浮云12.17 备用_2001147373441122306
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/Wan2.1 首尾帧 （时间11分钟-5秒视频） 浮云12.17 备用_2001147373441122306.json
hash: 95d939c8de6369c3
coverage: 0.847826
learned_at: 2026-11-14 01:04:32
nodes: [Note, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTorchCompileSettings, easy cleanGpuUsed, WanVideoDecode, easy cleanGpuUsed, WanVideoTeaCache, WanVideoBlockSwap, ImageConcanate, LayerUtility: PurgeVRAM, WanVideoClipVisionEncode, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, Note, CR Simple Image Compare, easy cleanGpuUsed, VHS_VideoCombine, WanVideoSLG, ImageBatchRepeatInterleaving, Note, Note, easy imageSize, easy imageSize, WanVideoImageToVideoEncode, easy cleanGpuUsed, Int, easy imageConcat, WanVideoTextEncode, WanVideoSampler, easy imageSize, LoadWanVideoT5TextEncoder, WanVideoEnhanceAVideo, WanVideoModelLoader, LoadWanVideoClipTextEncoder, WanVideoVAELoader, LayerUtility: ImageScaleByAspectRatio V2, CR Text, VHS_VideoCombine, LoadImage, LoadImage, PrimitiveNode, VHS_VideoCombine, CR Text, EmptyImage]
patterns: []
missing: []
---

# 平台全量/Wan2.1 首尾帧 （时间11分钟-5秒视频） 浮云12.17 备用_2001147373441122306.json

> 来源文件 `comfyui_library/workflows/平台全量/Wan2.1 首尾帧 （时间11分钟-5秒视频） 浮云12.17 备用_2001147373441122306.json`

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
- `LoadWanVideoT5TextEncoder`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `PrimitiveNode`
- `VHS_VideoCombine`
- `CR Text`
- `EmptyImage`

## 知识

覆盖率 **85%**（39/46）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTorchCompileSettings`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`ImageConcanate`、`LayerUtility: PurgeVRAM`、`WanVideoClipVisionEncode`、`CR Simple Image Compare`、`VHS_VideoCombine`、`WanVideoSLG`、`ImageBatchRepeatInterleaving`、`easy imageSize`、`WanVideoImageToVideoEncode`、`Int`、`easy imageConcat`、`WanVideoTextEncode`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoEnhanceAVideo`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`CR Text`、`LoadImage`、`EmptyImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoImageToVideoEncode、WanVideoTextEncode
