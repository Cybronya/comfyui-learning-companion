---
key: 视频生成/图生视频/wan2.2 图生视频｜ 4步lora 加速_1953398457706971138.json
name: wan2.2 图生视频｜ 4步lora 加速_1953398457706971138.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1953398457706971138.json
hash: 3259669bdf95a37d
coverage: 0.9
learned_at: 2026-10-15 22:31:05
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, TextBox, easy showAnything, Note, easy int, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, easy seed, DF_Integer, WanVideoImageToVideoEncode, SimpleMath+, WanVideoBlockSwap, easy cleanGpuUsed, WanVideoSampler, VHS_VideoCombine, easy cleanGpuUsed, WanVideoDecode, easy cleanGpuUsed, CreateCFGScheduleFloatList, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoTextEncode, WanVideoSampler, WanVideoLoraSelect, WanVideoLoraSelect, CR Text Replace, TextBox, RH_Captioner, PrimitiveBoolean, easy ifElse, easy showAnything, TextBox, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2 图生视频｜ 4步lora 加速_1953398457706971138.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953398457706971138.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `CreateCFGScheduleFloatList`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `LoadWanVideoT5TextEncoder`
- `TextBox`
- `easy showAnything`
- `Note`
- `easy int`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `easy seed`
- `DF_Integer`
- `WanVideoImageToVideoEncode`
- `SimpleMath+`
- `WanVideoBlockSwap`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `CreateCFGScheduleFloatList`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoTextEncode`
- `WanVideoSampler` ★核心
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `CR Text Replace`
- `TextBox`
- `RH_Captioner`
- `PrimitiveBoolean`
- `easy ifElse`
- `easy showAnything`
- `TextBox`
- `LoadImage`

## 知识

覆盖率 **90%**（36/40）

**有卡**：`WanVideoSetBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`TextBox`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`WanVideoModelLoader`、`easy seed`、`DF_Integer`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`WanVideoBlockSwap`、`easy cleanGpuUsed`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoDecode`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoTextEncode`、`WanVideoLoraSelect`、`CR Text Replace`、`RH_Captioner`、`PrimitiveBoolean`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
