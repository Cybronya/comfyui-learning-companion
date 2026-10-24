---
key: 图片生成/图生图/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_1995029039742115842.json
name: 首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_1995029039742115842
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/图片生成/图生图/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_1995029039742115842.json
hash: df9bc9ffbe8595ff
coverage: 0.972973
learned_at: 2026-10-23 13:33:12
nodes: [ImageResize+, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoLoraSelect, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoSetLoRAs, PrimitiveNode, JWInteger, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LoadWanVideoClipTextEncoder, CreateCFGScheduleFloatList, WanVideoModelLoader, WanVideoImageToVideoEncode, ImageResize+, WanVideoBlockSwap, LayerUtility: ImageScaleByAspectRatio V2, easy cleanGpuUsed, WanVideoDecode, LayerUtility: ImageScaleByAspectRatio V2, INTConstant, WanVideoSampler, WanVideoSampler, VHS_VideoCombine, WanVideoTextEncode, SimpleMath+, JWInteger, LoadImage, LoadImage, CR Prompt Text, JWInteger, Float]
patterns: []
missing: []
---

# 图片生成/图生图/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_1995029039742115842.json

> 来源文件 `comfyui_library/workflows/图片生成/图生图/首尾帧视频WAN2.2高质量版v2.0（支持10s以上）_1995029039742115842.json`

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
- `VHS_VideoCombine`
- `WanVideoTextEncode`
- `SimpleMath+`
- `JWInteger`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `JWInteger`
- `Float`

## 知识

覆盖率 **97%**（36/37）

**有卡**：`ImageResize+`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoLoraSelect`、`WanVideoModelLoader`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`JWInteger`、`LayerUtility: PurgeVRAM`、`LoadWanVideoClipTextEncoder`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoBlockSwap`、`LayerUtility: ImageScaleByAspectRatio V2`、`easy cleanGpuUsed`、`WanVideoDecode`、`INTConstant`、`WanVideoSampler`、`VHS_VideoCombine`、`WanVideoTextEncode`、`SimpleMath+`、`LoadImage`、`CR Prompt Text`、`Float`

**用到的条目**：LoadImage、LayerUtility: ImageScaleByAspectRatio V2、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode
