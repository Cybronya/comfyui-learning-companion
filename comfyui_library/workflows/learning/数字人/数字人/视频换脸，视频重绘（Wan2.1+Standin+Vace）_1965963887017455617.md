---
key: 数字人/数字人/视频换脸，视频重绘（Wan2.1+Standin+Vace）_1965963887017455617.json
name: 视频换脸，视频重绘（Wan2.1+Standin+Vace）_1965963887017455617
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/数字人/数字人/视频换脸，视频重绘（Wan2.1+Standin+Vace）_1965963887017455617.json
hash: a9fcb365367cc53d
coverage: 0.780488
learned_at: 2026-10-26 02:05:16
nodes: [GetNode, GetNode, WanVideoTorchCompileSettings, LoadWanVideoT5TextEncoder, WanVideoModelLoader, WanVideoVAELoader, AIO_Preprocessor, SetNode, FaceProcessorLoader, PreviewImage, ApplyFaceProcessor, WanVideoSetBlockSwap, WanVideoEncode, WanVideoVACEEncode, GetNode, SetNode, LoadImage, INTConstant, Anything Everywhere, WanVideoLoraSelect, WanVideoSetLoRAs, WanVideoDecode, WanVideoSampler, INTConstant, SimpleMath+, SetNode, VHS_LoadVideo, WanVideoTextEncode, VHS_VideoCombine, WanVideoAddStandInLatent, easy cleanGpuUsed, PreviewAny, WanVideoLoraSelect, WanVideoVACEModelSelect, ImageResizeKJv2, WanVideoBlockSwap, Text, INTConstant, VHS_VideoCombine, Int, CM_IntToFloat]
patterns: []
missing: []
---

# 数字人/数字人/视频换脸，视频重绘（Wan2.1+Standin+Vace）_1965963887017455617.json

> 来源文件 `comfyui_library/workflows/数字人/数字人/视频换脸，视频重绘（Wan2.1+Standin+Vace）_1965963887017455617.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（41 个）：
- `GetNode`
- `GetNode`
- `WanVideoTorchCompileSettings`
- `LoadWanVideoT5TextEncoder`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `AIO_Preprocessor`
- `SetNode`
- `FaceProcessorLoader`
- `PreviewImage`
- `ApplyFaceProcessor`
- `WanVideoSetBlockSwap`
- `WanVideoEncode`
- `WanVideoVACEEncode`
- `GetNode`
- `SetNode`
- `LoadImage`
- `INTConstant`
- `Anything Everywhere`
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `INTConstant`
- `SimpleMath+`
- `SetNode`
- `VHS_LoadVideo`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `WanVideoAddStandInLatent`
- `easy cleanGpuUsed`
- `PreviewAny`
- `WanVideoLoraSelect`
- `WanVideoVACEModelSelect`
- `ImageResizeKJv2`
- `WanVideoBlockSwap`
- `Text`
- `INTConstant`
- `VHS_VideoCombine`
- `Int`
- `CM_IntToFloat`

## 知识

覆盖率 **78%**（32/41）

**有卡**：`WanVideoTorchCompileSettings`、`LoadWanVideoT5TextEncoder`、`WanVideoModelLoader`、`WanVideoVAELoader`、`AIO_Preprocessor`、`FaceProcessorLoader`、`ApplyFaceProcessor`、`WanVideoSetBlockSwap`、`WanVideoEncode`、`WanVideoVACEEncode`、`LoadImage`、`INTConstant`、`WanVideoLoraSelect`、`WanVideoSetLoRAs`、`WanVideoDecode`、`WanVideoSampler`、`SimpleMath+`、`VHS_LoadVideo`、`WanVideoTextEncode`、`VHS_VideoCombine`、`WanVideoAddStandInLatent`、`easy cleanGpuUsed`、`WanVideoVACEModelSelect`、`ImageResizeKJv2`、`WanVideoBlockSwap`、`Text`、`Int`、`CM_IntToFloat`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoAddStandInLatent
