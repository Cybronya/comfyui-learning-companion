---
key: 视频生成/图生视频/Wan2.2 首尾帧视频工作流_1992174428303806466.json
name: Wan2.2 首尾帧视频工作流_1992174428303806466.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1992174428303806466.json
hash: c0b3d7430f3b9c90
coverage: 0.972222
learned_at: 2026-10-15 22:33:15
nodes: [LoadImage, LoadImage, JWInteger, JWInteger, JWInteger, CR Prompt Text, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoVAELoader, easy cleanGpuUsed, ImageResize+, ImageResize+, WanVideoSetLoRAs, JWInteger, PrimitiveNode, WanVideoSampler, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, CreateCFGScheduleFloatList, INTConstant, WanVideoSampler, WanVideoModelLoader, WanVideoDecode, WanVideoBlockSwap, WanVideoImageToVideoEncode, SimpleMath+, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoTextEncode, WanVideoClipVisionEncode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LoadWanVideoClipTextEncoder]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2 首尾帧视频工作流_1992174428303806466.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1992174428303806466.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（36 个）：
- `LoadImage`
- `LoadImage`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `CR Prompt Text`
- `WanVideoSetBlockSwap`
- `WanVideoModelLoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoVAELoader`
- `easy cleanGpuUsed`
- `ImageResize+`
- `ImageResize+`
- `WanVideoSetLoRAs`
- `JWInteger`
- `PrimitiveNode`
- `WanVideoSampler` ★核心
- `WanVideoBlockSwap`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoModelLoader`
- `WanVideoDecode`
- `WanVideoBlockSwap`
- `WanVideoImageToVideoEncode`
- `SimpleMath+`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `WanVideoClipVisionEncode`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LoadWanVideoClipTextEncoder` ★核心

## 知识

覆盖率 **97%**（35/36）

**有卡**：`LoadImage`、`JWInteger`、`CR Prompt Text`、`WanVideoSetBlockSwap`、`WanVideoModelLoader`、`WanVideoLoraSelect`、`WanVideoVAELoader`、`easy cleanGpuUsed`、`ImageResize+`、`WanVideoSetLoRAs`、`WanVideoSampler`、`WanVideoBlockSwap`、`CreateCFGScheduleFloatList`、`INTConstant`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`LoadWanVideoT5TextEncoder`、`VHS_VideoCombine`、`WanVideoTextEncode`、`WanVideoClipVisionEncode`、`LayerUtility: PurgeVRAM`、`LoadWanVideoClipTextEncoder`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
