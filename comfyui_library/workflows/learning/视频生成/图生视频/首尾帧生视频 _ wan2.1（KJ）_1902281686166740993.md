---
key: 视频生成/图生视频/首尾帧生视频 _ wan2.1（KJ）_1902281686166740993.json
name: 首尾帧生视频 _ wan2.1（KJ）_1902281686166740993.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧生视频 _ wan2.1（KJ）_1902281686166740993.json
hash: a3722d2587cbbc2e
coverage: 0.796875
learned_at: 2026-10-15 22:29:24
nodes: [easy imageSize, Reroute, Reroute, CR Simple Image Compare, Reroute, LoadImage, LoadImage, easy textSwitch, MathExpression|pysssss, MathExpression|pysssss, easy imageSize, easy imageSize, Reroute, Reroute, Reroute, WanVideoTorchCompileSettings, WanVideoDecode, LayerUtility: PurgeVRAM, Int, easy cleanGpuUsed, ImageBatchRepeatInterleaving, LayerUtility: ImageScaleByAspectRatio V2, ImageConcanate, LayerUtility: PurgeVRAM, easy cleanGpuUsed, VHS_VideoCombine, VHS_VideoCombine, VHS_VideoCombine, WanVideoVAELoader, WanVideoBlockSwap, WanVideoEnhanceAVideo, Int, WanVideoSampler, LoadWanVideoT5TextEncoder, easy cleanGpuUsed, TextBox, WanVideoTextEncode, easy cleanGpuUsed, Reroute, EmptyImage, WanVideoModelLoader, WanVideoVRAMManagement, WanVideoFlowEdit, WanVideoExperimentalArgs, WanVideoLoopArgs, easy cleanGpuUsed, WanVideoClipVisionEncode, WanVideoTeaCache, WanVideoSLG, LoadWanVideoClipTextEncoder, easy imageSize, Reroute, Reroute, Reroute, WanVideoImageToVideoEncode, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: ImageScaleByAspectRatio V2, Reroute, Reroute, easy imageConcat, LayerUtility: PurgeVRAM, Textbox, RH_Captioner, ShowText|pysssss]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧生视频 _ wan2.1（KJ）_1902281686166740993.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1902281686166740993.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（64 个）：
- `easy imageSize`
- `Reroute`
- `Reroute`
- `CR Simple Image Compare`
- `Reroute`
- `LoadImage`
- `LoadImage`
- `easy textSwitch`
- `MathExpression|pysssss`
- `MathExpression|pysssss`
- `easy imageSize`
- `easy imageSize`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoTorchCompileSettings`
- `WanVideoDecode`
- `LayerUtility: PurgeVRAM`
- `Int`
- `easy cleanGpuUsed`
- `ImageBatchRepeatInterleaving`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `ImageConcanate`
- `LayerUtility: PurgeVRAM`
- `easy cleanGpuUsed`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoEnhanceAVideo`
- `Int`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `easy cleanGpuUsed`
- `TextBox`
- `WanVideoTextEncode`
- `easy cleanGpuUsed`
- `Reroute`
- `EmptyImage`
- `WanVideoModelLoader`
- `WanVideoVRAMManagement`
- `WanVideoFlowEdit`
- `WanVideoExperimentalArgs`
- `WanVideoLoopArgs`
- `easy cleanGpuUsed`
- `WanVideoClipVisionEncode`
- `WanVideoTeaCache`
- `WanVideoSLG`
- `LoadWanVideoClipTextEncoder` ★核心
- `easy imageSize`
- `Reroute`
- `Reroute`
- `Reroute`
- `WanVideoImageToVideoEncode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `Reroute`
- `Reroute`
- `easy imageConcat`
- `LayerUtility: PurgeVRAM`
- `Textbox`
- `RH_Captioner`
- `ShowText|pysssss`

## 知识

覆盖率 **80%**（51/64）

**有卡**：`easy imageSize`、`CR Simple Image Compare`、`LoadImage`、`easy textSwitch`、`MathExpression|pysssss`、`WanVideoTorchCompileSettings`、`WanVideoDecode`、`LayerUtility: PurgeVRAM`、`Int`、`easy cleanGpuUsed`、`ImageBatchRepeatInterleaving`、`LayerUtility: ImageScaleByAspectRatio V2`、`ImageConcanate`、`VHS_VideoCombine`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoEnhanceAVideo`、`WanVideoSampler`、`LoadWanVideoT5TextEncoder`、`TextBox`、`WanVideoTextEncode`、`EmptyImage`、`WanVideoModelLoader`、`WanVideoVRAMManagement`、`WanVideoFlowEdit`、`WanVideoExperimentalArgs`、`WanVideoLoopArgs`、`WanVideoClipVisionEncode`、`WanVideoTeaCache`、`WanVideoSLG`、`LoadWanVideoClipTextEncoder`、`WanVideoImageToVideoEncode`、`easy imageConcat`、`Textbox`、`RH_Captioner`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
