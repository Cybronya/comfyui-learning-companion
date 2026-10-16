---
key: 视频生成/图生视频/Wan2.2_KJ版 首尾帧视频+补帧_高质量加速版V2_1998010318326497281.json
name: Wan2.2_KJ版 首尾帧视频+补帧_高质量加速版V2_1998010318326497281.json
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/图生视频/1998010318326497281.json
hash: 8a016c76caaec440
coverage: 0.97619
learned_at: 2026-10-15 22:33:31
nodes: [ImageResize+, ImageResize+, WanVideoClipVisionEncode, LoadWanVideoT5TextEncoder, WanVideoVAELoader, WanVideoBlockSwap, WanVideoSetBlockSwap, WanVideoSetLoRAs, JWInteger, INTConstant, PrimitiveNode, WanVideoTextEncode, CreateCFGScheduleFloatList, WanVideoImageToVideoEncode, WanVideoSetLoRAs, WanVideoSetBlockSwap, WanVideoModelLoader, WanVideoModelLoader, WanVideoBlockSwap, LayerUtility: PurgeVRAM, LayerUtility: PurgeVRAM, WanVideoLoraSelect, WanVideoLoraSelect, LoadWanVideoClipTextEncoder, easy cleanGpuUsed, WanVideoSampler, WanVideoSLG, WanVideoSLG, WanVideoDecode, SimpleMath+, WanVideoSampler, ColorMatch, VHS_VideoCombine, VHS_VideoCombine, JWInteger, JWInteger, JWInteger, Float, LoadImage, LoadImage, CR Prompt Text, RIFE VFI]
patterns: []
missing: []
---

# 视频生成/图生视频/Wan2.2_KJ版 首尾帧视频+补帧_高质量加速版V2_1998010318326497281.json

> 来源文件 `comfyui_library/workflows/视频生成/图生视频/1998010318326497281.json`

## 结构

**生成流程**：Model → Condition → Sampling → Process → Other

**节点**（42 个）：
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
- `LayerUtility: PurgeVRAM`
- `LayerUtility: PurgeVRAM`
- `WanVideoLoraSelect`
- `WanVideoLoraSelect`
- `LoadWanVideoClipTextEncoder` ★核心
- `easy cleanGpuUsed`
- `WanVideoSampler` ★核心
- `WanVideoSLG`
- `WanVideoSLG`
- `WanVideoDecode`
- `SimpleMath+`
- `WanVideoSampler` ★核心
- `ColorMatch`
- `VHS_VideoCombine`
- `VHS_VideoCombine`
- `JWInteger`
- `JWInteger`
- `JWInteger`
- `Float`
- `LoadImage`
- `LoadImage`
- `CR Prompt Text`
- `RIFE VFI`

## 知识

覆盖率 **98%**（41/42）

**有卡**：`ImageResize+`、`WanVideoClipVisionEncode`、`LoadWanVideoT5TextEncoder`、`WanVideoVAELoader`、`WanVideoBlockSwap`、`WanVideoSetBlockSwap`、`WanVideoSetLoRAs`、`JWInteger`、`INTConstant`、`WanVideoTextEncode`、`CreateCFGScheduleFloatList`、`WanVideoImageToVideoEncode`、`WanVideoModelLoader`、`LayerUtility: PurgeVRAM`、`WanVideoLoraSelect`、`LoadWanVideoClipTextEncoder`、`easy cleanGpuUsed`、`WanVideoSampler`、`WanVideoSLG`、`WanVideoDecode`、`SimpleMath+`、`ColorMatch`、`VHS_VideoCombine`、`Float`、`LoadImage`、`CR Prompt Text`、`RIFE VFI`

**用到的条目**：LoadImage、WanVideoSampler、CreateCFGScheduleFloatList、LoadWanVideoClipTextEncoder、LoadWanVideoT5TextEncoder、WanVideoDecode、WanVideoTextEncode、WanVideoVAELoader
