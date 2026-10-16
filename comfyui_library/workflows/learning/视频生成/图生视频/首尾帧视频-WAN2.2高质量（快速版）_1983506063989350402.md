---
key: 视频生成/图生视频/首尾帧视频-WAN2.2高质量（快速版）_1983506063989350402.json
name: 首尾帧视频-WAN2.2高质量（快速版）_1983506063989350402.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1983506063989350402.json
hash: 953838c272cbf73c
coverage: 0.973684
learned_at: 2026-10-15 22:32:44
nodes: [WanVideoSetBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, PrimitiveNode, SimpleMath+, JWInteger, JWInteger, JWInteger, ImageResize+, ImageResize+, LoadWanVideoClipTextEncoder, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, JWInteger, WanVideoSampler, WanVideoBlockSwap, CreateCFGScheduleFloatList, RHHiddenNodes, RHHiddenNodes, WanVideoModelLoader, easy cleanGpuUsed, LayerUtility: PurgeVRAM, WanVideoSampler, INTConstant, LayerUtility: PurgeVRAM, LoadImage, LoadImage, VHS_VideoCombine, CR Prompt Text, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧视频-WAN2.2高质量（快速版）_1983506063989350402.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1983506063989350402.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（38 个）：
- `WanVideoSetBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `SimpleMath+`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `ImageResize+`
- `ImageResize+`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `JWInteger`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `RHHiddenNodes`
- `RHHiddenNodes`
- `WanVideoModelLoader`
- `easy cleanGpuUsed`
- `LayerUtility: PurgeVRAM`
- `WanVideoSampler` ★核心
- `INTConstant`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadImage`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **97%**（37/38）

**有卡**：`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`SimpleMath+`、`JWInteger`、`ImageResize+`、`LoadWanVideoClipTextEncoder`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoTextEncode`、`WanVideoSampler`、`CreateCFGScheduleFloatList`、`RHHiddenNodes`、`easy cleanGpuUsed`、`LayerUtility: PurgeVRAM`、`INTConstant`、`LoadImage`、`VHS_VideoCombine`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoTextEncode、WanVideoVAELoader、WanVideoClipVisionEncode
