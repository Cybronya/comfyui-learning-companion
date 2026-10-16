---
key: 视频生成/图生视频/Wan2.2图生视频-Kijai版-课程专用_1950140877723361281.json
name: Wan2.2图生视频-Kijai版-课程专用_1950140877723361281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950140877723361281.json
hash: 86088330cb9b506d
coverage: 0.777778
learned_at: 2026-10-15 22:30:53
nodes: [WanVideoSetBlockSwap, WanVideoImageToVideoEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, Reroute, Reroute, Reroute, Int, Reroute, Int, WanVideoLoraSelect, WanVideoLoraSelect, Note, WanVideoTorchCompileSettings, Note, WanVideoBlockSwap, WanVideoSampler, WanVideoSampler, WanVideoEasyCache, WanVideoEnhanceAVideo, WanVideoSLG, StringToFloatList, Note, WanVideoExperimentalArgs, Int, Int, SimpleMath+, CreateCFGScheduleFloatList, WanVideoLoraSelect, Note, WanVideoLoraSelect, Note, WanVideoLoraSelect, ImageResizeKJ, WanVideoModelLoader, WanVideoModelLoader, WanVideoTextEncode, LoadImage, WanVideoDecode, VHS_VideoCombine, MarkdownNote, WanVideoLoraSelect]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2图生视频-Kijai版-课程专用_1950140877723361281.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950140877723361281.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（45 个）：
- `WanVideoSetBlockSwap`
- `WanVideoImageToVideoEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `Reroute`
- `Reroute`
- `Reroute`
- `Int`
- `Reroute`
- `Int`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `Note`
- `WanVideoTorchCompileSettings`
- `Note`
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoEasyCache`
- `WanVideoEnhanceAVideo`
- `WanVideoSLG`
- `StringToFloatList`
- `Note`
- `WanVideoExperimentalArgs`
- `Int`
- `Int`
- `SimpleMath+`
- `CreateCFGScheduleFloatList`
- `WanVideoLoraSelect`
- `Note`
- `WanVideoLoraSelect`
- `Note`
- `WanVideoLoraSelect`
- `ImageResizeKJ`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoTextEncode`
- `LoadImage`
- `WanVideoDecode`
- `VHS_VideoCombine`
- `MarkdownNote`
- `WanVideoLoraSelect`

## 知识

覆盖率 **78%**（35/45）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoImageToVideoEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoSetLoRAs`、`Int`、`WanVideoLoraSelect`、`WanVideoTorchCompileSettings`、`WanVideoBlockSwap`、`WanVideoSampler`、`WanVideoEasyCache`、`WanVideoEnhanceAVideo`、`WanVideoSLG`、`StringToFloatList`、`WanVideoExperimentalArgs`、`SimpleMath+`、`CreateCFGScheduleFloatList`、`ImageResizeKJ`、`WanVideoModelLoader`、`WanVideoTextEncode`、`LoadImage`、`WanVideoDecode`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
