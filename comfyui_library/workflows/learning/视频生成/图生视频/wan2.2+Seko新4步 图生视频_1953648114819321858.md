---
key: 视频生成/图生视频/wan2.2+Seko新4步 图生视频_1953648114819321858.json
name: wan2.2+Seko新4步 图生视频_1953648114819321858.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1953648114819321858.json
hash: 62ad46408c393293
coverage: 0.904762
learned_at: 2026-10-15 22:31:05
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, CreateCFGScheduleFloatList, WanVideoSetLoRAs, WanVideoSetLoRAs, LoadWanVideoT5TextEncoder, TextBox, easy showAnything, Note, easy int, LayerUtility: ImageScaleByAspectRatio V2, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, easy seed, DF_Integer, WanVideoImageToVideoEncode, SimpleMath+, WanVideoBlockSwap, easy cleanGpuUsed, VHS_VideoCombine, easy cleanGpuUsed, WanVideoDecode, easy cleanGpuUsed, CogVideoEnhanceAVideo, WanVideoSLG, WanVideoTextEncode, CR Text Replace, TextBox, RH_Captioner, PrimitiveBoolean, easy ifElse, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, easy showAnything, WanVideoSampler, WanVideoSampler, StringToFloatList, FloatToSigmas, CreateCFGScheduleFloatList, TextBox]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2+Seko新4步 图生视频_1953648114819321858.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1953648114819321858.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（42 个）：
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
- `VHS_VideoCombine`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `CogVideoEnhanceAVideo`
- `WanVideoSLG`
- `WanVideoTextEncode`
- `CR Text Replace`
- `TextBox`
- `RH_Captioner`
- `PrimitiveBoolean`
- `easy ifElse`
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `easy showAnything`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `StringToFloatList`
- `FloatToSigmas`
- `CreateCFGScheduleFloatList`
- `TextBox`

## 知识

覆盖率 **90%**（38/42）

**有卡**：`WanVideoSetBlockSwap`、`CreateCFGScheduleFloatList`、`WanVideoSetLoRAs`、`LoadWanVideoT5TextEncoder`、`TextBox`、`easy int`、`LayerUtility: ImageScaleByAspectRatio V2`、`WanVideoVAELoader`、`WanVideoModelLoader`、`easy seed`、`DF_Integer`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`WanVideoBlockSwap`、`easy cleanGpuUsed`、`VHS_VideoCombine`、`WanVideoDecode`、`CogVideoEnhanceAVideo`、`WanVideoSLG`、`WanVideoTextEncode`、`CR Text Replace`、`RH_Captioner`、`PrimitiveBoolean`、`LoadImage`、`WanVideoLoraSelect`、`WanVideoSampler`、`StringToFloatList`、`FloatToSigmas`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、easy seed、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
