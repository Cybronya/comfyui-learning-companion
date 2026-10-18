---
key: 视频生成/图生视频/Wan2.1+AI视频首尾帧丝滑动画过渡工作流【AI小王子】_1994010084806164482.json
name: Wan2.1+AI视频首尾帧丝滑动画过渡工作流【AI小王子】_1994010084806164482.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.1+AI视频首尾帧丝滑动画过渡工作流【AI小王子】_1994010084806164482.json
hash: 68a33bc0bdb634ff
coverage: 0.847826
learned_at: 2026-10-15 22:33:20
nodes: [Note, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTorchCompileSettings, easy cleanGpuUsed, WanVideoDecode, easy cleanGpuUsed, WanVideoTeaCache, WanVideoBlockSwap, ImageConcanate, LayerUtility: PurgeVRAM, WanVideoClipVisionEncode, LayerUtility: PurgeVRAM, LayerUtility: ImageScaleByAspectRatio V2, Note, CR Simple Image Compare, easy cleanGpuUsed, VHS_VideoCombine, WanVideoSLG, ImageBatchRepeatInterleaving, PrimitiveNode, Note, Note, easy imageSize, easy imageSize, WanVideoImageToVideoEncode, easy cleanGpuUsed, Int, easy imageConcat, WanVideoTextEncode, WanVideoSampler, easy imageSize, EmptyImage, CR Text, LoadWanVideoT5TextEncoder, WanVideoEnhanceAVideo, WanVideoModelLoader, LoadWanVideoClipTextEncoder, WanVideoVAELoader, LayerUtility: ImageScaleByAspectRatio V2, CR Text, VHS_VideoCombine, VHS_VideoCombine, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1+AI视频首尾帧丝滑动画过渡工作流【AI小王子】_1994010084806164482.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1994010084806164482.json`

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
- `CR Text`
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

## 知识

覆盖率 **85%**（39/46）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTorchCompileSettings`、`easy cleanGpuUsed`、`WanVideoDecode`、`WanVideoTeaCache`、`WanVideoBlockSwap`、`ImageConcanate`、`LayerUtility: PurgeVRAM`、`WanVideoClipVisionEncode`、`CR Simple Image Compare`、`VHS_VideoCombine`、`WanVideoSLG`、`ImageBatchRepeatInterleaving`、`easy imageSize`、`WanVideoImageToVideoEncode`、`Int`、`easy imageConcat`、`WanVideoTextEncode`、`WanVideoSampler`、`EmptyImage`、`CR Text`、`LoadWanVideoT5TextEncoder`、`WanVideoEnhanceAVideo`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
