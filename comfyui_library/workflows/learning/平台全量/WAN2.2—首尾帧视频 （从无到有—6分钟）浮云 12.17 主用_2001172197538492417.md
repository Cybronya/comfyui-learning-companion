---
key: 平台全量/WAN2.2—首尾帧视频 （从无到有—6分钟）浮云 12.17 主用_2001172197538492417.json
name: WAN2.2—首尾帧视频 （从无到有—6分钟）浮云 12.17 主用_2001172197538492417
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/平台全量/WAN2.2—首尾帧视频 （从无到有—6分钟）浮云 12.17 主用_2001172197538492417.json
hash: b8ab7a689579d5d9
coverage: 0.972222
learned_at: 2026-11-14 01:03:43
nodes: [WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, ImageResize+, ImageResize+, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, PrimitiveNode, INTConstant, JWInteger, WanVideoTextEncode, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoClipTextEncoder, WanVideoImageToVideoEncode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoSampler, WanVideoDecode, easy cleanGpuUsed, SimpleMath+, VHS_VideoCombine, LoadImage, LoadImage, JWInteger, JWInteger, JWInteger, CR Prompt Text, WanVideoBlockSwap]
patterns: []
missing: []
---

# 平台全量/WAN2.2—首尾帧视频 （从无到有—6分钟）浮云 12.17 主用_2001172197538492417.json

> 来源文件 `comfyui_library/workflows/平台全量/WAN2.2—首尾帧视频 （从无到有—6分钟）浮云 12.17 主用_2001172197538492417.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `ImageResize+`
- `ImageResize+`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `PrimitiveNode`
- `INTConstant`
- `JWInteger`
- `WanVideoTextEncode`
- `CreateCFGScheduleFloatList`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoImageToVideoEncode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `SimpleMath+`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `WanVideoBlockSwap`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`ImageResize+`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`INTConstant`、`JWInteger`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`WanVideoImageToVideoEncode`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`easy cleanGpuUsed`、`SimpleMath+`、`VHS_VideoCombine`、`LoadImage`、`CR Prompt Text`

**用到的条目**：LoadImage、CreateCFGScheduleFloatList、WanVideoSampler、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoClipVisionEncode、WanVideoDecode、WanVideoImageToVideoEncode
