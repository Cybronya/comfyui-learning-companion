---
key: 视频生成/文生视频/Wan2.2Stand-in视频面部交换实战_2004807686212513794.json
name: Wan2.2Stand-in视频面部交换实战_2004807686212513794
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/Wan2.2Stand-in视频面部交换实战_2004807686212513794.json
hash: dc61f3f1e822ec84
coverage: 0.914286
learned_at: 2026-10-11 02:57:38
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoBlockSwap, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoModelLoader, WanVideoTextEncode, WanVideoEncode, WanVideoAddStandInLatent, PreviewImage, WanVideoLoraSelect, INTConstant, FaceProcessorLoader, ApplyFaceProcessor, GetImageSize+, WanVideoEmptyEmbeds, WanVideoSampler, WanVideoVAELoader, WanVideoEncode, WanVideoDecode, ImageConcatMulti, FaceProcessorLoader, WanVideoLoraSelect, WanVideoLoraSelect, GetImageSizeAndCount, VideoInputPreprocessor, LoadImage, LoadWanVideoT5TextEncoder, ApplyFaceProcessor, FaceOnlyModeSwitch, PreviewImage, VHS_VideoCombine, VHS_VideoCombine, VHS_LoadVideo]
patterns: []
missing: [GetImageSize+]
discoveries: [次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/Wan2.2Stand-in视频面部交换实战_2004807686212513794.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/Wan2.2Stand-in视频面部交换实战_2004807686212513794.json`

## 结构

**生成流程**：Model → Sampling → Process → Output → Other

**节点**（35 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `WanVideoEncode`
- `WanVideoAddStandInLatent`
- `PreviewImage`
- `WanVideoLoraSelect`
- `INTConstant`
- `FaceProcessorLoader`
- `ApplyFaceProcessor`
- `GetImageSize+`
- `WanVideoEmptyEmbeds`
- `WanVideoSampler` ★核心
- `WanVideoVAELoader`
- `WanVideoEncode`
- `WanVideoDecode`
- `ImageConcatMulti`
- `FaceProcessorLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `GetImageSizeAndCount`
- `VideoInputPreprocessor`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `ApplyFaceProcessor`
- `FaceOnlyModeSwitch`
- `PreviewImage`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `VHS_LoadVideo`

## 知识

覆盖率 **91%**（32/35）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoTextEncode`、`WanVideoEncode`、`WanVideoAddStandInLatent`、`WanVideoLoraSelect`、`INTConstant`、`FaceProcessorLoader`、`ApplyFaceProcessor`、`WanVideoEmptyEmbeds`、`WanVideoVAELoader`、`WanVideoDecode`、`ImageConcatMulti`、`GetImageSizeAndCount`、`VideoInputPreprocessor`、`LoadImage`、`LoadWanVideoT5TextEncoder`、`FaceOnlyModeSwitch`、`VHS_VideoCombine`、`VHS_LoadVideo`

**缺卡**（1）：`GetImageSize+`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoAddStandInLatent

## 学习发现

- 次要节点 `GetImageSize+` 仅有 Resolution 的通用知识，没有该节点自己的说明
