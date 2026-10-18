---
key: 视频生成/图生视频/首尾帧视频-WAN2.2高质量版_1967833229766045698.json
name: 首尾帧视频-WAN2.2高质量版_1967833229766045698.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧视频-WAN2.2高质量版_1967833229766045698.json
hash: 424f02517cf9cc0a
coverage: 0.972222
learned_at: 2026-10-15 22:31:43
nodes: [ImageResize+, ImageResize+, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, PrimitiveNode, JWInteger, WanVideoTextEncode, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, INTConstant, easy cleanGpuUsed, LoadWanVideoClipTextEncoder, WanVideoBlockSwap, WanVideoSampler, WanVideoDecode, CreateCFGScheduleFloatList, WanVideoModelLoader, WanVideoSampler, WanVideoImageToVideoEncode, SimpleMath+, JWInteger, LoadImage, LoadImage, CR Prompt Text, JWInteger, JWInteger, VHS_VideoCombine]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧视频-WAN2.2高质量版_1967833229766045698.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1967833229766045698.json`

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
- `WanVideoImageToVideoEncode`
- `SimpleMath+`
- `JWInteger`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `JWInteger`
- `JWInteger`
- `VHS_VideoCombine`

## 知识

覆盖率 **97%**（35/36）

**有卡**：`ImageResize+`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`JWInteger`、`WanVideoTextEncode`、`LayerUtility: PurgeVRAM`、`INTConstant`、`easy cleanGpuUsed`、`LoadWanVideoClipTextEncoder`、`WanVideoSampler`、`WanVideoDecode`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`SimpleMath+`、`LoadImage`、`CR Prompt Text`、`VHS_VideoCombine`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
