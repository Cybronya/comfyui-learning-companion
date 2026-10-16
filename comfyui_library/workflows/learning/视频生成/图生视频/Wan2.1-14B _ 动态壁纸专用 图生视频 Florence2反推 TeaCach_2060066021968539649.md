---
key: 视频生成/图生视频/Wan2.1-14B _ 动态壁纸专用 图生视频 Florence2反推 TeaCach_2060066021968539649.json
name: Wan2.1-14B _ 动态壁纸专用 图生视频 Florence2反推 TeaCach_2060066021968539649.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2060066021968539649.json
hash: e276ab4a173b64e7
coverage: 0.717391
learned_at: 2026-10-15 22:38:45
nodes: [LoadWanVideoT5TextEncoder, SetNode, WanVideoSetBlockSwap, SetNode, WanVideoTorchCompileSettings, easy cleanGpuUsed, WanVideoVAELoader, WanVideoImageClipEncode, LoadWanVideoClipTextEncoder, GetNode, Florence2Run, DownloadAndLoadFlorence2Model, StringFunction|pysssss, GetNode, WanVideoLoraSelect, WanVideoTextEncode, GetNode, GetNode, WanVideoSampler, WanVideoDecode, SetNode, WanVideoSLG, WanVideoTeaCache, CogVideoEnhanceAVideo, GetNode, WanVideoBlockSwap, WanVideoModelLoader, LayerUtility: ImageScaleByAspectRatio V2, WanVideoBlockSwap, GetNode, SetNode, SetNode, LoadImage, VHS_VideoCombine, MathExpression|pysssss, TextInput_, TextInput_, Int, easy cleanGpuUsed, SetNode, CLIPTextEncode, Text, CLIPTextEncode, SetNode, CheckpointLoaderSimple, CLIPTextEncode]
patterns: []
missing: []
parameters: {"checkpoint": "Lock_8.32.safetensors"}
---

# 视频生成/图生视频/Wan2.1-14B _ 动态壁纸专用 图生视频 Florence2反推 TeaCach_2060066021968539649.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2060066021968539649.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（46 个）：
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoTorchCompileSettings`
- `easy cleanGpuUsed`
- `WanVideoVAELoader`
- `WanVideoImageClipEncode`
- `LoadWanVideoClipTextEncoder` ★核心
- `GetNode`
- `Florence2Run`
- `DownloadAndLoadFlorence2Model`
- `StringFunction|pysssss`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `SetNode`
- `WanVideoSLG`
- `WanVideoTeaCache`
- `CogVideoEnhanceAVideo`
- `GetNode`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoBlockSwap`
- `GetNode`
- `SetNode`
- `SetNode`
- `LoadImage`
- `VHS_VideoCombine`
- `MathExpression|pysssss`
- `TextInput_`
- `TextInput_`
- `Int`
- `easy cleanGpuUsed`
- `SetNode`
- `CLIPTextEncode` ★核心
- `Text`
- `CLIPTextEncode` ★核心
- `SetNode`
- `CheckpointLoaderSimple` ★核心
- `CLIPTextEncode` ★核心

## 关键参数

- `checkpoint` = `Lock_8.32.safetensors`

## 知识

覆盖率 **72%**（33/46）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`easy cleanGpuUsed`、`WanVideoVAELoader`、`WanVideoImageClipEncode`、`LoadWanVideoClipTextEncoder`、`Florence2Run`、`DownloadAndLoadFlorence2Model`、`StringFunction|pysssss`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoSLG`、`WanVideoTeaCache`、`CogVideoEnhanceAVideo`、`WanVideoBlockSwap`、`WanVideoModelLoader`、`LayerUtility: ImageScaleByAspectRatio V2`、`LoadImage`、`VHS_VideoCombine`、`MathExpression|pysssss`、`TextInput_`、`Int`、`CLIPTextEncode`、`Text`、`CheckpointLoaderSimple`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、LoadImage、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoImageClipEncode
