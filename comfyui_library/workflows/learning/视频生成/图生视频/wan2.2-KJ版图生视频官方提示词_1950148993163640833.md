---
key: 视频生成/图生视频/wan2.2-KJ版图生视频官方提示词_1950148993163640833.json
name: wan2.2-KJ版图生视频官方提示词_1950148993163640833.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1950148993163640833.json
hash: 2080e7ed6cd99b25
coverage: 0.632653
learned_at: 2026-10-15 22:30:53
nodes: [WanVideoTorchCompileSettings, ImageResizeKJv2, WanVideoModelLoader, SetNode, SetNode, WanVideoBlockSwap, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SetNode, SetNode, SimpleMath+, Int2Any_AS, SetNode, GetNode, WanVideoTextEncode, GetNode, GetNode, GetImageSizeAndCount, GetNode, GetNode, WanVideoImageToVideoEncode, INTConstant, INTConstant, CreateCFGScheduleFloatList, GetNode, GetNode, easy cleanGpuUsed, easy clearCacheAll, SetNode, SetNode, GetNode, WanVideoDecode, WanVideoSampler, WanVideoSampler, LoadImage, VHS_VideoCombine, CR Text, SetNode, GetNode, ShowText, SimpleCondition+, String, CLIPLoader, GetNode, Bjornulf_ShowStringText, RH_LLMAPI_NODE]
patterns: []
missing: []
---

# 视频生成/图生视频/wan2.2-KJ版图生视频官方提示词_1950148993163640833.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1950148993163640833.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（49 个）：
- `WanVideoTorchCompileSettings`
- `ImageResizeKJv2`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `WanVideoBlockSwap`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `SimpleMath+`
- `Int2Any_AS`
- `SetNode`
- `GetNode`
- `WanVideoTextEncode`
- `GetNode`
- `GetNode`
- `GetImageSizeAndCount`
- `GetNode`
- `GetNode`
- `WanVideoImageToVideoEncode`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `GetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `LoadImage`
- `VHS_VideoCombine`
- `CR Text`
- `SetNode`
- `GetNode`
- `ShowText`
- `SimpleCondition+`
- `String`
- `CLIPLoader`
- `GetNode`
- `Bjornulf_ShowStringText`
- `RH_LLMAPI_NODE`

## 知识

覆盖率 **63%**（31/49）

**有卡**：`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoLoraSelect`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`SimpleMath+`、`Int2Any_AS`、`WanVideoTextEncode`、`GetImageSizeAndCount`、`WanVideoImageToVideoEncode`、`INTConstant`、`CreateCFGScheduleFloatList`、`easy cleanGpuUsed`、`easy clearCacheAll`、`WanVideoDecode`、`WanVideoSampler`、`LoadImage`、`VHS_VideoCombine`、`CR Text`、`ShowText`、`SimpleCondition+`、`String`、`CLIPLoader`、`Bjornulf_ShowStringText`、`RH_LLMAPI_NODE`

**用到的条目**：CLIPLoader、LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
