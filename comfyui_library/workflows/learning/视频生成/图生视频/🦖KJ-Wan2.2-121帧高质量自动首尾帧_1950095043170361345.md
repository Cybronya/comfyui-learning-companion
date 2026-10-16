---
key: 视频生成/图生视频/🦖KJ-Wan2.2-121帧高质量自动首尾帧_1950095043170361345.json
name: 🦖KJ-Wan2.2-121帧高质量自动首尾帧_1950095043170361345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950095043170361345.json
hash: 89cfe751f5bf7f4d
coverage: 0.973684
learned_at: 2026-10-15 22:30:52
nodes: [WanVideoDecode, WanVideoModelLoader, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTorchCompileSettings, WanVideoSampler, Primitive integer [Crystools], WanVideoTextEncode, ResizeLongestToNode, ACE_ImageGetSize, WanVideoSampler, Note, CreateCFGScheduleFloatList, WanVideoBlockSwap, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoImageToVideoEncode, ACE_ImageGetSize, ResizeLongestToNode, GetImageSizeAndCount, EmptyImage, ImageConcatMulti, AddLabel, AddLabel, ImageConcatMulti, ImageResizeKJv2, ImageResizeKJv2, LoadImage, LoadImage, RH_Translator, VHS_VideoCombine, VHS_VideoCombine, MathExpression|pysssss]
patterns: []
missing: []
---

# 视频生成/图生视频/🦖KJ-Wan2.2-121帧高质量自动首尾帧_1950095043170361345.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950095043170361345.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTorchCompileSettings`
- `WanVideoSampler` ★核心
- `Primitive integer [Crystools]`
- `WanVideoTextEncode`
- `ResizeLongestToNode`
- `ACE_ImageGetSize`
- `WanVideoSampler` ★核心
- `Note`
- `CreateCFGScheduleFloatList`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoImageToVideoEncode`
- `ACE_ImageGetSize`
- `ResizeLongestToNode`
- `GetImageSizeAndCount`
- `EmptyImage`
- `ImageConcatMulti`
- `AddLabel`
- `AddLabel`
- `ImageConcatMulti`
- `ImageResizeKJv2`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `RH_Translator`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `MathExpression|pysssss`

## 知识

覆盖率 **97%**（37/38）

**有卡**：`WanVideoDecode`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoSampler`、`Primitive integer [Crystools]`、`WanVideoTextEncode`、`ResizeLongestToNode`、`ACE_ImageGetSize`、`CreateCFGScheduleFloatList`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoImageToVideoEncode`、`GetImageSizeAndCount`、`EmptyImage`、`ImageConcatMulti`、`AddLabel`、`ImageResizeKJv2`、`LoadImage`、`RH_Translator`、`VHS_VideoCombine`、`MathExpression|pysssss`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
