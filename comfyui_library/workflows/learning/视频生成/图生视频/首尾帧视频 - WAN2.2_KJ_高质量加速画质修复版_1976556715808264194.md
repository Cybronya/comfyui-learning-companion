---
key: 视频生成/图生视频/首尾帧视频 - WAN2.2_KJ_高质量加速画质修复版_1976556715808264194.json
name: 首尾帧视频 - WAN2.2_KJ_高质量加速画质修复版_1976556715808264194.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1976556715808264194.json
hash: 09e53484ae5e0780
coverage: 0.974359
learned_at: 2026-10-15 22:32:11
nodes: [SimpleMath+, CR Prompt Text, ImageResize+, ImageResize+, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, JWInteger, INTConstant, PrimitiveNode, WanVideoTextEncode, CreateCFGScheduleFloatList, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, VHS_VideoCombine, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, easy cleanGpuUsed, WanVideoSampler, WanVideoSampler, WanVideoSLG, WanVideoSLG, WanVideoDecode, JWInteger, JWInteger, JWInteger, ColorMatch, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧视频 - WAN2.2_KJ_高质量加速画质修复版_1976556715808264194.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1976556715808264194.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（39 个）：
- `SimpleMath+`
- `CR Prompt Text`
- `ImageResize+`
- `ImageResize+`
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `JWInteger`
- `INTConstant`
- `PrimitiveNode`
- `WanVideoTextEncode`
- `CreateCFGScheduleFloatList`
- `WanVideoImageToVideoEncode`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoModelLoader`
- `WanVideoBlockSwap`
- `VHS_VideoCombine`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `WanVideoSLG`
- `WanVideoDecode`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `ColorMatch`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **97%**（38/39）

**有卡**：`SimpleMath+`、`CR Prompt Text`、`ImageResize+`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`JWInteger`、`INTConstant`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoSLG`、`WanVideoDecode`、`ColorMatch`、`LoadImage`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
