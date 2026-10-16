---
key: 视频生成/图生视频/WAN2.2毛茸茸首尾帧动画_1978297110992969730.json
name: WAN2.2毛茸茸首尾帧动画_1978297110992969730.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1978297110992969730.json
hash: 870b858061ab8717
coverage: 0.975
learned_at: 2026-10-15 22:32:18
nodes: [SimpleMath+, WanVideoVAELoader, LoadWanVideoT5TextEncoder, WanVideoClipVisionEncode, ImageResize+, WanVideoSampler, WanVideoSampler, JWInteger, VHS_VideoCombine, LoadImage, LoadImage, LoadWanVideoClipTextEncoder, JWInteger, JWInteger, WanVideoModelLoader, WanVideoBlockSwap, WanVideoModelLoader, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoBlockSwap, CreateCFGScheduleFloatList, PrimitiveNode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoDecode, easy cleanGpuUsed, INTConstant, WanVideoTextEncode, JWInteger, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoLoraSelect, CR Prompt Text, ImageResize+]
patterns: []
missing: []
---

# 视频生成/图生视频/WAN2.2毛茸茸首尾帧动画_1978297110992969730.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1978297110992969730.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（40 个）：
- `SimpleMath+`
- `WanVideoVAELoader`
- `LoadWanVideoT5TextEncoder`
- `WanVideoClipVisionEncode`
- `ImageResize+`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `JWInteger`
- `VHS_VideoCombine`
- `LoadImage`
- `LoadImage`
- `LoadWanVideoClipTextEncoder` ★核心
- `JWInteger`
- `JWInteger`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `WanVideoModelLoader`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoBlockSwap`
- `CreateCFGScheduleFloatList`
- `PrimitiveNode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoDecode`
- `easy cleanGpuUsed`
- `INTConstant`
- `WanVideoTextEncode`
- `JWInteger`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `CR Prompt Text`
- `ImageResize+`

## 知识

覆盖率 **98%**（39/40）

**有卡**：`SimpleMath+`、`WanVideoVAELoader`、`LoadWanVideoT5TextEncoder`、`WanVideoClipVisionEncode`、`ImageResize+`、`WanVideoSampler`、`JWInteger`、`VHS_VideoCombine`、`LoadImage`、`LoadWanVideoClipTextEncoder`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetLoRAs`、`WanVideoSetBlockSwap`、`CreateCFGScheduleFloatList`、`LayerUtility: PurgeVRAM`、`WanVideoDecode`、`easy cleanGpuUsed`、`INTConstant`、`WanVideoTextEncode`、`WanVideoImageToVideoEncode`、`WanVideoLoraSelect`、`CR Prompt Text`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
