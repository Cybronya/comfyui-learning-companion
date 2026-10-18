---
key: 视频生成/图生视频/WAN2.2首尾帧视频工作流_1992060788846252034.json
name: WAN2.2首尾帧视频工作流_1992060788846252034.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/WAN2.2首尾帧视频工作流_1992060788846252034.json
hash: 467b67db63e82919
coverage: 0.972222
learned_at: 2026-10-15 22:33:15
nodes: [ImageResize+, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, PrimitiveNode, JWInteger, WanVideoTextEncode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, INTConstant, easy cleanGpuUsed, LoadWanVideoClipTextEncoder, WanVideoBlockSwap, WanVideoSampler, WanVideoDecode, CreateCFGScheduleFloatList, WanVideoModelLoader, WanVideoSampler, JWInteger, LoadImage, SimpleMath+, ImageResize+, JWInteger, JWInteger, WanVideoImageToVideoEncode, VHS_VideoCombine, LoadImage, CR Prompt Text]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2首尾帧视频工作流_1992060788846252034.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992060788846252034.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（36 个）：
- `ImageResize+`
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `JWInteger`
- `WanVideoTextEncode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `INTConstant`
- `easy cleanGpuUsed`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `CreateCFGScheduleFloatList`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `JWInteger`
- `LoadImage`
- `SimpleMath+`
- `ImageResize+`
- `JWInteger`
- `JWInteger`
- `WanVideoImageToVideoEncode`
- `VHS_VideoCombine`
- `LoadImage`
- `CR Prompt Text`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`ImageResize+`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`JWInteger`、`WanVideoTextEncode`、`LayerUtility: PurgeVRAM`、`INTConstant`、`easy cleanGpuUsed`、`LoadWanVideoClipTextEncoder`、`WanVideoSampler`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`LoadImage`、`SimpleMath+`、`WanVideoImageToVideoEncode`、`VHS_VideoCombine`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
