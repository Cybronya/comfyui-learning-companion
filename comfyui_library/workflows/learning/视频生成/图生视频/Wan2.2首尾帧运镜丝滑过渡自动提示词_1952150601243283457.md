---
key: 视频生成/图生视频/Wan2.2首尾帧运镜丝滑过渡自动提示词_1952150601243283457.json
name: Wan2.2首尾帧运镜丝滑过渡自动提示词_1952150601243283457.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/Wan2.2首尾帧运镜丝滑过渡自动提示词_1952150601243283457.json
hash: b533a3c270ede177
coverage: 0.62069
learned_at: 2026-10-15 22:31:00
nodes: [WanVideoTorchCompileSettings, WanVideoModelLoader, SetNode, SetNode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, SetNode, SetNode, GetNode, WanVideoTextEncode, INTConstant, INTConstant, CreateCFGScheduleFloatList, GetNode, GetNode, WanVideoDecode, WanVideoSampler, SetNode, GetNode, ShowText, SimpleCondition+, String, SimpleMath+, SetNode, Int2Any_AS, SetNode, SetNode, SetNode, ImageResizeKJv2, GetNode, easy cleanGpuUsed, easy clearCacheAll, WanVideoSampler, WanVideoImageToVideoEncode, GetNode, GetNode, DF_Get_image_size, LoadWanVideoClipTextEncoder, GetNode, GetNode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoLoraSelect, WanVideoClipVisionEncode, CLIPLoader, WanVideoBlockSwap, LoadImage, LoadImage, CR Text, RH_LLMAPI_NODE, GetNode, GetNode, PreviewImage, ImageConcanate, Bjornulf_ShowStringText, GetNode, VHS_VideoCombine, ImageResizeKJv2]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2首尾帧运镜丝滑过渡自动提示词_1952150601243283457.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1952150601243283457.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Output → Other

**节点**（58 个）：
- `WanVideoTorchCompileSettings`
- `WanVideoModelLoader`
- `SetNode`
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `SetNode`
- `SetNode`
- `GetNode`
- `WanVideoTextEncode`
- `INTConstant`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `GetNode`
- `GetNode`
- `WanVideoDecode`
- `WanVideoSampler` ★核心
- `SetNode`
- `GetNode`
- `ShowText`
- `SimpleCondition+`
- `String`
- `SimpleMath+`
- `SetNode`
- `Int2Any_AS`
- `SetNode`
- `SetNode`
- `SetNode`
- `ImageResizeKJv2`
- `GetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `GetNode`
- `GetNode`
- `DF_Get_image_size`
- `LoadWanVideoClipTextEncoder` ★核心
- `GetNode`
- `GetNode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoClipVisionEncode`
- `CLIPLoader`
- `WanVideoBlockSwap`
- `LoadImage`
- `LoadImage`
- `CR Text`
- `RH_LLMAPI_NODE`
- `GetNode`
- `GetNode`
- `PreviewImage`
- `ImageConcanate`
- `Bjornulf_ShowStringText`
- `GetNode`
- `VHS_VideoCombine`
- `ImageResizeKJv2`

## 知识

覆盖率 **62%**（36/58）

**有卡**：`WanVideoTorchCompileSettings`、`WanVideoModelLoader`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoTextEncode`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoDecode`、`WanVideoSampler`、`ShowText`、`SimpleCondition+`、`String`、`SimpleMath+`、`Int2Any_AS`、`ImageResizeKJv2`、`easy cleanGpuUsed`、`easy clearCacheAll`、`WanVideoImageToVideoEncode`、`DF_Get_image_size`、`LoadWanVideoClipTextEncoder`、`WanVideoLoraSelect`、`WanVideoClipVisionEncode`、`CLIPLoader`、`WanVideoBlockSwap`、`LoadImage`、`CR Text`、`RH_LLMAPI_NODE`、`ImageConcanate`、`Bjornulf_ShowStringText`、`VHS_VideoCombine`

**用到的条目**：CLIPLoader、LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
