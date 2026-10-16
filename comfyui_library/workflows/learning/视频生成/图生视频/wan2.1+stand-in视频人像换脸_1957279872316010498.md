---
key: 视频生成/图生视频/wan2.1+stand-in视频人像换脸_1957279872316010498.json
name: wan2.1+stand-in视频人像换脸_1957279872316010498.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1957279872316010498.json
hash: afed7195372bcf5e
coverage: 0.574468
learned_at: 2026-10-15 22:31:16
nodes: [WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, SetNode, WanVideoSetLoRAs, SetNode, LoadWanVideoT5TextEncoder, SetNode, WanVideoVAELoader, SetNode, WanVideoSampler, GetNode, GetNode, GetNode, GetNode, WanVideoDecode, WanVideoLoraSelect, SetNode, INTConstant, SetNode, SetNode, VHS_VideoCombine, GetNode, ImageResizeKJv2, GetNode, GetNode, GetNode, WanVideoEncode, SetNode, WanVideoAddStandInLatent, GetNode, WanVideoVACEEncode, SetNode, WanVideoModelLoader, WanVideoBlockSwap, AIO_Preprocessor, VHS_LoadVideo, INTConstant, INTConstant, WanVideoTextEncode, VHS_VideoCombine, FaceProcessorLoader, ApplyFaceProcessor, PreviewImage, GetNode, WanVideoVACEModelSelect, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.1+stand-in视频人像换脸_1957279872316010498.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1957279872316010498.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（47 个）：
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `SetNode`
- `WanVideoSetLoRAs`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `SetNode`
- `WanVideoVAELoader`
- `SetNode`
- `WanVideoSampler` ★核心
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `SetNode`
- `INTConstant`
- `SetNode`
- `SetNode`
- `VHS_VideoCombine`
- `GetNode`
- `ImageResizeKJv2`
- `GetNode`
- `GetNode`
- `GetNode`
- `WanVideoEncode`
- `SetNode`
- `WanVideoAddStandInLatent`
- `GetNode`
- `WanVideoVACEEncode`
- `SetNode`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `AIO_Preprocessor`
- `VHS_LoadVideo`
- `INTConstant`
- `INTConstant`
- `WanVideoTextEncode`
- `VHS_VideoCombine`
- `FaceProcessorLoader`
- `ApplyFaceProcessor`
- `PreviewImage`
- `GetNode`
- `WanVideoVACEModelSelect`
- `LoadImage`

## 知识

覆盖率 **57%**（27/47）

**有卡**：`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSampler`、`WanVideoDecode`、`INTConstant`、`VHS_VideoCombine`、`ImageResizeKJv2`、`WanVideoEncode`、`WanVideoAddStandInLatent`、`WanVideoVACEEncode`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`AIO_Preprocessor`、`VHS_LoadVideo`、`WanVideoTextEncode`、`FaceProcessorLoader`、`ApplyFaceProcessor`、`WanVideoVACEModelSelect`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoVACEEncode、WanVideoAddStandInLatent
