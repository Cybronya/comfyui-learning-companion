---
key: 视频生成/图生视频/DNR-WAN2.2 KJ 图生视频_1951706628657721345.json
name: DNR-WAN2.2 KJ 图生视频_1951706628657721345.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/DNR-WAN2.2 KJ 图生视频_1951706628657721345.json
hash: f4ac80a3e1b688b9
coverage: 0.65
learned_at: 2026-10-15 22:30:59
nodes: [SetNode, LoadWanVideoT5TextEncoder, WanVideoDecode, SetNode, SetNode, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, SetNode, INTConstant, CreateCFGScheduleFloatList, INTConstant, GetNode, GetNode, GetNode, GetNode, GetNode, SetNode, WanVideoLoraSelect, SetNode, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, WanVideoTorchCompileSettings, WanVideoSetBlockSwap, ImageResizeKJv2, WanVideoEasyCache, GetNode, GetNode, PrimitiveNode, WanVideoSampler, JWInteger, WanVideoSampler, VHS_VideoCombine, LoadImage, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/DNR-WAN2.2 KJ 图生视频_1951706628657721345.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1951706628657721345.json`

## 结构

**生成流程**：Model → Sampling → Process → Other

**节点**（40 个）：
- `SetNode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoDecode`
- `SetNode`
- `SetNode`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `SetNode`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `WanVideoLoraSelect`
- `SetNode`
- `WanVideoImageToVideoEncode`
- `WanVideoSetLoRAs`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoTorchCompileSettings`
- `WanVideoSetBlockSwap`
- `ImageResizeKJv2`
- `WanVideoEasyCache`
- `GetNode`
- `GetNode`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `JWInteger`
- `WanVideoSampler` ★核心
- `VHS_VideoCombine`
- `LoadImage`
- `CR Prompt Text`

## 知识

覆盖率 **65%**（26/40）

**有卡**：`LoadWanVideoT5TextEncoder`、`WanVideoDecode`、`WanVideoSetLoRAs`、`WanVideoTextEncode`、`WanVideoVAELoader`、`INTConstant`、`CreateCFGScheduleFloatList`、`WanVideoLoraSelect`、`WanVideoImageToVideoEncode`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoTorchCompileSettings`、`ImageResizeKJv2`、`WanVideoEasyCache`、`WanVideoSampler`、`JWInteger`、`VHS_VideoCombine`、`LoadImage`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader、WanVideoImageToVideoEncode
