---
key: 视频生成/图生视频/Wan2.2-lightx2v-6步加速图生视频-KJ版_1950132208273154049.json
name: Wan2.2-lightx2v-6步加速图生视频-KJ版_1950132208273154049.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950132208273154049.json
hash: 9b1444212b2ab174
coverage: 1
learned_at: 2026-10-15 22:30:53
nodes: [WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSampler, WanVideoLoraSelect, WanVideoSetLoRAs, CreateCFGScheduleFloatList, WanVideoTorchCompileSettings, WanVideoBlockSwap, WanVideoVAELoader, ImageResizeKJv2, WanVideoImageToVideoEncode, WanVideoModelLoader, WanVideoModelLoader, WanVideoSampler, LoadWanVideoT5TextEncoder, Primitive integer [Crystools], Primitive integer [Crystools], WanVideoSetBlockSwap, VHS_VideoCombine, WanVideoTextEncode, Primitive integer [Crystools], Text Multiline, WanVideoDecode, WanVideoLoraSelect, LoadImage, Primitive integer [Crystools], Primitive integer [Crystools], MathExpression|pysssss, CreateVideo, PreViewVideo]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2-lightx2v-6步加速图生视频-KJ版_1950132208273154049.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950132208273154049.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（30 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `WanVideoTorchCompileSettings`
- `WanVideoBlockSwap`
- `WanVideoVAELoader`
- `ImageResizeKJv2`
- `WanVideoImageToVideoEncode`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `LoadWanVideoT5TextEncoder`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `WanVideoSetBlockSwap`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `Primitive integer [Crystools]`
- `Text Multiline`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `LoadImage`
- `Primitive integer [Crystools]`
- `Primitive integer [Crystools]`
- `MathExpression|pysssss`
- `CreateVideo`
- `PreViewVideo`

## 知识

覆盖率 **100%**（30/30）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoLoraSelect`、`CreateCFGScheduleFloatList`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoVAELoader`、`ImageResizeKJv2`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`Primitive integer [Crystools]`、`VHS_VideoCombine`、`WanVideoTextEncode`、`Text Multiline`、`WanVideoDecode`、`LoadImage`、`MathExpression|pysssss`、`CreateVideo`、`PreViewVideo`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
