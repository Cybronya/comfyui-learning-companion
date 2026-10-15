---
key: 图片生成/文生图/首尾帧视频-WAN2.2高质量版_1980937502708158465.json
name: 首尾帧视频-WAN2.2高质量版_1980937502708158465
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/文生图/首尾帧视频-WAN2.2高质量版_1980937502708158465.json
hash: 06451172ab7434c2
coverage: 0.972222
learned_at: 2026-10-15 22:29:09
nodes: [ImageResize+, ImageResize+, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, PrimitiveNode, JWInteger, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, INTConstant, easy cleanGpuUsed, LoadWanVideoClipTextEncoder, WanVideoBlockSwap, WanVideoSampler, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoImageToVideoEncode, SimpleMath+, JWInteger, JWInteger, JWInteger, LoadImage, LoadImage, CreateCFGScheduleFloatList, VHS_VideoCombine, CR Prompt Text, WanVideoTextEncode]
patterns: []
missing: []
---

# 图片生成/文生图/首尾帧视频-WAN2.2高质量版_1980937502708158465.json

> 来源文件 `comfyui_library/workflows/图片生成/文生图/首尾帧视频-WAN2.2高质量版_1980937502708158465.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（36 个）：
- `ImageResize+`
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
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `INTConstant`
- `easy cleanGpuUsed`
- `LoadWanVideoClipTextEncoder` ★核心
- `WanVideoBlockSwap`
- `WanVideoSampler` ★核心
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler` ★核心
- `WanVideoImageToVideoEncode`
- `SimpleMath+`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `LoadImage`
- `LoadImage`
- `CreateCFGScheduleFloatList`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `WanVideoTextEncode`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`ImageResize+`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`JWInteger`、`LayerUtility: PurgeVRAM`、`INTConstant`、`easy cleanGpuUsed`、`LoadWanVideoClipTextEncoder`、`WanVideoSampler`、`WanVideoDecode`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`LoadImage`、`CreateCFGScheduleFloatList`、`VHS_VideoCombine`、`CR Prompt Text`、`WanVideoTextEncode`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
