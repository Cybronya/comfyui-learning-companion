---
key: 视频生成/图生视频/首尾帧视频-WAN2.2_1983929785862782977.json
name: 首尾帧视频-WAN2.2_1983929785862782977.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧视频-WAN2.2_1983929785862782977.json
hash: 8dd3d90b10e1aee7
coverage: 0.972222
learned_at: 2026-10-15 22:32:47
nodes: [WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, JWInteger, ImageResize+, ImageResize+, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, PrimitiveNode, INTConstant, JWInteger, WanVideoTextEncode, CreateCFGScheduleFloatList, WanVideoSampler, WanVideoModelLoader, WanVideoModelLoader, LoadWanVideoClipTextEncoder, WanVideoImageToVideoEncode, WanVideoBlockSwap, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoSampler, WanVideoDecode, easy cleanGpuUsed, JWInteger, JWInteger, SimpleMath+, VHS_VideoCombine, LoadImage, CR Prompt Text, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧视频-WAN2.2_1983929785862782977.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983929785862782977.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（36 个）：
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `JWInteger`
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
- `WanVideoBlockSwap`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `JWInteger`
- `JWInteger`
- `SimpleMath+`
- `VHS_VideoCombine`
- `LoadImage`
- `CR Prompt Text`
- `LoadImage`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`JWInteger`、`ImageResize+`、`WanVideoLoraSelect`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`WanVideoBlockSwap`、`INTConstant`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoSampler`、`WanVideoModelLoader`、`LoadWanVideoClipTextEncoder`、`WanVideoImageToVideoEncode`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`easy cleanGpuUsed`、`SimpleMath+`、`VHS_VideoCombine`、`LoadImage`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
