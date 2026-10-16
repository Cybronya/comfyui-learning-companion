---
key: 视频生成/图生视频/【视频】Wan2.2首尾帧一键生成视频_1952674570933309442.json
name: 【视频】Wan2.2首尾帧一键生成视频_1952674570933309442.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1952674570933309442.json
hash: 37911b19f2051ca5
coverage: 0.825
learned_at: 2026-10-15 22:31:03
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoTorchCompileSettings, WanVideoModelLoader, WanVideoModelLoader, WanVideoVAELoader, LoadWanVideoT5TextEncoder, INTConstant, WanVideoLoraSelect, WanVideoLoraSelect, INTConstant, WanVideoBlockSwap, CreateCFGScheduleFloatList, WanVideoDecode, GetImageSizeAndCount, VHS_VideoCombine, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSampler, Reroute, easy showAnything, Note, easy ifElse, RH_Captioner, TextBox, LoadImage, CR Text Replace, PrimitiveBoolean, TextBox, WanVideoTextEncode, Note, Reroute, WanVideoSampler, ImageResizeKJv2, easy showAnything, WanVideoImageToVideoEncode, ImageResizeKJv2, LoadImage, LoadImage, TextBox]
patterns: []
missing: []
---

# 视频生成/图生视频/【视频】Wan2.2首尾帧一键生成视频_1952674570933309442.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952674570933309442.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `INTConstant`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `INTConstant`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoDecode`
- `GetImageSizeAndCount`
- `VHS_VideoCombine`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `Reroute`
- `easy showAnything`
- `Note`
- `easy ifElse`
- `RH_Captioner`
- `TextBox`
- `LoadImage`
- `CR Text Replace`
- `PrimitiveBoolean`
- `TextBox`
- `WanVideoTextEncode`
- `Note`
- `Reroute`
- `WanVideoSampler` ★核心
- `ImageResizeKJv2`
- `easy showAnything`
- `WanVideoImageToVideoEncode`
- `ImageResizeKJv2`
- `LoadImage`
- `LoadImage`
- `TextBox`

## 知识

覆盖率 **82%**（33/40）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`INTConstant`、`WanVideoLoraSelect`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`GetImageSizeAndCount`、`VHS_VideoCombine`、`WanVideoSetLoRAs`、`WanVideoSampler`、`RH_Captioner`、`TextBox`、`LoadImage`、`CR Text Replace`、`PrimitiveBoolean`、`WanVideoTextEncode`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
