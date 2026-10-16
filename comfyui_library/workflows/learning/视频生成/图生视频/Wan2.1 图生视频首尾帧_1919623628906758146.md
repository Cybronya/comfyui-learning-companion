---
key: 视频生成/图生视频/Wan2.1 图生视频首尾帧_1919623628906758146.json
name: Wan2.1 图生视频首尾帧_1919623628906758146.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1919623628906758146.json
hash: 2f62e071e183c3cb
coverage: 0.825
learned_at: 2026-10-15 22:29:41
nodes: [Note, Note, Note, LayerUtility: ImageScaleByAspectRatio V2, WanVideoTorchCompileSettings, easy cleanGpuUsed, easy cleanGpuUsed, WanVideoBlockSwap, LayerUtility: PurgeVRAM, WanVideoClipVisionEncode, Note, easy imageSize, easy imageSize, Int, easy imageConcat, WanVideoTextEncode, WanVideoSampler, LoadWanVideoT5TextEncoder, WanVideoEnhanceAVideo, WanVideoModelLoader, LoadWanVideoClipTextEncoder, WanVideoVAELoader, LayerUtility: ImageScaleByAspectRatio V2, CR Text, LayerUtility: PurgeVRAM, WanVideoImageToVideoEncode, easy cleanGpuUsed, easy cleanGpuUsed, easy imageSize, EmptyImage, PrimitiveNode, LoadImage, LoadImage, CR Text, Note, Note, WanVideoSLG, WanVideoTeaCache, WanVideoDecode, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.1 图生视频首尾帧_1919623628906758146.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1919623628906758146.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（40 个）：
- `Note`
- `Note`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoTorchCompileSettings`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM`
- `WanVideoClipVisionEncode`
- `Note`
- `easy imageSize`
- `easy imageSize`
- `Int`
- `easy imageConcat`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoVAELoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `CR Text`
- `LayerUtility: PurgeVRAM`
- `WanVideoImageToVideoEncode`
- `easy cleanGpuUsed`
- `easy cleanGpuUsed`
- `easy imageSize`
- `EmptyImage`
- `PrimitiveNode`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `Note`
- `Note`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `WanVideoDecode`
- `VHS_VideoCombine`

## 知识

覆盖率 **82%**（33/40）

**有卡**：`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoTorchCompileSettings`、`easy cleanGpuUsed`、`WanVideoBlockSwap`、`LayerUtility: PurgeVRAM`、`WanVideoClipVisionEncode`、`easy imageSize`、`Int`、`easy imageConcat`、`WanVideoTextEncode`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`WanVideoEnhanceAVideo`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`WanVideoVAELoader`、`CR Text`、`WanVideoImageToVideoEncode`、`EmptyImage`、`LoadImage`、`WanVideoSLG`、`WanVideoTeaCache`、`WanVideoDecode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
