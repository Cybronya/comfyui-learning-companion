---
key: 视频生成/图生视频/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_2065457354044436482.json
name: 首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_2065457354044436482.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/2065457354044436482.json
hash: 348aea4cbdbff5b7
coverage: 0.972973
learned_at: 2026-10-15 22:39:41
nodes: [ImageResize+, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, PrimitiveNode, JWInteger, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LoadWanVideoClipTextEncoder, CreateCFGScheduleFloatList, WanVideoModelLoader, WanVideoImageToVideoEncode, ImageResize+, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, WanVideoSampler, WanVideoSampler, WanVideoTextEncode, SimpleMath+, JWInteger, JWInteger, Float, VHS_VideoCombine, CR Prompt Text, LoadImage, LoadImage]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_2065457354044436482.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/2065457354044436482.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（37 个）：
- `ImageResize+`
- `WanVideoClipVisionEncode`
- `LoadWanVideoT5TextEncoder`
- `WanVideoVAELoader`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `PrimitiveNode`
- `JWInteger`
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `LoadWanVideoClipTextEncoder` ★核心
- `CreateCFGScheduleFloatList`
- `WanVideoModelLoader`
- `WanVideoImageToVideoEncode`
- `ImageResize+`
- `WanVideoBlockSwap`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `easy cleanGpuUsed`
- `WanVideoDecode`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `INTConstant`
- `WanVideoSampler` ★核心
- `WanVideoSampler` ★核心
- `WanVideoTextEncode`
- `SimpleMath+`
- `JWInteger`
- `JWInteger`
- `Float`
- `VHS_VideoCombine`
- `CR Prompt Text`
- `LoadImage`
- `LoadImage`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`ImageResize+`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`JWInteger`、`LayerUtility: PurgeVRAM`、`LoadWanVideoClipTextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`WanVideoDecode`、`INTConstant`、`WanVideoSampler`、`WanVideoTextEncode`、`SimpleMath+`、`Float`、`VHS_VideoCombine`、`CR Prompt Text`、`LoadImage`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
