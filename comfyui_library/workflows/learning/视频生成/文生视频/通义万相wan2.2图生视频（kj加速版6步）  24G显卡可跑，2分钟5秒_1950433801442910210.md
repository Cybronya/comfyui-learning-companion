---
key: 视频生成/文生视频/通义万相wan2.2图生视频（kj加速版6步）  24G显卡可跑，2分钟5秒_1950433801442910210.json
name: 通义万相wan2.2图生视频（kj加速版6步）  24G显卡可跑，2分钟5秒_1950433801442910210.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/1950433801442910210.json
hash: d5a7e9ed00923e2e
coverage: 0.852941
learned_at: 2026-10-15 22:43:35
nodes: [LoadWanVideoT5TextEncoder, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoSampler, WanVideoSetBlockSwap, WanVideoLoraSelect, GetImageSizeAndCount, WanVideoTextEncode, WanVideoLoraSelect, Note, Note, Note, Note, Note, WanVideoVAELoader, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoModelLoader, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoDecode, CreateCFGScheduleFloatList, WanVideoTorchCompileSettings, WanVideoBlockSwap, Text Multiline, WanVideoSetLoRAs, VHS_VideoCombine, ImageResizeKJv2, LoadImage, Primitive integer [Crystools], MathExpression|pysssss, Primitive integer [Crystools], Primitive integer [Crystools]]
patterns: []
missing: []
---

# 视频生成/文生视频/通义万相wan2.2图生视频（kj加速版6步）  24G显卡可跑，2分钟5秒_1950433801442910210.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/1950433801442910210.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（34 个）：
- `LoadWanVideoT5TextEncoder`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSetBlockSwap`
- `WanVideoLoraSelect`
- `GetImageSizeAndCount`
- `WanVideoTextEncode`
- `WanVideoLoraSelect`
- `Note`
- `Note`
- `Note`
- `Note`
- `Note`
- `WanVideoVAELoader`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoDecode`
- `CreateCFGScheduleFloatList`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `Text Multiline`
- `WanVideoSetLoRAs`
- `VHS_VideoCombine`
- `ImageResizeKJv2`
- `LoadImage`
- `Primitive integer [Crystools]`
- `MathExpression|pysssss`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`

## 知识

覆盖率 **85%**（29/34）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoLoraSelect`、`GetImageSizeAndCount`、`WanVideoTextEncode`、`WanVideoVAELoader`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`Primitive integer [Crystools]`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`Text Multiline`、`VHS_VideoCombine`、`ImageResizeKJv2`、`LoadImage`、`MathExpression|pysssss`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
