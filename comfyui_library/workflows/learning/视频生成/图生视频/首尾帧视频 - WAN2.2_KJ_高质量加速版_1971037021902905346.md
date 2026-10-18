---
key: 视频生成/图生视频/首尾帧视频 - WAN2.2_KJ_高质量加速版_1971037021902905346.json
name: 首尾帧视频 - WAN2.2_KJ_高质量加速版_1971037021902905346.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/首尾帧视频 - WAN2.2_KJ_高质量加速版_1971037021902905346.json
hash: 08fcb1b0dab519d3
coverage: 0.975
learned_at: 2026-10-15 22:31:55
nodes: [ImageResize+, ImageResize+, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, JWInteger, INTConstant, PrimitiveNode, WanVideoTextEncode, CreateCFGScheduleFloatList, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, VHS_VideoCombine, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, LoadImage, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, LoadImage, easy cleanGpuUsed, WanVideoSampler, WanVideoSLG, WanVideoSLG, WanVideoDecode, ColorMatch, SimpleMath+, CR Prompt Text, WanVideoSampler, JWInteger, JWInteger, JWInteger, Float]
patterns: []
missing: []
---

# 视频生成/图生视频/首尾帧视频 - WAN2.2_KJ_高质量加速版_1971037021902905346.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1971037021902905346.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（40 个）：
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
- `LoadImage`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心
- `LoadImage`
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `WanVideoSLG`
- `WanVideoDecode`
- `ColorMatch`
- `SimpleMath+`
- `CR Prompt Text`
- `WanVideoSampler` ★核心
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Float`

## 知识

覆盖率 **98%**（39/40）

**有卡**：`ImageResize+`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`JWInteger`、`INTConstant`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`VHS_VideoCombine`、`LayerUtility: PurgeVRAM`、`LoadImage`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoSLG`、`WanVideoDecode`、`ColorMatch`、`SimpleMath+`、`CR Prompt Text`、`Float`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
