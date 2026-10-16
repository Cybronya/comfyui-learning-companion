---
key: 视频生成/图生视频/WAN2.2-首尾帧视频工作流_1981935370910744577.json
name: WAN2.2-首尾帧视频工作流_1981935370910744577.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1981935370910744577.json
hash: 7aaaea85fbd69ee9
coverage: 0.947368
learned_at: 2026-10-15 22:32:39
nodes: [SimpleMath+, WanVideoSampler, WanVideoSampler, WanVideoBlockSwap, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetLoRAs, WanVideoSetBlockSwap, ImageResize+, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, ImageResize+, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoTextEncode, WanVideoDecode, JWInteger, INTConstant, CreateCFGScheduleFloatList, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoVAELoader, WanVideoModelLoader, WanVideoModelLoader, easy cleanGpuUsed, PrimitiveNode, WanVideoImageToVideoEncode, LoadImage, LoadImage, VHS_VideoCombine, CR Prompt Text, JWInteger, JWInteger, JWInteger, MarkdownNote, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2-首尾帧视频工作流_1981935370910744577.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1981935370910744577.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（38 个）：
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `ImageResize+`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `ImageResize+`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoTextEncode`
- `WanVideoDecode`
- `JWInteger`
- `INTConstant`
- `CreateCFGScheduleFloatList`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoVAELoader`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `PrimitiveNode`
- `WanVideoImageToVideoEncode`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `MarkdownNote`
- `LoadImage`

## 知识

覆盖率 **95%**（36/38）

**有卡**：`SimpleMath+`、`WanVideoSampler`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`ImageResize+`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoLoraSelect`、`WanVideoTextEncode`、`WanVideoDecode`、`JWInteger`、`INTConstant`、`CreateCFGScheduleFloatList`、`LayerUtility: PurgeVRAM`、`WanVideoVAELoader`、`WanVideoModelLoader`、`easy cleanGpuUsed`、`WanVideoImageToVideoEncode`、`LoadImage`、`VHS_VideoCombine`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
